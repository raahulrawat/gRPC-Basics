import pandas as pd

"""
:param: Path(will be get from gRPC call to load the required file)

Note: main function/ project requirement code will be defined here !!!!
For this example, i have taken read a csv file from the file system and returning the status of the task.
"""

def read_file(Path):
    df = pd.read_csv(Path)
    loaded_df = pd.DataFrame(df)
    print(loaded_df)
    return "File loaded successfuly from the directory: {}".format(Path)