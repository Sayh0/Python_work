# MariaDB 자료 웹으로 출력

import MySQLdb
import pickle

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<h2>상품 정보</h2>')
print('<table border="1">')
print('''<tr>
            <th>코드</th>
            <th>품명</th>
            <th>수량</th>
            <th>단가</th>
        </tr>''')
with open('mydb.dat','rb') as obj:
    config= pickle.load(obj)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata")
    dates = cursor.fetchall()
    for code,sang,su,dan in datas:
        print('''<tr>
            <th>{0}</th>
            <th>{1}</th>
            <th>{2}</th>
            <th>{3}</th>
        </tr>'''.format(code,snag,du,dan))    
except Exception as e:
    print("ERROR : ",e)
finally:
    cursor.close()
    conn.close()
    
print('</table>')
print('</body></html>')