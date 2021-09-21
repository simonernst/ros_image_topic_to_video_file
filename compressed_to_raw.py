#!/usr/bin/env python2

import rospy
import cv2

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

class CompressedToRaw:

	def __init__(self):
		rospy.init_node('compressed_to_raw')
		self.image_pub = rospy.Publisher("camera/rgb/image_raw", Image)
		self.image_sub = rospy.Subscriber("camera/color/image_raw/compressed", CompressedImage, self.callback)
		self.bridge = CvBridge()
		rospy.spin()


	def callback(self, msg):
		cv_image = self.bridge.compressed_imgmsg_to_cv2(msg,"bgr8")
		self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image,"bgr8"))

if __name__ == "__main__":
	CompressedToRaw()