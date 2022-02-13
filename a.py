# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import fsspec
import numpy as np
import geopandas
import snappy
from fastparquet import ParquetFile
import pandas as pd
import pyarrow.parquet as pq
for i in range(10):
    
    filename = "/Users/russelltankaimin/Downloads/city=Jakarta/part-0000"+str(i)+"-8bbff892-97d2-4011-9961-703e38972569.c000.snappy.parquet"
    dff = pq.read_table(filename).to_pandas()
    print(dff)
    dff.to_csv("JK_Part"+str(i)+".csv",index=False)


