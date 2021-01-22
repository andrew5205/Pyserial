import serial 
import serial.tools.list_ports
import sys

import time

from datetime import datetime



print('Search...')
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print('Find port '+ port.device)

# ser = serial.Serial(port.device)
# if ser.isOpen():
#     ser.close()


all_ports_list = list()
for port in serial.tools.list_ports.comports():
    all_ports_list.append(port.device)
print(all_ports_list)


date = datetime.now().strftime('%d-%m-%Y')

# open available ports 
for i in range(len(all_ports_list)):
    p = serial.Serial(port=all_ports_list[i], baudrate=115200)

    # print(i)        # 0
    # print(p)        # Serial<id=0x1b75115eb80, open=True>(port='COM21', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
    # print(p.port)   # COM3
    if p.port:
        # file name pass in port.device after
        f = open('ser_{0}_{1}.log'.format(p.port, date), 'w+')
        # f = open('ser_%s.log' %p.port, 'w+')
        while True:
            debug_line = str(p.readline().decode(encoding='utf-8'))
            print(debug_line)
            f.write(debug_line)
        f.close()















