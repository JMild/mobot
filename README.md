# Mobot
To clone and run this appli

## Key Features

* LivePreview - Make changes, See changes
  - Instantly see what your Markdown documents look like in HTML as you create them.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Example 1](https://www.example.com)
- [Example 2](https://www.example.com)

## How To Use ZED2 Camera for change pointcloud2 to octomap 
To clone and run this application, you'll need package [octomap_server](https://github.com/OctoMap/octomap_mapping) and Getting Started with ROS2 and [ZED2](https://www.stereolabs.com/docs/ros2/) 

Now run the ZED2 Camera in your workspace:

    $ ros2 launch zed_wrapper zed2.launch.py

Now run the octomap_server_node & zed_oct in your workspace:

    $ ros2 run octomap_server octomap_server_node
    $ ros2 run mobot zed_oct.py

You can see the results in rviz:

    $ cd
    $ rviz2

## How To Use Aruco Marker with ZED2 Camera
To clone and run this application, you'll Getting Started with ROS2 and [ZED2](https://www.stereolabs.com/docs/ros2/) 

Published Topics:
/aruco_poses (geometry_msgs.msg.PoseArray)

Subscriptions:
/camera/image_raw (sensor_msgs.msg.Image)
  
Now run the ZED2 Camera in your workspace:

    $ ros2 launch zed_wrapper zed2.launch.py

Now run the aruco_node in your workspace:

    $ ros2 run ros2_aruco aruco_node 

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.
