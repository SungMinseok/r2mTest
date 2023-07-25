import re

def format_stats(input_str : str):
    """
    기획 능력치 스트링 [전체]를 받아와서 수/수/수... 형태로 리턴
    """
    result = ''
    for line in input_str.split('\n'):
        numbers = re.findall(r'\d+\.?\d*', line)
        temp = '/'.join(numbers)
        result += temp + "\n"

    return result.strip()

def format_stats_ingame(input_str):
    """
    인게임 능력치 스트링을 [개별]로 받아와서 수/수/수... 형태로 리턴
    능력치 스샷찍은 직후에 바로 사용
    """
    # split the input string by lines
    lines = input_str.strip().split('\n')

    # initialize an empty list to hold the final result
    result_list = []

    for line in lines:
        total = 0
        
        if '(' in line :
            line = line.replace('(', '').replace(')', '')
            values = line.strip().split('+')
            for value in values:
                try:
                    total += int(value.strip())
                except:
                    continue

        else : 
            values = line.strip().split('+')
            if '%' in values[1] :
                total = values[1].replace('%','')
            else :
                total = values[1]

        result_list.append(total)

    return '/'.join(str(x) for x in result_list)

# input_file_path = 'input.txt'
# with open(input_file_path, encoding='utf-8') as f:
#     input_str = f.read()

    
# result = format_stats(input_str)


# with open('output.txt', 'w') as f:
#     f.write(result)

input_str = "+20(+5)\n+22(+4)\n+3.25%\n+2\n+1"

result = format_stats_ingame(input_str.strip())
print(result)  # output: 30.0/40.0/17.0/3.0/3.0