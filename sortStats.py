import re
from tqdm import tqdm

def sort_values(input_str):
    
    rules = ["물리공격", "마법공격", "공속", "물리명중", "마법명중", "힘", "민첩", "지능", "HP","HP회복","MP " ,"MP회복"]
    lines = input_str.strip().split('\n')
    sorted_lines = []

    for line in tqdm(lines):
        values = line.split('/')
        sorted_values = []

        for rule in rules:
            for value in values:
                
                nonDigitStr = re.split(r"\d", value)
                nonDigitStr = nonDigitStr[0]
                if nonDigitStr.startswith(rule) and (len(rule)==len(nonDigitStr)):
                    sorted_values.append(value)
        
        for value in values:
            if value not in sorted_values:
                sorted_values.append(value)
        
        sorted_lines.append('/'.join(sorted_values))

    return '\n'.join(sorted_lines)


with open('input_sort_values.txt', 'r', encoding='utf-8') as f:
    input_str = f.read()

#input_str = "물리공격21/HP30/물리명중17/공속2.35%/[PVP슬레인]물리명중2"


output_str = sort_values(input_str)
#print(input_str)
#print(output_str)

with open('output_sort_values.txt', 'w', encoding='utf-8') as f:
    f.write(output_str)