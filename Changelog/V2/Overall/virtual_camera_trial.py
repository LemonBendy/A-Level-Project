import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("video_path", help="path to video file")
parser.add_argument("--fps", action="store_true", help="output fps every second")
parser.add_argument("--device", help="virtual camera device, e.g. /dev/video0 (optional)")
args = parser.parse_args()

video = cv2.VideoCapture(args.video_path)
if not video.isOpened():
    raise ValueError("Unable to open video: " + args.video_path)
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

with pyvirtualcam.CAmera(width, height, fps, fmt=PixelFormat.BGR, device=args.device, print_fps=args.fps) as cam:
    print(f"Virtual camera device: {cam.device}")
    
