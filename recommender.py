import pandas as pd


def load_data():
    return pd.read_csv("food_centers.csv")


def calculate_recommendations(
    food_type,
    quantity,
    refrigeration,
    urgency,
    population
):
    centers = load_data()
    recommendations = []

    for _, center in centers.iterrows():
        score = 0
        reasons = []

        # Food type match = 30 points
        if center["food_type"] == food_type:
            score += 30
            reasons.append("accepts this type of food")

        # Refrigeration match = 25 points
        if center["refrigeration"] == refrigeration:
            score += 25
            reasons.append("matches the storage requirement")

        # Capacity match = 20 points
        if quantity <= center["max_capacity"]:
            score += 20
            reasons.append("has enough capacity for this donation")

        # Urgency match = 15 points
        if center["urgency"] == urgency:
            score += 15
            reasons.append("matches the distribution urgency")

        # Community preference match = 10 points
        if population == "No Preference":
            score += 10
            reasons.append("is suitable without a population preference")
        elif center["population_served"] == population:
            score += 10
            reasons.append("serves the preferred community")

        recommendations.append({
            "center_name": center["center_name"],
            "score": score,
            "reason": ", ".join(reasons)
        })

    recommendations = sorted(
        recommendations,
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations[:3]
