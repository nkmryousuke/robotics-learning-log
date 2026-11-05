import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool

class PaisableDriver(Node):
    def __init__(self):
        super().__init__('pausable_driver')
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.on_timer)
        self.srv = self.create_service(SetBool,'set_paused',self.on_set_paused)
        self.paused = False
    def on_timer(self):
        if self.paused:
            return
        msg = Twist()
        msg.linear.x = 1.5
        msg.angular.z = 0.8
        self.pub.publish(msg)
    def on_set_paused(self,request,response):
        self.paused = request.data
        response.success = True
        response.message = '一時停止しました' if self.paused else 'saikaisimasita'
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)          # ROS 2の初期化
    node = PausableDriver()        # ノードを生成する
    try:
        rclpy.spin(node)           # 回し続ける（タイマーもサービスもここで処理される）
    except KeyboardInterrupt:
        pass                       # Ctrl+C で静かに抜ける
    finally:
        node.destroy_node()        # ノードを解放する
        if rclpy.ok():
            rclpy.shutdown()       # まだ動いていれば終了する


if __name__ == '__main__':
    main()                     
