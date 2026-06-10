# 📘 Assignment: JWT Authentication for FastAPI Endpoints

## 🎯 Objective

Implement token-based authentication in a FastAPI project using JWT so protected routes are only accessible to authenticated users. In this assignment, you will practice secure login flow, token validation, and authorization checks.

## 📝 Tasks

### 🛠️ Implement Login and Token Generation

#### Description
Use the provided starter structure to create a login endpoint that validates user credentials and returns a signed JWT access token.

#### Requirements
Completed program should:

- Implement `POST /token` using `OAuth2PasswordRequestForm`
- Validate username and password against the in-memory user store
- Generate a JWT with a user identifier (`sub`) and expiration (`exp`) claim
- Return the token in the response with `token_type: bearer`
- Return `401` for invalid credentials


### 🛠️ Protect Private Endpoints with JWT Validation

#### Description
Add dependency-based authentication so only requests with a valid bearer token can access private routes.

#### Requirements
Completed program should:

- Implement a function to decode and validate incoming JWT tokens
- Reject missing, invalid, or expired tokens with `401`
- Implement `GET /me` to return the currently authenticated user's public data
- Keep `GET /health` public while requiring authentication for private routes


### 🛠️ Add Authorization Checks for Admin-Only Access

#### Description
Enforce role-based access by allowing only admin users to call specific endpoints.

#### Requirements
Completed program should:

- Add a dependency or helper to verify whether the authenticated user has `role = admin`
- Implement `GET /admin/reports` as an admin-only endpoint
- Return `403` when a non-admin user attempts to access admin routes
- Return clear JSON messages for success and access-denied responses
