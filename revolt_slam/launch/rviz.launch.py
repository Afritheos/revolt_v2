import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_revolt_slam = get_package_share_directory('revolt_slam')

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_revolt_slam, 'rviz', 'revolt_slam.rviz')],
    )

    return LaunchDescription([
        rviz,
    ])
