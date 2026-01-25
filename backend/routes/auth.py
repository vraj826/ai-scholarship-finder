from fastapi import APIRouter, HTTPException, status
from schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from database.db import get_database
from utils.auth_utils import hash_password, verify_password, create_access_token
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse)
async def register(request: RegisterRequest):
    db = get_database()
    users_collection = db.users
    
    # Check if user exists
    existing_user = await users_collection.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user
    hashed_pwd = hash_password(request.password)
    user_doc = {
        "email": request.email,
        "hashed_password": hashed_pwd,
        "created_at": datetime.utcnow(),
        "has_profile": False
    }
    
    await users_collection.insert_one(user_doc)
    
    # Create token
    access_token = create_access_token(data={"sub": request.email})
    
    return TokenResponse(
        access_token=access_token,
        has_profile=False
    )

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    db = get_database()
    users_collection = db.users
    
    # Find user
    user = await users_collection.find_one({"email": request.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Verify password
    if not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Create token
    access_token = create_access_token(data={"sub": request.email})
    
    return TokenResponse(
        access_token=access_token,
        has_profile=user.get("has_profile", False)
    )