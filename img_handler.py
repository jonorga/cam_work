import os, cv2
import numpy as np

show_image = True
pic_list = [x for x in os.listdir() if x[-4:] == ".jpg"]
pic_list.sort()

# Image is rows of pixels
image1 = cv2.imread(pic_list[5])
image2 = cv2.imread(pic_list[3])


def pixelCoversion(pixel1, pixel2):
	# Blue, Green, Red
	out_pixel = []
	for color1, color2 in zip(pixel1, pixel2):
		color = color1 - color2 if color1 > color2 else color2 - color1
		out_pixel.append(color)

	return out_pixel



height = 600
width = 800
row = 0
column = 0
new_pic = []
while row < height:
	new_pic.append([])
	column = 0
	while column < width:
		pixel = pixelCoversion(image1[row][column], image2[row][column])
		new_pic[row].append(pixel)
		column += 1
	row += 1


formatted = np.array(new_pic)
cv2.imwrite("output.jpg", formatted)

if show_image:
	cv2.namedWindow("Image1", cv2.WINDOW_NORMAL)
	cv2.namedWindow("Image2", cv2.WINDOW_NORMAL)
	cv2.namedWindow("Output", cv2.WINDOW_NORMAL)

	cv2.imshow("Image1", image1)
	cv2.imshow("Image2", image2)
	cv2.resizeWindow("Image2", 500, 350)
	cv2.moveWindow("Image2", 0, 300)
	cv2.resizeWindow("Image1", 500, 350)
	
	cv2.imshow("Output", formatted)
	cv2.resizeWindow("Output", 500, 350)
	cv2.moveWindow("Output", 500, -100)
	cv2.waitKey(0)
	cv2.destroyAllWindows()