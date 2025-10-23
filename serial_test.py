import serial
do_serial = True

if do_serial:
	ser = serial.Serial('/dev/cu.usbserial-1430', 115200, timeout=5)

	while True:
		user_input = input("Input: ")
		if user_input == "q":
			exit()
		ser.write(bytes(user_input, "utf-8"))


		# Goal is to be able to send (write) something and get a specific response
		output = ser.readline()
		print(output)

		while len(output) > 3:
			output = str(ser.readline())
			print(len(output), output)





# while True:
# 	user_input = input("Input: ")
# 	if user_input == "q":
# 		break
# 	print(user_input)
# 	print(bytes(user_input, "utf-8"))