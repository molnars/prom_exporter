#!/usr/bin/env python

import os
import requests
import time #import sleep
import datetime
import subprocess
#from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import CollectorRegistry, start_http_server, Gauge, Histogram

freq = 60
registry = CollectorRegistry()
inotify_handle_count = Gauge("inotify_handle_total", "total count of process inotify handles" ) #, registry=registry)   #, ["inotify_count"],[""])
#hitl_psql_health_request_time = Histogram('hitl_psql_health_request_time', 'PSQL connection response time (seconds)')

def plog(severity, message, value):
    print(now.strftime("%d/%m/%Y %H:%M:%S"), " ", severity, " ", message, ": ", value)
    
def get_metrics():
#   inotify_handle_count.set(
   iTotal=subprocess.check_output('for foo in /proc/*/fd/*; do readlink -f $foo; done | grep inotify | wc -l', shell=True, text=True)
   #print(now.strftime("%d/%m/%Y %H:%M:%S"), " [INFO] inotify_handle_total: ", iTotal)
   plog("INFO","inotify_handle_total", iTotal)
   inotify_handle_count.set(iTotal)
            
            
if __name__ == '__main__':
    start_http_server(9000)
#    webServer = HTTPServer(("localhost", 9000), HTTPRequestHandler).serve_forever()
    freq = os.environ.get('frequency', freq)
    
    plog("INFO","Collection starting","")
    plog("INFO","frquency set at", freq)
    inotify_handle_count.set(-1)    
    while True:
        get_metrics()
        time.sleep(30)
