import pandas as pd


def get_file_details(filename):

    """
    Reads a file stored in s3 and prints to the console, the shape of the file

    args: filename (string)
    """

    print("File received: ", filename)

    data = {'year': [2014, 2018,2020,2017], 
        'make': ["toyota", "honda","hyndai","nissan"],
        'model':["corolla", "civic","accent","sentra"]
       }

    df = pd.DataFrame(data)

    print(df, "\n\n", df.shape)

