#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32 

nodeName='messagesubscriber'



#def callbackFunction(message):
	#print("We received %d"%message.data)
	
def callbackFunction1(msg):
    print("We received 1 %d"%msg.data)
    f1=open('/home/dinesh/testros/src/test_ros/python_script/test1.txt', 'w+')
    f1.write(str(msg.data))
    f1.close()

def callbackFunction2(msg):
    print("We received 2 %d"%msg.data)
    f2=open('/home/dinesh/testros/src/test_ros/python_script/test2.txt', 'w+')
    f2.write(str(msg.data))
    f2.close()
	
def callbackFunction3(msg):
    print("We received 3 %d"%msg.data)
    f3=open('/home/dinesh/testros/src/test_ros/python_script/test3.txt', 'w+')
    f3.write(str(msg.data))
    f3.close()
    
def callbackFunction4(msg):
    print("We received 4 %d"%msg.data)
    f4=open('/home/dinesh/testros/src/test_ros/python_script/test4.txt', 'w+')
    f4.write(str(msg.data))
    f4.close()
    
def callbackFunction5(msg):
    print("We received 5 %d"%msg.data)
    f5=open('/home/dinesh/testros/src/test_ros/python_script/test5.txt', 'w+')
    f5.write(str(msg.data))
    f5.close()

rospy.init_node(nodeName)
start_pub1=rospy.Publisher("start_ang1", Int32, queue_size = 5,latch = True)
start_pub2=rospy.Publisher("start_ang2", Int32, queue_size = 5,latch = True)
start_pub3=rospy.Publisher("start_ang3", Int32, queue_size = 5,latch = True)
start_pub4=rospy.Publisher("start_ang4", Int32, queue_size = 5,latch = True)
start_pub5=rospy.Publisher("start_ang5", Int32, queue_size = 5,latch = True)

with open('/home/dinesh/testros/src/test_ros/python_script/test1.txt', 'r') as file:
    text1 = int(file.read())
    start_pub1.publish(text1)
    
with open('/home/dinesh/testros/src/test_ros/python_script/test2.txt', 'r') as file:
    text2 = int(file.read())
    start_pub2.publish(text2)
    
with open('/home/dinesh/testros/src/test_ros/python_script/test3.txt', 'r') as file:
    text3 = int(file.read())
    start_pub3.publish(text3)
    
with open('/home/dinesh/testros/src/test_ros/python_script/test4.txt', 'r') as file:
    text4 = int(file.read())
    start_pub4.publish(text4)
    
with open('/home/dinesh/testros/src/test_ros/python_script/test5.txt', 'r') as file:
    text5 = int(file.read())
    start_pub5.publish(text5)


rospy.Subscriber("cur_ang1", Int32, callbackFunction1)
rospy.Subscriber("cur_ang2", Int32, callbackFunction2)
rospy.Subscriber("cur_ang3", Int32, callbackFunction3)
rospy.Subscriber("cur_ang4", Int32, callbackFunction4)
rospy.Subscriber("cur_ang5", Int32, callbackFunction5)
rospy.spin()


