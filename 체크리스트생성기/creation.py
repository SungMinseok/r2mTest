import pandas as pd

def create_checklist(input_file, output_file, criterion, required_parts):
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file,engine='openpyxl')
    
    # Check if all columns are required
    if required_parts == 'all':
        required_parts = df.columns
    
    # Convert the DataFrame into the desired checklist format
    result_data = []
    for _, row in df.iterrows():
        name = row[criterion]
        for part in required_parts:
            value = row[part]
            result_data.append([name, part.capitalize(), value])

    # Create the resulting DataFrame
    result_df = pd.DataFrame(result_data, columns=[criterion, 'Part', 'Value'])
    
    # Save the result to an output Excel file
    result_df.to_excel(output_file, index=False,engine='openpyxl')

# Example usage:
if __name__ == "__main__":
    input_file = "insert.xlsx"
    output_file = "result.xlsx"
    criterion = '이름'
    required_parts = ['아이템 설명','아이템 사용','비고']#'all'#['등급', '나이', '가격']
    #required_parts = 'all'#['등급', '나이', '가격']

    create_checklist(input_file, output_file, criterion, required_parts)

    import os
    os.startfile(output_file)