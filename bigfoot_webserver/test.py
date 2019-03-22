import serial
import time

ser=serial.Serial('/dev/ttyUSB0',57600)

while 1:
	ser.write("test\n")
	time.sleep(0.01)
