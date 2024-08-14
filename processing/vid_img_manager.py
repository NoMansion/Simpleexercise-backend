# Written by Lex Whalen

import pandas as pd
import cv2 as cv
from pose_estimator import PoseEstimator
from frame_operations import FrameOperations
import matplotlib.pyplot as plt
from glob import glob

import IPython.display as ipd
from tqdm import tqdm

import subprocess

plt.style.use('ggplot')

class VideoImgManager():

    def __init__(self):
        self.POSE_ESTIMATOR = PoseEstimator()
        self.FRAME_OPS = FrameOperations()

        self.FIRST = True

    def estimate_live_vid(self,webcam_id=0):
        """reads webcam, applies pose estimation on webcam"""
        cap = cv.VideoCapture(webcam_id)

        while(True):
            has_frame, frame = cap.read()

            if self.FIRST:
                self.WEB_CAM_H,self.WEB_CAM_W = frame.shape[0:2]
                self.FIRST = False

            frame = self.POSE_ESTIMATOR.get_pose_key_angles(frame)

            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    
    def estimate_img(self,img_path):
        """applies pose estimation on img"""

        img = cv.imread(img_path)

        img = self.POSE_ESTIMATOR.get_pose_key_angles(img)


        cv.imshow("Image Pose Estimation",img)

        cv.waitKey(0)
        cv.destroyAllWindows()
    
    def estimate_vid(self, vid_path):
        """Applies pose estimation on video"""
        cap = cv.VideoCapture(vid_path)

        # Check if video opened successfully
        if not cap.isOpened():
            print("Error opening video file:", vid_path)
            return

        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    # Process frame with pose estimation (example)
                    processed_frame = self.POSE_ESTIMATOR.get_pose_key_angles(frame)

                    # Check if processed_frame is None
                    if processed_frame is None:
                        print("Warning: get_pose_key_angles returned None for frame")
                        continue

                    # Display the resulting frame
                    cv.imshow('Frame', processed_frame)

                    # Press 'q' on keyboard to exit
                    if cv.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")

        # Release video capture and close all windows
        cap.release()
        cv.destroyAllWindows()
        print("Finished playing video:", vid_path) 
