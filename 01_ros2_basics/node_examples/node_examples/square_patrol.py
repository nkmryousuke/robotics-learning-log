import math
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.action import RotateAbsolute

# 東、北、西、南の向き（ラジアン）
HEADINGS = [0.0, math.pi / 2, math.pi, -math.pi / 2]


class SquarePatrol(Node):

    def __init__(self):
        super().__init__('square_patrol')
        self.declare_parameter('speed', 1.0)
        self.declare_parameter('side_time', 2.0)
        self.declare_parameter('laps', 2)

        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.clear_client = self.create_client(Empty, '/clear')
        self.rotate_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.timer = self.create_timer(0.1, self.on_timer)

        self.state = 'WAIT'
        self.state_start = self.get_clock().now()
        self.heading_index = 0
        self.sides_done = 0

    def elapsed(self):
        # 今の状態になってから何秒たったか
        return (self.get_clock().now() - self.state_start).nanoseconds / 1e9

    def change_state(self, new_state):
        self.state = new_state
        self.state_start = self.get_clock().now()
        self.get_logger().info(f'状態: {new_state}')

    def on_timer(self):
        if self.state == 'WAIT':
            if self.clear_client.service_is_ready() and self.rotate_client.server_is_ready():
                self.clear_client.call_async(Empty.Request())   # サービス：軌跡を消す
                self.start_turn()

        elif self.state == 'FORWARD':
            if self.elapsed() > self.get_parameter('side_time').value:
                self.sides_done += 1
                if self.sides_done >= 4 * self.get_parameter('laps').value:
                    self.change_state('DONE')
                    return
                self.heading_index = (self.heading_index + 1) % 4
                self.start_turn()
                return
            msg = Twist()                                          # トピック：直進
            msg.linear.x = self.get_parameter('speed').value
            self.pub.publish(msg)

        # TURNINGとDONEのときは何もしない（回転の結果を待つ）

    def start_turn(self):
        self.change_state('TURNING')
        goal = RotateAbsolute.Goal()                               # アクション：回転
        goal.theta = HEADINGS[self.heading_index]
        future = self.rotate_client.send_goal_async(goal)
        future.add_done_callback(self.on_goal_response)

    def on_goal_response(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('回転を断られました')
            self.change_state('DONE')
            return
        goal_handle.get_result_async().add_done_callback(self.on_turn_done)

    def on_turn_done(self, future):
        self.change_state('FORWARD')


def main(args=None):
    rclpy.init(args=args)
    node = SquarePatrol()
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