"""Starter code: JWT Authentication with FastAPI.

Run locally:
    uvicorn starter-code:app --reload
"""

from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI(title="JWT Auth Assignment")

# Use the same secret for local classroom exercises only.
SECRET_KEY = "change-me-in-class"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory user store for assignment purposes.
FAKE_USERS_DB = {
    "alice": {
        "username": "alice",
        "full_name": "Alice Johnson",
        "password": "alice123",
        "role": "student",
    },
    "teacher": {
        "username": "teacher",
        "full_name": "Teacher User",
        "password": "teacher123",
        "role": "admin",
    },
}


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create a JWT token with expiration.

    TODO: Students should verify the payload has `sub` and then sign it.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_user(username: str, password: str) -> dict | None:
    """Validate credentials against the fake user store."""
    user = FAKE_USERS_DB.get(username)
    if not user:
        return None
    if user["password"] != password:
        return None
    return user


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    """Decode JWT and return authenticated user.

    TODO: Students can improve error details and validation logic.
    """
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_error
    except jwt.InvalidTokenError as exc:
        raise credentials_error from exc

    user = FAKE_USERS_DB.get(username)
    if user is None:
        raise credentials_error
    return user


def require_admin(user: Annotated[dict, Depends(get_current_user)]) -> dict:
    """Allow only admin users."""
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> dict[str, str]:
    user = verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me")
def read_current_user(user: Annotated[dict, Depends(get_current_user)]) -> dict:
    return {
        "username": user["username"],
        "full_name": user["full_name"],
        "role": user["role"],
    }


@app.get("/admin/reports")
def read_admin_reports(admin_user: Annotated[dict, Depends(require_admin)]) -> dict:
    return {
        "message": "Sensitive report data",
        "requested_by": admin_user["username"],
    }
