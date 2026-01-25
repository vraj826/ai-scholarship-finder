def normalize_str(value):
    if value is None:
        return None
    return str(value).strip().lower()


def normalize_list(values):
    if not values:
        return []
    return [normalize_str(v) for v in values]


def check_eligibility(profile, scholarship):
    """
    Strict eligibility check.
    ALL mandatory conditions must pass.
    Optional conditions are checked only if present in scholarship.
    """

    reasons = {}

    # ---------------- PROFILE NORMALIZATION ----------------
    profile_cgpa = float(profile.get("cgpa", 0))
    profile_income = float(profile.get("income", 0))
    profile_category = normalize_str(profile.get("category"))
    profile_gender = normalize_str(profile.get("gender"))
    profile_state = normalize_str(profile.get("state"))
    profile_minority = normalize_str(profile.get("minority"))

    # ---------------- SCHOLARSHIP NORMALIZATION ----------------
    cgpa_cutoff = float(scholarship.get("cgpa_cutoff", 0))
    income_limit = float(scholarship.get("income_limit", 0))
    allowed_categories = normalize_list(scholarship.get("category"))
    required_gender = normalize_str(scholarship.get("gender"))
    required_state = normalize_str(scholarship.get("state"))
    allowed_minorities = normalize_list(scholarship.get("minority"))

    # ---------------- CGPA CHECK ----------------
    reasons["cgpa"] = profile_cgpa >= cgpa_cutoff

    # ---------------- INCOME CHECK ----------------
    reasons["income"] = profile_income <= income_limit

    # ---------------- CATEGORY CHECK ----------------
    reasons["category"] = profile_category in allowed_categories

    # ---------------- GENDER CHECK (OPTIONAL) ----------------
    if required_gender:
        reasons["gender"] = profile_gender == required_gender
    else:
        reasons["gender"] = None  # Not applicable

    # ---------------- STATE CHECK (OPTIONAL) ----------------
    if required_state:
        reasons["state"] = profile_state == required_state
    else:
        reasons["state"] = None  # Not applicable

    # ---------------- MINORITY CHECK (OPTIONAL) ----------------
    if allowed_minorities:
        reasons["minority"] = profile_minority in allowed_minorities
    else:
        reasons["minority"] = None  # Not applicable

    # ---------------- FINAL DECISION ----------------
    mandatory_checks = ["cgpa", "income", "category"]

    for check in mandatory_checks:
        if reasons[check] is False:
            return False, reasons

    # Optional checks must pass IF applicable
    for optional in ["gender", "state", "minority"]:
        if reasons[optional] is False:
            return False, reasons

    return True, reasons
