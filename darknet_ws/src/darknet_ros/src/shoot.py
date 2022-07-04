from roborts_msgs.msg import GimbalAngle
from roborts_msgs.msg import GimbalAngle
import rospy,sys
import math
from roborts_msgs.srv import *
from rospy.exceptions import ROSInterruptException
import time

def shoot():
    # d=depth
    # H=
    # g=9.8
    # v=25    
    # pub=rospy.Publisher('/cmd_gimbal_angle',GimbalAngle,queue_size=1)
    # 
    # mstheta=(v**2-math.sqrt(v**4-(g*d)**2+H*g))/g*dg=GimbalAngle()

    # msg.pitch_mode=1
    # msg.yaw_mode=0
    # msg.pitch_angle=math.atan(abs(theta))
    # msg.yaw_angle=0

    # pub.publish(msg)
    cmd_shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
    cmd_shoot(1,1)

