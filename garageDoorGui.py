import tkinter as tk
from tkinter import ttk

def getTemperature():
    return 24.7

def getHumindity():
    return 37.5

def getGassLevel():
    return 93.2

def garageDoorStatus():
    return 'Closed'

def getAlarmStatus():
    return 'Inactive'


class App(tk.Tk):
    def __init__(self):
        super().__init__()
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
        self.testAlarmButton = tk.Button(buttonFrame, text='Test Alarm', relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.testAlarmButton.grid(row=1, column=2, columnspan = 1, padx = 5, pady = 7,sticky=tk.W)
        self.openGarageButton = tk.Button(buttonFrame, text='Open Garage', relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.openGarageButton.grid(row=2, column=1, columnspan = 1, padx = 5, pady = 7,sticky=tk.W)
        self.closeGarageButton = tk.Button(buttonFrame, text='Close Garage', relief=tk.RAISED,background = '#e1c2b9',fg="red")
        self.closeGarageButton.grid(row=2, column=2, columnspan = 1, padx = 5, pady = 7,sticky=tk.E)
        
        self.Temperature.set(getTemperature())
        self.humidity.set(getHumindity())
        self.gasLevel.set(getGassLevel())
        self.garageState.set(garageDoorStatus())
        self.alarmState.set(getAlarmStatus())
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
