# # ******************************************************************************************************************************************************************************
# in Command line usage:

# # module: serial.tools.list_ports()
# python -m serial.tools.list_ports

# # module: serial tools.miniterm()
# python -m serial.tools.miniterm -h
# # ******************************************************************************************************************************************************************************

# module: serial.tools.list_ports()
# module: serial tools.miniterm()




# ******************************************************************************************************************************************************************************
import serial.tools.list_ports

# serial.tools.list_ports.comports()
# include_links (bool) – include symlinks under /dev when they point to a serial port
# a list containing ListPortInfo objects

ser = serial.tools.list_ports.comports(include_links=True)
print(ser)      # [<serial.tools.list_ports_common.ListPortInfo object at 0x000002A303714C70>]

# expend ListPortInfo object
for port, desc, hwid in ser:
    print(port)         # COM3
    print(desc)         # Prolific USB-to-Serial Comm Port (COM3)
    print(hwid)         # USB VID:PID=067B:2303 SER= LOCATION=1-2



# ******************************************************************************************************************************************************************************
# classserial.tools.list_ports.ListPortInfo
# port, desc, hwid = info

# ser = serial.tools.list_ports.comports(include_links=True)
for info in ser:
    print(info.device)          # COM3
    print(info.name)            # COM3
    print(info.hwid)            # USB VID:PID=067B:2303 SER= LOCATION=1-2       # return None if no device attached 

    # USB vendor ID
    print(info.vid)             # 1659

    # USB product ID
    print(info.pid)             # 8963

    # serial number: STR
    print(info.serial_number)   # NA

    # LOCATION - USB device location string (“<bus>-<port>[-<port>]…”)
    print(info.location)        # 1-2

    # manufactor 
    print(info.manufacturer)    # Prolific

    # product
    print(info.product)         # None


    # interface
    print(info.interface)       # None




