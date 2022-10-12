# 원격 데이터베이스 연동 프로그램 (MariaDB 사용)
# pip install mysqlclient
import MySQLdb

# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password = '123', database = 'test')
# print(conn)
# conn.close()

# sangdata table 과 연동
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123', 
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
try:
    conn = MySQLdb.connect(**config)
    # print(conn)
    cursor = conn.cursor()
    
    '''
    #insert
    # sql = "insert into sangdata(code,sang,su,dan) values(10,'신상1',5,'5000')"
    sql = "INSERT INTO sangdata VALUES(%s,%s,%s,%s)"
    sql_data = '11','아아', 12, 5500
    count = cursor.execute(sql, sql_data)
    print(count)
    #cursor.execute(sql)
    conn.commit()
    '''
    
    #update
    sql = "update sangdata set sang=%s, su=%s where code=%s"
    sql_data=('Python', 50, 11)
    count = cursor.execute(sql, sql_data)
    print(count)
    conn.commit()

    #delete
    code = '10'
    sql = "DELETE FROM sangdata WHERE code="+code
    cursor.execute(sql)
    conn.commit()

    # select
    sql = "select code,sang,su,dan from sangdata"    # sql문이 복잡할 때는 먼저 cmd창에서 돌려보고 붙여넣기를 하자!
    cursor.execute(sql)     # cursor가 sql의 값을 가지고 있음
    
    # 방법 1
    for data in cursor.fetchall():
        # print(data)
        print('%s %s %s %s'%data)
    
    # 방법 2
    print()
    for r in cursor:
        print(r)
        print(r[0], r[1], r[2], r[3])
        
    # 방법 3
    print()
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
        
    # 방법 3-1
    print()
    for (a, 품명, su, kbs) in cursor: # 1대1로 mapping 하기 위한 변수명임!
        print(a, 품명, su, kbs)
        
except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()    # 자원 관리를 목적으로 close를 권장!
    