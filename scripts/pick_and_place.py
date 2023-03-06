#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from open_manipulator_msgs.srv import *     # import srv all
from time import sleep   # sec

class Dummy(Node):
    def __init__(self):
        super().__init__('node_name')
        self.joint_name = ["Joint 1","Joint 2","Joint 3","Joint 4","Joint 5","Joint 6","Gripper"]
        self.enable_client = self.create_client(SetJointPosition,'/goal_joint_space_path')
        
        # check if the a service is available
        while not self.enable_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again')
        self.send_enable_request()
            
    def send_enable_request(self):
        req = SetJointPosition.Request()  
        req.joint_position.joint_name = self.joint_name

        # Move to initial position
        req.joint_position.position = [0. ,0. ,0. ,0. ,0. ,0., 0.]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())
        sleep(8) 
        
        # The TCP position is ... cm above the box.
        req.joint_position.position = [0. ,0. ,0. ,0. ,0. ,0., 0.]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())
        sleep(8) 

        # wait & close the gripper
        req.joint_position.position = [0. ,0. ,0. ,0. ,0. ,0., 0.1]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())
        sleep(8) 

        # Move to ตะกร้า 
        req.joint_position.position = [0. ,0. ,0. ,0. ,0. ,0., 0.1]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())
        sleep(8) 

        # open the gripper
        req.joint_position.position = [0. ,0. ,0. ,0. ,0. ,0., 0.0]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())
        sleep(8) 

        # Move back to the home position
        req.joint_position.position = [0.2 ,0. ,0. ,0. ,0. ,0.,0.]   # rad
        req.path_time = 5.0   # total time of trajectory
        future = self.enable_client.call_async(req)
        if future.result() is not None:
            self.get_logger().info('Result of service call: %s' % future.result())
        else:
            self.get_logger().info('Service call failed %r' % future.exception())


def main(args=None):
    rclpy.init(args=args)
    controller = Dummy()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()



