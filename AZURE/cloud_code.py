import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse: 
    """HTTP Azure Function.
    Expects JSON with total cholesterol (or query params as fallback).
    Returns a JSON classification of cholesterol levels.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    args = req.params

    cholesterol = data.get("cholesterol", args.get("cholesterol"))

    # Presence check
    if cholesterol is None:
        return func.HttpResponse(
           body= json.dumps({"error": "'cholesterol' is required."}),
            status_code=400,
            headers={"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        chol_val = float(cholesterol)
    except (TypeError, ValueError):
        return func.HttpResponse(
            body= json.dumps({"error": "'cholesterol' must be a number."}),
            status_code=400,
            headers={"Content-Type": "application/json"},
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

    return func.HttpResponse(
        body= json.dumps(payload), 
        status_code=200, 
        headers={"Content-Type": "application/json"}
    )