import cv2
import glob
import os

# Folder containing images
image_folder = 'images'
output_video = 'mandelbrot_video.mp4'

# Get all png files and sort them numerically
images = sorted(glob.glob(os.path.join(image_folder, '*.png')), key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

# Read the first image to get the frame size
frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width, height)

# Define the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # for .mp4
out = cv2.VideoWriter(output_video, fourcc, 20, size)  # 10 fps, adjust if needed

# Write each frame
for img_path in images:
    img = cv2.imread(img_path)
    out.write(img)

out.release()
print(f'Video saved as {output_video}')
