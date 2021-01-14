
# import serial.tools.list_ports


# Option 1
import serial.tools.list_ports
print(list(serial.tools.list_ports.comports()))         # WIN # [<serial.tools.list_ports_common.ListPortInfo object at 0x00000253F73B4C70>]
print(list(serial.tools.list_ports.comports()))         # MAC # [<serial.tools.list_ports_common.ListPortInfo object at 0x7ff5a69d68b0>, <serial.tools.list_ports_common.ListPortInfo object at 0x7ff5a69a7460>]


# option 2
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

print(ports)          # WIN # [<serial.tools.list_ports_common.ListPortInfo object at 0x00000253F73B4C70>]
print(ports)          # MAC # [<serial.tools.list_ports_common.ListPortInfo object at 0x7fe93f295340>, <serial.tools.list_ports_common.ListPortInfo object at 0x7fe93f29d4c0>]


# ************************************************************************************************************************************************
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))
# WIN # COM3: Prolific USB-to-Serial Comm Port (COM3) [USB VID:PID=067B:2303 SER= LOCATION=1-2]

# MAC # /dev/cu.usbmodem14101: u-blox 7 - GPS/GNSS Receiver [USB VID:PID=1546:01A7 LOCATION=20-1]


# ************************************************************************************************************************************************
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port in ports:
    # print(port.device)          # WIN # COM3
    # print(port.device)          # MAC # /dev/cu.usbmodem14101



