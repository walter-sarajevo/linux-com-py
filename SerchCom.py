# coding=utf-8

import serial
import serial.tools.list_ports

class SerchCom(object):

    # 
    
    def __init__(self):
        self.description = "Method to seach com in this machine."
        self.port_list = []
        self.port_count = 0
        self.error = 0

        ports = serial.tools.list_ports.comports()
        if len(ports) == 0:
            print("ÕÒ²»µ½´®¿Ú£¡")

        else:
            for i in range(0, len(ports)):
                name = str(ports[i]).split(' ', 1)
                self.port_list.append(name[i])
            self.port_count = len(ports)

    # def __call__(self):
    #     self.description = "Method to seach com in this machine."
    #     self.port_list = []
    #     self.port_count = 0
    #     self.error = 0

    #     # ports = list(serial.tools.list_ports.comports())
    #     ports = serial.tools.list_ports.comports()
    #     for i in range(0, len(ports)):
    #         name = str(ports[i]).split(' ', 1)
    #         self.port_list.append(name[i])
    #     # self.port_list = name.split(' ', 1)
    #     self.port_count = len(ports)
    #     print (self.port_list)

