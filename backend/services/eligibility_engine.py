def normalize_str(value):
    """Normalize string for case-insensitive comparison"""
    if value is None:
        return None
    return str(value).strip().lower()


def normalize_list(values):
    """Normalize list of strings for comparison"""
    if not values:
        return []
    return [normalize_str(v) for v in values]


def check_eligibility(profile, scholarship):
    """
    Check if a user profile is eligible for a scholarship.
    Returns (is_eligible, reasons_dict)
    
    ALL conditions are evaluated - no early returns.
    Reasons dict contains True/False/None for each criterion.
    """
    
    reasons = {
        "cgpa": None,
        "income": None,
        "category": None,
        "gender": None,
        "state": None,
        "minority": None
    }
    
    # ============================================================
    # NORMALIZE PROFILE DATA
    # ============================================================
    profile_cgpa = float(profile.get("cgpa", 0))
    profile_income = int(profile.get("income", 0))
    profile_category = normalize_str(profile.get("category"))
    profile_gender = normalize_str(profile.get("gender"))
    profile_state = normalize_str(profile.get("state"))
    profile_minority = normalize_str(profile.get("minority"))
    
    # ============================================================
    # NORMALIZE SCHOLARSHIP DATA
    # ============================================================
    cgpa_cutoff = float(scholarship.get("cgpa_cutoff", 0))
    income_limit = int(scholarship.get("income_limit", 0))
    allowed_categories = normalize_list(scholarship.get("category", []))
    required_gender = normalize_str(scholarship.get("gender"))
    scholarship_state = scholarship.get("state")
    allowed_minorities = normalize_list(scholarship.get("minority"))
    
    # Handle state as either string or list
    if scholarship_state:
        if isinstance(scholarship_state, list):
            allowed_states = normalize_list(scholarship_state)
        else:
            allowed_states = [normalize_str(scholarship_state)]
    else:
        allowed_states = []
    
    # ============================================================
    # EVALUATE ALL CONDITIONS (NO EARLY RETURNS)
    # ============================================================
    
    # CGPA Check (mandatory)
    reasons["cgpa"] = profile_cgpa >= cgpa_cutoff
    
    # Income Check (mandatory)
    reasons["income"] = profile_income <= income_limit
    
    # Category Check (mandatory)
    reasons["category"] = profile_category in allowed_categories
    
    # Gender Check (optional - only if scholarship has requirement)
    if required_gender is not None:
        reasons["gender"] = profile_gender == required_gender
    else:
        reasons["gender"] = None  # Not applicable
    
    # State Check (optional - only if scholarship has requirement)
    if allowed_states:
        reasons["state"] = profile_state in allowed_states
    else:
        reasons["state"] = None  # Not applicable
    
    # Minority Check (optional - only if scholarship has requirement)
    if allowed_minorities:
        reasons["minority"] = profile_minority in allowed_minorities
    else:
        reasons["minority"] = None  # Not applicable
    
    # ============================================================
    # DETERMINE OVERALL ELIGIBILITY
    # ============================================================
    # All mandatory checks must be True
    mandatory_failed = (
        reasons["cgpa"] is False or
        reasons["income"] is False or
        reasons["category"] is False
    )
    
    # Any applicable optional check must be True (not False)
    optional_failed = (
        reasons["gender"] is False or
        reasons["state"] is False or
        reasons["minority"] is False
    )
    
    is_eligible = not (mandatory_failed or optional_failed)
    
    return is_eligible, reasons