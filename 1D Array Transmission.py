import serial
import numpy as np
import time
import pickle
import base64

# Function to send data to Arduino and receive response
def write_read(serial_port, data):
    serial_port.write(data)
    time.sleep(0.05)  # Short delay to ensure data is transmitted and Arduino has time to respond
    if serial_port.inWaiting() > 0:
        response = serial_port.readline()
        return response

# Example array (this would be your tensor)
array = np.array([2, 3, 4, 5])

# Serialize the array using pickle
serialized_array = pickle.dumps(array)
print('Array being sent ',array)
print('Serialized array ',serialized_array)

encoded_array = base64.b64encode(serialized_array)
print('64 Encoded array ', encoded_array)

# Setup serial connection (replace 'COM4' with your actual serial port)
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

# Send the serialized array over serial and receive response
response = write_read(arduino, encoded_array)
print(response)  # Print the response from Arduino

arduino.close()  # Close the serial connection
