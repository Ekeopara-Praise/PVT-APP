import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

# Home Menu
home = st.Page(
    "Home/home.py", title="PVTSmart", icon=":material/home:", default=True
)
# Data Menu
upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:",)
view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:",)

# Match Menu
black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation", icon=":material/schema:")
view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")

# Predict Menu
predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")

# Settings Menu
settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [home],
            "Data": [upload_data, view_data],
            "Match": [black_oil_correlation, view_results],
            "Predict": [predict],
            "Settings": [settings],
            "Exit App": [logout_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

# import streamlit as st
#
# # Define pages
# pages = ["Home", "Data", "Match", "Predict", "Settings", "Help"]
#
# # Initialize session state
# if "selected_page" not in st.session_state:
#     st.session_state.selected_page = "Home"
#
# # Render navigation bar using Streamlit columns only
# cols = st.columns(len(pages))
# for i, page in enumerate(pages):
#     if cols[i].button(page):
#         st.session_state.selected_page = page
#
# # # Separator
# # st.divider()
#
# # Page content
# page = st.session_state.selected_page
# if page == "Home":
#     st.title("🏠 Welcome to the Home Page!")
#     st.write("This is your dashboard. Use the menu to navigate.")
# elif page == "Data":
#     st.title("📊 Data Page")
#     st.write("Upload and manage your data here.")
# elif page == "Match":
#     st.title("🔗 Match Page")
#     st.write("Match your input with existing profiles.")
# elif page == "Predict":
#     st.title("📈 Predict Page")
#     st.write("Use our models to predict outcomes.")
# elif page == "Settings":
#     st.title("⚙️ Settings Page")
#     st.write("Customize your preferences and configuration.")
# elif page == "Help":
#     st.title("❓ Help Page")
#     st.write("Get support and guidance here.")
