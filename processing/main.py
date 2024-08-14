# Written by Lex Whalen
import json
import select
import shutil
import time
import signal
import sys

import psycopg2
import requests
from vid_img_manager import VideoImgManager
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pose_estimator import PoseEstimator
from workout import Workout
from exercise import Exercise
import urllib.request
from workout_methods import *

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

print("Project Root:", project_root)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', ''YOUR ROOT_URL CONF')
import django
django.setup()

from core import signals
from core.views import send_workout_plan

def extract_id_from_url(url):
    # Split the URL by '/' and get the second-to-last part
    return url.rstrip('/').split('/')[-1]

def extract_values(arr):
    if len(arr) < 4:
        raise ValueError("Array must contain at least 4 elements")
    
    # Extract and parse the required values
    fifth_to_last_value = int(arr[-5])  # Parse as int
    
    try:
        fourth_to_last_value = int(arr[-4])
    except ValueError:
        fourth_to_last_value = arr[-4]
        range_parts = fourth_to_last_value.split('-')
        if len(range_parts) == 2:
            try:
                start_value = int(range_parts[0])
                end_value = int(range_parts[1])
                # Choose the middle value of the range (or you can define your own logic)
                fourth_to_last_value = (start_value + end_value) // 2
            except ValueError:
                raise ValueError("Range values must be integers")
        else:
            raise ValueError("Invalid range format")
        
    third_to_last_value = arr[-2]
    
    return [fifth_to_last_value, fourth_to_last_value, third_to_last_value]

class Main():
    def __init__(self):
        self.VI_M = VideoImgManager()

    def vid_estimation(self, vid_path):
        self.VI_M.estimate_vid(vid_path)

def get_latest_note():
    response = requests.get('YOUR URL')  # Adjust URL as needed
    if response.status_code == 200:
        latest_note = response.json()  # This is already a dictionary
        data_list = list(latest_note.values())  # Convert dictionary values to list
        return data_list
    else:
        raise Exception("Failed to retrieve latest note")

def send_workout(workout):
    api_endpoint = 'YOUR URL'
    data = {
        'workoutPlan': workout,
    }

    response = requests.put(api_endpoint, json=data)
    if response.status_code == 200:
        print('Update successful:', response.json())
    else:
        print('Update failed:', response.status_code, response.text)

def download_file_from_db(file_id, output_path):
    try:
        conn = psycopg2.connect(
            # YOUR DATABASE INFO
        )
        
        cursor = conn.cursor()
        cursor.execute('SELECT "binary" FROM core_note WHERE id = %s', (file_id,))
        result = cursor.fetchone()

        if result:
            file_data = result[0]

            # Debug: Print the type of file_data
            print(f"Type of file_data: {type(file_data)}")
            print(file_data)

            with open(output_path, 'wb') as f:
                f.write(file_data)
            print(f"File downloaded successfully and saved to {output_path}")
        else:
            print(f"No file found with id {file_id}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()


def listen_for_notifications():
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            # YOUR DATABASE INFO
        )

        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute("LISTEN new_item_channel;")
        print("Waiting for notifications on channel 'new_item_channel'...")

        # watcher = Watcher()
        
        try:
            while True:
                if select.select([conn], [], [], 5) == ([], [], []):
                    print("Waiting for new data...")
                else:
                    conn.poll()
                    while conn.notifies:
                        notify = conn.notifies.pop(0)
                        print(f"Received notification: {notify.payload}")
                        
                        note_data = get_latest_note()
                        file_id = extract_id_from_url(note_data[0])
                        output_path = os.path.join(r'your\directory\media\cvs', f'cv_{file_id}.mp4')
                        download_file_from_db(file_id, output_path)
                        avg_left_knee_angle, avg_right_knee_angle = PoseEstimator.extract_knee_angles_from_video(output_path)
                        try:
                            os.remove(output_path)
                            print(f"File {output_path} deleted successfully.")
                        except Exception as e:
                            print(f"Error deleting file {output_path}: {e}")
                        note_data = get_latest_note()
                        print(note_data)
                        processed_data = extract_values(note_data)
                        print(processed_data)
                        num_days = processed_data[0]
                        length = processed_data[1]
                        specificity = processed_data[2]
                        
                        leg_focus = False
                        chest_focus = False
                        back_focus = False
                        shoulder_focus = False
                        arm_focus = False

                        if avg_right_knee_angle is None:
                            leg_focus = False
                        elif avg_right_knee_angle >= 120 or avg_left_knee_angle >= 120:
                            leg_focus = True
                        
                        plan = create_weekly_plan(num_days, specificity, leg_focus, length)
                        print(plan)
                        send_workout(plan)
        except KeyboardInterrupt:
            print("Stopping listener...")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    app = Main()
    create_exercise_pools()
    listen_for_notifications()





