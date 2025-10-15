import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with total cholesterol (or query params as fallback).
    Returns a JSON classification of cholesterol levels.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    cholesterol = data.get("cholesterol", args.get("cholesterol"))

    # Presence check
    if cholesterol is None:
        return (
            json.dumps({"error": "'cholesterol' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        chol_val = float(cholesterol)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'cholesterol' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Conditional statements of total cholesterol level standards
    if chol_val <200:
        status = "optimal"
        category = "Optimal (<200 mg/dL)"
    elif chol_val <240:
        status = "borderline high"
        category = "Borderline High (200-240 mg/dL)"
    else:
        status = "high"
        category = "High (>=240 mg/dL)"

    payload = {
        "cholesterol": chol_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}