import threading
import matplotlib.pyplot as plt
from PIL import Image

# Global variable to signal image display stop
stop_signal = threading.Event()

def display_image(file_path):
    # Open the image file
    image = Image.open(file_path)
    
    # Display the image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')  # Hide axes

    # Define a function to close the plot
    def close(event):
        plt.close(fig)
    
    # Connect the close function to the key press event
    fig.canvas.mpl_connect('key_press_event', close)
    
    # Wait for the stop signal
    while not stop_signal.is_set():
        plt.pause(0.1)  # Check for stop signal periodically
    
    plt.close(fig)

def monitor_user_input():
    while True:
        command = input("Enter 'close' to close the image: ").strip().lower()
        if command == 'close':
            stop_signal.set()
            break

if __name__ == "__main__":
    try:
        image_file = r'C:\Users\RADHE RADHE\Desktop\my_file\PYTHON\others\Untitled-3.png'
    except FileNotFoundError as FNF:
        print(f"PROVIDE LINK IS NOT FOUND: [{FNF}]")
    # Start monitoring user input in a separate thread
    input_thread = threading.Thread(target=monitor_user_input)
    input_thread.start()

    # Display the image in the main thread
    display_image(image_file)

    # Wait for the input thread to finish
    input_thread.join()
