import base64
import pickle
import numpy as np

# Example base64 encoded data (you would replace this with your actual base64 string)
base64_encoded_data = 'gASVmAAAAAAAAACMFW51bXB5LmNvcmUubXVsdGlhcnJheZSMDF9yZWNvbnN0cnVjdJSTlIwFbnVtcHmUjAduZGFycmF5lJOUSwCFlEMBYpSHlFKUKEsBSwSFlGgDjAVkdHlwZZSTlIwCaTSUiYiHlFKUKEsDjAE8lE5OTkr/////Sv////9LAHSUYolDEAIAAAADAAAABAAAAAUAAACUdJRiLg=='

# Decode the base64 encoded data
decoded_data = base64.b64decode(base64_encoded_data)

# Deserialize the data to get back the original numpy array
numpy_array = pickle.loads(decoded_data)

# Print the resulting numpy array
print(numpy_array)
