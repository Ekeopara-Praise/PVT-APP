import streamlit as st
from pathlib import Path
# Set page configuration
# st.set_page_config(page_title="PVTSmart", layout="wide")

# -------- Background Gradient (soft blue) --------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #F5F7FA, #F5F7FA);
    background-size: cover;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------- Two-column Layout --------
left_col, right_col = st.columns([1, 1.2])


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

 # Add logo to sidebar using st.logo()
logo_path = load_image("logo.png")

with left_col:
    st.image(logo_path)  # Make sure this logo file is in the root directory

with right_col:
    st.markdown("""
    <h2 style='color: #0047AB;'>The fastest way to simulate PVT models</h2>
    <p style='font-size: 18px; color: #333;'>
        PVTSmart empowers petroleum engineers and researchers to analyze and model fluid behavior 
        accurately and efficiently. With an intuitive interface and powerful AI-assisted tools, 
        you can generate insights from your datasets in record time.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    # Call to Action Buttons
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        st.button("🚀 Get Started Now", use_container_width=True)
    with col_btn2:
        st.button("📩 Contact Us", use_container_width=True)

# -------- Animated Feature Highlights Section (zoomIn) --------
st.markdown("""
<hr style="border: 1px solid #ddd;"/>

<h3 style="color:#0047AB;">🔍 Key Features</h3>
<div class="features">
    <ul>
        <li>📊 Upload and visualize live PVT datasets</li>
        <li>🧠 Integrate with AI to forecast behavior</li>
        <li>🔄 Export charts and models</li>
        <li>🛠️ Customizable modules for labs or industry</li>
    </ul>
</div>

<style>
.features ul {
    list-style: none;
    padding-left: 0;
}

.features li {
    opacity: 0;
    transform: scale(0.8);
    animation: zoomIn 0.9s ease forwards;
    animation-delay: calc(var(--i) * 0.2s);
    margin: 10px 0;
    font-size: 18px;
    color: #333;
}

.features li:nth-child(1) { --i: 1; }
.features li:nth-child(2) { --i: 2; }
.features li:nth-child(3) { --i: 3; }
.features li:nth-child(4) { --i: 4; }
.features li:nth-child(5) { --i: 5; }

@keyframes zoomIn {
    0% {
        opacity: 0;
        transform: scale(0.8);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}
</style>
""", unsafe_allow_html=True)




# import streamlit as st
#
# #st.write("Welcome!... work in progress...")
#
# # Page config
# #st.set_page_config(page_title="PVTSmart", layout="wide")
#
# # Title
# title_html = """
# <h1 style="font-family: serif; color:blue; font-size: 30px; text-align: center;">
# Welcome to PVTSmart ✨
# </h1>
# """
# st.markdown(title_html, unsafe_allow_html=True)
#
# # Set a plain background color
# background_color = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background-color: 	#bdc3c7; /* Change this color to your preference */
# }
# </style>
# """
# st.markdown(background_color, unsafe_allow_html=True)
#
# # Scrolling text (marquee-style)
# scrolling_features = """
# <div style="overflow: hidden; white-space: nowrap; margin-top: 20px;">
#   <div style="
#     display: inline-block;
#     padding-left: 100%;
#     animation: scroll-left 25s linear infinite;
#     font-size: 18px;
#     color: #f9290a;
#   ">
#     📊 Upload your data | 🔍 Run custom ML models | 🌐 Visualize predictions | 📁 Export results | 🧠 Smart analytics powered by AI
#   </div>
# </div>
#
# <style>
# @keyframes scroll-left {
#   0% { transform: translateX(0%); }
#   100% { transform: translateX(-100%); }
# }
# </style>
# """
# st.markdown(scrolling_features, unsafe_allow_html=True)
#
# # Optional input box or interactive widgets can go below
# #st.text_input("Enter something here:", placeholder="Type your data or command...")
#
# # Placeholder for app features
# st.write("### App Features Coming Below")
# st.markdown("- Data upload and validation")
# st.markdown("- Interactive plots and dashboards")
# st.markdown("- Predictive modeling with adjustable parameters")
# st.markdown("- Exportable insights and reports")
