import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from darknet_ros_msgs.action import CheckForObjects

class YoloDetectorActionClient():

    def __init__(self,node):
        super().__init__()
        self._node = node
        self._action_client = ActionClient(self._node, CheckForObjects, 'checkForObjectsActionName')
        self.objectinfo = []
        self.class_id = []
        self.xmin = []
        self.xmax = []
        self.ymin = []
        self.ymax = []
        self.center_x = []
        self.center_y = []
        self.probability = []
        self.receive_data = False

    def send_goal(self):
        self.receive_data = False
        goal_msg = CheckForObjects.Goal()

        self._action_client.wait_for_server()

        # self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._node._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._node._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self._node.get_logger().info('Goal accepted :)')

        self._node._get_result_future = goal_handle.get_result_async()
        self._node._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        # print(result.bounding_boxes.bounding_boxes)
        # self.get_logger().info('Result: {0}'.format(result.bounding_boxes.bounding_boxes))
        for i in range(0,len(result.bounding_boxes.bounding_boxes)):
            self.objectinfo.append(result.bounding_boxes.bounding_boxes[i])
        self.get_object_info()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self._node.get_logger().info('Received feedback: {0}'.format(feedback))


    def get_object_info(self):
        # print(len(self.objectinfo))
        for i in range(0,len(self.objectinfo)):
            self.class_id.append(self.objectinfo[i].class_id)
            self.xmin.append(self.objectinfo[i].xmin)
            self.xmax.append(self.objectinfo[i].xmax)
            self.ymin.append(self.objectinfo[i].ymin)
            self.ymax.append(self.objectinfo[i].ymax)
            self.probability.append(self.objectinfo[i].probability)
        for i in range(0,len(self.xmin)):
            self.center_x.append((self.xmax[i]-self.xmin[i])/2+self.xmin[i])
            self.center_y.append((self.ymax[i]-self.ymin[i])/2+self.ymin[i])
        # print("class_id")
        # print(self.class_id)
        # print("probability")
        # print(self.probability)
        # print("center_x")
        # print(self.center_x)
        # print("center_y")
        # print(self.center_y)
        self.receive_data = True
        return self.class_id, self.probability, self.center_x, self.center_y

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('YoloDetector')

    action_client = YoloDetectorActionClient(node)
    action_client.send_goal()

    while rclpy.ok() and not action_client.receive_data:
        rclpy.spin_once(node)
    print(action_client.receive_data)
    print("+++++++++++===========++++++++++++++++")
    print("class_id")
    print(action_client.class_id)
    print("probability")
    print(action_client.probability)
    print("center_x")
    print(action_client.center_x)
    print("center_y")
    print(action_client.center_y)

    
if __name__ == '__main__':
    main()
