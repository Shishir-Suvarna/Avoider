!/usr/bin/env python

# moving bot inside a world
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

m = "global"

def callback(msg):
m = msg.ranges

def mover():
    pub = rospy.Publisher('cmd_vel',Twist, queue_size = 10)
    rospy.init_node('mover', anonymous=True)
    vel_msg = Twist()
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        for i in m[121:240]:                        #if the readings belong to the values in the middle of the laser arc,
          if i<0.4:                                #and if the values are less than a limit, i.e the robot gets too close to obstacle, then it turns randomly
             vel_msg.linear.x = 0
            vel_msg.linear.y = 0
              vel_msg.linear.z = 0
              vel_msg.angular.x = 0
              vel_msg.angular.y = 0
              vel_msg.angular.z = random.randint(0,30)
              rospy.loginfo(vel_msg)
              pub.publish(vel_msg)

          else:
             vel_msg.linear.x = 2
             vel_msg.linear.y = 0
             vel_msg.linear.z = 0
             vel_msg.angular.x = 0
             vel_msg.angular.y = 0
             vel_msg.angular.z = 0
             rospy.loginfo(vel_msg)
             pub.publish(vel_msg)
             rospy.spin()



if __name__ == '__main__':
  try:
     move()
  except rospy.ROSInterruptException:
     pass
