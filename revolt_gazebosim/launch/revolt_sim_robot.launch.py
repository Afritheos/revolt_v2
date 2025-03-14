import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Arguments
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_rviz = LaunchConfiguration('rviz')
    rviz_config_file = LaunchConfiguration('rviz_config_file')

    pkg_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_revolt_gazebosim = get_package_share_directory('revolt_gazebosim')

    use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true',
    )

    world_argument = DeclareLaunchArgument(
        name='world',
        default_value='empty.world',
        description='Full path to the world model file to load')

    use_rviz_argument = DeclareLaunchArgument(
        'rviz', default_value='true', description='Open RViz.'
    )
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value=os.path.join(
            pkg_revolt_gazebosim, 'rviz', 'revolt_gazebosim.rviz'),
        description='Full path to the RVIZ config file to use',
    )

    # Include revolt
    include_revolt = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_revolt_gazebosim, 'launch', 'spawn_robot.launch.py')
        ),
    )

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'world': LaunchConfiguration('world'),
        }.items()
    )

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-d', rviz_config_file],
    )

    revolt_visualization_timer = TimerAction(
        period=5.0, actions=[rviz], condition=IfCondition(use_rviz)
    )
    return LaunchDescription(
        [
            use_sim_time_argument,
            declare_rviz_config_file_cmd,
            world_argument,
            use_rviz_argument,
            gazebo,
            include_revolt,
            revolt_visualization_timer,
        ]
    )
