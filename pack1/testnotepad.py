
import MySQLdb

config = {
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
        cursor = conn.cursor()
        buser_info = input('직급 입력 : ')
        sql = """
            SELECT jikwon_no, jikwon_name, jikwon_jik, buser_num
            FROM jikwon
            INNER JOIN buser ON jikwon.buser_num=buser.buser_no
            WHERE jikwon_jik='{0}'
            """.format(buser_info)
        
        cursor.execute(sql)
        data = cursor.fetchall()
        
        if len(data) == 0:
            print(str(buser_info)+'에 해당되는 자료는 없습니다.')
            return 
        for jikwon_no, jikwon_name, jikwon_jik, buser in data:
            print(jikwon_no, jikwon_name, jikwon_jik, buser)
                    
    except Exception as e :
        print('ERROR : ', e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    chulbal()    