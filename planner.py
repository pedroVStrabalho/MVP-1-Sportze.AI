def generate_training_session(sport, goal, level, pain):
    if pain >= 7:
        return "High pain reported. Avoid hard training and seek a qualified professional."

    if sport == "Tennis":
        return [
            "5 min light bike",
            "Dynamic mobility",
            "Lateral movement drills",
            "Split squat 3x8",
            "Single-leg RDL 3x8",
            "Core rotation 3x12",
        ]

    return [
        "5 min warm-up",
        "Movement prep",
        "Main exercises",
        "Cooldown",
    ]
