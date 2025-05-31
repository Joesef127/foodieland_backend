## Foodieland Backend
==================

This is the backend for the Foodieland application, built with FastAPI. It provides RESTful APIs for managing recipes, blogs, and other application data. The backend uses SQLAlchemy for database interactions and supports both SQLite (for local development) and MySQL (for production).

## Features
--------

- CRUD operations for recipes and blogs.
- Toggle favorite status for recipes.
- Database migrations using Alembic.
- CORS support for frontend integration.
- Environment variable-based database configuration.

## Project Structure
-----------------

The project structure is as follows:

```
foodieland_backend/
├── app/
│   ├── database.py         # Database configuration
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── routes/
│   │   ├── recipe.py       # Recipe endpoints
│   │   ├── blog.py         # Blog endpoints
│   ├── populate_db.py      # Script to populate the database with mock data
│   ├── main.py             # FastAPI application entry point
│   ├── sqlmodel.py         # SQLModel configuration (optional)
├── migrations/             # Alembic migrations
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
└── README.md               # Project documentation
```

## Installation
1. Clone the Repository
```
git clone https://github.com/your-username/foodieland_backend.git
cd foodieland_backend
```

2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```

## API Endpoints

### Recipes
Method	Endpoint	                              Description
GET	    /recipes/	                              Get all recipes
GET	    /recipes/{recipe_id}	                  Get a recipe by ID
POST	  /recipes/	                              Create a new recipe
PUT	    /recipes/{recipe_id}	                  Update a recipe
DELETE	/recipes/{recipe_id}	                  Delete a recipe
PATCH	  /recipes/{recipe_id}/toggle_favorite	  Toggle favorite status

### Blogs
Method	   Endpoint	        Description
GET	      /blogs/	          Get all blogs
GET	      /blogs/{blog_id}	Get a blog by ID
POST	    /blogs/	          Create a new blog
PUT	      /blogs/{blog_id}	Update a blog
DELETE	  /blogs/{blog_id}	Delete a blog

