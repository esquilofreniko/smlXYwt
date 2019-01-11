import argparse
import math
import threading
import keyboard
import numpy as np
from pythonosc import dispatcher
from pythonosc import udp_client
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc.osc_message_builder import OscMessageBuilder

class OscClient:
    def __init__(self,ip,port,address):
        self.ip = ip
        self.port = port
        self.address = address
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=ip)
        parser.add_argument("--port", type=int, default=port)
        args = parser.parse_args()
        self.client = udp_client.SimpleUDPClient(args.ip, args.port)

    def sendMsg(self,msg):
        builder = OscMessageBuilder(address=self.address)
        for v in msg[0]:
            builder.add_arg(v)
        out = builder.build()
        # print("sent osc message to",self.ip,"on port",self.port,"with address",self.address)
        self.client.send(out)

class OscServer:
    def getX(self,unused_addr, *args):
        self.xin = args
        # print(self.xhandler,"received with size:",np.array(self.xin).size)

    def getY(self,unused_addr, *args):
        self.yin = args
    
    def addExample(self,unused_addr,*args):
        self.addexample = 1
    
    def delExample(self,unused_addr,*args):
        self.delexample = 1
    
    def delAll(self,unused_addr,*args):
        self.delall = 1
    
    def trainModel(self,unused_addr,*args):
        self.train = 1

    def close(self,unused_addr,*args):
        self.quit = 1
        
    def __init__(self,ip,port,xhandler,yhandler):
        self.addexample = 0
        self.delexample = 0
        self.delall = 0
        self.train = 0
        self.quit = 0
        self.xin = np.array([0])
        self.yin = np.array([0])
        self.xhandler = xhandler
        self.yhandler = yhandler
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map(xhandler, self.getX)
        self.dispatcher.map(yhandler,self.getY)
        self.dispatcher.map('/keras/addExample',self.addExample)
        self.dispatcher.map('/keras/delExample',self.delExample)
        self.dispatcher.map('/keras/delAll',self.delAll)
        self.dispatcher.map('/keras/train',self.trainModel)
        self.dispatcher.map('/keras/quit',self.close)
        self.server = osc_server.ThreadingOSCUDPServer((ip, port), self.dispatcher)
        print("OSC server listening on {}".format(self.server.server_address),"with handlers:",self.xhandler,self.yhandler)
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.start()