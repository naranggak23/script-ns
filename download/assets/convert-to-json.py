import zlib
import json

bin_file_path = 'accessory-effect'
json_file_path = 'accessory-effect.json'

with open (bin_file_path, 'rb') as bin_file:
    bin_data = bin_file.read()

try:
    decompressed_data = zlib.decompress(bin_data)
except zlib.error as e:
    print("Error decompressing data: ", e)
    decompressed_data = bin_data

try:
    json_data = json.loads(decompressed_data)
except json.JSONDecodeError as e:
    print("Error decoding JSON data: ", e)
    json_data = {}

with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4) 

print("Conversion complete")