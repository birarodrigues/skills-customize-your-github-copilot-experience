# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request handling, and basic in-memory data management. By the end, you will be able to design and test CRUD-style API endpoints.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application and create a health-check endpoint to confirm the server is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Run the API locally using Uvicorn
- Implement `GET /` that returns a JSON welcome message
- Implement `GET /health` that returns `{ "status": "ok" }`


### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Implement API endpoints for managing a simple resource (for example, tasks or books) using an in-memory Python list.

#### Requirements
Completed program should:

- Define a Pydantic model for request/response validation
- Implement `POST /items` to create a new item
- Implement `GET /items` to list all items
- Implement `GET /items/{item_id}` to retrieve one item
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item


### 🛠️ Validate Data and Handle Errors

#### Description
Improve API reliability by adding input validation and clear error responses.

#### Requirements
Completed program should:

- Return `404` when an item ID does not exist
- Return `422` automatically for invalid request data via Pydantic validation
- Use meaningful JSON messages for successful and failed operations
- Keep endpoint behavior consistent across create, read, update, and delete actions
