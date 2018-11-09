# coding = utf-8

import serial
import serial.tools.list_ports
import SerchCom

a = SerchCom.SerchCom()
# b = serial.tools.list_ports.comports()
print(a.port_list)
print(a(1))

