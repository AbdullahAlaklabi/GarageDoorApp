import sqlite3
import os.path
import garageDoorGui as gd

def openDatabase():
    
    #Get working directory
    path = os.getcwd()
    dbExists  = not os.path.exists("/garageDoor.db")
    print(path)
    if dbExists:
        print("garageDoor database found\nConnecting to database....")
        with sqlite3.connect(path + "/garageDoor.db") as conn:
            cursor = conn.cursor()
            #for row in cursor.fetchall():
                #DateTime,Temperature,Humidity, GasLevel, GarageDoorState, AlarmState, AlarmMessage, EventID = row
               # print(row)
            try:
                cursor.execute('SELECT * FROM garageSensorLog')
                #cursor.execute("INSERT INTO garageSensorLog VALUES(CURRENT_TIMESTAMP, gd.getTemperature(), gd.getHumindity(),gd.getGassLevel(),gd.garageDoorStatus(), gd.getAlarmStatus(), 'Action', 7)")
                cursor.execute("INSERT INTO garageSensorLog(DateTime, Temperature, Humidity, GasLevel,GarageDoorState,AlarmState,AlarmMessage,EventID)VALUES(datetime('now','localtime'), 934, 76, 25, 'Close', 'Inactive', 'All Clear', 7);")
            except Exception as err:
                print('Something went wrong. Unable to perform action on database')
                conn.rollback()
    else:
        print("Couldn't find garageDoor database")
openDatabase()    
   
   

