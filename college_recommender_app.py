import streamlit as st
import pandas as pd

# Sample college data
data = {
    "College": ["ABC Institute", "XYZ University", "Tech College", "Data School"],
    "Program": ["B.Tech AI & DS", "BCA AI", "MCA Data Science", "BSc AI"],
    "Location": ["Bangalore", "Chennai", "Bangalore", "Hyderabad"],
    "Min Score": [60, 55, 65, 50],
    "Domain": ["Data Science", "Artificial Intelligence", "Data Science", "AI"]
}
colleges_df = pd.DataFrame(data)

# Streamlit UI
st.title("🎓 AI College Recommendation System")

st.markdown("Enter your academic details to get personalized college suggestions.")

# User Input
name = st.text_input("Your Name")
interests = st.multiselect("Select Your Interest Areas", colleges_df["Domain"].unique())
score = st.number_input("Your Graduation Score (%)", min_value=0, max_value=100, value=70)
location = st.selectbox("Preferred Location", colleges_df["Location"].unique())

if st.button("Get Recommendations"):
    student_profile = {
        "name": name,
        "interests": interests,
        "score_graduation": score,
        "preferred_location": location
    }

    # Match logic
    matches = colleges_df[
        (colleges_df["Domain"].isin(student_profile["interests"])) &
        (colleges_df["Min Score"] <= student_profile["score_graduation"]) &
        (colleges_df["Location"] == student_profile["preferred_location"])
    ]

    if matches.empty:
        st.warning("😕 No colleges matched your profile. Try changing your preferences.")
    else:
        st.success("🎯 Recommended Colleges Based on Your Profile:")
        st.dataframe(matches)

        # Save and download
        matches.to_csv("recommended_colleges.csv", index=False)
        with open("recommended_colleges.csv", "rb") as file:
            st.download_button("📁 Download Recommendations", file, file_name="recommended_colleges.csv")

    # Optional advice
    st.markdown("### 📝 Advice")
    if score < 60:
        st.info("🔹 Try to improve your score or consider diploma programs.")
    elif location not in colleges_df["Location"].unique():
        st.info("🔹 Consider expanding your preferred location.")
    elif matches.empty:
        st.info("🔹 No exact match found. Try adjusting your interests.")
    else:
        st.success("🎉 Great fit! These programs align well with your profile.")