## 개인용 DF : SQLite3 파이썬 기본 개인용 데이터 RDBMS임.

import sqlite3
print(sqlite3.sqlite_version)

print()
# conn=sqlite3.connect('exam.db') #로컬이라서 뭐 서버연동하고 그런 염병 할 필요 없음.
conn=sqlite3.connect(':memory:') #RAM에 일시적 데이터 저장(휘발성, 테스트용). 응용프로그램 종료후 사라짐.

try:
    cursor = conn.cursor()  #cursor를 이용해 SQL 쿼리를 처리
    
    # table 생성
    cursor.execute("CREATE TABLE IF NOT EXISTS fritab(name TEXT, phone TEXT)")
    
    # 자료 추가
    cursor.execute("INSERT INTO fritab(name, phone) VALUES('한국인', '111-1111')")
    cursor.execute("INSERT INTO fritab VALUES('우주인', '222-1111')")
    cursor.execute("INSERT INTO fritab VALUES(?, ?)", ('신기해', '333-1111')) #맵핑도 가능
    inputdata=('신기루','444-1111')
    cursor.execute("INSERT INTO fritab VALUES(?,?)", inputdata)
    conn.commit() #파이썬은 오토커밋 아니라 커밋써줘야 해.
    
    # select
    cursor.execute("SELECT * FROM fritab")
    print(cursor.fetchone()) # 하나 읽기
    print(cursor.fetchall()) # 몽땅 읽기
    
    
except Exception as e:
    print('ERROR : ', e)
    conn.rollback() # 실패시 롤백
finally:
    conn.close()