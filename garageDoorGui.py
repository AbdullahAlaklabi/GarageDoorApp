#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22

#Pin that connects to the temperature humididty sensor
tempHumidityPin = 4

#this is GPIO18
garageDoorPin = 12

#This is GPIO17
buzzerPin = 11

temperature  = 0.0
humidity = 0.0

def getTemperature():
    global temperature
    global humidity
    humid, temp = Adafruit_DHT.read_retry(sensor, tempHumidityPin)
    temperature = round(temp, 2)
    humidity = round(humid, 2)
    if humidity is not None and temperature is not None:
        print('Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity))
        return temperature
    else:
        print('Failed to get reading. Try again!')
        temperature = round(0.0, 2)
        humidity = round(0.0, 2)
        return temperature
    

def getHumindity():
    global humidity
    return humidity

def getGassLevel():
    return 93.2

def garageDoorStatus():
    return 'Closed'

def getAlarmStatus():
    return 'Inactive'
    
def setupBoard():
    #Suppress warning
    GPIO.setwarnings(False)
    #Use physical pin numbering
    GPIO.setmode(GPIO.BOARD)
    
    
def sensorCallback(channel):
  # Called if sensor output changes
  if GPIO.input(channel):
    # No magnet
    print("Garage Door is open")
  else:
    # Magnet
    print("Garage Door is Closed")

def main():

  # Get initial reading
  sensorCallback(40)
  getTemperature()

  try:
    # Loop until users quits with CTRL-C
    while True :
      time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BOARD)

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(40 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(40, GPIO.BOTH, callback=sensorCallback, bouncetime=200)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #setup GPIO once the GUI is opened
        setupBoard()
        global garageDoorPin
        global buzzerPin
        self.title("Garage Door App")
        self.configure(background = '#e1c2b9')
                
        #declare variables
        self.garageState = tk.StringVar()
        self.alarmState = tk.StringVar()
        self.gasLevel = tk.DoubleVar()
        self.Temperature = tk.DoubleVar()
        self.humidity = tk.DoubleVar()
        
        #styling
        self.style = ttk.Style()
        self.style.configure('TLabel', font = ('Arial', 11))
        self.style.configure('TFrame', background = '#e1c2b9')
                       
        self.geometry("270x300+500+30")
        #this stops the gui from being resized
        self.resizable(False, False)
        firstFrame = tk.LabelFrame(self, padx=10, pady=10,
                                   text = "Garage Status",font = ('Arial', 9, 'bold'), background = '#e1c2b9')
        firstFrame.pack(padx=10, pady=15)
        
        ttk.Label(firstFrame, text='Garage Door State ',font = ('Calibri', 9),background = '#e1c2b9').grid(row=0)
        tk.Label(firstFrame, text='Garage Alarm State',font = ('Calibri', 9),background = '#e1c2b9').grid(row=1)
        tk.Entry(firstFrame, width=8, state="readonly", textvariable = self.garageState).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(firstFrame, width=8, state="readonly", textvariable = self.alarmState ).grid(row=1, column=1, sticky=tk.W)
        
        secondFrame = tk.LabelFrame(self, padx=15, pady=10,
                                        text = "Sensor Reading",font = ('Arial', 9, 'bold'),background = '#e1c2b9')
        secondFrame.pack(padx=10, pady=5)
        tk.Label(secondFrame, text="Temperature",font = ('Calibri', 9),background = '#e1c2b9').grid(row=0)
        tk.Label(secondFrame, text="Humidity      ",font = ('Calibri', 9),background = '#e1c2b9').grid(row=1)
        tk.Label(secondFrame, text="C02 level      ",font = ('Calibri', 9),background = '#e1c2b9').grid(row=2)
        
        tk.Entry(secondFrame, width=8, state="readonly", textvariable = self.Temperature).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(secondFrame, width=8, state="readonly", textvariable =self.humidity).grid(row=1, column=1, sticky=tk.W)
        tk.Entry(secondFrame, width=8, state="readonly", textvariable = self.gasLevel).grid(row=2, column=1,
                                        sticky=tk.W)
        
        #button frame
        buttonFrame =ttk.Frame(self)
        buttonFrame.pack()
        self.exitButton = tk.Button(buttonFrame, text='    Exit App ', command=self.destroy, relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.exitButton.grid(row=1,column=1, columnspan = 2, padx = 15, pady = 7,sticky=tk.W)
        self.testAlarmButton = tk.Button(buttonFrame, text='Test Alarm',command =self.alarm, relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.testAlarmButton.grid(row=1, column=2, columnspan = 1, padx = 5, pady = 7,sticky=tk.W)
        self.openGarageButton = tk.Button(buttonFrame, text='Open Garage',command =self.openGarageDoor, relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.openGarageButton.grid(row=2, column=1, columnspan = 1, padx = 5, pady = 7,sticky=tk.W)
        self.closeGarageButton = tk.Button(buttonFrame, text='Close Garage', command =self.openGarageDoor, relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.closeGarageButton.grid(row=2, column=2, columnspan = 1, padx = 5, pady = 7,sticky=tk.E)
        
        self.Temperature.set(getTemperature())
        self.humidity.set(getHumindity())
        self.gasLevel.set(getGassLevel())
        self.garageState.set(garageDoorStatus())
        self.alarmState.set(getAlarmStatus())
        
        
        
    def openGarageDoor(self):
        #setupBoard()
        GPIO.setup(garageDoorPin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(garageDoorPin, GPIO.LOW)
        GPIO.output(garageDoorPin, GPIO.HIGH)
        self.after(500)
        #time.sleep(0.5)
        GPIO.output(garageDoorPin, GPIO.LOW)
        
    def alarm(self):
        GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(buzzerPin, GPIO.HIGH)
        self.after(500)
        GPIO.output(buzzerPin, GPIO.LOW)
        
     
              
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    setupBoard()
    
