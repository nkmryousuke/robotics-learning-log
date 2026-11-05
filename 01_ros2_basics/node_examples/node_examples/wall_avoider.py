import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class WallAvoider(Node):
    def __init__(self):
        super().__init__('wall_avoider')
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.sub = self.create_subscription(Pose,'/turtle1/pose',self.on_pose,10)
        self.timer = self.create_timer(0.1,self.on_timer)
        self.pose = None

    def on_pose(self,msg):
        self.pose = msg
    
    def on_timer(self):
        if self.pose is None:
            return
        ahead_x = self.pose.x + 1.0 * math.cos(self.pose.theta)
        ahead_y = self.pose.y + 1.0 * math.sin(self.pose.theta)
        safe = 1.0 < ahead_x <10.0 and 1.0 < ahead_y < 10.0

        msg = Twist()
        
        if safe:
            msg.linear.x = 2.0
        else:
            msg.angular.z = 1.5
        
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WallAvoider()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()  
        if rclpy.ok():
            rclpy.shutdown() 

if __name__ == '__main__':
    main()             