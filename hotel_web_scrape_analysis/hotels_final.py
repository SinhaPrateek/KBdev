import pandas as pd

df1 = pd.read_csv("29_Nov.csv")
df2 = pd.read_csv("30_Nov.csv")
df3 = pd.read_csv("1_Dec.csv")
df4 = pd.read_csv("2_Dec.csv")
df5 = pd.read_csv("3_Dec.csv")
df6 = pd.read_csv("4_Dec.csv")
df7 = pd.read_csv("5_Dec.csv")
df8 = pd.read_csv("6_Dec.csv")
df9 = pd.read_csv("7_Dec.csv")
df10 = pd.read_csv("8_Dec.csv")


print(df1.shape)
df = pd.DataFrame()
j = 0
i = 0
while(j<50):
    a = df1['Hotel_name'][i]
    if df2.loc[df2['Hotel_name'] == a]['Hotel_name'].any():
        if df3.loc[df3['Hotel_name'] == a]['Hotel_name'].any():
            if df4.loc[df4['Hotel_name'] == a]['Hotel_name'].any():
                if df5.loc[df5['Hotel_name'] == a]['Hotel_name'].any():
                    if df6.loc[df6['Hotel_name'] == a]['Hotel_name'].any():
                        if df7.loc[df7['Hotel_name'] == a]['Hotel_name'].any():
                            if df8.loc[df8['Hotel_name'] == a]['Hotel_name'].any():
                                if df9.loc[df9['Hotel_name'] == a]['Hotel_name'].any():
                                    if df10.loc[df10['Hotel_name'] == a]['Hotel_name'].any():
                                        df = df.append(df1.loc[df1['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df2.loc[df2['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df3.loc[df3['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df4.loc[df4['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df5.loc[df5['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df6.loc[df6['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df7.loc[df7['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df8.loc[df8['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df9.loc[df9['Hotel_name'] == a], ignore_index=True)
                                        df = df.append(df10.loc[df10['Hotel_name'] == a], ignore_index=True)
                                        j = j+1
                                        i = i+1
                                    else:
                                        i = i+1
                                else:
                                    i = i+1
                            else:
                                i = i+1
                        else:
                            i = i+1
                    else:
                        i = i+1
                else:
                    i = i+1
            else:
                i = i+1
        else:
            i = i+1
    else:
        i = i+1

df.to_csv("final.csv", index = False)