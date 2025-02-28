# in Excel, CONCATENATE(A1,",")
import os.path

list1 = [2748,
1904,
9251,
12865,
11049,
2098,
2253,
11047,
1541,
1931,
1946,
1700
         ]
# define_type
ans1 = int(input('만들고 싶은 파일 유형(0 or 1)을 입력하세요 (Python : 0, Cpp : 1) : '))
option = ['py', 'cpp']  # 쓰는 언어 없으면 option에 추가하세여
lang = option[ans1]
# make_file
print('현재 경로: %s' % (os.getcwd()))
ans2 = int(input('만들고 싶은 경로가 맞습니까? (Yes : 0, No : 1) : '))
if(ans2 == 2):
    print('파이썬 코드를 원하는 경로에서 실행시켜 주세요')
else:
    for i in range(len(list1)):
        file_dir = str(os.getcwd() + "\%s_%s.%s" % ("정글_4", list1[i], lang))
        # print(file_dir)
        if(os.path.isfile(file_dir)):  # 이미 파일이 생성되어 있으면
            print('"%s_%s.%s" is exist' % ("정글_4", list1[i], lang))
        else:
            f = open("%s_%s.%s" % ("정글_4", list1[i], lang), 'w')  # 파일이 없으면
            f.close()