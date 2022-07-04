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
    print("getting image data")
    msg=rospy.wait_for_message('/camera/color/image_raw',Image)
    print("tp")
   
    depth_msg=rospy.wait_for_message('/camera/aligned_depth_to_color/image_raw',Image) 
    cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
    frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    print(cv_image.shape) #720*1280
    print("\n")
    print(frame.shape)#720*1280
    #frame= cv2.resize(frame,(640,480),cv2.INTER_CUBIC)
    x,y,w,h=cv2.selectROI("frame",frame)
    print(x,y,w,h)
    depth1=cv_image[y][x]
    depth2=cv_image[y][x+w]
    depth3=cv_image[y+h][x]
    depth4=cv_image[y+h][x+w]
    array=np.array([np.array([x,y,depth1]),np.array([x+w,y,depth2]),np.array([x,y+h,depth3]),np.array([x+w,y+h,depth4])])
    return array 
def magnitude(vtr):
    sum=0
    for i in range(len(vtr)):
        sum+=(vtr[i])**2
    return math.sqrt(sum)

def translation_vector(position_array,cx,cy,fx,fy):
    centeral_vector=np.array([0.0,0.0,0.0])
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
    rospy.wait_for_service('cmd_fric_wheel')
    fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    fric_mode(1)
    try: 
        rospy.init_node('image_converter', anonymous=True)
        pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)
        #rospy.wait_for_service('shoot_cmd')
        pixel_array=get_img_data()
        final_vtr=translation_vector(pixel_array,321.573,240.033,381.939,381.939)
        z=final_vtr[2]
        x=final_vtr[0]
        print(x)
        yaw=math.atan((x-36)/z)
        print("z:"+str(z))
        print(yaw)
        msg=GimbalAngle()
        msg.yaw_mode=True
        msg.pitch_mode=False
        msg.yaw_angle=float(-yaw)
        msg.pitch_angle=0.0        
        pub.publish(msg)
        # rospy.wait_for_service('cmd_fric_wheel')
        # shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
        #shoot(1,1)
                  
    except KeyboardInterrupt:
        print("Shutting Down")
        cv2.destroyAllWindows()
        pass
        
