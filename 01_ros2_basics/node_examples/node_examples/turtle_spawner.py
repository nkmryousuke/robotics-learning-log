import random
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class TurtleSpawner(Node):

    def __init__(self):
        super().__init__('turtle_spawner')
        self.declare_parameter('count', 3)
        self.declare_parameter('interval', 2.0)
        self.max_count = self.get_parameter('count').value

        self.cli = self.create_client(Spawn, '/spawn')
        self.timer = self.create_timer(self.get_parameter('interval').value, self.on_timer)
        self.spawned = 0

    def on_timer(self):
        if self.spawned >= self.max_count:
            self.timer.cancel()             
            self.get_logger().info('全部増やしました')
            return
        if not self.cli.service_is_ready():
            self.get_logger().info('/spawn を待っています')
            return

        req = Spawn.Request()
        req.x = random.uniform(1.0, 10.0)
        req.y = random.uniform(1.0, 10.0)
        req.theta = 0.0
        future = self.cli.call_async(req)
        future.add_done_callback(self.on_spawned)   
        self.spawned += 1

    def on_spawned(self, future):
        try:
            name = future.result().name
            self.get_logger().info(f'{name} が生まれた')
        except Exception as e:
            self.get_logger().error(f'失敗しました: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
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