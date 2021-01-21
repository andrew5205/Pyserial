import serial 
import serial.tools.list_ports
import sys

import time

from datetime import datetime



print('Search...')
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print('Find port '+ port.device)

ser = serial.Serial(port.device)
if ser.isOpen():
    ser.close()


all_ports_list = list()
for port in serial.tools.list_ports.comports():
    all_ports_list.append(port.device)
print(all_ports_list)



p0 = serial.Serial(port=all_ports_list[0], baudrate=115200)
# p1 = serial.Serial(port=all_ports_list[1], baudrate=115200)
# p2 = serial.Serial(port=all_ports_list[2], baudrate=115200)
# p3 = serial.Serial(port=all_ports_list[3], baudrate=115200)

# f = open('log_line.txt', 'w+')

while all_ports_list[0]:
    # p0 = serial.Serial(port=all_ports_list[0], baudrate=115200)
    f = open('p0.txt', 'w+')
    debug_line = str(p0.readline().decode(encoding='utf-8'))
    print(debug_line)
    f.write(debug_line)
# while all_ports_list[1]:
#     debug_line = str(p1.readline().decode(encoding='utf-8'))
#     print(debug_line)
#     f.write(debug_line)
# while p2:
#     debug_line = str(p2.readline().decode(encoding='utf-8'))
#     print(debug_line)
#     f.write(debug_line)
# while p3:
#     debug_line = str(p3.readline().decode(encoding='utf-8'))
#     print(debug_line)
#     f.write(debug_line)

