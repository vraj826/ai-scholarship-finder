from fastapi import APIRouter, HTTPException, status, Depends
from schemas.profile import ProfileCreate, ProfileUpdate, ProfileResponse
from database.db import get_database
from utils.auth_utils import get_current_user

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.post("/", response_model=ProfileResponse)
async def create_profile(
    profile: ProfileCreate,
    current_user: str = Depends(get_current_user)
):
    db = get_database()
    profiles_collection = db.profiles
    users_collection = db.users
    
    # Check if profile exists
    existing_profile = await profiles_collection.find_one({"email": current_user})
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile already exists"
        )
    
    # Create profile
    profile_doc = {
        "email": current_user,
        **profile.dict()
    }
    
    await profiles_collection.insert_one(profile_doc)
    
    # Update user has_profile flag
    await users_collection.update_one(
        {"email": current_user},
        {"$set": {"has_profile": True}}
    )
    
    return ProfileResponse(**profile_doc)

@router.get("/", response_model=ProfileResponse)
async def get_profile(current_user: str = Depends(get_current_user)):
    db = get_database()
    profiles_collection = db.profiles
    
    profile = await profiles_collection.find_one({"email": current_user})
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    return ProfileResponse(**profile)

@router.put("/", response_model=ProfileResponse)
async def update_profile(
    profile_update: ProfileUpdate,
    current_user: str = Depends(get_current_user)
):
    db = get_database()
    profiles_collection = db.profiles
    
    # Get existing profile
    existing_profile = await profiles_collection.find_one({"email": current_user})
    if not existing_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    # Update only provided fields
    update_data = {k: v for k, v in profile_update.dict().items() if v is not None}
    
    if update_data:
        await profiles_collection.update_one(
            {"email": current_user},
            {"$set": update_data}
        )
    
    # Fetch updated profile
    updated_profile = await profiles_collection.find_one({"email": current_user})
    
    return ProfileResponse(**updated_profile)