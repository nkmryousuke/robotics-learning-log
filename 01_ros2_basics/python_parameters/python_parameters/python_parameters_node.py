import rclpy
from rclpy.node import Node


class MinimalParam(Node):

    def __init__(self):
        super().__init__('minimal_param_node')
        self.declare_parameter('my_parameter', 'world')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        name = self.get_parameter('my_parameter').value
        self.get_logger().info(f'Hello {name}!')


def main(args=None):
    rclpy.init(args=args)
    node = MinimalParam()
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