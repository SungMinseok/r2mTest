# import pandas as pd

# # Read the input and output files as dataframes
# df_in = pd.read_csv('ingame.txt', header=None, names=['A'])
# df_out = pd.read_csv('output.txt', header=None, names=['B'])

# # Merge the dataframes on their index
# df_merged = pd.concat([df_in, df_out], axis=1)

# # Check if each row is equal between the two columns
# df_merged['C'] = df_merged.apply(lambda row: 'Pass' if row['A'] == row['B'] else 'Fail', axis=1)

# # Export the merged dataframe to Excel
# df_merged.to_excel('output.xlsx', index=False)


import pandas as pd

# read the files
with open('ingame.txt', 'r') as f:
    ingame_lines = f.readlines()

with open('output.txt', 'r') as f:
    output_lines = f.readlines()

# initialize the data to be written to Excel
data = {'ID': [], 'ingame': [], 'output': [], 'result': []}

# process each line
for output_line in output_lines:
    # get the ID from the output line
    output_id = output_line.split('/')[0]

    # find the corresponding line in ingame
    for ingame_line in ingame_lines:
        if ingame_line.startswith(output_id):
            # extract the values from the lines
            ingame_values = ingame_line.strip().split('/')[1:]
            output_values = output_line.strip().split('/')[1:]

            # compare the values and determine the result
            result = 'Pass' if ingame_values == output_values else 'Fail'

            # add the values to the data
            data['ID'].append(output_id)
            data['ingame'].append('/'.join(ingame_values))
            data['output'].append('/'.join(output_values))
            data['result'].append(result)

            # we found the corresponding line, so break out of the loop
            break

# create a DataFrame from the data and write to Excel
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
