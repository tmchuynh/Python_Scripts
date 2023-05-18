import os
folder_location = 'C:\\Users\\user\\Downloads\\demo'

os.chdir(folder_location)
list_of_files = os.listdir()

## Selecting All Images
images = [content for content in list_of_files if content.endswith(('.png','.jpg','.jpeg'))] 

for index, image in  enumerate(images):
    os.rename(image,f'{index}.png')


## Deleting All Images
################## Write Your Script Here ######## Try To Create Your Own Code 