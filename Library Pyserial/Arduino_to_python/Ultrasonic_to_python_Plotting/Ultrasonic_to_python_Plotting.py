# import serial
# ser = serial.Serial('COM7', baudrate= 9600, timeout=1)
# while 1:
# 	# arduinoData = ser.readline()
# 	arduinoData = ser.readline().decode('ascii')
# 	print(arduinoData)



import serial
import time
import numpy
import matplotlib.pyplot as plt
from drawnow import *
import keyword
import re
 
tempF = []
pressure = []
 
arduinoData = serial.Serial('COM7', baudrate= 9600, timeout=1) #sesuaikan port dan baudrate | port ada bisa dilihat di device manager | baudrate ada di arduino IDE
plt.ion()       #Tell matplotlib you want interactive mode to plot live data
cnt = 0
 
def makeFig():              # Create a function that makes our desired plot
    #plt.ylim(490,530)         # Menambahkan limit sumbu y
    plt.title('My Live Streaming Sensor Data')
    plt.grid(True)          # Tambahkan grid
    plt.ylabel('Temp F')    # Tambahkan label
    plt.plot(tempF, '-', label='Degrees F')
    plt.legend(loc='upper left')
 
while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    #print(arduinoString)
    #print(type(arduinoString))
    filterbyte = arduinoString.replace(b'\r\n', b'') #menghilangkan '\r\n' pada tipe data byte
    #print(filterbyte)
    #print(type(filterbyte))
    dataArray = filterbyte.split(b',') #memisah tipe data byte beradasarkan koma
    temp = float (dataArray[0])
    P = float (dataArray[1])
    print(temp,",",P)   # cek data sudah bisa di-split atau belum
    tempF.append(temp)
    pressure.append(P)
    #print tempF        # cek append sudah bisa atau belum
    drawnow(makeFig)    # Call drawnow to update our live graph
    plt.pause(.000001) #seseuikan dengan baudrate sehingga tidak terjadi delay
    # plt.pause(1) #ini diberikan jeda sedikit lama agar anda bisa menutup program dengan cara kill terminal tapi plotting akan terlambat dari serial monitor dari arduino
    cnt = cnt + 1
    if(cnt > 50):       # setting sumbu x = 50, agar data tidak menumpuk
        tempF.pop(0)
        pressure.pop(0)

    if(P < 5):
        break #menghentikan program jika P lebih kecil dari 5 

        