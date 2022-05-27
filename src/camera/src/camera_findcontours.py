import cv2
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	img2 = frame.copy()
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	
	
	cv2.imshow('img2', gray)
	cv2.waitKey(1)
		
