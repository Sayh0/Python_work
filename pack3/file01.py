##File i/o
import os

print(os.getcwd())

try:
    print('읽기 ------')
    f1 = open(r'C:\work\psou\pro\pack3\file_test.txt', mode='r', encoding='utf8')
    #f1=open(r'c')
    print(f1)
    print(f1.read())
    f1.close()
    
    print('저장--------')
    f2=open('file_test2.txt', mode='w', encoding='utf-8')
    f2.write('My friends\n')
    f2.write('홍길동과 나길동')
    f2.close()
    
    print('추가----------')
    f3=open('file_test2.txt', mode='a', encoding='utf-8')
    f3.write('저팔계와 사오정\n')
    f3.write('금각과 은각')
    f3.close()    
    
    print('읽기--------')
    f4=open('file_test2.txt', mode='r', encoding='utf-8')
    print(f4.readline())
    print(f4.readline())
    f4.close()
    
except Exception as e:
    print('ERROR : ', e)