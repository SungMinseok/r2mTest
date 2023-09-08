import pandas as pd
from xlsx_processing import *
import os
import time 
def merge_rows_by_category1(df):
    grouped_df = df.groupby('Category1').agg(lambda x: ' '.join(x)).reset_index()
    return grouped_df

def create_checklist(sheet_name , input_file, output_file, criterion, required_parts):
    '''
    체크리스트생성
    '''
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file, sheet_name)
    df[criterion] = df[criterion].fillna(method='ffill')
    
    # Check if all columns are required
    if required_parts == 'all':
        required_parts = df.columns

    # Convert the DataFrame into the desired checklist format
    result_data = []
    for _, row in df.iterrows():
        name = row[criterion]
        for part in required_parts:
            if isinstance(part, tuple):
                # Handle tuples by combining their values in one row
                combined_value = ' x'.join(str(row[p]) for p in part )
                result_data.append([name, ' & '.join(part), combined_value])
            else:
                if part != criterion :
                    value = row[part]
                    result_data.append([name, part, value])

    # Create the resulting DataFrame
    result_df = pd.DataFrame(result_data, columns=['Category1', 'Category2', 'Category3'])
    
    # Merge rows with the same values in Category1
    #result_df = merge_rows_by_category1(result_df)

    # Save the result to an output Excel file
    result_df.to_excel(output_file, index=False)

    postprocess_cashshop(output_file)

def create_checklist2(input_file, output_file, criterion, required_parts):
    '''
    체크리스트생성
    '''
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file)

    id_list = df[criterion].dropna(axis=0)
    id_index_list = id_list.index
    totalCount = len(id_index_list)
    #df[criterion] = df[criterion].fillna(method='ffill')
    
    # Check if all columns are required
    if required_parts == 'all':
        required_parts = df.columns

    result_data = []

    for i in tqdm(range(0,totalCount)):
        #print(cashShopIdIndexList[j], j+1)

        if (i+1) >= totalCount :
            tempDf = df[id_index_list[i]:]
        else :
            tempDf = df[id_index_list[i]:id_index_list[i+1]]
        tempDf = tempDf.reset_index()

        split_char = 'x'
        temp_val = split_char.join(tempDf['능력치'].dropna().values)

        print(tempDf['능력치'].dropna().values)

        tempDf = tempDf[:1]
        tempDf['능력치'] = temp_val

        
        result_data.append(tempDf)


    # Create the resulting DataFrame
    #result_df = pd.DataFrame(result_data, columns=['Category1', 'Category2', 'Category3'])
    
    # Merge rows with the same values in Category1
    #result_df = merge_rows_by_category1(result_df)

    # Save the result to an output Excel file
    #result_df.to_excel(output_file, index=False)

    postprocess_cashshop(output_file)

# Example usage:
if __name__ == "__main__":
    input_file = "insert2.xlsx"
    output_file = f"result{time.strftime('_%y%m%d_%H%M%S')}.xlsx"
    criterion = '이름'
    required_parts = 'all'#['미믹 코인','대성공1', '대성공2', '대성공3']#[('능력치', '수치'), '등록 성공 확률']
    #required_parts = ['처치 수', '경험치',('아이템명1','수량1'),('아이템명2','수량2'),('아이템명3','수량3'),'스택획득확률']#[('능력치', '수치'), '등록 성공 확률']
    #required_parts = ['이름', '경험치']
    #required_parts = ['아이템 설명','아이템 사용','비고']#'all'#['등급', '나이', '가격']
    #required_parts = ['등급','설명','아이템 사용','무브리밋']#'all'#['등급', '나이', '가격']

    sheet_name = "아이템CL(수동)"
    sheet_name = "제작CL"
    sheet_name = "상자CL"

    if sheet_name == "아이템CL(수동)" :
        '''
        아이템CL(수동시트)
        '''
        criterion = '이름'
        required_parts = ['등급','이미지','설명','무브리밋','아이템 사용']#아이템CL
    elif sheet_name == "제작CL" :
        '''
        제작CL
        '''
        criterion = '제작 아이템'
        required_parts = ['카테고리','제작 수량','제작 제한','골드 비용','재료','성공 확률','실제 제작']#아이템CL
    elif sheet_name == "상자CL" :
        '''
        상자CL
        '''
        criterion = '이름'
        required_parts = ['구성품 획득','뽑기 구성']#아이템CL
        
    '''
    기본
    '''
    # criterion = '이름'
    # required_parts = 'all'
    #create_checklist2(input_file, output_file, criterion, required_parts)
    
    create_checklist(sheet_name,input_file, output_file, criterion, required_parts)
    os.startfile(output_file)
