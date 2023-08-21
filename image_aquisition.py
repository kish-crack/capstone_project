import cv2
import time

# Create a VideoCapture object to access the camera (usually 0 for the default camera).
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully.
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Initialize variables for timing.
start_time = time.time()
capture_interval = 2  # Capture an image every 2 seconds

# Initialize a frame counter for saved images.
frame_number = 0

while True:
    ret, frame = cap.read()  # Read a frame from the camera.

    if not ret:
        # If there's an issue with the camera, exit the loop.
        print("Error: Could not read a frame from the camera.")
        break

    # Calculate the elapsed time since the last capture.
    elapsed_time = time.time() - start_time

    if elapsed_time >= capture_interval:
        # Save the current frame as an image.
        image_filename = f"capture_{frame_number:04d}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Captured {image_filename}")

        # Reset the timer and increment the frame number.
        start_time = time.time()
        frame_number += 1

    # To exit the loop and stop capturing images, you can press 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close any open windows.
cap.release()
cv2.destroyAllWindows()
