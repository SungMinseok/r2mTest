import pandas as pd

def get_column_name_from_number(df, column_number):
    return df.columns[column_number]

def create_checklist(input_file, output_file, criterion, required_parts):
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file)
    
    # Convert column numbers to column names
    if isinstance(criterion, int):
        criterion = get_column_name_from_number(df, criterion)
    
    if isinstance(required_parts, int):
        required_parts = [get_column_name_from_number(df, required_parts)]
    elif isinstance(required_parts, tuple):
        required_parts = [get_column_name_from_number(df, p) for p in required_parts]
    else:
        required_parts = [get_column_name_from_number(df, p) if isinstance(p, int) else p for p in required_parts]

    # Convert the DataFrame into the desired checklist format
    result_data = []
    for _, row in df.iterrows():
        name = row[criterion]
        for part in required_parts:
            if isinstance(part, tuple):
                # Handle tuples by combining their values in one row
                combined_value = ' and '.join(str(row[p]) for p in part)
                result_data.append([name, ' & '.join(part), combined_value])
            else:
                value = row[part]
                result_data.append([name, part, value])

    # Create the resulting DataFrame
    result_df = pd.DataFrame(result_data, columns=['Category1', 'Category2', 'Category3'])
    
    # Save the result to an output Excel file
    result_df.to_excel(output_file, index=False)

# Example usage:
if __name__ == "__main__":
    input_file = "insert.xlsx"
    output_file = "result.xlsx"
    criterion = 0  # Assuming 'Name' is the first column (0-indexed)
    required_parts = [(1, 2), 4]  # Assuming ('Rating', 'Age') are the second and third columns (1 and 2), and 'Price' is the fifth column (4)

    # Get column names from column numbers
    df = pd.read_excel(input_file)
    if isinstance(criterion, int):
        criterion = get_column_name_from_number(df, criterion)
    
    if isinstance(required_parts, int):
        required_parts = [get_column_name_from_number(df, required_parts)]
    elif isinstance(required_parts, tuple):
        required_parts = [get_column_name_from_number(df, p) for p in required_parts]
    else:
        required_parts = [get_column_name_from_number(df, p) if isinstance(p, int) else p for p in required_parts]

    create_checklist(input_file, output_file, criterion, required_parts)
