#!/usr/bin/env python3
# import rosservice
# from roborts_msgs.msg import GimbalAngle
# from roborts_msgs.srv import *
# import rospy,sys
# import cv2
# import numpy as np
# import math
# from rospy.exceptions import ROSInterruptException
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge,CvBridgeError

# def get_img_data():
#     msg=rospy.wait_for_message('/camera/color/image_raw',Image)
#     print("tp")
   
#     depth_msg=rospy.wait_for_message('/camera/aligned_depth_to_color/image_raw',Image) 
#     cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
#     frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
#     print(cv_image.shape) #720*1280
#     print("\n")
#     print(frame.shape)#720*1280
#     #frame= cv2.resize(frame,(640,480),cv2.INTER_CUBIC)
#     x,y,w,h=cv2.selectROI("frame",frame)
#     print(x,y,w,h)
#     depth1=cv_image[y,x]
#     depth2=cv_image[y,x+w]
#     depth3=cv_image[y+h,x]
#     depth4=cv_image[y+h,x+w]
#     array=np.array([np.array([x,y,depth1]),np.array([x+w,y,depth2]),np.array([x,y+h,depth3]),np.array([x+w,y+h,depth4])])
#     return array 
# def magnitude(vtr):
#     sum=0
#     for i in range(len(vtr)):
#         sum+=(vtr[i])**2
#     return math.sqrt(sum)

# def translation_vector(position_array,cx,cy,fx,fy):
#     centeral_vector=np.array([0.0,0.0,0.0])
#     for position in position_array:
#         print(position)
#         u=position[0]
#         v=position[1]
#         z=position[2]
#         xc=float(((u-cx)*z)/fx)
#         yc=float(((v-cy)*z)/fy)
#         centeral_vector+=np.array([xc,yc,float(z)])
#     return centeral_vector/4


# if __name__ == '__main__':
#     # rospy.wait_for_service('cmd_fric_wheel')
#     # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
#     # fric_mode(1)
#     try: 
#         rospy.init_node('image_converter', anonymous=True)
#         pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)
#         #rospy.wait_for_service('shoot_cmd')
#         pixel_array=get_img_data()
#         final_vtr=translation_vector(pixel_array,642.621,360.055,636.565,636.565)
#         z=final_vtr[2]
#         x=final_vtr[0]
#         print(x)
#         yaw=math.atan((x-36.3)/z)
#         print("z:"+str(z))
#         print(yaw)
#         msg=GimbalAngle()
#         msg.yaw_mode=True
#         msg.pitch_mode=False
#         msg.yaw_angle=float(-yaw)
#         msg.pitch_angle=0.0        
#         pub.publish(msg)
#         # rospy.wait_for_service('cmd_fric_wheel')
#         # shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
#         #shoot(1,1)
                  
#     except KeyboardInterrupt:
#         print("Shutting Down")
#         cv2.destroyAllWindows()
#         pass
        
# ,b[1]+b[3])-y
    

#         #!/usr/bin/env python
# import rospy,sys
# import cv2
# import numpy as np
# import math
# from rospy.exceptions import ROSInterruptException
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge,CvBridgeError
# class image_converter:
#     def get_img_data(self,data):
       
#         self.pixel_cords=[[],[],[],[]]         
#         lower_bound=0
#         upper_bound=100
#         frame = self.bridge.imgmsg_to_cv2(data, "bgr8")  #change
#         hsv_low = np.array([22,59,76], np.uint8)
#         hsv_high = np.array([165,255,255], np.uint8)
#         hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#         # making mask for hsv range
#         mask = cv2.inRange(hsv, hsv_low, hsv_high)
#         # masking HSV value selected color becomes black
#         res = cv2.bitwise_and(frame,frame, mask=mask)
#         res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#         contours, hierarchy = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#         for cnt in contours:
#             area=cv2.contourArea(cnt)
#             if(20<area):
                
#                 #Health Bar detected
#                 x,y,w,h = cv2.boundingRect(cnt)
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=1,lineType=cv2.LINE_AA)
#                 cv2.putText(frame,str(int(area)),(x,y),fontScale=0.375,fontFace=cv2.FONT_HERSHEY_SIMPLEX,color=(0,255,0),thickness=1,lineType=cv2.LINE_AA)

        
        
#         return frame
       
        

#     def __init__(self):
#         self.bridge=CvBridge()
#         self.pub=rospy.Publisher("img_topic_1",Image,queue_size=1)
#         while 1:
#             msg=rospy.wait_for_message('/back_camera/image_raw',Image)
#             frame=self.get_img_data(msg)
#             try:
#                 self.pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
#             except CvBridgeError as e:
#                 print(e)

# if __name__ == '__main__':
#     try: 
#         rospy.init_node('image_converter', anonymous=True)
#         image_converter() roslaunch realsense2_camera rs_camera.launch align_depth:=true color_width:=1280 color_height:=720 depth_width:=1280 depth_height:=720
#     except KeyboardInterrupt and rospy.ServiceException as e:
#         print("Shutting Down")
#         print(e)
#         cv,b[1]+b[3])-y
    # 2.destroyAllWindows()
#         pass


# import rosservice
# from roborts_msgs.msg import GimbalAngle
# from roborts_msgs.srv import *
# import rospy,sys
# import cv2
# import numpy as np
# import math
# from rospy.exceptions import ROSInterruptException
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge,CvBridgeError
# import time
# from shoot import shoot


# def union(a,b):
#     x=min(a[0],b[0])
#     y=min(a[1],b[1])
#     w=max(a[0]+a[2],b[0]+b[2])-x
#     h=max(a[1]+a[3],b[1]+b[3])-y
    
#     return (x,y,w,h)
# # class img_data:
# #     def __init__(self):
# #         rospy.Subscriber('/camera/color/image_raw',Image,self.callback1)
# #         rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,self.callback2)

# #     def callback1(self,data):
# #         print("1")
# #         self.msg=data
        
# #     def callback2(self,data):
# #         print("in 2")
# #         self.depth_msg=data

# def callback1(data):
#     global msg
#     msg=data
        
# def callback2(data):
    
#     global depth_msg
#     depth_msg=data

# def get_img_data():
#     t1=time.time()
#     # msg=rospy.wait_for_message('/camera/color/image_raw',Image)v4l2-ctl -d /dev/video4 -c exposure_auto=1
#     #msg = rospy.Subscriber("/camera/color/image_raw",Image,callback) callback function likhna padega
#     #print("getting image data")
#     # depth_msg=rospy.wait_for_message('/camera/aligned_depth_to_color/image_raw',Image)
    
    
#     t2=time.time()
#     #print("Wait : "+str(t2-t1)) 
#     cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
#     frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
#     #print(cv_image.shape) #720*1280
#     #print("\n")
#     #rint(frame.shape)#720*1280
#     sx = 640.0 / 1280.0
#     sy = 480.0 / 720.0

#     frame = cv2.resize(frame,(640,480),0,0,interpolation=cv2.INTER_LINEAR)
#     # x,y,w,h=cv2.selectROI("frame",frame)
#     hsv_low = np.array([0,0,46], np.uint8)
#     hsv_high = np.array([28,255,255], np.uint8)
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, hsv_low, hsv_high)
#     res = cv2.bitwise_and(frame,frame, mask=mask)
    
#     res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#     # cv2.imwrite("test.jpg",res)
#     _,countours, hierarchy = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     countours=sorted(countours,key=cv2.contourArea,reverse=True)
#     print(len(countours))
#     dim = union(cv2.boundingRect(countours[0]),cv2.boundingRect(countours[1]))
#     x=dim[0]
#     y=dim[1]
#     w=dim[2]
#     h=dim[3]
#     cv2.drawContours(frame, countours, -1, (0,255,0),1)
#     cv2.imshow("cont", frame)
#     cv2.waitKey(1) 
#     # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
#     # fric_mode(1)

#     depthA=cv_image[y][x]
#     depthB=cv_image[y][x+w]
#     depthC=cv_image[y+h,x]
#     depthD=cv_image[y+h,x+w]
#     array=np.array([np.array([x,y,depthA]),np.array([x+w,y,depthB]),np.array([x,y+h,depthC]),np.array([x+w,y+h,depthD])])
#     return array 
# def magnitude(vtr):
#     sum=0
#     for i in range(len(vtr)):
#         sum+=(vtr[i])**2
#     return math.sqrt(sum)

# def translation_vector(position_array,cx,cy,fx,fy):
#     centeral_vector = np.array([0.0,0.0,0.0])
#     for position in position_array:
#         #print(position)
#         u=position[0]
#         v=position[1]
#         z=position[2]
#         xc=float(((u-cx)*z)/fx)
#         yc=float(((v-cy)*z)/fy)
#         centeral_vector+=np.array([xc,yc,float(z)])
#     return centeral_vector/4


# if __name__ == '__main__':
#     curr_yaw=0
#     # rospy.wait_for_service('cmd_fric_wheel')
#     # fric_mode=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
#     # fric_mode(1)
#     #print("started")
#     rospy.init_node('image_converter', anonymous=True)
    
#     pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=2)
#     #rospy.wait_for_service('cmd_fric_wheel')

#     integral_sum=0
#     bool1=1
#     bool2=0
#     i=1
#     r=rospy.Rate(30)
#     i=1
#     while not rospy.is_shutdown():
#         rospy.Subscriber('/camera/color/image_raw',Image,callback1)
#         rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,callback2)
#         if bool1:
#             print("wait for a while.....")
#             time.sleep(1.5)
#             bool1=0

#         # img_class=img_data()
#         t1=time.time()
#         pixel_array=get_img_data()
#         final_vtr=translation_vector(pixel_array,642.621,360.055,636.565,636.565)
#         z=final_vtr[2]
#         x=final_vtr[0]
#         dt3=time.time()-t1
#         #print("cal t :"+str(dt3))
#         print("x: {} z:{}".format(x,z))
#         yaw=math.atan((x)/z)
#        # print("z:"+str(z))
#         print(yaw)
#         pub_msg=GimbalAngle()
#         pub_msg.yaw_mode=True
#         pub_msg.pitch_mode=False
#         pub_msg.yaw_angle=float(-yaw)
#         pub_msg.pitch_angle=0.0
#         kp=0.6#.255
#         kd=0.000
#         ki=0
#         curr_yaw=pub_msg.yaw_angle 
#         t2=time.time()
#         dt=t2-t1
#         print("dt : "+str(dt))
#         print("t2 : ",str(t2))
#         integral_sum=integral_sum+curr_yaw*dt
#         if bool2:
#             curr_yaw= kp*pub_msg.yaw_angle-(kd*(prev_yaw-curr_yaw))/dt-ki*integral_sum
#         else:
#             bool2=1
#             curr_yaw= kp*pub_msg.yaw_angle-ki*integral_sum
#             pass
#         # if(abs(yaw)<0.1):
#         #     pub_msg.yaw_angle=0
#         #     curr_yaw=0
#         # else:
#         pub_msg.yaw_angle=curr_yaw
#         # d=(z-70)/1000
#         # H=
#         # g=9.8
#         # v=25
#         # theta=(v**2-math.sqrt(v**4-(g*d)**2+H*g))/g*d
#         # msg.pitch_angle=math.atan(abs(theta))
#         print("Pub_yaw  "+str(pub_msg.yaw_angle))
#         pub.publish(pub_msg)
#         # if (curr_yaw>-.08 and curr_yaw<.08):
#         #     shoot(z)
#         prev_yaw=curr_yaw
#         i=i-1
#         r.sleep()
#         # rospy.wait_for_service('cmd_fric_wheel')
#         # shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
#         # shoot(1,1)
                
    
#from tokenize import String, cookie_re
from types import coroutine
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
from std_msgs.msg import String

def union(a,b):
    x=min(a[0],b[0])
    y=min(a[1],b[1])
    w=max(a[0]+a[2],b[0]+b[2])-x
    h=max(a[1]+a[3],b[1]+b[3])-y
    
    return (x,y,w,h)
# class img_data:
#     def __init__(self):
#         rospy.Subscriber('/camera/color/image_raw',Image,self.callback1)
#         rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,self.callback2)

#     def callback1(self,data):
#         print("1")
#         self.msg=data
        
#     def callback2(self,data):
#         print("in 2")
#         self.depth_msg=data
corner_array=[]

def callback1(data):
    global corner_array
    coords = str(data.data).split(" ")
    #print(coords[1][:-1],coords[2][:-1])
    #coords = [float(value) for value in str(data).split(' ')]
    
    corner_array= [int(coords[1][:-1]) , int(coords[2][:-1]) , int(coords[1][:-1]) + int(coords[3][:-1]) ,int(coords[2][:-1]), int(coords[1][:-1]) + int(coords[3][:-1]) ,int(coords[2][:-1]) - int(coords[4][:-1]) ,int(coords[1][:-1]), int(coords[2][:-1]) - int(coords[4][:-1])]
    
    # for i in [0,1,2,3]:
    #     print(corner_array[0])
    #     print(" ")
   
def callback2(data):
    
    global depth_msg
    depth_msg=data

def get_img_data():
    print("getting image data")
    t1=time.time()
    # msg=rospy.wait_for_message('/camera/color/image_raw',Image)
    #msg = rospy.Subscriber("/camera/color/image_raw",Image,callback) callback function likhna padega
    #print("getting image data")
    # t3=time.time()
    # depth_msg=rospy.wait_for_message('/camera/aligned_depth_to_color/image_raw',Image)
    # t4=time.time()
    # dt4=t4-t3
   # print("dt4: "+ str(float(1/dt4)))
    print("got image data")
    
    t2=time.time()
    # print("Wait : "+str(t2-t1)) 
    cv_image = CvBridge().imgmsg_to_cv2(depth_msg,"passthrough")#720, 1280
    # frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    print(cv_image.shape) #720*1280
    print("\n")
    # #rint(frame.shape)#720*1280
    # # sx = 640.0 / 1280.0
    # # sy = 480.0 / 720.0
    # sx = 1.0
    # sy = 1.0

    # #frame = cv2.resize(frame,(640,480),0,0,interpolation=cv2.INTER_LINEAR)
    # # x,y,w,h=cv2.selectROI("frame",frame)
    # hsv_low = np.array([0,0,46], np.uint8)
    # hsv_high = np.array([28,255,255], np.uint8)
    # hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, hsv_low, hsv_high)
    # res = cv2.bitwise_and(frame,frame, mask=mask)
    
    # res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    # # cv2.imwrite("test.jpg",res)
    # _,countours, hierarchy = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # countours=sorted(countours,key=cv2.contourArea,reverse=True)
    # cv2.drawContours(frame, countours, -1, (0,255,0),1)
    # cv2.imshow("cont", frame)
    # cv2.waitKey(1) 
    # print(len(countours))
    # if(len(countours)<2):
    #     return False, np.array([0])
    # # x,y,w,h = cv2.boundingRect((cnt[0]),(cnt[1]
    # #cv2.drawContours(frame, countours, -1, (0,255,0),1)
    # #cv2.imshow("cont", frame)
    # #cv2.waitKey(1)

    # rect= union(cv2.boundingRect(countours[0]),cv2.boundingRect(countours[1]))
    # x = int(rect[0] / sx)
    # y = int(rect[1] / sy)
    # w = int(rect[2] / sx)
    # h = int(rect[3] / sy)
    # depthA=cv_image[y,x]
    # depthB=cv_image[y,x+w]
    # depthC=cv_image[y+h,x]
    # depthD=cv_image[y+h,x+w]
    depthA=cv_image[corner_array[1],corner_array[0]]
    depthB=cv_image[corner_array[3],corner_array[2]]
    depthC=cv_image[corner_array[5],corner_array[4]]
    depthD=cv_image[corner_array[7],corner_array[6]]
    # depthA=cv_image[corner_array[0],corner_array[1]]
    # depthB=cv_image[corner_array[2],corner_array[3]]
    # depthC=cv_image[corner_array[4],corner_array[5]]
    # depthD=cv_image[corner_array[6],corner_array[7]]
   
    array=np.array([np.array([corner_array[0],corner_array[1],depthA]),np.array([corner_array[2],corner_array[3],depthB]),np.array([corner_array[4],corner_array[5],depthC]),np.array([corner_array[6],corner_array[7],depthD])])
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
        rospy.Subscriber('/image_coordinates',String,callback1)
        rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,callback2)
        if bool1:
            print("wait for a while.....")
            time.sleep(3)
            bool1=0

        # img_class=img_data()
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
        H=0.26
        g=9.8
        v=25.0
        theta=(v**2-math.sqrt(v**4-(g*d)**2+H*g))/g*d
        # pub_msg.pitch_angle=math.atan(abs(theta))
        pub_msg.pitch_angle=0.6*math.atan(H/d)
        if (curr_yaw>-.08 and curr_yaw<.08 and iteration>90):
            shoot()
            iteration =0
        
        t2=time.time()
        dt=t2-t1
        # print("dt : "+str(dt))
        # print("t2 : ",str(t2))
        print("dt: {}".format(float(1/dt)))
        
        # integral_sum=integral_sum+curr_yaw*dt
        # if bool2:
        #     curr_yaw= kp*pub_msg.yaw_angle-(kd*(prev_yaw-curr_yaw))/dt-ki*integral_sum
        # else:
        #     bool2=1
        #     curr_yaw= kp*pub_msg.yaw_angle-ki*integral_sum
        #     pass
        # d=(z-70)/1000
        # H=29/100
        # g=9.8
        # v=25
        # theta=(v**2-math.sqrt(v**4-(g*d)**2+H*g))/g*d
        # pub_msg.pitch_angle=math.atan(abs(theta))
        
        print("Pub_ pitch: "+str(pub_msg.pitch_angle))
        pub_msg.yaw_angle=curr_yaw * kp_yaw
        print("Pub_yaw  "+str(pub_msg.yaw_angle))
        pub.publish(pub_msg)
        # if (curr_yaw>-.08 and curr_yaw<.08):
        #     shoot(z)
        prev_yaw=curr_yaw
        iteration=iteration+1
        r.sleep()

        # rospy.wait_for_service('cmd_fric_wheel')
        # shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
        # shoot(1,1)
                
  
