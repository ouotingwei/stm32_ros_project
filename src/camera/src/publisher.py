#!/usr/bin/env python
# license removed for brevity
import os
import rospy
import sys

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def talker():
     pub = rospy.Publisher('/tutorial/image', Image, queue_size=1)
     rospy.init_node('talker', anonymous=True)
     rate = rospy.Rate(30)
     bridge = CvBridge()
     Video = cv2.VideoCapture(0)
     
     
     while not rospy.is_shutdown():
         ret, img = Video.read()
         gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
         cv2.imshow("talker", gray)
         cv2.waitKey(30)
         pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
         rate.sleep()

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass


