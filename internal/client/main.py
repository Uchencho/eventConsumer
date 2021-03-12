import os
import pandas as pd

class S3Client:

    s3_client = None
    source_bucket_name = os.getenv('aws_access_key_id')

    def __init__(self):
        """
        initializes an s3 client from environment variables

        """
        aws_access_key_id = os.environ['aws_access_key_id']
        aws_secret_access_key = os.environ['aws_secret_access_key']
        if not aws_access_key_id or not aws_secret_access_key:
            raise EnvironmentError("aws_access_key_id and aws_secret_access_key is needed to run this function")
        try:
            # client = boto3.client(boto_resource, region_name='us-east-1', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
            # return client
            # s3_client = client # set the returned client to s3 client
            print("Initializing client...")
        except Exception as error:
            print('client - Error initializing boto client for s3: ' + repr(error))
            raise


    def read_prev_data_updates(self, file_read_name):
        """
        Pulls the previous month of reporting's data updates file from S3
        Args:
            file_read_name: str
        Returns:
            df: pandas dataFrame
        """
        try:
            obj = self.s3_client.get_object(Bucket = source_bucket_name, Key = file_read_name)
        except Exception as error:
            print(f"client - unable to get object from bucket {source_bucket_name} and key {file_read_name}" + repr(error))
            raise
        try:
            df = pd.read_csv(obj['Body'])
        except Exception as e:
            print('client - unable to read file ', file_read_name)
            raise

        return df

