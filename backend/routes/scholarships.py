from fastapi import APIRouter, Depends
from typing import List
from schemas.scholarship import EligibilityResult, WhatIfRequest
from database.db import get_database
from utils.auth_utils import get_current_user
from services.eligibility_engine import check_eligibility
from services.scoring_engine import calculate_score
from services.explanation_engine import generate_explanation

router = APIRouter(prefix="/scholarships", tags=["Scholarships"])


@router.get("/eligible", response_model=List[EligibilityResult])
async def get_eligible_scholarships(
    current_user: str = Depends(get_current_user)
):
    db = get_database()
    profiles_collection = db.profiles
    scholarships_collection = db.scholarships

    profile = await profiles_collection.find_one({"email": current_user})
    if not profile:
        return []

    scholarships = await scholarships_collection.find({}).to_list(length=None)

    results = []

    for scholarship in scholarships:
        is_eligible, reasons = check_eligibility(profile, scholarship)

        if is_eligible:
            score = calculate_score(profile, scholarship)
            explanation = generate_explanation(
                profile,
                scholarship,
                reasons
            )

            results.append(
                EligibilityResult(
                    scholarship_name=scholarship.get("name"),
                    provider=scholarship.get("provider"),
                    amount=scholarship.get("amount"),
                    is_eligible=True,
                    match_score=score,
                    explanation=explanation,
                    description=scholarship.get("description"),
                )
            )

    results.sort(key=lambda x: x.match_score, reverse=True)
    return results


@router.get("/missed", response_model=List[EligibilityResult])
async def get_missed_scholarships(
    current_user: str = Depends(get_current_user)
):
    db = get_database()
    profiles_collection = db.profiles
    scholarships_collection = db.scholarships

    profile = await profiles_collection.find_one({"email": current_user})
    if not profile:
        return []

    scholarships = await scholarships_collection.find({}).to_list(length=None)

    results = []

    for scholarship in scholarships:
        is_eligible, reasons = check_eligibility(profile, scholarship)

        if not is_eligible:
            explanation = generate_explanation(
                profile,
                scholarship,
                reasons
            )

            results.append(
                EligibilityResult(
                    scholarship_name=scholarship.get("name"),
                    provider=scholarship.get("provider"),
                    amount=scholarship.get("amount"),
                    is_eligible=False,
                    match_score=0,
                    explanation=explanation,
                    description=scholarship.get("description"),
                )
            )

    return results


@router.post("/what-if", response_model=List[EligibilityResult])
async def what_if_simulation(
    what_if: WhatIfRequest,
    current_user: str = Depends(get_current_user),
):
    db = get_database()
    profiles_collection = db.profiles
    scholarships_collection = db.scholarships

    profile = await profiles_collection.find_one({"email": current_user})
    if not profile:
        return []

    temp_profile = profile.copy()
    temp_profile["cgpa"] = what_if.cgpa
    temp_profile["income"] = what_if.income

    scholarships = await scholarships_collection.find({}).to_list(length=None)

    results = []

    for scholarship in scholarships:
        is_eligible, reasons = check_eligibility(temp_profile, scholarship)
        score = calculate_score(temp_profile, scholarship) if is_eligible else 0

        explanation = generate_explanation(
            temp_profile,
            scholarship,
            reasons
        )

        results.append(
            EligibilityResult(
                scholarship_name=scholarship.get("name"),
                provider=scholarship.get("provider"),
                amount=scholarship.get("amount"),
                is_eligible=is_eligible,
                match_score=score,
                explanation=explanation,
                description=scholarship.get("description"),
            )
        )

    results.sort(key=lambda x: (x.is_eligible, x.match_score), reverse=True)
    return results
