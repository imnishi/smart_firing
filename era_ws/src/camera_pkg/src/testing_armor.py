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

def get_img_data():
    msg=rospy.wait_for_message('/back_camera/image_raw',Image)
    frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    print(frame.size)
    #frame= cv2.resize(frame,(640,480),cv2.INTER_CUBIC)
    print("getting image data")
    x,y,w,h=cv2.selectROI("frame",frame)
    return np.array([[x,y],[x+w,y],[x,y+h],[x+w,y+h]])
def magnitude(vtr):
    sum=0
    for i in range(len(vtr)):
        sum+=(vtr[i])**2
    return math.sqrt(sum)
def translation_vector(pixel_cord,w,h):
    real_world_cord=np.array([[0,0],[0+w,0],[0,0+h],[0+w,0+h]])
    K=np.array([457.1367,0,0,0,607.4540,0,331.8406,234.2436,1]).reshape(3,3).transpose()
    H,status=cv2.findHomography(real_world_cord,pixel_cord)
    #print(H@(np.array([0,0,1]).transpose()))
    res=np.matmul(np.linalg.inv(K),H)
    magntitude_res=magnitude(res[:,0].transpose())
    res=res/magntitude_res
    t=res[:,2]
    r1=res[:,0]
    r2=res[:,1]
    r3=np.cross(r1,r2)
    res_final=np.matmul(np.array([r1,r2,r3]),t)
    yaw=math.acos(-t[2]/magnitude(t))
    if(yaw>1.5709):
        yaw=1.5709-yaw
    
    return yaw
        

if __name__ == '__main__':
    # rospy.wait_for_service('cmd_fric_wheel')
    # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    # fric_mode(1)
    try: 
        rospy.init_node('image_converter', anonymous=True)
        pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)
        
        #rospy.wait_for_service('shoot_cmd')
        cords=get_img_data()
        yaw=translation_vector(cords,13.4,5.5)
        print(yaw)
        msg=GimbalAngle()
        msg.yaw_mode=True
        msg.pitch_mode=False
        msg.yaw_angle=float(yaw)
        msg.pitch_angle=0.0        
        pub.publish(msg)
        # rospy.wait_for_service('cmd_fric_wheel')
        # shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
        #shoot(1,1)
                  
    except KeyboardInterrupt:
        print("Shutting Down")
        cv2.destroyAllWindows()
        pass
        
