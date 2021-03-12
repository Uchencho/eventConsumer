from internal.workflow.workflow import get_file_details


class App:

    function_map = {
        'renewals' : get_file_details
    }

    def __init__(self, appName):
        print("Initializing with ", appName)


    def consume(self, event_key):
        available_keys = self.function_map.keys()

        print("Consuming event with wvent key: ", event_key)

        for k in available_keys:
            if k in event_key:
                func_to_invoke = self.function_map[k]
                func_to_invoke(event_key)
                return
        
        raise KeyError(f"{event_key} is not registered among consumers")
