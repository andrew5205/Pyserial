
import serial

# open serial port 
ser = serial.Serial('/dev/ttyUSB0')

# write a sting in binary
ser.write(b'hello')

# close port 
ser.close()





















