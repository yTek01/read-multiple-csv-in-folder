
import pandas as pd 
import glob
import opendatasets as od


od.download("https://www.kaggle.com/datasets/datasnaek/youtube-new")

path = "youtube-new"
files = glob.glob(path + "/*.csv")

content = []
for filename in files:
    print(filename)
    try:
        df = pd.read_csv("./"+ filename, index_col=None)
        content.append(df)
    except:
        df = pd.read_csv("./"+ filename, index_col=None, encoding="ISO-8859-1")
        content.append(df)
        pass

data_frame = pd.concat(content)
print(data_frame)