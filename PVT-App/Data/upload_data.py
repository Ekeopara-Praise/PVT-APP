# import libraries
from dataclasses import dataclass
import streamlit as st


@dataclass
class Sand_Installation:
    """A class to assess the feasibility of installing sand control in an oil well."""

    def Reservoir_Data(self, compressive_strength: float, permeability: float, porosity: float,
                       fluid_viscosity: float) -> int:
        """
        A function to determine if sand control installation is required based on reservoir data.

        Args:
            compressive_strength (float): The compressive_strength of the formation rock.
            permeability (float): The permeability of the formation.
            porosity (float): The porosity of the formation.
            fluid_viscosity (float): The viscosity of the fluid in the formation.

        Returns:
            int: 1 if sand control installation is required, 0 otherwise.
        """
        decision_list = []
        if compressive_strength > 1000:
            decision_list.append(1)
        else:
            decision_list.append(0)

        if 500 <= permeability <= 8000:
            decision_list.append(1)
        else:
            decision_list.append(0)

        if porosity > 30:
            decision_list.append(1)
        else:
            decision_list.append(0)

        if fluid_viscosity >= 1000:
            decision_list.append(1)
        else:
            decision_list.append(0)

        return 1 if 1 in decision_list else 0

    def Production_Data(self, production_rate: str, water_cut: float) -> int:
        """
        A function to determine if sand control installation is required based on production data.

        Args:
            production_rate (str): The production rate of the well.
            water_cut (float): The water cut of the well.

        Returns:
            int: 1 if sand control installation is required, 0 otherwise.
        """
        decision_list = []
        if production_rate == 'Above critical rate':
            decision_list.append(1)
        elif production_rate == "Below critical rate":
            decision_list.append(0)
        else:
            decision_list.append(0)

        if water_cut > 40:
            decision_list.append(1)
        else:
            decision_list.append(0)

        return 1 if 1 in decision_list else 0

    def Well_Completion_Data(self, completion_type: str) -> int:
        """
        A function to determine if sand control installation is required based on well completion data.

        Args:
            completion_type (str): The type of well completion.

        Returns:
            int: 1 if sand control installation is required, 0 otherwise.
        """
        if completion_type == 'Open hole or Barefoot':
            return 1
        elif completion_type == 'Cased or Liner':
            return 0
        else:
            return 0

    def Economic_Data(self, economic_feasibility: str) -> int:
        """
        A function to determine if sand control installation is economically feasible.

        Args:
            economic_feasibility (str): The economic feasibility of sand control installation.

        Returns:
            int: 1 if sand control installation is economically feasible, 0 otherwise.
        """
        if economic_feasibility == 'Positive':
            return 1
        elif economic_feasibility == 'Can be sorted':
            return 1
        else:
            return 0

    def Environmental_Data(self, impact: str) -> int:
        """
        Calculates the environmental impact score based on user input.

        Args:
            impact (str): User selection for the environmental impact of the project.

        Returns:
            int: 1 if the impact is positive, otherwise 0.
        """
        if impact == 'Minimal':  # if the user selects positive environmental impact
            return 1  # return 1
        else:  # if the user selects negative environmental impact
            return 0  # return 0


####################################################################################################
#""" Streamlit Application """
####################################################################################################
# Define column layout for the page
#col1, col2, col3 = st.columns([1, 3, 1])

# Set empty space in first and third columns to center the image in the second column
# with col1:
#     st.write("")
#
# with col2:
#     # Display logo image in the center column
#     st.write('app_logo.PNG')
#
# with col3:
#     st.write("")
# # Create two tabs on the page: "Sand Control" and "About"
# #tab1, tab2 = st.tabs(["**Sand Control**", "**About**"])

# with tab1:
    # Display an image in the sidebar
    #st.sidebar.image('app_background.PNG', width=290)
# st.write("")
#
# # Add a caption and link to the author's LinkedIn profile in the sidebar
# st.sidebar.caption("Made in 🎈 [Streamlit](https://www.streamlit.io/), "
#                    "by [Praise Ekeopara](https://www.linkedin.com/in/praiseekeopara).")
# st.sidebar.markdown("")

col1, col2 = st.columns(2)


# Add a heading for the "Reservoir Characteristics Data" section
# st.write('**Reservoir Characteristics Data**')

# Create an expander to contain input fields for the "Reservoir Data" section
with st.expander("✨ Enter Fluid Information", expanded=True):
    # Divide the expander into four columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    # Add a selectbox for "Rock Consolidation" in the first column with a description in the help tooltip
    with col1:
        rock_compressive_strength = st.number_input(
            "**Rock strength (psi)**",
            help="""
            Enter the Rock compressive strength.
            """,
        )

    # Add a selectbox for "Permeability (mD)" in the second column with a description in the help tooltip
    with col2:
        perm = st.number_input(
            "**Permeability (mD)**",
            help="""
            Enter the reservoir permeability mD.
            """,
        )

    # Add a selectbox for "Grain size" in the third column with a description in the help tooltip
    with col3:
        poro = st.number_input(
            "**Porosity (%)**",
            help="Enter the formation porosity",
        )

    # Add a selectbox for "Fluid viscosity" in the fourth column with a description in the help tooltip
    with col4:
        fluid_visco = st.number_input(
            "**Fluid viscosity (cP)**",
            help="Enter the suitable Fluid viscosity")

# Add a heading for the "Production & Completion Data" section
# st.write('**Production & Completion Data**')
# Create an expander to contain input fields for the "Production and Completion Data" section
with st.expander("✨ Enter Reservoir Information", expanded=True):
    # Divide the expander into three columns for input fields
    col1, col2, col3 = st.columns(3)

    # Add a selectbox for "Production rate" in the first column with a description in the help tooltip
    with col1:
        prod_rate = st.selectbox(
            "**Production rate**",
            ("Above critical rate", 'Below critical rate', "None"),
            help="""
            Enter the suitable production rate condition.
            """,
        )

    # Add a selectbox for "Water cut" in the second column with a description in the help tooltip
    with col2:
        waterCut = st.number_input(
            "**Water cut (%)**",
            help="""
            Select the suitable Degree of Water cut.
            """,
        )

    # Add a selectbox for "Completion type" in the third column with a description in the help tooltip
    with col3:
        completionType = st.selectbox(
            "**Completion type**",
            ("Cased or Liner", "Openhole or Barefoot"),
            key='completionType',
            help="""
               Select the suitable well completion type.
               """,
        )

# Add a heading for the "Economic & Environmental Data" section
#st.write('**Economic & Environmental Data**')
# Create an expander to contain input fields for the "Economic & Environmental Data" section
with st.expander("✨ Upload PVT Lab Reports", expanded=True):
    # Divide the expander into second columns for input fields
    #col1, col2 = st.columns(2)
    st.button(label="Export file template",
              help='Click to recommend Sand Control installation',
              use_container_width=True)

    # Add a selectbox for "Economic feasibility" in the first column with a description in the help tooltip
    # with col1:
    uploaded_files = st.file_uploader('Kindly upload the data file you have populated!', accept_multiple_files=True)
    # feasibility = st.selectbox(
    #     "**Economic feasibility**",
    #     ("Positive", "Negative", 'Can be sorted'),
    #     key='feasibility',
    #     help="""
    #     Select the suitable economic feasibility of the project.
    #     """,
    # )

    # Add a selectbox for "Environmental impact" in the second column with a description in the help tooltip
    # with col2:
    # st.write("")
    # st.write("")
    # st.write("")
    #col1, col2, col3, col4 = st.columns(4)
    #with col2:

        # environmental_impact = st.selectbox(
        #     "**Environmental impact**",
        #     ("Minimal", "Maximal"),
        #     key='environmental_impact',
        #     help="""
        #     Select the suitable environmental impact of the project.
        #     """,
        # )

#     # Create an instance of the Sand_Installation class
#     sand_control = Sand_Installation()
#
#     # Calculate the reservoir_data, production_data, completion_data, economic_data, and environmental_data based on the input
#     reservoir_data = sand_control.Reservoir_Data(rock_compressive_strength, perm, poro, fluid_visco)
#     production_data = sand_control.Production_Data(prod_rate, waterCut)
#     completion_data = sand_control.Well_Completion_Data(completionType)
#     economic_data = sand_control.Economic_Data(feasibility)
#     environmental_data = sand_control.Environmental_Data(feasibility)
#
#     # Create a list of the calculated data
#     general_decision_list = [reservoir_data, production_data, completion_data, economic_data, environmental_data]
#
#     # Find the most common item in the list
#     most_common = max(set(general_decision_list), key=general_decision_list.count)
#
#     # Create two columns to display the recommendation and a button to trigger the recommendation
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button(label="Recommend", help='Click to recommend Sand Control installation'):
#             if economic_data == 0:
#                 col2.write('<span style="color: red;">**Do not Install Sand Control Facilities!**</span>',
#                            unsafe_allow_html=True)
#             # Display a recommendation based on the most common item in the list
#             elif most_common == 1:
#                 col2.write('<span style="color: red;">**Install Sand Control Facilities!**</span>',
#                            unsafe_allow_html=True)
#             elif most_common == 0:
#                 col2.write('<span style="color: red;">**Do not Install Sand Control Facilities!**</span>',
#                            unsafe_allow_html=True)
#             else:
#                 col2.write('<span style="color: red;">**Check information entered!**</span>', unsafe_allow_html=True)
#
# # # Describes the Software in the 'About' section
# #with tab2:
#     # st.write("## Welcome to SCID! 👋")
#     #
#     # st.markdown(
#         """
#         **SCID** is a **S**and **C**ontrol **I**nstallation **D**ecision-making software designed for Production and other Energy experts
#         for faster and reliable decision making on whether to install Sand Control facilities or not.
#
#         It's credibility is attributed to it's vast factor considerations leveraging various information of the well
#         such as;
#
#         1. Reservoir Characteristics
#         2. Production information
#         3. Completion types
#         4. Environmental impact information
#         5. Economic feasibility information
#
#         Enjoy the decision making power of **SCID** with a simple click on the "**Recommend**" button !
#
#
#         ### Have a demo today!
#         # """