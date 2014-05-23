import unittest
import os
from read_gtrends import read_gtrends

class Test_gtrends(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # set test data directory
        cls.testdatapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

    def test_read_gtrend(self):
        report_file = os.path.join(self.testdatapath, 'report_boating.csv')
        time_ser = read_gtrends.read_gtrends(report_file)
        self.assertTrue(time_ser.size == 3290)
        self.assertTrue(time_ser[0] == 44)
        self.assertTrue(time_ser.index[0].strftime('%Y-%m-%d %H:%M:%S') == '2004-01-04 00:00:00')
        self.assertTrue(time_ser[-1] == 18)
        self.assertTrue(time_ser.index[-1].strftime('%Y-%m-%d %H:%M:%S') == '2013-01-05 00:00:00')

if __name__ == '__main__':
    unittest.main()
