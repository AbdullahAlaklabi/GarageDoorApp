import boto3

def getDynamoDBTable():

    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1',
        aws_access_key_id='',
        aws_secret_access_key='')

    return dynamodb.Table('Garage_Sensor_Log_Table')


