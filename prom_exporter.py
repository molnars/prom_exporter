#!/usr/bin/env python

import os
import requests
import time #import sleep
from datetime import datetime
import subprocess
import platform
#from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import CollectorRegistry, start_http_server, Gauge, Histogram

registry = CollectorRegistry()
inotify_watch_count = Gauge("inotify_user_watch_total", "total count of user inotify watches",["instance"] ) #, registry=registry)   #, ["inotify_count"],[""])
inotify_watch_max = Gauge("inotify_max_user_watches", "max instances user inotify watches",["instance"] )
inotify_instance_count = Gauge("inotify_user_instance_total", "total count of user inotify instances",["instance"] ) #, registry=registry)   #, ["inotify_count"],[""])
inotify_instance_max = Gauge("inotify_max_user_instances", "max instances user inotify instances",["instance"] )

#hitl_psql_health_request_time = Histogram('hitl_psql_health_request_time', 'PSQL connection response time (seconds)')

def plog(severity, message, value):
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'[',severity.upper(),']',message,":", value)
    
def get_metrics():
#   inotify_handle_count.set(
   iTotal=int(subprocess.check_output('for foo in /proc/*/fd/*; do readlink -f $foo; done | grep inotify | wc -l', shell=True, text=True))
   plog("INFO","inotify_user_instance_total", iTotal)
#   inotify_instance_count.labels(instance=platform.node()).set(iTotal)


   iwTotal=int(subprocess.check_output('for foo in /proc/*/fd/*; do readlink -f $foo; done | grep inotify | wc -l', shell=True, text=True))
   plog("INFO","inotify_user_watch_total", iwTotal)
   inotify_watch_count.labels(instance=platform.node()).set(iwTotal)


#/proc/sys/fs/inotify/max_user_watches
   with open('/proc/sys/fs/inotify/max_user_instances') as f:
     max_user_instances = int(f.read())
   plog("INFO","inotify_max_user_instances",max_user_instances)
   inotify_instance_max.labels(instance=platform.node()).set(max_user_instances)

   with open('/proc/sys/fs/inotify/max_user_watches') as f:
     max_user_watches = int(f.read())
   plog("INFO","inotify_max_user_watches",max_user_watches)
   inotify_watch_max.labels(instance=platform.node()).set(max_user_watches)
            
if __name__ == '__main__':
    start_http_server(9000)
#    webServer = HTTPServer(("localhost", 9000), HTTPRequestHandler).serve_forever()
    freq = int(os.environ.get('frequency', 60))
    
    plog('INFO',"Collection starting",platform.node())
    plog('INFO',"Frequency set at", freq)
#    inotify_watch_count.set(-1)    
    inotify_watch_count.labels(instance=platform.node()).set(-1)
    inotify_watch_max.labels(instance=platform.node()).set(-1)
    inotify_instance_count.labels(instance=platform.node()).set(-1)
    inotify_instance_max.labels(instance=platform.node()).set(-1)
    while True:
        get_metrics()
        time.sleep(freq)
