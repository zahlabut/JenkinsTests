import os,sys
cur_path=os.path.abspath('.')
sys.path.append(cur_path)
from UnitestWithJenkins import *

#print GET_YNET()
#print NV_LOG_IN_OUT(NV_URL,NV_USER,NV_PASS)




class NV_Tests(unittest.TestCase):
    def test_ynet(self):
        self.assertEqual(GET_YNET(), True)
    def test_nv(self):
        self.assertEqual(NV_LOG_IN_OUT(NV_URL,NV_USER,NV_PASS), True)