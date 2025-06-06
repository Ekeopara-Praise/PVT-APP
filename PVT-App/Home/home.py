# import streamlit as st
# from pathlib import Path
#
# # Set page layout to wide for better positioning
# st.set_page_config(layout="wide")
#
#
# # Initialize session state for login tracking
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#
#
# # Function to handle image loading safely
# def load_image(image_path):
#     try:
#         resolved_path = Path(__file__).parent / image_path
#         if resolved_path.exists():
#             return str(resolved_path)
#         if Path(image_path).exists():
#             return image_path
#         raise FileNotFoundError
#     except:
#         return None
#
#
# # Login Form (now with proper submit button)
# def login():
#     with st.form(key="login_form", border=True):
#         coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
#         with coln2:
#             logo_path = load_image("logo_.jpg")
#             if logo_path:
#                 st.image(logo_path)
#             else:
#                 st.warning("Logo image not found")
#
#             # # Added username/password fields for proper form submission
#             # username = st.text_input("Username")
#             # password = st.text_input("Password", type="password")
#
#             # Proper submit button
#             submitted = st.form_submit_button("Log in", use_container_width=True)
#             if submitted:
#                 # if username and password:  # Basic validation
#                 st.session_state.logged_in = True
#                 st.rerun()
#                 # else:
#                 #     st.error("Please enter both username and password")
#
#
# # Logout Form (with proper submit button)
# def logout():
#     with st.form(key="logout_form", border=True):
#         coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
#         with coln2:
#             logo_path = load_image("logo_.jpg")
#             if logo_path:
#                 st.image(logo_path)
#             else:
#                 st.warning("Logo image not found")
#
#             # Proper submit button
#             submitted = st.form_submit_button("Log out", use_container_width=True)
#             if submitted:
#                 st.session_state.logged_in = False
#                 st.rerun()
#
#
# # Define Login/Logout Pages
# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
#
# # Define App Menu Structure
# home = st.Page("Home/home.py", title="PVTSmart", icon=":material/home:", default=True)
# upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:")
# view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:")
# black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation",
#                                 icon=":material/schema:")
# view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")
# predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")
# settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")
#
# # Navigation logic based on login state
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
#
# # import streamlit as st
# # import os
# # from pathlib import Path
# #
# # # --- Page Configuration ---
# # st.set_page_config(
# #     page_title="PVT Smart App",
# #     page_icon="🛢️",
# #     layout="wide"
# # )
# #
# # # --- Session State Initialization ---
# # if "logged_in" not in st.session_state:
# #     st.session_state.logged_in = False
# #
# #
# # # --- Path Handling ---
# # def get_image_path(image_name):
# #     """Helper function to locate image files"""
# #     try:
# #         base_path = Path(__file__).parent
# #         return base_path / image_name
# #     except:
# #         return image_name  # Fallback to direct path if error
# #
# #
# # # --- Login/Logout Functions ---
# # def login():
# #     """Login page with form and validation"""
# #     with st.form(key="login_form", border=True):
# #         col1, col2, col3 = st.columns([1.5, 1, 1.5])
# #
# #         with col2:
# #             # Load logo with error handling
# #             logo_path = get_image_path("logo_.jpg")
# #             try:
# #                 st.image(str(logo_path), use_column_width=True)
# #             except Exception as e:
# #                 st.warning(f"Logo not found at: {logo_path}")
# #                 st.error("Please contact admin - missing logo file")
# #
# #             # Login form elements
# #             username = st.text_input("Username")
# #             password = st.text_input("Password", type="password")
# #
# #             if st.form_submit_button("Log in", use_container_width=True):
# #                 # Basic validation (replace with real auth)
# #                 if username and password:  # Add your auth logic here
# #                     st.session_state.logged_in = True
# #                     st.session_state.user = username
# #                     st.rerun()
# #                 else:
# #                     st.error("Please enter credentials")
# #
# #
# # def logout():
# #     """Logout confirmation page"""
# #     with st.form(key="logout_form", border=True):
# #         col1, col2, col3 = st.columns([1.5, 1, 1.5])
# #
# #         with col2:
# #             logo_path = get_image_path("logo_.jpg")
# #             try:
# #                 st.image(str(logo_path), use_column_width=True)
# #             except:
# #                 st.warning("App logo")
# #
# #             st.markdown(f"**Logged in as:** {st.session_state.get('user', 'Unknown')}")
# #
# #             if st.form_submit_button("Log out", use_container_width=True):
# #                 st.session_state.logged_in = False
# #                 st.session_state.pop("user", None)
# #                 st.rerun()
# #
# #
# # # --- Page Definitions ---
# # def get_page_sections():
# #     """Returns properly structured navigation sections"""
# #     return [
# #         st.NavigationSection(
# #             "Home",
# #             [
# #                 st.Page(
# #                     "Home/home.py",
# #                     title="PVT Smart",
# #                     icon="🏠",
# #                     default=True
# #                 )
# #             ]
# #         ),
# #         st.NavigationSection(
# #             "Data",
# #             [
# #                 st.Page(
# #                     "Data/upload_data.py",
# #                     title="Upload Data",
# #                     icon="📤"
# #                 ),
# #                 st.Page(
# #                     "Data/view_data.py",
# #                     title="View Data",
# #                     icon="👀"
# #                 )
# #             ]
# #         ),
# #         st.NavigationSection(
# #             "Match",
# #             [
# #                 st.Page(
# #                     "Match/BlackOil_correlation.py",
# #                     title="Black Oil Correlation",
# #                     icon="📊"
# #                 ),
# #                 st.Page(
# #                     "Match/view_results.py",
# #                     title="View Results",
# #                     icon="🔍"
# #                 )
# #             ]
# #         ),
# #         st.NavigationSection(
# #             "Predict",
# #             [
# #                 st.Page(
# #                     "Predict/predict.py",
# #                     title="Predict",
# #                     icon="🔮"
# #                 )
# #             ]
# #         ),
# #         st.NavigationSection(
# #             "Settings",
# #             [
# #                 st.Page(
# #                     "Settings/settings.py",
# #                     title="Settings",
# #                     icon="⚙️"
# #                 )
# #             ]
# #         )
# #     ]
# #
# #
# # # --- Main App Logic ---
# # def main():
# #     # Create login/logout pages
# #     login_page = st.Page(login, title="Login", icon="🔑")
# #     logout_page = st.Page(logout, title="Logout", icon="🚪")
# #
# #     # Navigation based on auth state
# #     if st.session_state.logged_in:
# #         sections = get_page_sections()
# #         # Add logout to navigation
# #         sections.append(
# #             st.NavigationSection(
# #                 "Exit",
# #                 [logout_page]
# #             )
# #         )
# #         pg = st.navigation(sections)
# #     else:
# #         pg = st.navigation([login_page])
# #
# #     pg.run()
# #
# #
# # if __name__ == "__main__":
# #     main()
# #
# #
# # # import streamlit as st
# # #
# # # # Set page layout to wide for better positioning
# # # st.set_page_config(layout="wide")
# # #
# # # # Create three columns to center the logo
# # # # coln1, coln2, coln3 = st.columns([1, 3, 1])  # Middle column is wider
# # #
# # # # Place the logo in the center column
# # # # with coln2:
# # #
# # #
# # # # Initialize session state for login tracking
# # # if "logged_in" not in st.session_state:
# # #     st.session_state.logged_in = False
# # #
# # # # Login Form
# # # def login():
# # #     with st.form(key="login_form", border=True):
# # #         coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
# # #         with coln2:
# # #             st.image("logo.PNG")
# # #             login_button = st.form_submit_button("Log in", use_container_width=True)
# # #             if login_button:
# # #                 st.session_state.logged_in = True
# # #                 st.rerun()
# # #
# # # # Logout Form
# # # def logout():
# # #     with st.form(key="logout_form", border=True):
# # #         coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
# # #         with coln2:
# # #             st.image("logo.PNG")
# # #         #st.write("Log out from your account")
# # #             logout_button = st.form_submit_button("Log out", use_container_width=True)
# # #             if logout_button:
# # #                 st.session_state.logged_in = False
# # #                 st.rerun()
# # #
# # # # Define Login/Logout Pages
# # # login_page = st.Page(login, title="Log in", icon=":material/login:")
# # # logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# # #
# # # # Define App Menu Structure
# # # home = st.Page("Home/home.py", title="PVTSmart", icon=":material/home:", default=True)
# # # upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:")
# # # view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:")
# # # black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation", icon=":material/schema:")
# # # view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")
# # # predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")
# # # settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")
# # #
# # # # Navigation logic based on login state
# # # if st.session_state.logged_in:
# # #     pg = st.navigation(
# # #         {
# # #             "Home": [home],
# # #             "Data": [upload_data, view_data],
# # #             "Match": [black_oil_correlation, view_results],
# # #             "Predict": [predict],
# # #             "Settings": [settings],
# # #             "Exit App": [logout_page],
# # #         }
# # #     )
# # # else:
# # #     pg = st.navigation([login_page])
# # #
# # # pg.run()
# # #
# # # st.logo(r"logo.png")
# # #
# # # # import streamlit as st
# # # #
# # # # # Define pages
# # # # pages = ["Home", "Data", "Match", "Predict", "Settings", "Help"]
# # # #
# # # # # Initialize session state
# # # # if "selected_page" not in st.session_state:
# # # #     st.session_state.selected_page = "Home"
# # # #
# # # # # Render navigation bar using Streamlit columns only
# # # # cols = st.columns(len(pages))
# # # # for i, page in enumerate(pages):
# # # #     if cols[i].button(page):
# # # #         st.session_state.selected_page = page
# # # #
# # # # # # Separator
# # # # # st.divider()
# # # #
# # # # # Page content
# # # # page = st.session_state.selected_page
# # # # if page == "Home":
# # # #     st.title("🏠 Welcome to the Home Page!")
# # # #     st.write("This is your dashboard. Use the menu to navigate.")
# # # # elif page == "Data":
# # # #     st.title("📊 Data Page")
# # # #     st.write("Upload and manage your data here.")
# # # # elif page == "Match":
# # # #     st.title("🔗 Match Page")
# # # #     st.write("Match your input with existing profiles.")
# # # # elif page == "Predict":
# # # #     st.title("📈 Predict Page")
# # # #     st.write("Use our models to predict outcomes.")
# # # # elif page == "Settings":
# # # #     st.title("⚙️ Settings Page")
# # # #     st.write("Customize your preferences and configuration.")
# # # # elif page == "Help":
# # # #     st.title("❓ Help Page")
# # # #     st.write("Get support and guidance here.")
