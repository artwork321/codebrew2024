import streamlit as st
import csv
import requests
from io import BytesIO
from PIL import Image

file_url = 'https://raw.githubusercontent.com/artwork321/crewcode2024/hedy/pages/datadotgov_ais19_editedsheet.csv'

def database_loader(charity):
    def read_csv_file(file_path):
        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    csv_name = row[0]

                    if csv_name == charity:
                        return [csv_name, row[1], row[2], row[3]]
        except FileNotFoundError:
            st.error("File not found. Please check the file path.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    def display_image(url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            # Open the image using Pillow
            image = Image.open(BytesIO(image_data))
            # Resize the image to 100x100
            image_resized = image.resize((200, 200))
            # Display the image in Streamlit
            st.image(image_resized, use_column_width=False)
        else:
            st.write("Failed to load image")

    # Inputting File Path
    file_path = r"mainpage.csv"
    data = read_csv_file(file_path)

    if data is not None:
        display_image(data[3])
        st.write(data[0])
        st.write(data[1])
        st.write(data[2])  
    else:
        st.error("Charity not found in the database")