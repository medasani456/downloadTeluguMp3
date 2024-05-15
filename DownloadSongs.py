import os
import requests
import re
from urllib.parse import urlsplit, unquote


# Function to extract folder name from URL
def extract_folder_name(url):
    last_part = url.split("/")[-1]
    folder_name = last_part.split("-songs")[0].replace('-',' ')
    return folder_name


# Function to decode URL-encoded filename
def decode_filename(filename):
    return unquote(filename)

# Read URLs from text file
with open("AllMovieList.txt", "r") as file:
    urls = file.readlines()

# Process each URL
for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace and newlines

    # Extract folder name from the URL
    folder_name = extract_folder_name(url)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Fetch the HTML content of the webpage
    response = requests.get(url)
    html_content = response.text

    # Define a regular expression pattern to match .mp3 URLs
    pattern = r'href="(https?://[^"]+\.mp3)"'

    # Find all matches of the pattern in the HTML content
    mp3_links = re.findall(pattern, html_content)


    # Function to download mp3 files
    def download_mp3(url, filename):
        with open(os.path.join(folder_name, filename), 'wb') as file:
            response = requests.get(url)
            file.write(response.content)


    # Download each mp3 file
    for mp3_link in mp3_links:
        filename = mp3_link.split('/')[-1]  # Extract filename from URL
        # Decode the filename
        decoded_filename = decode_filename(filename)

        # Download the file with the decoded filename
        download_mp3(mp3_link, decoded_filename)
        print(f"Downloaded: {decoded_filename} for {folder_name}")
