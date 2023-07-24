import re
from tqdm import tqdm

'''
날것의기획능력치.txt > 정렬된기획능력치.txt > 정렬된기획능력치_숫자만.txt

'''


def sort_values(input_str : str):
    input_str = input_str.replace('+','')
    input_str = input_str.replace(' ','')
    
    rules = ["물리방어",
             "마법방어",
             "물리공격", 
             "마법공격",
             "마나소모감소율",
             "공속", 
             "공격속도", 
             "물리명중", 
             "포션회복량",
             "물리피해감소",
             "마법피해감소",
             "이속",
             "이동속도",
             "포션회복률",
             "마법명중",
             "치명타확률",
             "치명타공격력",
             "치명타회피",
             "HP",
             "HP회복",
             "MP",
             "MP회복",
             "힘", 
             "민첩", 
             "지능",
             "추가무게", 
             "[" 
             ]
    lines = input_str.strip().split('\n')
    sorted_lines = []

    for line in tqdm(lines):
        values = line.split('/')
        sorted_values = []
        
        cc_start_index = 99
        slain_start_index = 99
        
        for i in range(0,len(values)) :
            temp_val = values[i]
            if "[PVP]" in temp_val :
                cc_start_index = i
                break

        for i in range(0,len(values)) :
            temp_val = values[i]
            if "[" in temp_val :
                slain_start_index = i
                break

        for rule in rules:
            for i in range(0,len(values)):
                
                nonDigitStr = re.split(r"\d", values[i])
                nonDigitStr = nonDigitStr[0]
                #if nonDigitStr == "MP":
                #    print(nonDigitStr)
                if nonDigitStr == rule and i < slain_start_index :
                #if nonDigitStr.startswith(rule) and (len(rule)==len(nonDigitStr)):
                    #if nonDigitStr == "MP":
                    #    print(nonDigitStr)
                        
                    #else :
                    sorted_values.append(values[i])


                # elif "[" in nonDigitStr :
                #     slain_check = True
        
        for value in values:
            if value not in sorted_values:
                sorted_values.append(value)

        if cc_start_index != 99 :
            cc_stat = sorted_values[cc_start_index]
            sorted_values.remove(cc_stat)
            sorted_values.insert(slain_start_index,cc_stat)
            print(sorted_values)
        
        sorted_lines.append('/'.join(sorted_values))

    return '\n'.join(sorted_lines)

def format_stats(input_str : str):
    """
    기획 능력치 스트링 [전체]를 받아와서 수/수/수... 형태로 리턴
    """
    result = ''
    for line in tqdm(input_str.split('\n')):
        numbers = re.findall(r'\d+\.?\d*', line)
        temp = '/'.join(numbers)
        result += temp + "\n"

    return result.strip()

if __name__ == "__main__" :


    with open('날것의기획능력치.txt', 'r', encoding='utf-8') as f:
        input_str = f.read()

    output_str = sort_values(input_str)

    with open('정렬된기획능력치.txt', 'w', encoding='utf-8') as f:
        f.write(output_str) 
        
    #input_file_path = '정렬된기획능력치.txt'
    #with open(input_file_path, encoding='utf-8') as f:
    #    input_str = f.read()

        
    result = format_stats(output_str)

    with open('정렬된기획능력치_숫자만.txt', 'w') as f:
        f.write(result)