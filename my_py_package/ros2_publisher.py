#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String #it is used for importing example msg's

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")   
        
        self.robot_name=" Tarse "
        self._publisher_= self.create_publisher(String, "robot_news",10) #creating publisher
        self.timer_ = self.create_timer(0.5, self.publish_msg) #it will call the publish_msg function after every 0.5sec
        self.get_logger().info("Robot News Station has been started") #it will print the info just like the normal print statement
    
    def publish_msg(self): # msg to be published on the publisher
        msg = String()
        msg.data ="Hello Omkar this is" + str(self.robot_name) + "from the robot news station."
        self._publisher_.publish(msg) 

def main(args=None):
    rclpy.init(args=args) #it is used to initialize the node
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown() #it is use to shutdown the node

if __name__ == "__main__":
    main()    
