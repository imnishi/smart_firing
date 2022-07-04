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



def union(a,b):
    x=min(a[0],b[0])
    y=min(a[1],b[1])
    w=max(a[0]+a[2],b[0]+b[2])-x
    h=max(a[1]+a[3],b[1]+b[3])-y
    return (x,y,w,h)

def get_img_data():
    msg=rospy.wait_for_message('/camera/color/image_raw',Image)
    depth_msg=rospy.wait_for_message('/camera/aligned_depth_to_color/image_raw',Image) 
    cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
    frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    print(cv_image.shape) #720*1280
    print("\n")
    print(frame.shape)#720*1280
    frame= cv2.resize(frame,(640,480),cv2.INTER_CUBIC)
    x,y,w,h=cv2.selectROI("frame",frame)
    hsv_low = np.array([0,32,22], np.uint8)
    hsv_high = np.array([26,255,255], np.uint8)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    countours=sorted(countours,key=cv2.contourArea,reverse=True)
    # x,y,w,h = cv2.boundingRect((cnt[0]),(cnt[1])
    rect = cv2.boundingRect((cnt[0]),(cnt[1]))
    x = rect.x
    y = rect.y
    w = rect.width
    h = rect.height
    depthA=cv_image[y][x]
    depthB=cv_image[y][x+w]
    depthC=cv_image[y+h][x]
    depthD=cv_image[y+h][x+w]
    array=np.array([np.array([x,y,depthA]),np.array([x+w,y,depthB]),np.array([x,y+h,depthC]),np.array([x+w,y+h,depthD])])

def magnitude(vtr):
    sum=0
    for i in range(len(vtr)):
        sum+=(vtr[i])**2
    return math.sqrt(sum)

def translation_vector(position_array,cx,cy,fx,fy):
    centeral_vector = np.array([0,0,0,0])
    for position in position_array:
        print(position)
        u=position[0]
        v=position[1]
        z=position[2]
        xc=float(((u-cx)*z)/fx)
        yc=float(((v-cy)*z)/fy)
        centeral_vector+=np.array([xc,yc,float(z)])
    return centeral_vector/4


if __name__ == '__main__':
    # rospy.wait_for_service('cmd_fric_wheel')
    # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    # fric_mode(1)
    print("started")
    rospy.init_node('image_converter', anonymous=True)
    pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)
    # rospy.wait_for_service('shoot_cmd')
    while not rospy.is_shutdown():
        pixel_array=get_img_data()
        final_vtr=translation_vector(pixel_array,642.621,360.055,636.565,636.565)
        z=final_vtr[2]
        x=final_vtr[0]
        print(x)
        yaw=math.atan((x)/z)
        print("z:"+str(z))
        print(yaw)
        msg=GimbalAngle()
        msg.yaw_mode=True
        msg.pitch_mode=False
        msg.yaw_angle=float(-yaw)
        msg.pitch_angle=0.0        
        pub.publish(msg)
        rospy.wait_for_service('cmd_fric_wheel')
        shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
        shoot(1,1)
                
    
    