# import streamlit as st
#
# # Custom title with styling
# original_title = """
# <h1 style="font-family: serif; color:white; font-size: 24px; text-align: center;">
# Welcome to PVTSmart ✨
# </h1>
# """
# st.markdown(original_title, unsafe_allow_html=True)
#
# # Set the background image with optimized CSS
# background_image = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0,0,0,0.1)),
#                 url("https://plus.unsplash.com/premium_photo-1693166985133-8a849aa237de?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fENydWRlJTIwb2lsfGVufDB8fDB8fHww") no-repeat center center fixed;
#     background-size: cover;
# }
# </style>
# """
# st.markdown(background_image, unsafe_allow_html=True)
#
# # Improved input box styling
# input_style = """
# <style>
# input[type="text"] {
#     background-color: transparent;
#     color: #a19eae; /* Text color inside the input box */
# }
#
# div[data-baseweb="base-input"] {
#     background-color: transparent !important;
# }
#
# [data-testid="stAppViewContainer"] {
#     background-color: transparent !important;
# }
# </style>
# """
# #st.markdown(input_style, unsafe_allow_html=True)
#
# # Add a placeholder text input for user interaction
# # st.text_input("", placeholder="Streamlit CSS Styling")
