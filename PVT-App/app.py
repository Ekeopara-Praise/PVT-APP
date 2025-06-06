import streamlit as st
from pathlib import Path

# Set page layout to wide for better positioning
st.set_page_config(layout="wide")

# Initialize session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Function to handle image loading safely
def load_image(image_path):
    try:
        resolved_path = Path(__file__).parent / image_path
        if resolved_path.exists():
            return str(resolved_path)
        if Path(image_path).exists():
            return image_path
        raise FileNotFoundError
    except:
        return None


# Login Form
def login():
    with st.form(key="login_form", border=True):
        coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
        with coln2:
            logo_path = load_image("logo.png")
            if logo_path:
                st.image(logo_path)
            else:
                st.warning("Logo image not found")

            submitted = st.form_submit_button("Log in", use_container_width=True)
            if submitted:
                st.session_state.logged_in = True
                st.rerun()


# Logout Form
def logout():
    with st.form(key="logout_form", border=True):
        coln1, coln2, coln3 = st.columns([1.5, 1, 1.5])
        with coln2:
            logo_path = load_image("logo.png")
            if logo_path:
                st.image(logo_path)
            else:
                st.warning("Logo image not found")

            submitted = st.form_submit_button("Log out", use_container_width=True)
            if submitted:
                st.session_state.logged_in = False
                st.rerun()


# Define Login/Logout Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

# Define App Menu Structure
home = st.Page("Home/home.py", title="PVTSmart", icon=":material/home:", default=True)
upload_data = st.Page("Data/upload_data.py", title="Upload data", icon=":material/upload:")
view_data = st.Page("Data/view_data.py", title="View data", icon=":material/visibility:")
black_oil_correlation = st.Page("Match/BlackOil_correlation.py", title="Black oil correlation",
                                icon=":material/schema:")
view_results = st.Page("Match/view_results.py", title="View results", icon=":material/visibility:")
predict = st.Page("Predict/predict.py", title="Predict", icon=":material/timeline:")
settings = st.Page("Settings/settings.py", title="Settings", icon=":material/settings:")
help = st.Page("Help/help.py", title="Help", icon=":material/help:")

# Main app logic
def main():
    # Add logo to sidebar using st.logo()
    logo_path = load_image("logo.png")
    if logo_path:
        st.logo(logo_path)

    # Navigation based on auth state
    if st.session_state.logged_in:
        pg = st.navigation(
            {
                "Home": [home],
                "Data": [upload_data, view_data],
                "Match": [black_oil_correlation, view_results],
                "Predict": [predict],
                "Settings": [settings],
                "Help": [help],
                "Exit App": [logout_page],
            }
        )
    else:
        pg = st.navigation([login_page])

    pg.run()


if __name__ == "__main__":
    main()