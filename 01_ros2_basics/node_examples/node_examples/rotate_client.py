import math
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtlesim.action import RotateAbsolute


class RotateClient(Node):

    def __init__(self):
        super().__init__('rotate_client')
        self.declare_parameter('target_deg', 90.0)
        self.client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.timer = self.create_timer(0.5, self.send_goal_once)

    def send_goal_once(self):
        if not self.client.server_is_ready():
            self.get_logger().info('アクションサーバーを待っています')
            return
        self.timer.cancel()     

        goal = RotateAbsolute.Goal()
        goal.theta = math.radians(self.get_parameter('target_deg').value)
        future = self.client.send_goal_async(goal, feedback_callback=self.on_feedback)
        future.add_done_callback(self.on_goal_response)

    def on_goal_response(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('断られました')
            return
        self.get_logger().info('引き受けてもらえました')
        goal_handle.get_result_async().add_done_callback(self.on_result)

    def on_feedback(self, feedback_msg):
        remaining = feedback_msg.feedback.remaining
        self.get_logger().info(f'残り {math.degrees(remaining):.1f} 度')

    def on_result(self, future):
        result = future.result().result
        self.get_logger().info(f'完了: {math.degrees(result.delta):.1f} 度回りました')


def main(args=None):
    rclpy.init(args=args)
    node = RotateClient()
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