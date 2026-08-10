import streamlit as st
from recommender import calculate_recommendations


# Configure the Streamlit page
st.set_page_config(
    page_title="Community Food Rescue Recommender",
    page_icon="🥕",
    layout="centered"
)


# Application title
st.title("🥕 Community Food Rescue Recommender")

st.write(
    "This recommendation system helps match surplus food donations "
    "with suitable fictional community food centers."
)


# User input section
st.subheader("Enter Donation Details")

food_type = st.selectbox(
    "Food Type",
    [
        "Fresh Produce",
        "Packaged Food",
        "Dairy",
        "Grains"
    ]
)

quantity = st.number_input(
    "Quantity (lbs)",
    min_value=1,
    max_value=200,
    value=25
)

refrigeration = st.selectbox(
    "Does the food require refrigeration?",
    ["Yes", "No"]
)

urgency = st.selectbox(
    "Distribution Urgency",
    [
        "High",
        "Medium",
        "Low"
    ]
)

population = st.selectbox(
    "Preferred Community",
    [
        "No Preference",
        "Families",
        "Seniors",
        "Youth",
        "General Community"
    ]
)


# Recommendation button
if st.button("Find Best Matches"):

    recommendations = calculate_recommendations(
        food_type,
        quantity,
        refrigeration,
        urgency,
        population
    )

    st.subheader("Top 3 Recommended Centers")

    # Display each recommendation
    for position, recommendation in enumerate(
        recommendations,
        start=1
    ):

        st.markdown(
            f"### {position}. {recommendation['center_name']}"
        )

        score = recommendation["score"]

        # Visual progress bar for recommendation score
        st.progress(score / 100)

        st.write(
            f"**Match Score:** {score}%"
        )

        # Convert the numerical score into
        # an easy-to-understand confidence level
        if score >= 90:
            confidence = "Excellent Match"
        elif score >= 75:
            confidence = "Strong Match"
        elif score >= 60:
            confidence = "Moderate Match"
        else:
            confidence = "Limited Match"

        st.write(
            f"**Recommendation Confidence:** {confidence}"
        )

        # Explain why the recommendation was generated
        st.write(
            f"**Why recommended:** "
            f"{recommendation['reason']}."
        )

        st.divider()


# Ethical transparency notice
st.caption(
    "Academic prototype: All community center names and data "
    "used in this application are fictional."
)