from datetime import datetime
from os import walk, path
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Set the path to the folder containing the videos
folder_path = '/path/to/videos'

# Loop through all of the folders and subfolders in the specified folder
for root, dirs, files in walk(folder_path):
    # Create an empty list to store the clips for each day
    day_clips = []
    
    # Loop through all of the files in the current folder
    for filename in files:
        # Check if the file is a video file
        if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mov'):
            # Get the full path of the file
            file_path = path.join(root, filename)
            
            # Get the creation time of the file as a datetime object
            creation_time = datetime.fromtimestamp(path.getctime(file_path))
            
            # Check if there are any clips already in the list for this day
            if len(day_clips) > 0 and creation_time.date() != day_clips[-1]['date']:
                # If there are clips in the list and the current file was created on a different day than the previous
                # clips, concatenate the clips for the current day and add them to the final output list
                day_clips.sort(key=lambda x: x['creation_time'])
                clips_to_concatenate = [VideoFileClip(clip['file_path']) for clip in day_clips]
                final_clip = concatenate_videoclips(clips_to_concatenate)
                output_filename = f"{day_clips[0]['creation_time'].strftime('%Y-%m-%d')}.mp4"
                final_clip.write_videofile(output_filename)
                
                # Reset the list of clips for the current day
                day_clips = []
            
            # Add the current clip to the list for the current day
            day_clips.append({'file_path': file_path, 'creation_time': creation_time, 'date': creation_time.date()})
    
    # Concatenate any remaining clips for the last day in the folder
    if len(day_clips) > 0:
        day_clips.sort(key=lambda x: x['creation_time'])
        clips_to_concatenate = [VideoFileClip(clip['file_path']) for clip in day_clips]
        final_clip = concatenate_videoclips(clips_to_concatenate)
        output_filename = f"{day_clips[0]['creation_time'].strftime('%Y-%m-%d')}.mp4"
        final_clip.write_videofile(output_filename)
