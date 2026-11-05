import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpeedLimiter(Node):
    def __init__(self):
        super().__init__('speed_limiter')
        self.declare_parameter('max_linear',1.0)
        self.sub = self.create_subscription(Twist,'/cmd_vel_raw',self.on_cmd,10)
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)

    def on_cmd(self,msg):
        limit= self.get_parameter('max_linear').value
        msg.linear.x = max(-limit,min(limit,msg.linear.x))
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SpeedLimiter()
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

#ros2 run turtlesim turtle_teleop_key --ros-args -r /turtle1/cmd_vel:=/cmd_vel_raw