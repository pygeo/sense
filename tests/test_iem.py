import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import I2EM

class Test_IEM(unittest.TestCase):
    def setUp(self):
        self.eps = 4.+0.j
        self.ks = 1.
        self.theta = 0.5
        self.kl = 2.

    def tearDown(self):
        pass
    
    def test_init(self):
        O = I2EM(self.eps, self.ks, self.kl, self.theta)
        self.assertEqual(O.eps, self.eps)
        self.assertEqual(O.ks, self.ks)
        self.assertEqual(O.kl, self.kl)


if __name__ == '__main__':
    unittest.main()
