from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    DeclareLaunchArgument(
            "cloud_in",
            default_value="/livox/lidar",
            description="Input PointCloud2 topic"
        ),
    DeclareLaunchArgument(
            "scan",
            default_value="/livox/scan",
            description="Output LaserScan topic"
        ),
    
    return LaunchDescription(
        [
            Node(
                package="pointcloud_to_laserscan",
                executable="pointcloud_to_laserscan_node",
                parameters=[
                    {
                        "target_frame": "livox_frame",
                        "transform_tolerance": 0.01,
                        "min_height": 0.0,  # 0
                        "max_height": 1.3,  # 1
                        "angle_min": -3.14,  # -M_PI/ 2-1.5708
                        "angle_max": 3.14,  # M_PI/2
                        "angle_increment": 0.0087,  # M_PI/360.0
                        "scan_time": 0.3333,
                        "range_min": 0.6,
                        "range_max": 50.0,
                        "use_inf": True,
                        "inf_epsilon": 1.0,
                        "cloud_in": LaunchConfiguration("cloud_in"),
                        "scan": LaunchConfiguration("scan")
                    }
                ],
                name="pointcloud_to_laserscan",
            )
        ]
    )
