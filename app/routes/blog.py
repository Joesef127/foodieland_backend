from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Blog
from app.schemas import Blog as BlogSchema
from ..database import get_db

router = APIRouter(prefix="/blogs", tags=["Blogs"])

# Create a new blog
@router.post("/", response_model=BlogSchema, status_code=201)
async def create_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    db_blog = Blog(**blog.model_dump(exclude={"id"})) 
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

# Get all blogs
@router.get("/", response_model=list[BlogSchema])
async def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs

# Get a single blog by ID
@router.get("/{blog_id}", response_model=BlogSchema)
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Update a blog
@router.put("/{blog_id}", response_model=BlogSchema)
async def update_blog(blog_id: int, updated_blog: BlogSchema, db: Session = Depends(get_db)):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    for key, value in updated_blog.model_dump(exclude_unset=True).items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog

# Delete a blog
@router.delete("/{blog_id}", status_code=204)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(db_blog)
    db.commit()
    return {"message": "Blog deleted successfully"}