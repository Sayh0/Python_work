## 예외처리는 어떻게?
# 예외처리 : 작업 도중 발생하는 에러에 대처하기.
# try ~ except (자바의 try - catch)
# 자바는 외부장치와 연결할 때( ex)키보드 작업, 파일작업(보조기억장치), 네트워크작업 등 ) try catch를 강요함

def divide(a, b):
    return a / b

print(' doing something...')

c=divide(5, 2)
print(c)

print()
try:
    c=divide(5,2)
    print(c)
    
    aa=[1,2]
    print(aa[5])
except ZeroDivisionError:
    print('ERROR : 0으로 나눌 수 없습니다.')
except IndexError as err:
    print('ERROR : err', err)
except Exception as e:
    print('ERROR : etc', e)    
finally:
    print('에러 상관없이 반드시 실행')    
    
print('program terminated.') 
