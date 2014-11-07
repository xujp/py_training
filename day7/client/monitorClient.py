from conf.configure import *
import time
import socket,json
import tab

HOST = '192.168.93.130'
PORT = 50007
hostname = "localhost"

def send_status_data(status_data):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    print "-------sending----------"
    s.sendall(status_data)
    data = s.recv(1024)
    print 'Server:=>>',data
    s.close()

monitor_dict = {}
for k,v in enabled_services.items():
    if k == 'service':
        for(s_name,service_api) in v :
             monitor_dict[s_name] = {
                'latestCheck':0,
                'interval' : service_api.interval,
                'plugin' : service_api
            }
             #print s_name, service_api.interval
             #print service_api.plugin.monitor()

#print monitor_dict                

while True: 
    status_dict={'hostname':hostname}
    for  service_name,value_dict in monitor_dict.items():
        print service_name,value_dict['latestCheck']
        print value_dict['latestCheck']+value_dict['interval']-time.time()
        if time.time() - value_dict['latestCheck'] >= value_dict['interval']:
            print "\033[42;1mstart performance next roudin\033[0m" ,service_name
            status_dict[service_name]=value_dict['plugin'].plugin.monitor()
            value_dict['latestCheck'] = time.time()
            if len(status_dict) > 1:
	        send_status_data(json.dumps(status_dict))
"""
    for k,v in status_dict.items():
        if k != "hostname":
            for index ,value in v.items():
                print '\t',index,value        
"""    
    time.sleep(2)
