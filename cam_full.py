import serial, struct, time
import datetime




def writeJPEG(timestamp):
    ser = serial.Serial('/dev/cu.usbserial-1440', 115200, timeout=5)

    while True:
        ser.write(bytes("h", "utf-8"))

        # output = ser.readline()
        # print(output)
        # if "error" in str(output):
        #     print("Error found in response")
        #     break



        # Wait for header
        header = ser.read(4)
        if header != b'IMG0':
            continue

        # Read length (4 bytes)
        length_bytes = ser.read(4)
        if len(length_bytes) < 4:
            continue
        (length,) = struct.unpack('<I', length_bytes)
        print(f"Frame length: {length}")

        # Read the image data
        data = ser.read(length)

        if len(data) != length:
            print("Incomplete frame!")
            print("Trying anyways...")
            #continue

        # Optionally read footer
        footer = ser.read(4)
        if footer != b'DONE':
            print("Bad footer, skipping frame.")
            continue

        with open(f"capture_{timestamp}.jpg", 'wb') as f:
            f.write(data)
        print("Saved capture.jpg")
        break

while True:
    print("q for quit, h for capture")
    read = input("Input: ")
    if read == "q":
        exit()
    if read == "h":
        formatted = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-")[:-3]
        writeJPEG(formatted)





