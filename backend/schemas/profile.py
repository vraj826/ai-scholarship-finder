from pydantic import BaseModel, Field
from typing import Optional

class ProfileCreate(BaseModel):
    name: str = Field(..., min_length=1)
    cgpa: float = Field(..., ge=0.0, le=10.0)
    income: int = Field(..., ge=0)
    category: str  # General, OBC, SC, ST
    gender: str  # Male, Female, Other
    state: str
    minority: Optional[str] = None  # Muslim, Christian, Sikh, Buddhist, Jain, Parsi, None

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    cgpa: Optional[float] = Field(None, ge=0.0, le=10.0)
    income: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None
    gender: Optional[str] = None
    state: Optional[str] = None
    minority: Optional[str] = None

class ProfileResponse(BaseModel):
    email: str
    name: str
    cgpa: float
    income: int
    category: str
    gender: str
    state: str
    minority: Optional[str] = None