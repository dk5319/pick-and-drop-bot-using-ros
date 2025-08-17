#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32

nodeName='messagepublisher'

topicName1='cur_ang1'
topicName2='cur_ang2'
topicName3='cur_ang3'
topicName4='cur_ang4'
topicName5='cur_ang5'


rospy.init_node(nodeName, anonymous=True)

publisher1=rospy.Publisher(topicName1,Int32, queue_size = 5)
publisher2=rospy.Publisher(topicName2,Int32, queue_size = 5)
publisher3=rospy.Publisher(topicName3,Int32, queue_size = 5)
publisher4=rospy.Publisher(topicName4,Int32, queue_size = 5)
publisher5=rospy.Publisher(topicName5,Int32, queue_size = 5)

ratePublisher=rospy.Rate(1)

intMessage=0

while not rospy.is_shutdown():

	rospy.loginfo(intMessage)
	
	publisher1.publish(intMessage)
	publisher2.publish(intMessage)
	publisher3.publish(intMessage)
	publisher4.publish(intMessage)
	publisher5.publish(intMessage)
	
	intMessage=intMessage+1
	
	ratePublisher.sleep()
	
	


