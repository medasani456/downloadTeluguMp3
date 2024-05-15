import os

# Function to change subfolder names in a directory based on a pattern
def change_subfolder_names(directory):
    # Iterate over all items in the directory
    for item in os.listdir(directory):
        # Construct full path of the item
        item_path = os.path.join(directory, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Split folder name by "-"
            words = item.split("-")
            # Capitalize each word and join them with a space
            new_name = " ".join(word.capitalize() for word in words)
            # Construct old and new paths
            old_path = os.path.join(directory, item)
            new_path = os.path.join(directory, new_name)
            # Rename the folder
            os.rename(old_path, new_path)
            print(f"Renamed '{item}' to '{new_name}'")

# Specify the directory path
directory_path = "D:/Songs"

# Change subfolder names in the specified directory
change_subfolder_names(directory_path)
