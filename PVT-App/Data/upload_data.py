# import libraries
from dataclasses import dataclass
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from io import BytesIO

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
with st.expander("✨ Enter Reservoir Information", expanded=True):
    # Divide the expander into three columns for input fields
    col1, col2, col3 = st.columns(3)

    # Add a selectbox for "Production rate" in the first column with a description in the help tooltip
    with col1:
        prod_rate = st.text_input(
            "**Reservoir Name**",
            placeholder ='E4000X',
            help="""
            Enter the suitable production rate condition.
            """,
        )

    # Add a selectbox for "Water cut" in the second column with a description in the help tooltip
    with col2:
        waterCut = st.number_input(
            "**Reservoir Pressure (psia)**",
            help="""
            Select the suitable Degree of Water cut.
            """,
        )

    # Add a selectbox for "Completion type" in the third column with a description in the help tooltip
    with col3:
        completionType = st.number_input(
            "**Reservoir Temperature (F)**",
            help="""
               Select the suitable well completion type.
               """,
        )

# Create an expander to contain input fields for the "Reservoir Data" section
with st.expander("✨ Enter Fluid Information", expanded=True):
    # Divide the expander into four columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    # Add a selectbox for "Rock Consolidation" in the first column with a description in the help tooltip
    with col1:
        rock_compressive_strength = st.number_input(
            "**Bubble point pressure (psia)**",
            help="""
            Enter the Rock compressive strength.
            """,
        )

    # Add a selectbox for "Permeability (mD)" in the second column with a description in the help tooltip
    with col2:
        perm = st.number_input(
            "**Oil API Gravity**",
            help="""
            Enter the reservoir permeability mD.
            """,
        )

    # Add a selectbox for "Grain size" in the third column with a description in the help tooltip
    with col3:
        poro = st.number_input(
            "**Gas Gravity**",
            help="Enter the formation porosity",
        )

    # Add a selectbox for "Fluid viscosity" in the fourth column with a description in the help tooltip
    with col4:
        fluid_visco = st.number_input(
            "**Fluid viscosity (cP)**",
            help="Enter the suitable Fluid viscosity")

with st.expander("✨ Enter Separator Information", expanded=True):
    # Divide the expander into four columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    # Add a selectbox for "Rock Consolidation" in the first column with a description in the help tooltip
    with col1:
        rock_compressive_strength = st.number_input(
            "**Bodb**",
            help="""
            Enter the Rock compressive strength.
            """,
        )

    # Add a selectbox for "Permeability (mD)" in the second column with a description in the help tooltip
    with col2:
        perm = st.number_input(
            "**Bofb**",
            help="""
            Enter the reservoir permeability mD.
            """,
        )

    # Add a selectbox for "Grain size" in the third column with a description in the help tooltip
    with col3:
        poro = st.number_input(
            "**Rsdb**",
            help="Enter the formation porosity",
        )

    # Add a selectbox for "Fluid viscosity" in the fourth column with a description in the help tooltip
    with col4:
        fluid_visco = st.number_input(
            "**Rsfb**",
            help="Enter the suitable Fluid viscosity")


def get_path(datapath):
    try:
        resolved_path = Path(__file__).parent / datapath
        if resolved_path.exists():
            return str(resolved_path)
        if Path(datapath).exists():
            return datapath
        raise FileNotFoundError
    except:
        return None

# Create an expander to contain input fields for the "Economic & Environmental Data" section
@st.cache_data
def get_data():
    # Separate data for each sheet
    CCE = pd.DataFrame(columns=[
        'Pressure (psia)',
        'Relative Volume',
        'Y-Function',
        'Density (g/cc)',
        'Compressibility (1/psia)',
        'Corrected Relative Volume'
    ])

    DLE = pd.DataFrame(columns=[
        'Pressure (psig)',
        'Solution Gas / Oil RatioRsd, (Scf/Stb)',
        'Relative Oil Volume Bod, (Bbl/Stb)',
        'Oil Density (gm/cc)',
        'Bg (cuft/SCF)',
        'Gas Viscosity (cP)',
        'Gas Density (g/cc)',
        'Gas Z - Factor'
    ])

    separator = pd.DataFrame(columns=[
        'Pressure (psia)',
        'Temperature (F)',
        'GOR (SCF/STB)',
        'Oil Density (g/cc)',
        'Gas MW (g/mol)',
        'Gas Gravity(air = 1)',
        'Sep vol factor(Sep bbl/St bbl)'
    ])

    return CCE, DLE, separator

@st.cache_data
def convert_to_excel(sheet1, sheet2, sheet3):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        sheet1.to_excel(writer, sheet_name='CCE', index=False)
        sheet2.to_excel(writer, sheet_name='DLE', index=False)
        sheet3.to_excel(writer, sheet_name='separator', index=False)
    return output.getvalue()

sheet1, sheet2, sheet3 = get_data()
excel_data = convert_to_excel(sheet1, sheet2, sheet3)

with st.expander("✨ Upload PVT Lab Reports", expanded=True):
    st.download_button(
        label="Export Excel",
        data=excel_data,
        file_name="pvt_data_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

    uploaded_files = st.file_uploader('Kindly upload the data file you have populated!', accept_multiple_files=True)
