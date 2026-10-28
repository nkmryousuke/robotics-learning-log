import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MinimalClient(Node):

    def __init__(self):
        super().__init__('minimal_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスを待っています...')

    def send_request(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        return self.cli.call_async(req)


def main(args=None):
    rclpy.init(args=args)
    node = MinimalClient()
    a, b = int(sys.argv[1]), int(sys.argv[2])
    future = node.send_request(a, b)
    rclpy.spin_until_future_complete(node, future)
    node.get_logger().info(f'結果: {a} + {b} = {future.result().sum}')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()