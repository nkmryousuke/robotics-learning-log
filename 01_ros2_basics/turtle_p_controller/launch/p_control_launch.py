from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    goal_x = LaunchConfiguration('goal_x')
    goal_y = LaunchConfiguration('goal_y')
    kp_linear = LaunchConfiguration('kp_linear')
    kp_angular = LaunchConfiguration('kp_angular')
    tolerance = LaunchConfiguration('tolerance')

    return LaunchDescription([
        DeclareLaunchArgument('goal_x', default_value='8.0'),
        DeclareLaunchArgument('goal_y', default_value='8.0'),
        DeclareLaunchArgument('kp_linear', default_value='1.0'),
        DeclareLaunchArgument('kp_angular', default_value='4.0'),
        DeclareLaunchArgument('tolerance', default_value='0.1'),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
        ),
        Node(
            package='turtle_p_controller',
            executable='p_controller',
            name='p_controller',
            parameters=[{
                'goal_x': goal_x,
                'goal_y': goal_y,
                'kp_linear': kp_linear,
                'kp_angular': kp_angular,
                'tolerance': tolerance,
            }],
        ),
    ])