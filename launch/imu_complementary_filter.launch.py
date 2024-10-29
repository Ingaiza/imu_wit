# File: imu_complementary_filter_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='imu_complementary_filter',
            executable='complementary_filter_node',
            name='imu_complementary_filter',
            output='screen',
            parameters=[
                {'use_mag': True},  # Set to True to use magnetometer data for better yaw
                {'publish_tf': False},  # Set to True to publish a TF for the IMU orientation
                {'use_magnetic_field_msg': False},  # Set to True if /mag publishes sensor_msgs/MagneticField messages
                {'world_frame': 'enu'},  # ENU (East-North-Up) or NWU (North-West-Up) based on your IMU frame
                {'frequency': 10.0},  # Match this with IMU data publishing frequency
                {'gain_acc': 0.01},  # Adjust this gain for accelerometer influence
                {'gain_mag': 0.01}   # Adjust this gain for magnetometer influence (only relevant if `use_mag` is True)
            ],
            remappings=[
                ('imu/data_raw', 'imu/data_raw'),  # Remap to your raw IMU data topic
                ('imu/mag', 'imu/mag')  # Remap to your magnetometer data topic
            ]
        )
    ])
