import os.path
import time
import datetime
import unittest

from database.impl import GarageSensorLogger


class TesDatabaseInsert(unittest.TestCase):
    def test_database_insert(self):
        success_flag = False
        unix = time.time()
        Date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        almMessage = 'Alarm Message'

        print("Connecting to database....")
        try:
            GarageSensorLogger.insert_log_to_dynamodb(Date, 1, 2, 3, "Garage Door Status", "Alarm Status", almMessage)
            success_flag = True
        except Exception as err:
            print('Something went wrong. Unable to perform action on database: ', err)

        self.assert_(success_flag, True)

    if __name__ == '__main__':
        unittest.main()
