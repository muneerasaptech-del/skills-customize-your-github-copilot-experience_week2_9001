from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI(title="Student API", description="A simple REST API for managing students")

# Pydantic model for request/response
class Student(BaseModel):
    id: int
    name: str
    email: str
    grade: int

# In-memory storage (replace with database in production)
students_db = [
    Student(id=1, name="Alice Johnson", email="alice@example.com", grade=10),
    Student(id=2, name="Bob Smith", email="bob@example.com", grade=11),
]

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Student API!", "version": "1.0"}

# GET all students
@app.get("/students", response_model=List[Student])
def get_students():
    """Get all students"""
    return students_db

# GET a specific student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """Get a specific student by ID"""
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# POST - Create a new student
@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    """Create a new student"""
    # Check if ID already exists
    for s in students_db:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    
    students_db.append(student)
    return student

# DELETE a student
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    """Delete a student by ID"""
    for i, student in enumerate(students_db):
        if student.id == student_id:
            students_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Student not found")

# Run with: uvicorn starter-code:app --reload
