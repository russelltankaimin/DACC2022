# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import geopandas
import snappy
from fastparquet import ParquetFile
import pandas as pd
import pyarrow.parquet as pq;

filename = "/Users/russelltankaimin/Downloads/city=Singapore/part-00000-8bbff892-97d2-4011-9961-703e38972569.c000.snappy.parquet"
#df = pq.read_table(filename).to_pandas()
a = df = pq.read_table(source=filename).to_pandas()
print(a)

