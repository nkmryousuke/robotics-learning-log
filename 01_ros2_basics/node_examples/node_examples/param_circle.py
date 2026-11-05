import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rcl_interfaces.msg import SetParametersResult

class ParamCircle(Node):
    def __init__(self):
        super().__init__('param_circle')
        self.declare_parameter('linear_speed',2.0)
        self.declare_parameter('angular_speed',1.0)
        self.declare_parameter('rate_hz',10.0)
        self.linear = self.get_parameter('linear_speed').value
        self.angular = self.get_parameter('angular_speed').value
        rate = self.get_parameter('rate_hz').value
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.timer = self.create_timer(1.0 / rate,self.on_timer)
        self.add_on_set_parameters_callback(self.on_params)

    def on_params(self,params):
        for p in params:
            if p.name == 'linear_speed':
                if abs(p.value) > 5.0:
                    return SetParametersResult(
                        successful=False, reason='速すぎます（5.0まで）')
                self.linear = p.value
            elif p.name == 'angular_speed':
                self.linear = p.value
        return SetParametersResult(successful=True)
    
    def on_timer(self):
        msg = Twist()
        msg.linear.x = self.linear
        msg.angular.z = self.angular
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ParamCircle()
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