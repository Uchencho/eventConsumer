from internal.workflow.main import get_file_details
from internal.client.main import S3Client

class App:

    s3_client = None

    function_map = {
        'renewals' : get_file_details
    }

    def __init__(self, appName, s3_client = None):
        print("Initializing with ", appName)

        self.s3_client = s3_client
        if not s3_client:
            self.s3_client = S3Client()
        print(self.s3_client) # Rather than printing, you would pass this into workflow


    def consume(self, event_key):
        available_keys = self.function_map.keys()

        print("Consuming event with event key: ", event_key)

        for k in available_keys:
            if k in event_key:
                func_to_invoke = self.function_map[k]
                r = func_to_invoke(event_key, self.s3_client)
                return r
        
        raise KeyError(f"{event_key} is not registered among consumers")
