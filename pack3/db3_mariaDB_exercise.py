
## 키보드에서 부서 번호를 입력받아 해당 부서 직원 자료(사번, 이름, 부서, 연봉, 직급)를 출력하기
#jikwon_no
#jikwon_name
#buser_num

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    #config = pickle.load(obj) # 시험 볼 때는 config 통으로 써 주세용
    config ={
    'host':'127.0.0.1',
    'user':'root',
    'password':'123', 
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
    } 

def chulbal():
    try:
        conn=MySQLdb.connect(**config)
        #print(conn)
        cursor = conn.cursor()
        buser_info = input('부서 이름 : ')
        sql = """
            SELECT jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik
            FROM jikwon
            INNER JOIN buser ON jikwon.buser_num=buser.buser_no
            WHERE buser_name='{0}' #문자니까 작은따옴표
            """.format(buser_info)
        #print(sql)
        
        cursor.execute(sql)
        data = cursor.fetchall()
        # print(data, len(data))
        
        if len(data) == 0:
            print(str(buser_info)+'에 해당되는 자료는 없습니다.')
            return # 함수를 탈출    #프로그램 강제종료는 sys.exit(0)
        
        for jikwon_no, jikwon_name, buser, jikwon_pay, jikwon_jik in data:
            print(jikwon_no, jikwon_name, buser, jikwon_pay, jikwon_jik)
            
        print('인원 수 : {}'.format(len(data)))
        
    except Exception as e :
        print('ERROR : ', e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    chulbal()