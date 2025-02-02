from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='misty_core',
            executable='misty_low_level',
            name='misty_low_level_node',
            #namespace= "misty_3", 
            output='screen',
            emulate_tty=True,
            # node_namespace='misty_3',
            parameters=[
                {'ip_address': '192.168.1.39'},
                {'robot_name': 'misty_3'}
            ]
        ),
        Node(
            package='misty_navigation',
            executable='misty_nav',
            name='misty_navigation',
            #namespace= "misty_3", 
            output='screen',
            emulate_tty=True,
        ),
    ])


