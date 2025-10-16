import cv2
import glob
import os

image_folder = 'images'
output_video = 'mandelbrot_video.mp4'

images = sorted(glob.glob(os.path.join(image_folder, '*.png')), key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))


frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, 20, size) 

for img_path in images:
    img = cv2.imread(img_path)
    out.write(img)

out.release()
print(f'Video saved as {output_video}')

