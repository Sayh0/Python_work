import cgi

form = cgi.FieldStorage() #자바의 서블렛

name = form["name"].value #자바의 request.getparameter("name")
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
    <html>
    <body>
    친구의 이름은 : {0}
    <br>
    전화번호는 : {1}
    <br>
    성별은 {2}
    </body>
    </html>
    '''.format(name, phone, gen))