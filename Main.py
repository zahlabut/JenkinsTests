NV_URL='http://127.0.0.1:8182/shunra/controller'
NV_USER='admin123'
NV_PASS='Admin123'

import os,sys
cur_path=os.path.abspath('.')
sys.path.append(cur_path)
from UnitestWithJenkins import *
print GET_YNET()
print NV_LOG_IN(NV_URL,NV_USER,NV_PASS)



