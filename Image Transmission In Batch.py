import serial
import numpy as np
import time
import pickle
import base64
from PIL import Image
import os

# Load your image
image_path = '/home/pi/Desktop/LoRa/Screenshot/receiverpy.png'
image = Image.open(image_path)
print("Image loaded successfully.")

# Get the size of the image file in bytes
image_file_size = os.path.getsize(image_path)
print(f"Image file size: {image_file_size} bytes")

# Convert the image to a numpy array
image_array = np.array(image)
print("Image converted to numpy array.")

# Serialize the numpy array using pickle
serialized_image = pickle.dumps(image_array)
print("Image serialized.")
print(f"Serialized image size: {len(serialized_image)} bytes")

# Encode the serialized image in base64
encoded_image = base64.b64encode(serialized_image)
print("Image encoded in base64.")
print(f"Encoded image size: {len(encoded_image)} bytes")

# Constants for transmission
BATCH_SIZE = 250  # The maximum data batch size in bytes (adjust as needed)
END_OF_BATCH = b'\n'  # Delimiter to signify the end of a batch

# Setup serial connection (replace '/dev/ttyACM0' with your Adafruit's serial port)
arduino = serial.Serial('/dev/ttyACM2', 9600)
time.sleep(2)  # Wait for the connection to establish
print("Serial connection established.")

# Start the total transmission timer
total_start_time = time.time()

# Send the base64 encoded serialized image over serial in batches
for i in range(0, len(encoded_image), BATCH_SIZE):
    start_time = time.time()  # Start time of batch transmission
    
    batch = encoded_image[i:i + BATCH_SIZE]
    arduino.write(batch)
    arduino.write(END_OF_BATCH)  # Signify end of batch
    
    end_time = time.time()  # End time of batch transmission
    time_taken = end_time - start_time  # Calculate time taken to send the batch
    
    print(f"Sent batch {i // BATCH_SIZE + 1}/{(len(encoded_image) + BATCH_SIZE - 1) // BATCH_SIZE}, Time taken: {time_taken:.3f} seconds")
    time.sleep(1)  # Wait a bit for the receiver to process this batch

# End the total transmission timer
total_end_time = time.time()
total_time_taken = total_end_time - total_start_time

print(f"All batches sent. Total transmission time: {total_time_taken:.3f} seconds.")
arduino.close()  # Close the serial connection
