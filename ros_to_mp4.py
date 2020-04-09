#!/usr/bin/env python
from cv_bridge import CvBridge
import cv2
from sensor_msgs.msg import Image
import rospy


class RosConverterVideo:

	def __init__(self):
		rospy.init_node('ros_converter_video',anonymous=True)
		self.Bridge=CvBridge()
		self.image_sub=rospy.Subscriber("/darknet_ros/detection_image", Image, self.callback, queue_size=100)
		self.vwriter = cv2.VideoWriter("test.mp4",cv2.VideoWriter_fourcc(*'mp4v'),10,(640,480))

	def callback(self,msg):
		topic_img=self.Bridge.imgmsg_to_cv2(msg,"bgr8")
		self.vwriter.write(topic_img)
		

def main():
	ros_to_mp4=RosConverterVideo()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')



if __name__=='__main__':
	main()
