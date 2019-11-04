#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

class BuzzerTest(unittest.TestCase):
<<<<<<< HEAD
    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/buzzer',nodes, "node does not exist")

if __name__== '__main__':
   time.sleep(3)
   rospy.init_node('travis_test_buzzer')
   rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)
=======
	def test_node_exist(self):
	    nodes = rosnode.get_node_names()
	    self.assertIn('/buzzer',nodes, "node does not exist")

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('travis_test_buzzer')
	rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)
>>>>>>> a92e2737f1c92f25defc6bacd33519cc7047d34e
