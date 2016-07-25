#!/usr/bin/python


import threading
import thread
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import time
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep,listdir
import os,sys
import json
import socket
import ast
import types
import cgi

FILE = 'index.html'
IP=''
PORT = 7000

target_host=""
target_port=0

REQUEST_QUEUE_SIZE = 1024
ev3_list=[]

def initList():
    with open('logfile.txt','r') as f:
         ev3_list=f.readlines()
         print ev3_list





class HttPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        length = int(self.headers.getheader('content-length'))
        otype=self.headers.getheader('content-type')
        address=self.client_address[0]
        data_string = self.rfile.read(length)
        print data
        data=json.loads(data_string)
        #print length
        print data_string
        #print otype
        #print type(data)
        #print address

        data['orgi']=address
        print data
        target_host=data['ip']
        target_port=int(data['port'])
        sdata=str(data)
        #print type(sdata)
        sdata=json.dumps(sdata)
        #sends='helll'
        #print target_host,target_port
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print sdata
        try:
            client.connect((target_host,target_port))
            client.sendall(sdata+"\n")
            #print 'send: ',sends
            recv = conn.recv(1024)
            print ev3address
            #self.wfile.write(recv)

        finally:
            client.close()
        send={}
        if recv.find('sensor')==-1:
            print 'no sensor'
            print recv
            send=recv

        else:
            recv2=json.loads(recv)
            print type(recv2)
            for i in range(1,5):
                test1=recv2['port{}'.format(i)]
        #print test1
        #print type(test1)
                test2=ast.literal_eval(test1)
        #print type(test2)
                send['port{}'.format(i)]=test2
        #recv2['port1']=test2
        #print recv2['port1']
        #send['port1']=test2
            send['message']='Sensor updated'
            send=json.dumps(send)
            print send
        #else:
            #send=recv
            #print recv

        self.wfile.write(send)





def WebServerThread():
        try:
                #Create a web server and define the handler to manage the
                #incoming request
                server_address = (IP, PORT)
                server = BaseHTTPServer.HTTPServer(server_address, HttPHandler)
                print 'Started httpserver on port ' , PORT
                #Wait forever for incoming htto requests
                server.serve_forever()

        except KeyboardInterrupt:
                print '^C received, shutting down the web server'
                server.socket.close()
                sys.exit(0)

def registraion():
    
    try:
        register_PORT=8999
        counting_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        counting_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        counting_socket.bind((IP,register_PORT))
        print 'waiting for registration'

    
        while True:
              data,addr=counting_socket.recvfrom(1024)
              print 'Received registration request from '+addr[0]
              ev3info={'ip':addr[0],'port':addr[1]}
#              initList()
              if ev3info not in ev3_list:
                 ev3_list.append(ev3info)
                 ev3infos=json.dumps(ev3info)
                 log=open('logfile.txt','a+')
                 log.write(ev3infos+'\n')
                 log.close()
              print data
              counting_socket.sendto('registered',(addr[0],addr[1]))
    except KeyboardInterrupt:
               counting_socket.close()
               os._exit(0)




if __name__ == "__main__":

     PID=os.fork()
     if PID==0:
        registraion()
     else:
        WebServerThread()













