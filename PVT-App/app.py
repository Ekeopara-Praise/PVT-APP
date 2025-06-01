import streamlit as st

# Define pages
pages = ["Home", "Data", "Match", "Predict", "Settings", "Help"]

# Initialize session state
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# Render navigation bar using Streamlit columns only
cols = st.columns(len(pages))
for i, page in enumerate(pages):
    if cols[i].button(page):
        st.session_state.selected_page = page

# # Separator
# st.divider()

# Page content
page = st.session_state.selected_page
if page == "Home":
    st.title("🏠 Welcome to the Home Page!")
    st.write("This is your dashboard. Use the menu to navigate.")
elif page == "Data":
    st.title("📊 Data Page")
    st.write("Upload and manage your data here.")
elif page == "Match":
    st.title("🔗 Match Page")
    st.write("Match your input with existing profiles.")
elif page == "Predict":
    st.title("📈 Predict Page")
    st.write("Use our models to predict outcomes.")
elif page == "Settings":
    st.title("⚙️ Settings Page")
    st.write("Customize your preferences and configuration.")
elif page == "Help":
    st.title("❓ Help Page")
    st.write("Get support and guidance here.")
