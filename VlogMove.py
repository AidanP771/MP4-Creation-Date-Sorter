# Import required modules
import os
import shutil
from datetime import datetime

# Set the path to the folder containing the MP4 files
folder_path = 'C:/Users/aidan/Desktop/Test_vllog/Unsorted'

# Set the path to the destination folder for the month folders
month_folder_destination_path = 'C:/Users/aidan/Desktop/Test_vllog'

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

# Function to sort folders into month folders
def sort_into_month_folders():
    # Loop through folders in folder_path
    for folder_name in os.listdir(folder_path):
        # Check if folder name is in "Month Day" format
        if len(folder_name.split()) == 2:
            month_name, day_number = folder_name.split()
            # Get month number from month_dict
            month_number = list(month_dict.keys())[list(month_dict.values()).index(month_name)]
            # Create folder for month if not already existing
            month_folder_path = os.path.join(folder_path, month_name)
            if not os.path.exists(month_folder_path):
                os.mkdir(month_folder_path)
            # Move day folder into month folder
            day_folder_path = os.path.join(folder_path, folder_name)
            dest_folder_path = os.path.join(month_folder_path, folder_name)
            shutil.move(day_folder_path, dest_folder_path)
    
    # Loop through month folders in folder_path
    for month_name in month_dict.values():
        month_folder_path = os.path.join(folder_path, month_name)
        # Check if month folder exists
        if os.path.exists(month_folder_path):
            # Move month folder to month_folder_destination_path
            dest_folder_path = os.path.join(month_folder_destination_path, month_name)
            shutil.move(month_folder_path, dest_folder_path)

# Loop through MP4 files in folder
mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.MP4')]
mp4_files.sort()
for file_name in mp4_files:
    # Get file creation time
    creation_time = os.path.getctime(os.path.join(folder_path, file_name))
    creation_date = datetime.fromtimestamp(creation_time).date()
    
    # Get month name and day number from creation date
    month_name = month_dict[creation_date.month]
    day_number = creation_date.day
    
    # Create folder based on date (if not already existing)
    date_folder_name = f"{month_name} {day_number}"
    date_folder_path = os.path.join(folder_path, date_folder_name)
    if not os.path.exists(date_folder_path):
        os.mkdir(date_folder_path)
    
    # Move file into date folder
    source_file_path = os.path.join(folder_path, file_name)
    dest_file_path = os.path.join(date_folder_path, file_name)
    shutil.move(source_file_path, dest_file_path)

# Call the sort_into_month_folders() function
sort_into_month_folders()
