import zlib
import json

json_file_path = 'accessory-effect.json'
bin_file_path = 'accessory-effect'

with open (json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

json_string = json.dumps(json_data)
binary_data = json_string.encode('utf-8')

try: 
    compressed_data = zlib.compress(binary_data)
except zlib.error as e:
    print("Error compressing data:", e)
    compressed_data = binary_data

with open(bin_file_path, 'wb') as bin_file:
    bin_file.write(compressed_data)

print('Conversion completed')