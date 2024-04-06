#importing Streamlit Module
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from io import BytesIO, StringIO
import pandas as pd


st.set_page_config(layout="wide") 

# Load your database from a file (replace 'your_database.csv' with your actual file path)
file_url = 'https://raw.githubusercontent.com/artwork321/crewcode2024/hedy/pages/datadotgov_ais19_editedsheet.csv'

# Functions for each of the pages



#A Function used for displaying images
def display_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        # Open the image using Pillow
        image = Image.open(BytesIO(image_data))
        # Resize the image to 100x100
        image_resized = image.resize((100, 100))
        # Display the image in Streamlit
        st.image(image_resized, use_column_width=False)
    else:
        st.write("Failed to load image")

custom_style = {
    "font-family": "Calibri",
    "font-size": "18px"
}


def aged_care():
    # Title
    st.title("Aged Care")

    # Subtext
    st.subheader("Focusing on the impact area of helping Aged Care")
    st.markdown('''In these results, you will find how different charities that focus on helping
                aged cares and how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'aged care'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['aged care'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")


def animal_protection():
    # Title
    st.title("Animal Protection")

    # Subtext
    st.subheader("Focusing on the impact area of Animal Protection")
    st.markdown('''In these results, you will find how different charities that focus on animal
                protection and how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'animal protection'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['animal protection'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")

def economic_social_and_community_development():
    # Title
    st.title("Economic social and community development")

    # Subtext
    st.subheader("Focusing on the impact area of helping economic social and community development")
    st.markdown('''In these results, you will find how different charities that focus on helping
               economic social and community development, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'economic social and community development'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['economic social and community development'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")


def emergency_relief():
    # Title
    st.title("Emergency Relief")

    # Subtext
    st.subheader("Focusing on the impact area of helping emergency relief operations")
    st.markdown('''In these results, you will find how different charities that focus on helping
               emergency relief operations, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'emergency relief'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['emergency relief'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")

def environmental_activities():
    # Title
    st.title("Environmental Activities")

    # Subtext
    st.subheader("Focusing on the impact area of helping the environment")
    st.markdown('''In these results, you will find how different charities that focus on helping
               the environment, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'environmental activities'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['environmental activities'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
def emergency_relief():
    # Title
    st.title("Emergency Relief")

    # Subtext
    st.subheader("Focusing on the impact area of helping emergency relief operations")
    st.markdown('''In these results, you will find how different charities that focus on helping
               emergency relief operations, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'emergency relief'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['emergency relief'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")

def environmental_activities():
    # Title
    st.title("Environmental Activities")

    # Subtext
    st.subheader("Focusing on the impact area of helping the environment")
    st.markdown('''In these results, you will find how different charities that focus on helping
               the environment, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'environmental activities'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['environmental activities'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")

def hospital_services():
    # Title
    st.title("Hospital Services & Rehabilitation Activities")

    # Subtext
    st.subheader("Focusing on the impact area of helping hospital services and rehabilitation.")
    st.markdown('''In these results, you will find how different charities that focus on helping
               hospital services and rehabilitation, alongside how they pursue this impact! ''')
   
    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            # Read the fetched file into a Pandas DataFrame
            df = pd.read_csv(StringIO(response.text))
        
            # Get user input for filtering
            filter_value = 'hospital services and rehabilitation activities'
            # Check if the filter value is empty
            if filter_value:
                # Filter the DataFrame based on the specified column and value
                filtered_df = df[df['hospital services and rehabilitation activities'] == 'y'].copy()  # Replace 'Column_Name' with the actual column name
                
                # List of column names to keep in the copied DataFrame
                columns_to_keep = ['charity name', 'how purposes were pursued']  # Replace with actual column names
                
                # Select only the specified columns in the copied DataFrame
                filtered_df = filtered_df[columns_to_keep]
                
                st.write("#### Charities")

                # Pagination
            page_number = st.slider("Select page number", 1, len(filtered_df) // 10 + 1, 1)

            # Calculate start and end indices for displaying rows
            start_idx = (page_number - 1) * 10
            end_idx = min(start_idx + 10, len(filtered_df))

            # Display the selected page
            st.write(f"## Page {page_number} - Rows {start_idx + 1} to {end_idx} of {len(filtered_df)}")
            st.write(filtered_df[start_idx:end_idx], index = False)

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")






#Development of the Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title      =   'Filters',
        options         =   ['Main', 'Aged care', 'Animal protection', 'Economic social and community development', 'Emergency relief', 'Environmental activities', 'Hospital services and rehabilitation activities'],
        menu_icon       =   'filter',
        default_index   =   0,
        styles = {
        "container": {
            "display": "flex",
            "padding": "20px 40px",
            "gap": "50px",
            "box-shadow": "0px 8px 8px -2px rgba(0, 0, 0, 0.341)",
            "background-color": "#A8D6A7",
        },
        "menu-title": {
            "font-size": "35px",
            "text-decoration": "none",
            "color": "black",
            "font-family": "'Calibri'",
            "margin-right": "auto"
        },
        "nav": {
            "list-style-type": "none",
            "padding": "0",
            "margin": "0"
        },
        "nav-link": {
            "font-size": "25px",
            "text-decoration": "none",
            "color": "black",
            "font-family": "'Calibri'"
        },
        "nav-link:hover": {
            "color": "#A8D6A7"
        }
    }
    )


def main():
    st.title('Charities')

    row1 = option_menu(
        menu_title      =   None,
        options         =   ['Caritas', 'World Vision Australia', 'The Smith Family', 'RSPCA Australia'],
        menu_icon       =   None,
        default_index   =   0,
        orientation     =   'horizontal',
        styles = {
            "container": {
                "display": "flex",
                "padding": "20px 40px",
                "gap": "50px",
                "box-shadow": "0px 8px 8px -2px rgba(0, 0, 0, 0.341)",
                "background-color": "#64B661"
            },
            "menu-title": {
                "font-size": "35px",
                "text-decoration": "none",
                "color": "black",
                "font-family": "'Calibri'",
                "margin-right": "auto"
            },
            "nav": {
                "list-style-type": "none",
                "padding": "0",
                "margin": "0"
            },
            "nav-link": {
                "font-size": "25px",
                "text-decoration": "none",
                "color": "black",
                "font-family": "'Calibri'",
                "background-color": "#64B661"  # Background color
            },
            # Remove hover effect
            "nav-link:hover": {
                "color": "inherit",
                "background-color": "inherent"
            },
            "icon": {
            "display": "none"
            },
        }
        
    )

    if row1 == 'Caritas':

        # Displaying Dataframes and Images
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiURz1xi1_VpLK2qwAGULMHmG1UGwRUX_DVwuTUnlOTw&s')

        # Caritas Dataframe
        name = 'Caritas'
        purpose = 'Caritas Internationalis is a global network of Catholic charitable organizations, operating in over 200 countries. It provides aid, promotes social justice, and empowers communities in need worldwide.'

        # Display the information
        st.write(f"Name: {name}", style=custom_style)
        st.write(f"Purpose: {purpose}")

    if row1 == 'World Vision Australia':
        # Displaying Dataframes and Images
        display_image('https://pbs.twimg.com/profile_images/1009985406069141504/c_0KvxaW_400x400.jpg')

        # World Vision Australia Dataframe
        name = 'World Vision Australia'
        purpose = 'World Vision Australia is a humanitarian organization dedicated to helping children and communities in need through various programs, including child sponsorship, emergency relief, and community development.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")

    if row1 == 'The Smith Family':
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnIz-AXLJ8KIPuKuJO2wJbPQVnXipcpqY449AMghhZmw&s')

        # RSPCA Australia Dataframe
        name = 'RSPCA Australia'
        purpose = 'RSPCA Australia is an animal welfare organization in Australia. It works to prevent cruelty to animals by promoting animal welfare standards, conducting investigations, and providing shelter, adoption, and veterinary services for animals in need.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")

    if row1 == 'RSPCA Australia':
        #Displaying Dataframes and Images
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnIz-AXLJ8KIPuKuJO2wJbPQVnXipcpqY449AMghhZmw&s')
        
        #RSPCA Australia
        name = 'RSPCA Australia'
        purpose = 'RSPCA Australia is an animal welfare organization in Australia. It works to prevent cruelty to animals by promoting animal welfare standards, conducting investigations, and providing shelter, adoption, and veterinary services for animals in need.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")



    row2 = option_menu(
        menu_title      =   None,
        options         =   ['Carita', 'WVA', 'TSF', 'RSPCA'],
        menu_icon       =   None,
        default_index   =   0,
        orientation     =   'horizontal',
        styles = {
            "container": {
                "display": "flex",
                "padding": "20px 40px",
                "gap": "50px",
                "box-shadow": "0px 8px 8px -2px rgba(0, 0, 0, 0.341)",
                "background-color": "#64B661"
            },
            "menu-title": {
                "font-size": "35px",
                "text-decoration": "none",
                "color": "black",
                "font-family": "'Calibri'",
                "margin-right": "auto"
            },
            "nav": {
                "list-style-type": "none",
                "padding": "0",
                "margin": "0"
            },
            "nav-link": {
                "font-size": "25px",
                "text-decoration": "none",
                "color": "black",
                "font-family": "'Calibri'",
                "background-color": "#64B661"  # Background color
            },
            # Remove hover effect
            "nav-link:hover": {
                "color": "inherit",
                "background-color": "inherent"
            },
            "icon": {
            "display": "none"
            },
        }
        
    )

    if row2 == 'Carita':

        # Displaying Dataframes and Images
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiURz1xi1_VpLK2qwAGULMHmG1UGwRUX_DVwuTUnlOTw&s')

        # Caritas Dataframe
        name = 'Caritas'
        purpose = 'Caritas Internationalis is a global network of Catholic charitable organizations, operating in over 200 countries. It provides aid, promotes social justice, and empowers communities in need worldwide.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")

    if row2 == 'WVA':
        # Displaying Dataframes and Images
        display_image('https://pbs.twimg.com/profile_images/1009985406069141504/c_0KvxaW_400x400.jpg')

        # World Vision Australia Dataframe
        name = 'World Vision Australia'
        purpose = 'World Vision Australia is a humanitarian organization dedicated to helping children and communities in need through various programs, including child sponsorship, emergency relief, and community development.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")

    if row2 == 'TSF':
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnIz-AXLJ8KIPuKuJO2wJbPQVnXipcpqY449AMghhZmw&s')

        # RSPCA Australia Dataframe
        name = 'RSPCA Australia'
        purpose = 'RSPCA Australia is an animal welfare organization in Australia. It works to prevent cruelty to animals by promoting animal welfare standards, conducting investigations, and providing shelter, adoption, and veterinary services for animals in need.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")

    if row2 == 'RSPCA':
        #Displaying Dataframes and Images
        display_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnIz-AXLJ8KIPuKuJO2wJbPQVnXipcpqY449AMghhZmw&s')
        
        #RSPCA Australia
        name = 'RSPCA Australia'
        purpose = 'RSPCA Australia is an animal welfare organization in Australia. It works to prevent cruelty to animals by promoting animal welfare standards, conducting investigations, and providing shelter, adoption, and veterinary services for animals in need.'

        # Display the information
        st.write(f"Name: {name}")
        st.write(f"Purpose: {purpose}")


if selected == 'Main':
    main()
elif selected == 'Animal protection':
    animal_protection()
elif selected == 'Aged care':
    aged_care()
elif selected == 'Economic social and community development':
    economic_social_and_community_development()
elif selected == 'Emergency relief':
    emergency_relief()
elif selected == 'Environmental activities':
    environmental_activities()
elif selected == 'Hospital services and rehabilitation activities':
    hospital_services()