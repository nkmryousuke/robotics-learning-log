import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class PController(Node):

    def __init__(self):
        super().__init__('p_controller')
        self.declare_parameter('goal_x',8.0)
        self.declare_parameter('goal_y',8.0)
        self.declare_parameter('kp_linear',2.0)
        self.declare_parameter('kp_angular',2.0)
        self.declare_parameter('tolerance',0.2)
        self.goal_x = self.get_parameter('goal_x').value
        self.goal_y = self.get_parameter('goal_y').value
        self.kp_linear = self.get_parameter('kp_linear').value
        self.kp_angular = self.get_parameter('kp_angular').value
        self.tolerance = self.get_parameter('tolerance').value
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.sub = self.create_subscription(Pose,'/turtle1/pose',self.on_pose,10)
        self.timer = self.create_timer(0.1,self.on_timer)
        self.pose = None
        # TODO: パラメータの宣言（設計ノートの3）
        # TODO: 受信口、送信口、タイマー（設計ノートの2と8）
        # TODO: 覚えておくものの初期値（設計ノートの4）

    # TODO: 位置を受け取ったときの関数
    def on_pose(self,msg):
        self.pose = msg
        self.msg = msg
        self.now_x = self.msg.x
        self.now_y = self.msg.y
        self.now_theta = self.msg.theta

    # TODO: タイマーで呼ばれる関数（設計ノートの5、6、7）
    def on_timer(self):
        if self.pose is None:
            return
        if not math.sqrt((self.goal_x - self.now_x)**2 + (self.goal_y - self.now_y)**2) < self.tolerance:
            msg = Twist()
            msg.linear.x = self.kp_linear * math.sqrt((self.goal_x - self.now_x)**2 + (self.goal_y - self.now_y)**2)
            if math.atan2(self.goal_y - self.now_y,self.goal_x - self.now_x) - self.now_theta >= 0:
                msg.angular.z = self.kp_angular * (math.atan2(self.goal_y - self.now_y,self.goal_x - self.now_x) - self.now_theta)
            elif math.atan2(self.goal_y - self.now_y,self.goal_x - self.now_x) - self.now_theta < 0:
                msg.angular.z = self.kp_angular * (math.atan2(self.goal_y - self.now_y,self.goal_x - self.now_x) - self.now_theta)
            self.pub.publish(msg)
        else:
            return

def main(args=None):
    rclpy.init(args=args)
    node = PController()
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