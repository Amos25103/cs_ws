import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped


class JointMover(Node):

    def __init__(self):
        super().__init__("joint_mover")
        self.joint_publisher=self.create_publisher(JointState, "/joint_states", 10)
        self.joint_subscription = self.create_subscription(
            PoseStamped, "/goal_pose",self.goal_pose_callback, 10)
        

    def goal_pose_callback(self, msg:PoseStamped):
        position = msg.pose.position
        orientation = msg.pose.orientation
        self.get_logger().info(f'Received Goal Pose: Position(x={position.x}, y={position.y}, z={position.z}), '
                               f'Orientation(x={orientation.x}, y={orientation.y}, z={orientation.z}, w={orientation.w})')

                # Convert PoseStamped to JointState (placeholder logic)
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = ['rev1', 'rev2','rev3','rev4','rev5','rev6']  # Replace with actual joint names
        joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Replace with computed joint positions

        self.joint_publisher.publish(joint_state)

def main(args=None):
    rclpy.init(args=args)
    node=JointMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()