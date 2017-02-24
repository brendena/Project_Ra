# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

fileNames = ["USA_CA_Los.Angeles.Intl.AP.722950_TMY3_", "USA_FL_Tampa.Intl.AP.722110_TMY3_",
             "USA_ME_Portland.Intl.Jetport.726060_TMY3_", "USA_NY_Albany.County.AP.725180_TMY3_",
             "USA_NY_New.York-J.F.Kennedy.Intl.AP.744860_TMY3_", "USA_TX_Houston-Bush.Intercontinental.AP.722430_TMY3_",
             "USA_WA_Seattle-Boeing.Field.727935_TMY3_", "USA_WI_Milwaukee-Mitchell.Intl.AP.726400_TMY3_"]

suffixes = ["BASE", "LOW", "HIGH"]

writeTo = open(r"C:\Users\Sam\Desktop\Solar Datasets\Residential\output.txt", "w+")

for name in fileNames:
    for suffix in suffixes:
        filename = r"C:\Users\Sam\Desktop\Solar Datasets\Residential" + "\\" + name + suffix + ".csv"
        df = pd.read_csv(filename, low_memory = False)
        
        print(name[4:6] + " " + suffix, file = writeTo)
        print("---------------------------------------------------------------", file = writeTo)
        print(df.mean(), file = writeTo)
        print("\n", file = writeTo)
    print("===============================================================\n", file = writeTo)

writeTo.flush()
writeTo.close()