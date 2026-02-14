def check_no_surprises_act(bill_data: dict) -> dict | None:
    """
    Check if the No Surprises Act (2022) may apply to this bill.

    NSA protects patients from:
    1. Surprise out-of-network bills for emergency services
    2. Out-of-network bills from providers at in-network facilities
    3. Air ambulance bills from out-of-network providers
    """
    line_items = bill_data.get("line_items", [])

    emergency = any(
        item.get("cpt_code") and item["cpt_code"].startswith("9928")
        for item in line_items
    )

    total_charged = bill_data.get("total_charged", 1) or 1
    total_patient_owes = bill_data.get("total_patient_owes", 0) or 0
    high_patient_responsibility = total_patient_owes > total_charged * 0.5

    out_of_network = any(
        "out of network" in (item.get("description", "").lower())
        or "non-par" in (item.get("description", "").lower())
        for item in line_items
    )

    if not emergency:
        return None

    if not (high_patient_responsibility or out_of_network):
        return None

    return {
        "type": "no_surprises_act",
        "applicable": True,
        "severity": "high",
        "potential_savings": round(total_patient_owes * 0.5, 2),
        "message": (
            "This appears to be an emergency visit with high out-of-pocket costs. "
            "The No Surprises Act (2022) protects you from surprise out-of-network "
            "bills for emergency services. Your insurer should cover this at "
            "in-network rates. If you're being balance-billed, you have the right "
            "to dispute."
        ),
    }
