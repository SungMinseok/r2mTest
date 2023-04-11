import re
from tqdm import tqdm

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


input_file_path = '정렬된기획능력치.txt'
with open(input_file_path, encoding='utf-8') as f:
    input_str = f.read()

    
result = format_stats(input_str)


with open('정렬된기획능력치_숫자만.txt', 'w') as f:
    f.write(result)