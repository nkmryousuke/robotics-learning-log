import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer,CancelResponse,GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from example_interfaces.action import Fibonacci

class FibonacciServer(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self.server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            execute_callback = self.execute_callback,
            goal_callback = self.goal_callback,
            cancel_callback = self.cancel_callback,
            callback_group = ReentrantCallbackGroup(),
        )
    def goal_callback(self, goal_request):
        if not 1 <= goal_request.order <= 30:
            self.get_logger().info(f'断ります: order={goal_request.order}')
            return GoalResponse.REJECT
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('キャンセルを受け付けます')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'開始: order={goal_handle.request.order}')
        sequence = [0, 1]
        feedback = Fibonacci.Feedback()

        for i in range(1, goal_handle.request.order):
            if goal_handle.is_cancel_requested:     
                goal_handle.canceled()
                result = Fibonacci.Result()
                result.sequence = sequence
                return result

            sequence.append(sequence[i] + sequence[i - 1])
            feedback.sequence = sequence
            goal_handle.publish_feedback(feedback)  
            time.sleep(0.5)                        

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = sequence
        return result


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciServer()
    try:
        rclpy.spin(node, executor=MultiThreadedExecutor())
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()