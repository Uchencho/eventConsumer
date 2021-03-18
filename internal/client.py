import os, boto3
import pandas as pd

class S3Client:

    s3_client = None
    source_bucket_name = os.getenv('SOURCE_BUCKET')
    transformed_bucket = os.getenv("TRANSFORMED_BUCKET")
    boto_resource = "s3"

    def __init__(self):
        """
        initializes an s3 client from environment variables

        """
        print("initializing s3 client")
        try:
            self.s3_client = boto3.client("s3", region_name='us-east-1')
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
            obj = self.s3_client.get_object(Bucket = self.source_bucket_name, Key = file_read_name)
            df = pd.read_csv(obj['Body'])
            print('finished writing')
            
        except Exception as error:
            print(f"client - unable to get object from bucket {self.source_bucket_name} and key {file_read_name}" + error)
            raise
        # try:
        #     df = pd.read_csv(obj['Body'])
        # except Exception as e:
        #     print('client - unable to read file ', self.file_read_name)
        #     raise
        

        return df


    def write_to_s3(self, filename):
        """
        Writes a zip file to s3
        args: filename
        """
        print('writing to s3 bucket')
        try:
            self.s3_client.upload_file(f'/tmp/{filename}', self.transformed_bucket, filename,
            ExtraArgs={
                'Metadata': {'-clientFilename': filename},
                'ContentType' : 'application/zip',
                }
            )
        except Exception as e:
            print('client - error uploading zip file to s3 with ', e)
            raise e

        print('finished writing')

