#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from octomap_msgs.msg import Octomap
from octomap_msgs.srv import GetOctomap

class PointCloudToOctomap(Node):
    def __init__(self):
        super().__init__('pointcloud_to_octomap')
        self.subscription = self.create_subscription(PointCloud2,'/zed2/zed_node/point_cloud/cloud_registered',self.pointcloud_callback,10)
        self.publisher = self.create_publisher(PointCloud2, '/cloud_in', 10)
        
    def pointcloud_callback(self, msg):
        self.publisher.publish(msg)
        self.get_logger().info('Octomap server ready!')
        

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudToOctomap()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
