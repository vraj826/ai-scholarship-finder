def generate_explanation(profile, scholarship, is_eligible, reasons, score):
    """
    Generate human-readable explanation based on reasons dictionary.
    
    Parameters:
    - profile: user profile dict
    - scholarship: scholarship dict
    - is_eligible: boolean eligibility status
    - reasons: dict with True/False/None for each criterion
    - score: integer match score
    
    Returns list of explanation strings.
    """
    
    explanation = []
    
    # ============================================================
    # HEADER
    # ============================================================
    if is_eligible:
        explanation.append(f"✅ You are eligible! Match Score: {score}")
    else:
        explanation.append("❌ You are not eligible for this scholarship")
    
    # ============================================================
    # CGPA EXPLANATION
    # ============================================================
    cgpa_cutoff = scholarship.get("cgpa_cutoff", 0)
    profile_cgpa = profile.get("cgpa", 0)
    
    if reasons.get("cgpa") is True:
        explanation.append(
            f"✔ CGPA {profile_cgpa} meets requirement (≥ {cgpa_cutoff})"
        )
    elif reasons.get("cgpa") is False:
        explanation.append(
            f"✘ CGPA {profile_cgpa} is below requirement (need ≥ {cgpa_cutoff})"
        )
    
    # ============================================================
    # INCOME EXPLANATION
    # ============================================================
    income_limit = scholarship.get("income_limit", 0)
    profile_income = profile.get("income", 0)
    
    if reasons.get("income") is True:
        explanation.append(
            f"✔ Income ₹{profile_income:,} is within limit (≤ ₹{income_limit:,})"
        )
    elif reasons.get("income") is False:
        explanation.append(
            f"✘ Income ₹{profile_income:,} exceeds limit (must be ≤ ₹{income_limit:,})"
        )
    
    # ============================================================
    # CATEGORY EXPLANATION
    # ============================================================
    allowed_categories = scholarship.get("category", [])
    profile_category = profile.get("category", "")
    
    if reasons.get("category") is True:
        explanation.append(
            f"✔ Category '{profile_category}' matches requirement"
        )
    elif reasons.get("category") is False:
        categories_str = ", ".join(allowed_categories)
        explanation.append(
            f"✘ Category '{profile_category}' does not match (need one of: {categories_str})"
        )
    
    # ============================================================
    # GENDER EXPLANATION (OPTIONAL)
    # ============================================================
    required_gender = scholarship.get("gender")
    profile_gender = profile.get("gender", "")
    
    if reasons.get("gender") is True:
        explanation.append(
            f"✔ Gender '{profile_gender}' matches requirement"
        )
    elif reasons.get("gender") is False:
        explanation.append(
            f"✘ This scholarship is only for '{required_gender}' students"
        )
    # If None, skip (not applicable)
    
    # ============================================================
    # STATE EXPLANATION (OPTIONAL)
    # ============================================================
    scholarship_state = scholarship.get("state")
    profile_state = profile.get("state", "")
    
    if reasons.get("state") is True:
        explanation.append(
            f"✔ State '{profile_state}' matches requirement"
        )
    elif reasons.get("state") is False:
        if isinstance(scholarship_state, list):
            states_str = ", ".join(scholarship_state)
            explanation.append(
                f"✘ Your state '{profile_state}' is not in allowed states ({states_str})"
            )
        else:
            explanation.append(
                f"✘ This scholarship is only for '{scholarship_state}' residents"
            )
    # If None, skip (not applicable)
    
    # ============================================================
    # MINORITY EXPLANATION (OPTIONAL)
    # ============================================================
    allowed_minorities = scholarship.get("minority")
    profile_minority = profile.get("minority")
    
    if reasons.get("minority") is True:
        explanation.append(
            f"✔ Minority status '{profile_minority}' matches requirement"
        )
    elif reasons.get("minority") is False:
        if allowed_minorities:
            minorities_str = ", ".join(allowed_minorities)
            current_minority = profile_minority if profile_minority else "None"
            explanation.append(
                f"✘ This scholarship requires minority status from: {minorities_str} (you have: {current_minority})"
            )
    # If None, skip (not applicable)
    
    return explanation