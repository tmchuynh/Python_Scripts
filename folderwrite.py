import requests
import os

# API link to fetch the photos
api_link = "https://api.pexels.com/v1/search?query=rooms&per_page=80&page=1&api_key=563492ad6f91700001000001c3df0f0bcc3d45309a293e4edeac3cf2"
# Adjust the "per_page" parameter to control the number of photos fetched (maximum 80)

# Folder path to save the downloaded files
folder_path = "/home/tmchuynh/Documents/Coding Dojo/Java Stack/wedding_planner/src/main/resources/static/images/rooms"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Specify the desired number of photos to save
num_photos_to_save = 1118

# Make a request to the API
response = requests.get(api_link, headers={"Authorization": "563492ad6f91700001000001c3df0f0bcc3d45309a293e4edeac3cf2"})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    photos = data.get("photos", [])

    for i, photo in enumerate(photos[:num_photos_to_save], start=1390):
        file_url = photo["src"]["original"]
        filename = f"image{i}.jpg"
        file_path = os.path.join(folder_path, filename)

        # Download the file and save it to the folder
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"File '{filename}' downloaded and saved successfully.")
        else:
            print(f"Failed to download file '{filename}'.")
else:
    print("Failed to fetch photo list from the API.")