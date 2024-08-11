import cv2
import threading
import sys

# Global variable to signal video stop
stop_signal = threading.Event()

def play_video(file_path):
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        print(f"Error opening video file: {file_path}")
        return

    print(f"Playing video: {file_path}")

    while cap.isOpened():
        if stop_signal.is_set():
            break

        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Player', frame)

        # Check for keypress
        key = cv2.waitKey(1) & 0xFF
        if key != 255:  # 255 means no key was pressed
            break

    cap.release()
    cv2.destroyAllWindows()

def monitor_user_input():
    while True:
        command = input("Enter 'stop' to stop the video: ").strip().lower()
        if command == 'stop':
            stop_signal.set()
            break

if __name__ == "__main__":
    video_file = r'C:\Users\RADHE RADHE\Desktop\my_file\PYTHON\Untitled.mp4'

    # Start the video playback in a separate thread
    video_thread = threading.Thread(target=play_video, args=(video_file,))
    video_thread.start()

    # Start monitoring user input
    monitor_user_input()

    # Wait for the video thread to finish
    video_thread.join()
