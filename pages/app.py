import streamlit as st
import pandas as pd

# Title
st.title("Animal Protection")

# Subtext
st.subheader("Focusing on the impact area of Animal Protection")
st.markdown('''In these results, you will find how different charities that focus on animal
            protection and how they pursue this impact! ''')
# Load your database from a file (replace 'your_database.csv' with your actual file path)
file_path = '/Users/hedyshi/Desktop/crewcode2024/pages/datadotgov_ais19_editedsheet.csv'
try:
    df = pd.read_csv(file_path)
    
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

        
        # Further processing if needed
        # Additional logic here
        