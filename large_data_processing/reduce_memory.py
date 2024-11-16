import numpy as np
import pandas as pd

def summarize_columns(df):
    '''get memory usage of each column in a DataFrame
    convert all possible object types to native or numpy types. Ex: datetime, int64 to int8'''

    for c in df.columns:
        print(c, len(df[c].unique()),
              df[c].memory_usage(deep=True) // (1024 ** 2), sep="\t")

    # Ex: df['column'] = df['column'].astype(np.int8)
    # ex: df['float64'] = df['float64'].astype(np.float32) or 16
    # remove NA values with some native type's value to reduce memory usage


    df = pd.read_csv(
        'yellow_tripdata.csv.gz',
        dtype={
            'mta_tax': np.float16
            },
        parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'],
        usecols=['vendor_id','tpep_pickup_datetime', 'tpep_dropoff_datetime', 'mta_tax'],
        converters={
        "vendor_id": lambda x: np.int8(["","1", "2"].index(x))
        }
    )