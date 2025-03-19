import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch_ros.actions import Node
from xacro import process_file

pkg_revolt_gz = get_package_share_directory('revolt_gazebosim')

def get_robot_description() -> str:
    """
    Obtain the urdf from the xacro file.

    This replace package tag by file tag to works with gazebo
    # See  https://github.com/ros-simulation/gazebo_ros_pkgs/pull/1284



    Returns
    -------
        urdf of the robot with gazebo data

    """
    doc = process_file(
        os.path.join(pkg_revolt_gz, 'urdf', 'revolt_gazebosim.xacro'
        ),
        mappings={
            
            'use_real_ros_control': 'false',
            'use_fixed_caster': 'false',
        },
    )
    robot_desc = doc.toprettyxml(indent='  ')
    folder = get_package_share_directory('revolt_description')
    robot_desc = robot_desc.replace(
        'package://revolt_description/', f'file://{folder}/'
    )
    return robot_desc


def generate_launch_description():
    # Arguments
    use_sim_time = LaunchConfiguration('use_sim_time')
    initial_pose_x = LaunchConfiguration('initial_pose_x')
    initial_pose_y = LaunchConfiguration('initial_pose_y')
    initial_pose_z = LaunchConfiguration('initial_pose_z')
    initial_pose_yaw = LaunchConfiguration('initial_pose_yaw')
    
    
    robot_description_topic = LaunchConfiguration('robot_description_topic')
    rsp_frequency = LaunchConfiguration('rsp_frequency')

    x_argument = DeclareLaunchArgument(
        'initial_pose_x',
        default_value='0.0',
        description='Initial x pose of revolt in the simulation',
    )
    y_argument = DeclareLaunchArgument(
        'initial_pose_y',
        default_value='0.0',
        description='Initial y pose of revolt in the simulation',
    )
    z_argument = DeclareLaunchArgument(
        'initial_pose_z',
        default_value='0.05',
        description='Initial z pose of revolt in the simulation',
    )
    yaw_argument = DeclareLaunchArgument(
        'initial_pose_yaw',
        default_value='0.0',
        description='Initial yaw pose of revolt in the simulation',
    )
    
  
    robot_desc_argument = DeclareLaunchArgument(
        'robot_description_topic',
        default_value='/robot_description',
        description='robot description topic ',
    )
    rsp_frequency_argument = DeclareLaunchArgument(
        'rsp_frequency',
        default_value='30.0',
        description='robot state publisher frequency',
    )
    use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true',
    )


    # TODO (olmerg) Multirobot. How to change the name of topic with entity parameter
    remappings = [('/tf', 'tf'), ('/tf_static', 'tf_static')]

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'use_sim_time': use_sim_time,
                'publish_frequency': rsp_frequency,
                'robot_description': get_robot_description(),
            }
        ],
        remappings=remappings,
        
    )

    bridge_config_file = os.path.join(pkg_revolt_gz, 'config', 'gz_bridge.yaml')


    gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',
        parameters=[{
            'config_file': bridge_config_file
        }],
    )

    gz_image_bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        arguments=["camera/image_raw"],
        output='screen',

    )

  
    robot_spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic',
            robot_description_topic,
            '-name',
            'revolt',
            '-x',
            initial_pose_x,
            '-y',
            initial_pose_y,
            '-z',
            initial_pose_z,
            '-R',
            '0.0',
            '-P',
            '0.0',
            '-Y',
            initial_pose_yaw,
        ],
    )
    

    return LaunchDescription(
        [
            use_sim_time_argument,
            x_argument,
            y_argument,
            z_argument,
            robot_desc_argument,
            rsp_frequency_argument,
            yaw_argument,
            rsp,
            robot_spawn,
            gz_bridge_node,
            gz_image_bridge,
            
        ]
    )