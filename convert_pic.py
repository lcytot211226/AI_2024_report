import cv2
import os

folder_path = 'picture'

image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

frame_width, frame_height = 640, 480
frame_rate = 2

video_writer = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (frame_width, frame_height))
    video_writer.write(frame)

video_writer.release()

print("Video creation completed.")