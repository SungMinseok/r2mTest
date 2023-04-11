import pandas as pd

def txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r', encoding='UTF8') as file:
        rows = file.readlines()
    
    option_count = 2

    data = []
    for i in range(0, len(rows)):
        row_data = []


        for j in range(0,option_count):
            cur_option_index = i % (option_count + 1)
            row_data.append(rows[cur_option_index])
        data.append(row_data)
    
    df = pd.DataFrame(data, columns=['Col1', 'Col2'])#, 'Col3', 'Col4', 'Col5'])
    df.to_csv(csv_file_path, index=False, encoding='cp949')
    #df.to_csv(csv_file_path, index=False, encoding='UTF8')


txt_file_path = '72000_10EA_1.txt'
csv_file_path = 'result.csv'

txt_to_csv(txt_file_path, csv_file_path)