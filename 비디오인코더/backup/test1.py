from tqdm import tqdm
import pandas as pd

df = pd.read_excel('통합 문서1.xlsx', usecols=[0, 1])

print("done")
#for chunk in tqdm(pd.read_excel('아이템_230421_14시18분 기준.xlsx.xlsx', chunksize=1000)):
    # Do something with chunk of data
