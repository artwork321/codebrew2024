import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.set_page_config(layout="wide") 

# Load your database from a file (replace 'your_database.csv' with your actual file path)
file_url = 'https://raw.githubusercontent.com/artwork321/crewcode2024/hedy/pages/datadotgov_ais19_editedsheet.csv'

# Functions for each of the pages
def home():
    st.header('To be filled')
    try:
        # Fetch the database file
        df = pd.read_csv(file_url)

        # Display the database
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error: {str(e)}")



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
            st.dataframe(filtered_df[start_idx:end_idx])

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")


# Sidebar setup
st.sidebar.title('Navigation')

#Sidebar navigation
options = st.sidebar.selectbox('Our Pages', ['Home', 'Aged Care', 'Animal Protection', 
'Economic Social & Community Development', 'Emergency Relief', 'Environmental Activities', 
'Hospital Services & Rehabilitation Activities'])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

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
            st.dataframe(filtered_df[start_idx:end_idx])

    except FileNotFoundError:
        st.error("File not found. Please check the file path.")



# Function to render the charity information based on user input
def charity_info():
    # Title
    st.title("Charity Information")

    # Text input for user to enter charity name
    charity_name = st.text_input("Enter the name of the charity:", '')

    try:
        # Fetch and display data
        df = pd.read_csv(file_url)
        
        # Filter the dataset based on the entered charity name
        filtered_df = df[df['charity name'].str.contains(charity_name, case=False)].copy()

        # Select only the desired columns (charity name, how purposes were pursued, and age group columns)
        filtered_df = filtered_df[['charity name', 'how purposes were pursued', 'aboriginal or tsi', 'adults 25 to 65', 
                                    'early childhood - under 6', 'adults - 65 and over', 'children 6 to under 15', 
                                    'communities overseas', 'families', 'financially disadvantaged people', 
                                    'gay lesbian bisexual transgender or intersex persons', 'general community in australia', 
                                    'males', 'migrants refugees or asylum seekers', 'pre or post release offenders', 
                                    'people with chronic illness', 'people with disabilities', 'people from a CALD background', 
                                    'people at risk of homelessness', 'people in rural/regional/remote communities', 
                                    'unemployed persons', 'veterans or their families', 'victims of crime', 'victims of disasters',
                                    'females', 'youth 15 to U25']]

        # Combine the age group columns into a single column containing tags
        filtered_df['specific groups of people'] = filtered_df.iloc[:, 2:].apply(lambda x: ',  '.join(x.index[x == 'y']), axis=1)

        # Drop the individual age group columns
        filtered_df.drop(filtered_df.columns[2:-1], axis=1, inplace=True)

        # Display the filtered dataset
        st.dataframe(filtered_df)

    except Exception as e:
        st.error(f"Error: {str(e)}")




# Navigation options
if options == 'Home':
    home()
elif options == 'Animal Protection':
    animal_protection()
    charity_info()
elif options == 'Aged Care':
    aged_care()
    charity_info()
elif options == 'Economic Social & Community Development':
    economic_social_and_community_development()
    charity_info()
elif options == 'Emergency Relief':
    emergency_relief()
    charity_info()
elif options == 'Environmental Activities':
    environmental_activities()
    charity_info()
elif options == 'Hospital Services & Rehabilitation Activities':
    hospital_services()
    charity_info()