def calculate_score(profile, scholarship):
    """
    Calculate a relevance score for a scholarship.
    Higher score = better match
    """

    # Default weights (used if scholarship has none)
    default_weights = {
        "cgpa": 0.4,
        "income": 0.3,
        "category": 0.2,
        "state": 0.1
    }

    # Use scholarship-specific weights if present
    weights = scholarship.get("weights", default_weights)

    score = 0.0

    # =========================
    # CGPA score
    # =========================
    min_cgpa = scholarship.get("min_cgpa")
    if min_cgpa:
        score += weights.get("cgpa", 0) * min(
            profile.get("cgpa", 0) / min_cgpa, 1
        )

    # =========================
    # Income score
    # =========================
    max_income = scholarship.get("max_income")
    if max_income:
        score += weights.get("income", 0) * min(
            max_income / max(profile.get("income", 1), 1), 1
        )

    # =========================
    # Category match
    # =========================
    if scholarship.get("category") == profile.get("category"):
        score += weights.get("category", 0)

    # =========================
    # State match
    # =========================
    if scholarship.get("state") == profile.get("state"):
        score += weights.get("state", 0)

    return round(score, 2)
