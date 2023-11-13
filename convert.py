import subprocess
import sys

if(len(sys.argv)>1):
    print ("args: " +  str(sys.argv[1]))
    audio_file = sys.argv[1]
else: 
    print("Errore: no file specifided\n")
    print("Usage: Export audio file in raw unsigned 16 bit with audacity\n\nUsage: python convert.py <filename.estension>\nExample: python convert.py audio.raw")
    exit(1)


subprocess.run(["xxd", "-i", audio_file, "{}.h".format(audio_file)])

with open('{}.h'.format(audio_file), 'r') as file:
    result = file.read()

bytes_string = result[result.find("{")+1:result.find("};")]

bytes_string = bytes_string.replace('\n', '').strip()

bytes_string = bytes_string.split(",");


hex_values = []

for byte in bytes_string:
    hex_values.append(int(byte.strip(), 16))


with open('{}.h'.format(audio_file), 'w') as file:
# with open('file.h', 'w') as file:
    file.write("const unsigned char sample[] PROGMEM = {")
    for value in hex_values:
        file.write(str(value) + ",")
    
    file.write("};")

print("File saved as {}.h".format(audio_file))
