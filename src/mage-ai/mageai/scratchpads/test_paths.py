"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from glob import glob
import pyarrow.parquet as pq

paths = glob('/home/mage/data/raw_parquets/*/**')
#paths_nested = glob('/home/mage/data/raw_parquets/*/**')
print(paths, end='\n')

#schemas = []
#for p in paths:
#    parquet_file = pq.ParquetFile(p)
#    print(parquet_file.schema, end='\n')