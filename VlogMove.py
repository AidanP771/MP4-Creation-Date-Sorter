# Import required modules
import os
import shutil
from datetime import datetime

# Set the path to the folder containing the MP4 files
folder_path = 'C:/Users/aidan/Desktop/VLOG/Unsorted Video'

# Set the path to the destination folder for the month folders
month_folder_destination_path = 'C:/Users/aidan/Desktop/VLOG'

# Define a dictionary to map month numbers to month names
month_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}