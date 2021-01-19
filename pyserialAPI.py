


import serial

# class serial.Serial
#     __init__(
#     port=None, 
#     baudrate=9600, 
#     bytesize=EIGHTBITS, 
#     parity=PARITY_NONE, 
#     stopbits=STOPBITS_ONE, 
#     timeout=None,   # Set a read timeout value in sec 
#     xonxoff=False, 
#     rtscts=False, 
#     write_timeout=None,         # Set a write timeout value.
#     dsrdtr=False, 
#     inter_byte_timeout=None, 
#     exclusive=None
#     )



# The port is immediately opened on object creation, when a port is given. 
# It is not opened when port is None and a successive call to open() is required.

# port is a device name: depending on operating system. e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.

# write() is blocking by default, unless write_timeout is set


import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device)          # WIN # COM3
    print(port.device)          # MAC # /dev/cu.usbmodem14101

ser = serial.Serial('COM3', 115200)




# ****************************************************************************************************************
# open() - open port 
ser.open()

# close() - immediately close port
ser.close()

# read(size) - read size in byte 
ser.read()

# read_until(size) - expected size in byte
ser.read_until()


# write() - data to send
ser.write(str.encode('data'+'\r\n')) 


# flush() - wait until all data is writen, flush objects
ser.flush()


# in_waiting() - return # of byte in RX buffer 
ser.in_waiting()
ser.inWaiting()
# out_waiting() - return # of byte in TX buffer 
ser.out_waiting()
ser.outWaiting()

# reset_input_buffer() - flush input buffer and content
ser.reset_input_buffer()
ser.flushInput()
# reset_out_buffer() - aborting current output and discarding all that is in the buffer 
ser.reset_output_buffer()
ser.flushOutput()


# break_condition() - BREAK
ser.break_condition()

# rts()
# dts()
# cts()
# dsr()
# ri()
# cd()



# serial.name - read_only
ser.name            # COM3


# is_open() - get the state of serial port
ser.is_open()


# ser.port()

# ser.baudrate
print(ser.baudrate)


# ser.bytesize
print(ser.bytesize)         # 8


# ser.stopbits
print(ser.stopbits)             #1


# ser.timeout
# ser.write_timeout()
# ****************************************************************************************************************

# # LIST OF ALL 
# BAUDRATES
print(ser.BAUDRATES)        # (50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200)
# BYTESIZES
print(ser.BYTESIZES)        # (5, 6, 7, 8)
# PARITIES
print(ser.PARITIES)         # ('N', 'E', 'O', 'M', 'S')
# STOPBITS
print(ser.STOPBITS)         # (1, 1.5, 2)




ser.readline()
ser.readlines()
ser.writelines()



# ****************************************************************************************************************
# ****************************************************************************************************************
# __enter__()

# automatically open ports

port = serial.Serial()
port.port = '...'
with port as s:
    s.write(b'hello')

# __exit__()






