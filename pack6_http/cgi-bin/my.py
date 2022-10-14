# 사용자가 전송한 정보를 수신 후 ...

import cgi

form = cgi.FieldStorage()
name = form['name'].value #자바의 requestparameter
age = form['age'].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
    <html>
    <body>
    이름은 {0}
    <br>
    나이는 {1}
    </body>
    </html>
    '''.format(name, age))
    
    #자바의 HTTPServletRequest가 하는 역할과 비슷. CGI가 함. simple~ 걔는 못함