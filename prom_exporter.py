#!/usr/bin/env python

import os
import requests
import time #import sleep
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import CollectorRegistry, start_http_server, Gauge, Histogram

registry = CollectorRegistry()
inotify_handle_count = Gauge("inotify_handle_total", "total count of process inotify handles" ) #, registry=registry)   #, ["inotify_count"],[""])
#hitl_psql_health_request_time = Histogram('hitl_psql_health_request_time', 'PSQL connection response time (seconds)')

class HTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("<b> Hello World !</b>", "utf-8"))
#            request_counter.labels(status_code='200', instance=platform.node()).inc()
#            get_metrics()
        else:
            self.send_error(404)
#            request_counter.labels(status_code='404', instance=platform.node()).inc()

def get_metrics():
#   inotify_handle_count.set(
   iTotal=subprocess.check_output('for foo in /proc/*/fd/*; do readlink -f $foo; done | grep inotify | wc -l', shell=True, text=True)
   #print(iTotal)
   inotify_handle_count.set(iTotal)
            
            
if __name__ == '__main__':
    start_http_server(9000)
#    webServer = HTTPServer(("localhost", 9000), HTTPRequestHandler).serve_forever()
    inotify_handle_count.set(-1)    
    while True:
        get_metrics()
        time.sleep(15)
