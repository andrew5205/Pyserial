import serial 
import serial.tools.list_ports
import sys
import threading
import time

from datetime import datetime

date = datetime.now().strftime('%d-%m-%Y-%H:%M:%S')

br=115200

all_ports_list = list()
for port in serial.tools.list_ports.comports():
    all_ports_list.append(port.device)
print(all_ports_list)
# ['/dev/cu.Bluetooth-Incoming-Port', '/dev/cu.usbmodem14201', '/dev/cu.usbserial-A9QYP8U']

# for i in all_ports_list:
#     select_port = i
#     print(select_port)

def loging1():
    p = serial.Serial(port=all_ports_list[1], baudrate=br)
    f = open('{}{}.log'.format(all_ports_list[1][8:],date), 'w+')
    while True:
        debug_line = str(p.readline().decode(encoding='utf-8'))
        print(debug_line)
        f.write(debug_line)
        f.flush()
        # time.sleep(0.001)
    f.close()
    
def loging2():
    p = serial.Serial(port=all_ports_list[2], baudrate=br)
    f = open('{}{}.log'.format(all_ports_list[2][8:],date), 'w+')
    while True:
        debug_line = str(p.readline().decode(encoding='utf-8'))
        print(debug_line)
        f.write(debug_line)
        f.flush()
        # time.sleep(0.001)
    f.close()
    
def loging3():
    p = serial.Serial(port=all_ports_list[3], baudrate=br)
    f = open('{}{}.log'.format(all_ports_list[3][8:],date), 'w+')
    while True:
        debug_line = str(p.readline().decode(encoding='utf-8'))
        print(debug_line)
        f.write(debug_line)
        f.flush()
        # time.sleep(0.001)
    f.close()
    
def loging4():
    p = serial.Serial(port=all_ports_list[4], baudrate=br)
    f = open('{}{}.log'.format(all_ports_list[4][8:],date), 'w+')
    while True:
        debug_line = str(p.readline().decode(encoding='utf-8'))
        print(debug_line)
        f.write(debug_line)
        f.flush()
        # time.sleep(0.001)
    f.close()
    


for i in range(len(all_ports_list)):
    sys.argv.append(all_ports_list[i])
print(sys.argv)
# ['mtest.py', '/dev/cu.Bluetooth-Incoming-Port', '/dev/cu.usbmodem14201', '/dev/cu.usbserial-A9QYP8U']

# for _ in range(len(sys.argv[2:])):
#     print(len(sys.argv[2:]))        # 2

# loging1()
# loging2()


for _ in range(len(sys.argv[2:])):
    x = threading.Thread(target=loging1)
    y = threading.Thread(target=loging2)
    z = threading.Thread(target=loging3)
    w = threading.Thread(target=loging4)

    x.start()
    y.start()
    z.start()
    w.start()
    
# x.join()
# y.join()
# z.join()
# w.join()


# ['/dev/cu.Bluetooth-Incoming-Port', '/dev/cu.usbmodem14201', '/dev/cu.usbserial-A9QYP8U']
# /dev/cu.Bluetooth-Incoming-Port
# /dev/cu.usbmodem14201
# /dev/cu.usbserial-A9QYP8U
