import os

# Function to remove specified text patterns from each file name under subfolders in a directory
def remove_text_from_filenames(directory, text_patterns):
    # Iterate over all subfolders and files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct full path of the file
            file_path = os.path.join(root, file)
            # Check if any of the text patterns are in the file name
            for pattern in text_patterns:
                if pattern in file:
                    # Remove the text pattern from the file name
                    new_file_name = file.replace(pattern, "")
                    # Construct the new file path
                    new_file_path = os.path.join(root, new_file_name)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file}' to '{new_file_name}'")
                    break  # Stop checking other patterns once one is found


# Specify the directory path
directory_path = "D:/Songs"

# Text patterns to remove from file names
text_patterns = [" [www.SenSongsMp3.co] ", " [SenSongsMp3.Co]", " - SenSongsmp3.Co" , " SenSongsmp3.Co", ]

# Remove text patterns from file names in all subfolders under the specified directory
remove_text_from_filenames(directory_path, text_patterns)
