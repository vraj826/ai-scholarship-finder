from pydantic import BaseModel
from typing import List, Optional

class EligibilityResult(BaseModel):
    scholarship_name: str
    provider: str
    amount: int
    is_eligible: bool
    match_score: int
    explanation: List[str]
    description: str

class WhatIfRequest(BaseModel):
    cgpa: float
    income: int