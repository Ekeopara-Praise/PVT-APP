import streamlit as st
# Make sure this import works in your deployment environment
from streamlit_navigation_bar import st_navbar

# Define your navigation pages
pages = ["Home", "Data", "Match", "Predict", "Settings", "Help"]
logo_path = None  # Optional logo

# Define styling for the navigation bar
styles = {
    "nav": {
        "background-color": "#283747",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    }
}

# Options for the navigation bar
options = {
    "show_menu": True,
    "show_sidebar": False,
}

# Create the navigation bar
page = st_navbar(
    pages,
    selected='Home',
    logo_path=logo_path,
    styles=styles,
    options=options,
)

# ✅ Debug output to check what's being returned
st.write("Selected page:", page)

# Render the appropriate page content
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
