import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointMover(Node):

    def __init__(self):
        super().__init__("joint_mover")
        self.joint_publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.timer = self.create_timer(1.0, self.publish_joint_state)  # 1-second interval
        self.current_point = 'A'  # Start at point A

    def publish_joint_state(self):
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = ['rev1', 'rev2', 'rev3', 'rev4', 'rev5', 'rev6']  # Replace with actual joint names
        
        point_A = [0.0, -1.472, -1.746, 4.624, 1.5708, 0.0]
        point_B = [0.9, -1.472, -1.746, 4.624, 1.5708, 0.0]
        
        if self.current_point == 'A':
            joint_state.position = point_A
            self.current_point = 'B'
        else:
            joint_state.position = point_B
            self.current_point = 'A'
        
        joint_state.velocity = []
        joint_state.effort = []

        self.joint_publisher.publish(joint_state)
        self.get_logger().info(f'Published Joint State: Positions={joint_state.position}')

def main(args=None):
    rclpy.init(args=args)
    node = JointMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
