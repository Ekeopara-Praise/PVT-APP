import streamlit as st

# Set page layout to wide for better positioning
st.set_page_config(layout="wide")

# Create three columns to center the logo
# coln1, coln2, coln3 = st.columns([1, 3, 1])  # Middle column is wider

# Place the logo in the center column
# with coln2:
st.logo("logo.PNG")

# Initialize session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Form
def login():
    with st.form(key="login_form", border=True):
        coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
        with coln2:
            st.image("logo.PNG")
            login_button = st.form_submit_button("Log in", use_container_width=True)
            if login_button:
                st.session_state.logged_in = True
                st.rerun()

# Logout Form
def logout():
    with st.form(key="logout_form", border=True):
        coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
        with coln2:
            st.image("logo.PNG")
        #st.write("Log out from your account")
            logout_button = st.form_submit_button("Log out", use_container_width=True)
            if logout_button:
                st.session_state.logged_in = False
                st.rerun()

# Define Login/Logout Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

# Define App Menu Structure
home = st.Page("Home/home.py", title="PVTSmart", icon=":material/home:", default=True)
upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:")
view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:")
black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation", icon=":material/schema:")
view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")
predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")
settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")

# Navigation logic based on login state
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
