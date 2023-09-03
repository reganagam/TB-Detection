import cv2
import os

# Set the path of the input folder
input_folder = '../PERCOBAAN/Dataset/Validation/Normal' #Source Folder

# Set the path of the output folder
output_folder = '../PERCOBAAN/Dataset/Validation/Normal New' #Destination Folder

# Set the desired width and height of the resized images
width = 150
height = 150

# Loop through all the images in the input folder
for filename in os.listdir(input_folder):
    # Read the image
    img = cv2.imread(os.path.join(input_folder, filename))

    # Resize the image
    resized_img = cv2.resize(img, (width, height))

    # Save the resized image to the output folder with the same filename
    cv2.imwrite(os.path.join(output_folder, filename), resized_img)