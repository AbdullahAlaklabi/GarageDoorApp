from __future__ import print_function
from botocore.exceptions import ClientError
from database.config import DatabaseConnectionHandler
from datetime import datetime

import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)




def insert_log_to_dynamodb(current_date_time, temperature, humidity, gas_level, garage_door_state, alarm_state, alarm_message):
    table = DatabaseConnectionHandler.getDynamoDBTable()

    try:
        response = table.put_item(
            Item={
                "Time_Logged": current_date_time,
                "Gas_Level": gas_level,
                "Humidity": humidity,
                "Temperature": temperature,
                "Alarm_Message": alarm_message,
                "Alarm_State": alarm_state,
                "Garage_Door_State": garage_door_state
            }
        )


    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        print("GetItem succeeded:")

    print(json.dumps(response, indent=4, cls=DecimalEncoder))


