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
    
    # Check CGPA
    if profile["cgpa"] >= scholarship["cgpa_cutoff"]:
        reasons["cgpa"] = True
    else:
        reasons["cgpa"] = False
    
    # Check Income
    if profile["income"] <= scholarship["income_limit"]:
        reasons["income"] = True
    else:
        reasons["income"] = False
    
    # Check Category
    if profile["category"] in scholarship["category"]:
        reasons["category"] = True
    else:
        reasons["category"] = False
    
    # Check Gender (if scholarship has gender requirement)
    if scholarship["gender"] is not None:
        if profile["gender"] == scholarship["gender"]:
            reasons["gender"] = True
        else:
            reasons["gender"] = False
    else:
        reasons["gender"] = None  # Not applicable
    
    # Check State (if scholarship has state requirement)
    if scholarship["state"] is not None:
        if profile["state"] == scholarship["state"]:
            reasons["state"] = True
        else:
            reasons["state"] = False
    else:
        reasons["state"] = None  # Not applicable
    
    # Check Minority (if scholarship has minority requirement)
    if scholarship["minority"] is not None:
        if profile["minority"] and profile["minority"] in scholarship["minority"]:
            reasons["minority"] = True
        else:
            reasons["minority"] = False
    else:
        reasons["minority"] = None  # Not applicable
    
    # Determine overall eligibility
    # All mandatory checks must pass
    mandatory_checks = ["cgpa", "income", "category"]
    for check in mandatory_checks:
        if reasons[check] is False:
            return False, reasons
    
    # Gender check (if applicable)
    if reasons["gender"] is False:
        return False, reasons
    
    # State check (if applicable)
    if reasons["state"] is False:
        return False, reasons
    
    # Minority check (if applicable)
    if reasons["minority"] is False:
        return False, reasons
    
    return True, reasons