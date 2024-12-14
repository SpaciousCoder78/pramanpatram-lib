# Pramanpatram library functions

'''
Pramanpatram Library Functions

File Name: pramanpatram.py
Author: Aryan Karamtoth
Last Revised: 14 Dec 2024
License: MIT License
Version: 1.0.0
'''
from warnings import catch_warnings

# importing required libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

class Pramanpatram:
    def generate_certificates(self, csv_path, sample_path, text_coords_x, text_coords_y, text_size, r_value, g_value, b_value, text_width, certificate_text, certificate_path):
        try:
            print(f"Reading CSV file from path: {csv_path}")
            persons = pd.read_csv(csv_path)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return "Error, failed to read csv file"

        name_columns = [col for col in persons.columns if "Attendee" in col]
        if not name_columns:
            return "Names of attendees are not present in the csv file"

        for name_column in name_columns:
            namelist = persons[name_column].tolist()
            for i in namelist:
                try:
                    im = Image.open(sample_path)
                except Exception as e:
                    return "Failed to open sample certificate file"

                draw = ImageDraw.Draw(im)
                location = (text_coords_y, text_coords_x)
                text_color = (r_value, g_value, b_value)
                select_font = ImageFont.load_default()

                text = f"{certificate_text.replace('{name}', i)}"
                wrapper = textwrap.TextWrapper(width=text_width)
                text_lines = wrapper.wrap(text=text)

                for line in text_lines:
                    draw.text(location, line, fill=text_color, font=select_font)
                    location = (location[0], location[1] + 35)

                try:
                    save_path = os.path.join(certificate_path, f"certificate_{i}.jpg")
                    im.save(save_path)
                    print(f"Certificate saved for {i} at {save_path}")
                except Exception as e:
                    print(f"Error saving certificate for {i}: {e}")
                    return "Error, failed to save certificate file"

        return "Successfully generated certificate file"