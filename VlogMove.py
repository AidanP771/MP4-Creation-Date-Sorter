import os
import shutil
from datetime import datetime

# Path to folder containing MP4 files
folder_path = 'C:/Users/aidan/Desktop/VLOG/Unsorted Video'

#dict that maps month numbers to month names
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

# Loop through files in folder
for file_name in os.listdir(folder_path):
    # Check if file is an MP4
    if file_name.endswith('.MP4'):
        # Get file creation time
        creation_time = os.path.getctime(os.path.join(folder_path, file_name))
        creation_date = datetime.fromtimestamp(creation_time).date()
        
        #get month name and day number from creation date
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
