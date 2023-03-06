#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseStamped



class ArucoDetector(Node):
    def __init__(self):
        super().__init__('aruco_detector')

        # Subscribe to the camera topic
        self.subscription = self.create_subscription(
            Image,'/zed2/zed_node/rgb/image_rect_color', self.detect_aruco,10)
        self.subscription

        # Initialize OpenCV aruco dictionary
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

        # Initialize OpenCV aruco parameters
        self.aruco_params = cv2.aruco.DetectorParameters()

        # Initialize the ROS image converter
        self.bridge = CvBridge()

        # Initialize the publisher to publish pose of the detected ArUco marker
        self.publisher = self.create_publisher(PoseStamped, 'aruco_pose', 10)

        # Set the pose frame id
        self.pose_frame_id = 'camera_link'

    def detect_aruco(self, data):
        # Convert ROS Image message to OpenCV image
        cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')

        # Convert to grayscale
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        # Detect aruco markers
        corners, ids, _ = cv2.aruco.detectMarkers(
            gray,
            self.aruco_dict,
            parameters=self.aruco_params)

        # If markers are detected, estimate pose
        if ids is not None:
            #rvecs การหมุนของวัตถุ (radian)
            #tvecs วัตถุอยู่ห่างจากตัวกล้องเท่าไหร่ (meters)
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners,0.05, # Marker size in meters
                np.eye(3), # Camera matrix (identity matrix)
                np.zeros((4, 1))) # Distortion coefficients
            
             # Create PoseStamped message
            pose_msg = PoseStamped()
            pose_msg.header.stamp = self.get_clock().now().to_msg()
            pose_msg.header.frame_id = 'camera_link'
            pose_msg.pose.position.x = tvecs[0][0][0]
            pose_msg.pose.position.y = tvecs[0][0][1]
            pose_msg.pose.position.z = tvecs[0][0][2]
            pose_msg.pose.orientation.x = rvecs[0][0][0]
            pose_msg.pose.orientation.y = rvecs[0][0][1]
            pose_msg.pose.orientation.z = rvecs[0][0][2]
            pose_msg.pose.orientation.w = 1.0
            
            # Publish the pose
            self.publisher.publish(pose_msg)

def main(args=None):
    rclpy.init(args=args)
    aruco_detector = ArucoDetector()
    rclpy.spin(aruco_detector)
    aruco_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

