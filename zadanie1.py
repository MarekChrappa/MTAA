from email import message
import sipfullproxy as sip
import socketserver
import re
import string
import socket
#import threading
import sys
import time
import logging



if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 5060   
    print("start") 
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)
    server = socketserver.UDPServer((HOST, PORT), sip.UDPHandler)
    server.serve_forever()