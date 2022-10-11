## 동 이름을 입력해 해당 동 관련 우편번호 및 주소 출력하기.

try:
    dong = input('동 이름 입력 : ')
    print(dong)
    
    with open('zipcode.txt', mode='r', encoding='euc-kr') as f:
        line = f.readline()
        #print(line)
        while line:
            #lines =line.split('\t')
            lines =line.split(chr(9)) # 아스키코드값으로 바꿔주는 내장함수 chr
            #print(lines)
            if lines[3].startswith(dong):
                #print(lines)
                print('['+lines[0]+']'+lines[1]+' '+lines[2]+' '+lines[3]+' '+lines[4])
                
            line = f.readline()    
except Exception as e:
    print('ERROR : ',e)