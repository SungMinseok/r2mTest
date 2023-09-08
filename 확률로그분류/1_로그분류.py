from tqdm import tqdm

# 파일 이름과 검색할 문자열 설정
file_name = "Field20230906164445.txt"
arg_0 = ["뽑기 확률테스트","변신카드 합성 확률테스트","서번트카드 합성 확률테스트"]
#arg_1 = "매터리얼 합성"

# 파일을 읽기 모드로 열기
with open(file_name, "r", encoding="utf-16") as file:
    lines = file.readlines()

# 결과를 저장할 빈 문자열 초기화

# 파일 내용을 순회하면서 검색 및 추출
#in_arg_0_section = False
for i in range(0,len(arg_0)):
    result = ""
    result_re = ""
    for line in tqdm(lines):
        #for item in arg_0:
        if arg_0[i] in line:
        #if arg_0 in line:
                #in_arg_0_section = True
            if arg_0[i] =="뽑기 확률테스트":
                if "다시뽑기" in line:
                    result_re += line
                else:
                    
                    result += line
            else:
                result += line
        # elif arg_1 in line and in_arg_0_section:
        #     in_arg_0_section = False
        #     #result += line
        #     break  # arg_1이 발견되면 처리를 중단합니다.

    # 결과를 새로운 파일에 저장
    output_file_name = f"{arg_0[i]}.txt"
    with open(output_file_name, "w", encoding="utf-16") as output_file:
        output_file.write(result)

    if result_re != "":
        output_file_name = f"다시뽑기 확률테스트.txt"
        with open(output_file_name, "w", encoding="utf-16") as output_file:
            output_file.write(result_re)

    print(f"{output_file_name} 파일로 내보내기 완료되었습니다.")
