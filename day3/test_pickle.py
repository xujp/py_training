#!/usr/bin/env python

import tab,pickle

dict_info = {
    'shawn' : [29,'IT'],
    'rahel' : {
                'age' : 30,
                'job' : 'salesman'           
    },
    'jack' : 999
}

f = file ('account.pkl','wb')
pickle.dump(dict_info,f)
f.close()
