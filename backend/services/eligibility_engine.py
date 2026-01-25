def check_eligibility(profile, scholarship):
    """
    Check if a user profile is eligible for a scholarship.
    Returns (is_eligible, reasons_dict)
    """

    reasons = {
        "cgpa": None,
        "income": None,
        "category": None,
        "gender": None,
        "state": None,
        "minority": None
    }

    # =========================
    # CGPA Check
    # =========================
    min_cgpa = scholarship.get("min_cgpa")
    if min_cgpa is not None:
        reasons["cgpa"] = profile.get("cgpa", 0) >= min_cgpa
    else:
        reasons["cgpa"] = True  # No CGPA restriction

    # =========================
    # Income Check
    # =========================
    max_income = scholarship.get("max_income")
    if max_income is not None:
        reasons["income"] = profile.get("income", 0) <= max_income
    else:
        reasons["income"] = True  # No income restriction

    # =========================
    # Category Check
    # =========================
    scholarship_category = scholarship.get("category")
    if scholarship_category:
        reasons["category"] = profile.get("category") == scholarship_category
    else:
        reasons["category"] = True  # Open to all categories

    # =========================
    # Gender Check (optional)
    # =========================
    scholarship_gender = scholarship.get("gender")
    if scholarship_gender:
        reasons["gender"] = profile.get("gender") == scholarship_gender
    else:
        reasons["gender"] = None  # Not applicable

    # =========================
    # State Check (optional)
    # =========================
    scholarship_state = scholarship.get("state")
    if scholarship_state:
        reasons["state"] = profile.get("state") == scholarship_state
    else:
        reasons["state"] = None  # Not applicable

    # =========================
    # Minority Check (optional)
    # =========================
    scholarship_minority = scholarship.get("minority")
    if scholarship_minority:
        reasons["minority"] = (
            profile.get("minority") is not None
            and profile.get("minority") in scholarship_minority
        )
    else:
        reasons["minority"] = None  # Not applicable

    # =========================
    # Final Eligibility Decision
    # =========================
    mandatory_checks = ["cgpa", "income", "category"]

    for check in mandatory_checks:
        if reasons[check] is False:
            return False, reasons

    for optional in ["gender", "state", "minority"]:
        if reasons[optional] is False:
            return False, reasons

    return True, reasons
