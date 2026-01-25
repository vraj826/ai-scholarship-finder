def calculate_score(profile, scholarship):
    """
    Calculate match score (0-100) based on scholarship weights.
    Higher score = better match for eligible scholarships.
    
    Returns integer score between 0 and 100.
    """
    
    score = 0
    
    # Get weights from scholarship (with defaults if missing)
    weights = scholarship.get("weights", {})
    
    # ============================================================
    # NORMALIZE DATA
    # ============================================================
    profile_cgpa = float(profile.get("cgpa", 0))
    profile_income = int(profile.get("income", 0))
    profile_category = str(profile.get("category", "")).strip().lower()
    profile_gender = str(profile.get("gender", "")).strip().lower()
    profile_state = str(profile.get("state", "")).strip().lower()
    profile_minority = profile.get("minority")
    if profile_minority:
        profile_minority = str(profile_minority).strip().lower()
    
    cgpa_cutoff = float(scholarship.get("cgpa_cutoff", 0))
    income_limit = int(scholarship.get("income_limit", 1))
    
    allowed_categories = [str(c).strip().lower() for c in scholarship.get("category", [])]
    
    required_gender = scholarship.get("gender")
    if required_gender:
        required_gender = str(required_gender).strip().lower()
    
    scholarship_state = scholarship.get("state")
    if scholarship_state:
        if isinstance(scholarship_state, list):
            allowed_states = [str(s).strip().lower() for s in scholarship_state]
        else:
            allowed_states = [str(scholarship_state).strip().lower()]
    else:
        allowed_states = []
    
    allowed_minorities = scholarship.get("minority")
    if allowed_minorities:
        allowed_minorities = [str(m).strip().lower() for m in allowed_minorities]
    else:
        allowed_minorities = []
    
    # ============================================================
    # CGPA SCORING
    # ============================================================
    cgpa_weight = weights.get("cgpa", 0)
    if cgpa_weight > 0 and profile_cgpa >= cgpa_cutoff:
        # Base points for meeting cutoff
        score += cgpa_weight
        
        # Bonus points for exceeding cutoff (up to 50% of base weight)
        if cgpa_cutoff > 0:
            excess_ratio = min((profile_cgpa - cgpa_cutoff) / cgpa_cutoff, 0.5)
            score += int(cgpa_weight * excess_ratio)
    
    # ============================================================
    # INCOME SCORING
    # ============================================================
    income_weight = weights.get("income", 0)
    if income_weight > 0 and profile_income <= income_limit:
        # More points for lower income relative to limit
        income_ratio = 1 - (profile_income / max(income_limit, 1))
        score += int(income_weight * income_ratio)
    
    # ============================================================
    # CATEGORY MATCH
    # ============================================================
    category_weight = weights.get("category_match", 0)
    if category_weight > 0 and profile_category in allowed_categories:
        score += category_weight
    
    # ============================================================
    # GENDER MATCH (OPTIONAL)
    # ============================================================
    gender_weight = weights.get("gender_match", 0)
    if gender_weight > 0 and required_gender and profile_gender == required_gender:
        score += gender_weight
    
    # ============================================================
    # STATE MATCH (OPTIONAL)
    # ============================================================
    state_weight = weights.get("state_match", 0)
    if state_weight > 0 and allowed_states and profile_state in allowed_states:
        score += state_weight
    
    # ============================================================
    # MINORITY MATCH (OPTIONAL)
    # ============================================================
    minority_weight = weights.get("minority_match", 0)
    if minority_weight > 0 and allowed_minorities and profile_minority in allowed_minorities:
        score += minority_weight
    
    # Ensure score is within 0-100 range
    final_score = max(0, min(100, int(score)))
    
    return final_score