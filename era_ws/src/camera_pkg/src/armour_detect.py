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
from shoot import shoot


def union(a,b):
    x=min(a[0],b[0])
    y=min(a[1],b[1])
    w=max(a[0]+a[2],b[0]+b[2])-x
    h=max(a[1]+a[3],b[1]+b[3])-y
    
    return (x,y,w,h)


def callback1(data):
    
    global msg
    msg=data
        
def callback2(data):
    
    global depth_msg
    depth_msg=data

def get_img_data():
    t1=time.time()
   
    
    t2=time.time()
    print("Wait : "+str(t2-t1)) 
    cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
    frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
 
    sx = 1.0
    sy = 1.0

    hsv_low = np.array([0,0,46], np.uint8)
    hsv_high = np.array([28,255,255], np.uint8)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    
    res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("test.jpg",res)
    _,countours, hierarchy = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    countours=sorted(countours,key=cv2.contourArea,reverse=True)
    cv2.drawContours(frame, countours, -1, (0,255,0),1)
    cv2.imshow("cont", frame)
    cv2.waitKey(1) 
    print(len(countours))
    if(len(countours)<2):
        return False, np.array([0])

    rect= union(cv2.boundingRect(countours[0]),cv2.boundingRect(countours[1]))
    x = int(rect[0] / sx)
    y = int(rect[1] / sy)
    w = int(rect[2] / sx)
    h = int(rect[3] / sy)
    depthA=cv_image[y,x]
    depthB=cv_image[y,x+w]
    depthC=cv_image[y+h,x]
    depthD=cv_image[y+h,x+w]
    array=np.array([np.array([x,y,depthA]),np.array([x+w,y,depthB]),np.array([x,y+h,depthC]),np.array([x+w,y+h,depthD])])
    return True, array 
def magnitude(vtr):
    sum=0
    for i in range(len(vtr)):
        sum+=(vtr[i])**2
    return math.sqrt(sum)

def translation_vector(position_array,cx,cy,fx,fy):
    centeral_vector = np.array([0.0,0.0,0.0])
    for position in position_array:
        #print(position)
        u=position[0]
        v=position[1]
        z=position[2]
        xc=float(((u-cx)*z)/fx)
        yc=float(((v-cy)*z)/fy)
        centeral_vector+=np.array([xc,yc,float(z)])
    return centeral_vector/4


if __name__ == '__main__':
    curr_yaw=0
    rospy.wait_for_service('cmd_fric_wheel')
    fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    fric_mode(1)
    print("started")
    rospy.init_node('image_converter', anonymous=True)
    
    pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=2)
    # rospy.wait_for_service('shoot_cmd')

    integral_sum=0
    itr=0
    bool1=1
    bool2=0
    i=1
    r=rospy.Rate(30)
    iteration=0

    while not rospy.is_shutdown():
        rospy.Subscriber('/camera/color/image_raw',Image,callback1)
        rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,callback2)
        if bool1:
            print("wait for a while.....")
            time.sleep(1)
            bool1=0
        print("here")

        t1=time.time()
        result, pixel_array=get_img_data()

        if(not result):
            continue

    
        final_vtr=translation_vector(pixel_array,642.621,360.055,636.565,636.565)
        z=final_vtr[2]
        x=final_vtr[0]
        dt3=time.time()-t1
        print("cal t :"+str(dt3))
        print(x)
        yaw=math.atan((x)/z)
        print("z:"+str(z))
        print(yaw)
        pub_msg=GimbalAngle()
        pub_msg.yaw_mode=1
        pub_msg.pitch_mode=0
        pub_msg.yaw_angle=float(-yaw)
        pub_msg.pitch_angle=0.0
        kp_yaw=0.6#.255
        kd=0
        ki=0
        curr_yaw=pub_msg.yaw_angle 
        
        d=(z+100)/1000.0
        # if(d<1.8):
        #     H=0.26
        # if((d>1.8)and(d<2.5)):
        #     H=0.22
        # else:
        #     H=0.18
        H=0.26
        g=9.8
        v=11.5

        # theta=(v**2-math.sqrt(v**4-g*(d*d)+2*v*v*H))/g*d
        
        theta=-((v*v)-math.sqrt((v*v*v*v)-(g*g*d*d)+(2*g*v*v*H)))/(g*d)
        print("theta:",theta*(180/math.pi))
        pub_msg.pitch_angle=math.atan(theta)
        # pub_msg.pitch_angle=0.6*math.atan(H/d)
        if (curr_yaw>-.08 and curr_yaw<.08 and iteration>90):
            shoot()
            iteration =0
        
        print("Pub_ pitch: "+str(pub_msg.pitch_angle*180/math.pi))
        pub_msg.yaw_angle=curr_yaw * kp_yaw
        print("Pub_yaw  "+str(pub_msg.yaw_angle*180/math.pi))
        pub.publish(pub_msg)
        # if (curr_yaw>-.08 and curr_yaw<.08):
        #     shoot()
        prev_yaw=curr_yaw
        iteration=iteration+1
        r.sleep()

  