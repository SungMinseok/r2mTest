import matplotlib.font_manager as fm
#fm._rebuild() # 시스템에 폰트파일 복사 후 최초 1회 수행
# 폰트 설정
fm.get_fontconfig_fonts()
font_location = '/usr/share/fonts/truetype/nanum/NanumGothicOTF.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
print('font_name:', font_name)
#matplotlib.rc('font', family=font_name)