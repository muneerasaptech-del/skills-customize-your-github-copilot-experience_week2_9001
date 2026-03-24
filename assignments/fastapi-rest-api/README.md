# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework. You'll create endpoints to handle HTTP requests, work with request and response models, and understand the basics of web API development with Python.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Build the foundation of a REST API with basic GET and POST endpoints to handle different types of requests and demonstrate the core FastAPI concepts.

#### Requirements
Completed program should:

- Create a FastAPI application with a root endpoint that returns a welcome message
- Implement a GET endpoint that returns a list of items (e.g., books, products, or students)
- Implement a POST endpoint that accepts JSON data and adds a new item to the list
- Use Pydantic models to define the structure of request and response data
- Test the endpoints using the interactive Swagger UI documentation


### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API with input validation, error handling, and status codes to make it more robust and production-ready.

#### Requirements
Completed program should:

- Add request validation using Pydantic models with field requirements and types
- Implement proper HTTP status codes (200, 201, 400, 404)
- Add a GET endpoint with path parameters (e.g., get a specific item by ID)
- Include error handling that returns meaningful error messages
- Add a DELETE endpoint to remove items from the list
- Document all endpoints with descriptions in the Swagger UI
