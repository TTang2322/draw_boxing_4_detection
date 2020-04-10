#!/usr/bin/python3

import cv2

def draw_rectangle(arg_im_name,arg_im_path,arg_factor):
	im_name = arg_im_name

	im_path = arg_im_path

	im = cv2.imread(im_path)

	im_shap = im.shape
	wight = im_shap[0]
	height = im_shap[1]
	lable = 'prism'

	factor = arg_factor

	left_x = int(height*float(factor[0]))
	left_y = int(wight*float(factor[1]))
	right_x = int(height*float(factor[2]))
	right_y = int(wight*float(factor[3]))


	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.rectangle(im,(left_x,left_y),(right_x,right_y),(0,255,0),4)
	cv2.putText(im,lable,(left_x,left_y-10),font,1,(0,255,0),2)
	cv2.imwrite('./Labeled/'+im_name,im)


def image_info(arg_file_path):
	file_path = arg_file_path

	counter = 0

	with open(file_path,'r') as f:
		lines = f.readlines()

		for line in lines:

			counter +=1

			items = line.split(',')

			im_name = items[1]
			im_names = im_name.split('/')
			im_name = im_names[4]
			im_label = items[2]
			factor = []
			factor.append(items[3])
			factor.append(items[4])
			factor.append(items[7])
			factor.append(items[8])

			im_path = "./Images/"+im_name

			try:
				draw_rectangle(im_name,im_path,factor)
				print(str(counter)+': '+im_name+" is boxed successfully")
			except:
				print(str(counter)+': '+"Error: no image is found")
				pass

if __name__ == '__main__':
	file_path = "./Data/labeled_data_from_googleCloud__open.txt"
	image_info(file_path)
