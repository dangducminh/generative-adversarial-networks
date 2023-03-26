from PIL import Image
import os

# Set the path to the folder containing the images
folder_path = './resize_image_cat/'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        img = Image.open(os.path.join(folder_path, filename))

        # Resize the image
        img = img.resize((64, 64))

        # Save the resized image with a new filename
        new_filename = filename
        img.save(os.path.join(folder_path, new_filename))