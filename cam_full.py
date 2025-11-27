import serial, struct, time
import datetime




def writeJPEG(timestamp):
    ser = serial.Serial('/dev/cu.usbserial-14510', 115200, timeout=10)

    sofar = []
    tries = 1
    count = 0

    while True:
        ser.write(bytes("h", "utf-8"))

        # output = ser.readline()
        # sofar.append(output)
        # print(output)
        # if "error" in str(output):
        #     print("Error found in response")
        #     break



        # Wait for header
        header = ser.read(4)
        sofar.append(header)
        if header != b'IMG0':
            continue

        # Read length (4 bytes)
        length_bytes = ser.read(4)
        sofar.append(length_bytes)
        if len(length_bytes) < 4:
            continue
        (length,) = struct.unpack('<I', length_bytes)
        print(f"Frame length: {length}")

        # Read the image data
        data = ser.read(length)
        sofar.append(data)

        if len(data) != length:
            print("Incomplete frame!")
            print("Trying anyways...", count, tries)
            count += 1
            #continue

        # Optionally read footer
        footer = ser.read(4)
        sofar.append(footer)
        if footer != b'DONE':
            print("Bad footer, skipping frame.")
            break
            
        if count == tries:
            break

        with open(f"capture_{timestamp}.jpg", 'wb') as f:
            f.write(data)
        print("Saved capture.jpg")
        break
    # analysis = [len(x) for x in sofar]
    # print(analysis)
    # print(sofar[-1][-100:])
    # print(sofar[-1])
    # for i in sofar:
    #     if len(i) < 100:
    #         print(len(i), i)

while True:
    print("q for quit, h for capture")
    read = input("Input: ")
    if read == "q":
        exit()
    if read == "h":
        formatted = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-")[:-3]
        writeJPEG(formatted)





