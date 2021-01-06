import pandas as pd

def merge_iso_code(df1, df2, iso):
    right = df2[df2.iso_code == iso].rename({"stringency_index": iso}, axis = 1)
#     print(df2.columns)
#     print(df2.dtypes, df1.dtypes)
    df1 = df1.merge(right[["DATE", iso]], on = "DATE")
    return df1