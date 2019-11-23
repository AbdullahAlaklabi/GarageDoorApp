import os.path
import time
import garageDoorGui as gd
import datetime


def insert_data_into_database():
    unix = time.time()
    Date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    EventID = 5
    almMessage = 'Something is wrong'

    print("Connecting to database....")
    try:
        (Date, gd.getTemperature(), gd.getHumindity(),gd.getGassLevel(),gd.garageDoorStatus(), gd.getAlarmStatus(),almMessage,EventID))
        print(Date, gd.getTemperature(), gd.getHumindity(),gd.getGassLevel(),gd.garageDoorStatus(), gd.getAlarmStatus(),almMessage,EventID)
    except Exception as err:
        print('Something went wrong. Unable to perform action on database: ', err)


   

