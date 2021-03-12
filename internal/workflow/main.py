import pandas as pd


def get_file_details(filename, s3_client):

    """
    Reads a file stored in s3 and prints to the console, the shape of the file

    args: filename (string)
    """

    print("File received: ", filename)

    df = s3_client.read_prev_data_updates(filename)

    if df.shape == 0:
        raise IndexError(f"Shape of file {filename} cannot be zero")

    print("Shape of the file is: ", df.shape)
    print("File contains these columns: ", df.columns)

    return df.shape[0]

