
import serial 


# ser.read() is only going to return 1 byte at a time.

# ser.readline()
# line = ser.readline()

# on MAC
# ls /dev/tty.*

# ************************************************************************************************************************************************
ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

while True:
    debug_line = str(ser.readline())
    print(debug_line)
# b'$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50\r\n'
# b'$GPTXT,01,01,02,HW  UBX-G70xx   00070000 *77\r\n'
# b'$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59\r\n'
# b'$GPTXT,01,01,02,PROTVER 14.00*1E\r\n'
# b'$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20\r\n'
# b'$GPTXT,01,01,02,ANTSTATUS=OK*3B\r\n'
# b'$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFD-FFFFFFFF-FFFFFFFF-FFFFFFF9*53\r\n'
# b'$GPRMC,033821.00,V,,,,,,,140121,,,N*71\r\n'
# b'$GPVTG,,,,,,,,,N*30\r\n'
# b'$GPGGA,033821.00,,,,,0,00,99.99,,,,,,*6D\r\n'
# b'$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30\r\n'
# b'$GPGSV,1,1,02,06,,,23,17,,,22*7A\r\n'
# b'$GPGLL,,,,,033821.00,V,N*41\r\n'



# ************************************************************************************************************************************************
ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

while True:
    debug_line = str(ser.readline())
    # get rid of 'b and \r\n'
    print(debug_line[2:][:-5])      
# $GPTXT,01,01,02,u-blox ag - www.u-blox.com*50
# $GPTXT,01,01,02,HW  UBX-G70xx   00070000 *77
# $GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59
# $GPTXT,01,01,02,PROTVER 14.00*1E
# $GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20
# $GPTXT,01,01,02,ANTSTATUS=OK*3B
# $GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFD-FFFFFFFF-FFFFFFFF-FFFFFFF9*53
# $GPRMC,034016.00,V,,,,,,,140121,,,N*7A
# $GPVTG,,,,,,,,,N*30
# $GPGGA,034016.00,,,,,0,00,99.99,,,,,,*66
# $GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30
# $GPGSV,1,1,01,06,,,20*7C
# $GPGLL,,,,,034016.00,V,N*4A



# ************************************************************************************************************************************************
ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

f = open('log_line_mac.txt', 'w+')

while True:
    debug_line = str(ser.readline().decode(encoding='utf-8'))
    # get rid of 'b and \r\n'  
    print(debug_line)
    f.write(debug_line)




# ************************************************************************************************************************************************
ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

while True:
    debug_char = str(ser.read())
    print(debug_char) 
# b'2'
# b'2'
# b'5'
# b'.'
# b'0'
# b'0'
# b','




#  ************************************************************************************************************************************************
ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

f = open('log_char_mac.txt', 'w+')

while True:
    debug_char = str(ser.read())
    # print(debug_char) 
    f.write(debug_char)
















