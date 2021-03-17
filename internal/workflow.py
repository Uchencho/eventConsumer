from zipfile import ZipFile
import os


def get_file_details(filename, s3_client):

    """
    Reads a file stored in s3 and prints to the console, the shape of the file

    args: filename (string)
    """

    print("File received: ", filename)

    s3_client.read_prev_data_updates(filename)

    # if df.shape == 0:
    #     raise IndexError(f"Shape of file {filename} cannot be zero")

    # print("Shape of the file is: ", df.shape)
    # print("File contains these columns: ", df.columns)
    # df["owing_column"] = "not - owing"

    zip_file_for_s3('586863f5-836c-40ee-8d99-de983c22eeb9')

    s3_client.write_to_s3('586863f5-836c-40ee-8d99-de983c22eeb9')


def zip_file_for_s3(file_id):
    """
    Zips all files ending with .csv for upload to s3
    args:
        id: file_id (str)
    """
    print("zipping file...")
    print('path is ', f'/tmp/{file_id}')
    zf = ZipFile(f'/tmp/{file_id}', 'w')
    for f in os.listdir('/tmp/'):
        print("File found is: ", f)
        if f.endswith("txt"):
            print("Attempting to write ", '/tmp/'+f)
            zf.write('/tmp/'+f)
    zf.close()
    print("Zipped file successfully")

