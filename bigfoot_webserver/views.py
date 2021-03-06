from django.shortcuts import render
from django.http import HttpResponse
import serial
import time
import threading

ser=serial.Serial('/dev/ttyUSB0',57600)
ser.rtscts=True
#ser.write('+++'.encode('ascii'))
mutex=threading.Lock()


def index(request):
	return render(request,'bigfoot.html')

def send_call1(request):
	#thread=threading.Thread(target=write_gpio_high,args=())
	#thread.daemon=True
	#thread.start()
	write_serial_cmd(1)
	return render(request,'bigfoot.html')

def send_call2(request):
	#thread=threading.Thread(target=write_gpio_high,args=())
	#thread.daemon=True
	#thread.start()
	write_serial_cmd(2)
	return render(request,'bigfoot.html')

def send_call3(request):
	#thread=threading.Thread(target=write_gpio_high,args=())
	#thread.daemon=True
	#thread.start()
	write_serial_cmd(3)
	return render(request,'bigfoot.html')

def write_serial_cmd(cmd):
	print("Writing Test to serial")
	packet = ('big' + str(cmd) + '\n').encode('ascii')
	print(packet)
	ser.write(packet)


def write_gpio_high():
	mutex.acquire()
	try:
		print("Setting AT Mode")
		ser.write('\r\n'.encode('ascii'))
		#ser.write('+++'.encode('ascii'))
		time.sleep(2)
		print(ser.read(ser.inWaiting()).decode('ascii'))
		print("Setting Remote GPIO High")
		ser.write('RTPC=4,1\r\n'.encode('ascii'))
		time.sleep(5)
		print(ser.read(ser.inWaiting()).decode('ascii'))
		print("Setting Remote GPIO Low")
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		print(ser.read(ser.inWaiting()).decode('ascii'))
		print("Exiting Serial Thread")
	except ex:
		print(ex)
		print("SOmething failed")
	finally:
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		ser.write('RTPC=4,0\r\n'.encode('ascii'))
		mutex.release()
