def summarize_columns(df):
    '''get memory usage of each column in a DataFrame
    convert all possible object types to native or numpy types. Ex: datetime, int64 to int8'''

    for c in df.columns:
        print(c, len(df[c].unique()),
              df[c].memory_usage(deep=True) // (1024 ** 2), sep="\t")

    # Ex: df['column'] = df['column'].astype(np.int8)