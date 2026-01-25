from pydantic import BaseModel
from typing import Optional, List, Dict

class Scholarship(BaseModel):
    name: str
    provider: str
    amount: int
    category: List[str]
    income_limit: int
    cgpa_cutoff: float
    gender: Optional[str] = None
    state: Optional[str] = None
    minority: Optional[List[str]] = None
    weights: Dict[str, int]
    description: str