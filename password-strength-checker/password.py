import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS for better UI
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput {
        border-radius: 10px;
        padding: 8px;
    }
    .stTitle {
        color: #3c3c3c;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
    }
    .stMarkdown {
        font-size: 18px;
    }
    .stButton>button {
        background-color: #d4e5ef;
        color: #0c2a5a;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0c2a5a;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("🔒 Password Strength Checker")

# Introduction
st.markdown("""
## Welcome to the ultimate password strength checker! 
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **strong password** 💡""")


# Password Input
password = st.text_input("Enter Password", type="password")

st.button("Check Strength 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters long**.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase and lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number**.")

    if re.search(r"[!@#$%&*,.]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (!@#$%^&*)**.")

    return score, feedback

 

# Checking Password Strength
if password:
    score, feedback = check_password_strength(password)

    # Strength Levels
    strength_levels = ["❌ Very Weak", "⚠️ Weak", "⚠️ Moderate", "✅ Good", "👏 Strong"]
    
    # Progress Bar
    st.progress(score / 4)

    # Display Strength Level
    st.markdown(f"### **Strength Level:** {strength_levels[score]}")

    # Show Feedback & Suggestions
    if feedback:
        st.markdown("### **🔹 Suggestions to Improve Your Password:**")
        for tip in feedback:
            st.write(tip)
    else:
        st.success("🎉 Your password is strong! Great job!")

        
   
    
    
else:
    st.info("🔹 Please enter a password to check its strength.")