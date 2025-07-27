# FastAPI POST API

This project is a simple backend API built with **FastAPI** that demonstrates how to create a RESTful POST endpoint to add users and store them in a SQLite database using SQLAlchemy ORM.

---

## Features

- FastAPI for building the API  
- SQLite database for storing data  
- SQLAlchemy ORM for database operations  
- Pydantic models for data validation  
- Swagger UI for interactive API documentation  
- Simple GET and POST endpoints

---

## Project Structure

- `main.py` — The main FastAPI application file  
- `venv/` — Python virtual environment (recommended to exclude from GitHub using `.gitignore`)  
- `test.db` — SQLite database file generated at runtime  

---

## Requirements

- Python 3.7 or higher  
- FastAPI  
- Uvicorn (ASGI server)  
- SQLAlchemy  
- Pydantic  

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/akdinesh2003/fastapi-post-api.git
cd fastapi-post-api
````

2. **Create and activate a virtual environment**

* Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

* Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy
```

4. **Run the FastAPI server**

```bash
uvicorn main:app --reload
```

5. **Open the API docs**

Navigate your browser to:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET `/`

Returns a simple welcome message.

**Response Example:**

```json
{
  "message": "Hello, DINESH"
}
```

---

### POST `/users`

Create a new user by providing JSON body:

```json
{
  "name": "Your Name",
  "email": "your.email@example.com"
}
```

**Response Example:**

```json
{
  "message": "User created successfully",
  "user": {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
}
```

---

## Notes

* The project uses SQLite as the database, and the database file `test.db` is created automatically in the project root on the first run.
* The virtual environment folder `venv/` should be excluded from version control (add it to `.gitignore`).
* You can extend this project by adding more endpoints like GET all users, update user, delete user, etc.

---

## Author

**AK Dinesh** [https://github.com/akdinesh2003](https://github.com/akdinesh2003)

