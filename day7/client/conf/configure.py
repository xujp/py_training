import sys
from service import * 

base_dir = "/home/shawn/py_training/day7/client"
sys.path.append(base_dir)


enabled_services = {
    'service':(
            ('upCheck', upCheckMonitor()),

            )


}
