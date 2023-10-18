import os
import requests
from bs4 import BeautifulSoup

# Replace with the URL of the website you want to scrape
url = 'http://xxxx.htm'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a directory to save the downloaded files
    download_folder = 'downloads'
    os.makedirs(download_folder, exist_ok=True)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the anchor tags (links) in the HTML
    links = soup.find_all('a')

    # Extract and download the href attribute of each link
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            # Generate a filename from the link
            filename = os.path.join(download_folder, os.path.basename(href))                        
            # Check if the filename is not a directory
            if not os.path.isdir(filename):
                # Send an HTTP GET request to the link and download the content
                link_response = requests.get(href)                
                if link_response.status_code == 200:                    
                    new_filename = filename.replace("%20", "_")
                    with open(new_filename, 'wb') as file:
                        file.write(link_response.content)
                    print(f"Downloaded: {new_filename}")
                else:
                    print(f"Failed to download {href}. Status code: {link_response.status_code}")

    print(f"Downloaded all files to the '{download_folder}' folder.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
