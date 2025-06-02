# import streamlit as st
#
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#
# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()
#
# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()
#
# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
#
# # Home Menu
# home = st.Page(
#     "Home/home.py", title="PVTSmart", icon=":material/home:", default=True
# )
# # Data Menu
# upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:",)
# view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:",)
#
# # Match Menu
# black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation", icon=":material/schema:")
# view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")
#
# # Predict Menu
# predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")
#
# # Settings Menu
# settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")
#
#
# if st.session_state.logged_in:
#     pg = st.navigation(
#         {
#             "Home": [home],
#             "Data": [upload_data, view_data],
#             "Match": [black_oil_correlation, view_results],
#             "Predict": [predict],
#             "Settings": [settings],
#             "Exit App": [logout_page],
#         }
#     )
# else:
#     pg = st.navigation([login_page])
#
# pg.run()

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


# st.logo(image="logo.png")

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