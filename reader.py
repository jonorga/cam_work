import serial, struct

ser = serial.Serial('/dev/cu.usbserial-1430', 115200, timeout=5)

while True:
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
        continue

    # Optionally read footer
    footer = ser.read(4)
    if footer != b'DONE':
        print("Bad footer, skipping frame.")
        continue

    with open('capture.jpg', 'wb') as f:
        f.write(data)
    print("Saved capture.jpg")
    break