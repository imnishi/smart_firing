#!/usr/bin/env python
import rosservice
from roborts_msgs.msg import GimbalAngle
from roborts_msgs.srv import *
import rospy,sys
import cv2
import numpy as np
import math
from rospy.exceptions import ROSInterruptException
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import time



if __name__ == '__main__':
    print("1")
    # rospy.wait_for_service('cmd_fric_wheel')
    # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    # fric_mode(1)
    #print("started")
    rospy.init_node('pitch_pub', anonymous=True)
    
    pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)

    time.sleep(0.2)

    msg=GimbalAngle()
    global_pitch=-(25*(math.pi)/180)
    while not rospy.is_shutdown():
        msg.pitch_mode=0
        msg.yaw_mode=1
        msg.yaw_angle=0
        msg.pitch_angle=global_pitch
        pub.publish(msg)
        print("hui")
        global_pitch+=(math.pi)/180
        time.sleep(0.3)
                

    #rospy.spin()


