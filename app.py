import pandas as pd
from controllers.process import *
from controllers.email import *
from configs.processes import processes

df = pd.DataFrame()

for process in processes:
    if check(process['name']):
        # print(f"Process {process['name']} from {process['path']} is running")
        df = add_process(process['name'], process['path'], df)
    else:
        # print(f"Process {process['name']} from {process['path']} is not running")
        df = add_process(process['name'], process['path'], df)
        # start(process['name'])

print(df.head())
