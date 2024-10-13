#Creating Data Frames

import pandas as pd
import numpy as np

#type 1 using dictonaries

data={
    "SNO":[1,2,3],
    "name":["AK","PK","kk"]
}

df_dict=pd.DataFrame(data)

print(df_dict)

data2=[[1,"AK"],[2,"PK"],[3,"kk"]]

df_lst=pd.DataFrame(data2,columns=["ID","NAME"])
print(df_lst)

id_arr=np.array([1,2,3])
name_arr=np.array(["AK","PK","kk"])

df_arr=pd.DataFrame({
    "ID":id_arr,
    "NAME":name_arr
})

df_arr=pd.DataFrame(df_arr)

print(df_arr)