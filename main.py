from internal.app import App

import os

def main(event, context):
    print("Context contains: ", context)

    print("Event contains ", event)

    app_name = os.getenv("SERVICE_NAME")
    new_app = App(app_name)

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']

        print("Bucket name is ", bucket)

        key = record['s3']['object']['key']

        print("Key is: ", key)

        try:
            new_app.consume(key)
        except Exception as e:
            print("Error in consuming app wih exception ", e)

