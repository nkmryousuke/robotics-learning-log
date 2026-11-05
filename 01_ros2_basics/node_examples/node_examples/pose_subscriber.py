import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.sub = self.create_subscription(Pose,'/turtle1/pose',self.on_pose,10)
        self.count = 0
    def on_pose(self,msg):
        self.count += 1
        if self.count % 60 ==0:
            self.get_logger().info(
                f'x={msg.x:.2f},y={msg.y:.2f},'
                f'向き={math.degrees(msg.theta):.1f}度,'
                f'速さ={msg.linear_velocity:.2f}'
            )

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
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