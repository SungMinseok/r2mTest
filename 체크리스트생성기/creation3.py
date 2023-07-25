import pandas as pd
from xlsx_processing import *
def merge_rows_by_category1(df):
    grouped_df = df.groupby('Category1').agg(lambda x: ' '.join(x)).reset_index()
    return grouped_df

def create_checklist(input_file, output_file, criterion, required_parts):
    '''
    체크리스트생성
    '''
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file)
    df = df.fillna(method='ffill')
    
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
                combined_value = ' | '.join(str(row[p]) for p in part )
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
# Example usage:
if __name__ == "__main__":
    input_file = "insert.xlsx"
    output_file = "result.xlsx"
    criterion = '몬스터 이름'
    required_parts = 'all'#[('능력치', '수치'), '등록 성공 확률']

    create_checklist(input_file, output_file, criterion, required_parts)
