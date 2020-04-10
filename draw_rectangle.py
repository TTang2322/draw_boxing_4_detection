#!/usr/bin/python3

import cv2

def draw_rectangle(arg_im_path):
	# pass
	im_path = arg_im_path

	im = cv2.imread(im_path)

	im_shap = im.shape
	wight = im_shap[0]
	height = im_shap[1]
	lable = 'prism'

	# factor=[0.528736,0.436224,0.558357,0.481889]
	factor = [0.380275,0.385850,0.438417,0.476157]

	# left_x = int(wight*factor[0])
	# left_y = int(height*factor[1])

	# # right_x = left_x+100
	# # right_y = left_y+100
	# right_x = int(wight*factor[2])
	# right_y = int(height*factor[3])
	# 
	left_x = int(height*factor[0])
	left_y = int(wight*factor[1])

	# right_x = left_x+100
	# right_y = left_y+100
	right_x = int(height*factor[2])
	right_y = int(wight*factor[3])

	print('left x,y are %f,%f'%(left_x,left_y))
	print('right x,y are %f,%f'%(right_x,right_y))

	font = cv2.FONT_HERSHEY_SIMPLEX

	cv2.rectangle(im,(left_x,left_y),(right_x,right_y),(0,255,0),4)
	cv2.putText(im,lable,(left_x,left_y-10),font,1,(0,255,0),2)

	cv2.imwrite('131449_000046.jpeg',im)

	print('Image processed')


def image_info(arg_file_path):
	# pass
	file_path = arg_file_path

	with open(file_path,'r') as f:
		lines = f.readlines()

		line_num = len(lines)




	return(line_num,)

	
if __name__ == '__main__':
	# main()
	im_path = "./Images/131449_000046.jpg"


	# image_num = image_info()

	draw_rectangle(im_path)
