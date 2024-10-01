#Tabla 1
producto1="lapicero"
stock1=1
valor1=4.3
iva=0.16
total1=valor1+(valor1*iva)
producto2="borrador"
stock2=10
valor2=5.1
total2=valor2+(valor2*iva)
producto3="pluma"
stock3=23
valor3=9.9
total3=valor3+(valor3*iva)
producto4="marcador"
stock4=10
valor4=4.4
total4=valor4+(valor4*iva)
producto5="cartulina"
stock5=9
valor5=5.5
total5=valor5+(valor5*iva)
producto6="sacapuntas"
stock6=4
valor6=9.3
total6=valor6+(valor6*iva)
print("{:^20}   {:^20}   {:^20}   {:^20}".format("producto","stock","valor sin IVA","total de compra"))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto1,stock1,valor1,total1))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto2,stock2,valor2,total2))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto3,stock3,valor3,total3))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto4,stock4,valor4,total4))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto5,stock5,valor5,total5))
print("{:^20}   {:^20}   {:^20}   {:^20,.2f}".format(producto6,stock6,valor6,total6))

#Tabla 2
contrato1="Simple"
tipopersona1="moral"
monto1=576.99
comision=9.9
apertura1=monto1+(monto1*comision)
contrato2="Cuenta Corriente"
tipopersona2="fisica"
monto2=5322.23
apertura2=monto2+(monto2*comision)
contrato3="Anticipo de Ventas"
tipopersona3="empresarial"
monto3=937.29
apertura3=monto3+(monto3*comision)
contrato4="Microapoyo"
tipopersona4="moral"
monto4=576.99
apertura4=monto4+(monto4*comision)
contrato5="Negocios y Empresas"
tipopersona5="moral"
monto5=2346.99
apertura5=monto5+(monto5*comision)
contrato6="Empuje Negocios"
tipopersona6="empresarial"
monto6=3426.99
apertura6=monto6+(monto6*comision)
print("{:<20}   {:<20}   {:<20}   {:<20}".format("contrato","tipopersona","monto sin comision","apertura"))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato1,tipopersona1,monto1,apertura1))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato2,tipopersona2,monto2,apertura2))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato3,tipopersona3,monto3,apertura3))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato4,tipopersona4,monto4,apertura4))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato5,tipopersona5,monto5,apertura5))
print("{:<20}   {:<20}   {:<20}   {:<20,.2f}".format(contrato6,tipopersona6,monto6,apertura6))

#Tabla 3
producto1="pumpkin"
unidades1= 3
valor1=55.7
extra=8.14
final1=valor1+(valor1*extra)
producto2="caramelo"
unidades2= 4
valor2=68.5
final2=valor2+(valor2*extra)
producto3="vainilla"
unidades3= 8
valor3=89.2
final3=valor3+(valor3*extra)
producto4="chocolate"
unidades4= 5
valor4=56.9
final4=valor4+(valor4*extra)
producto5="capuccino"
unidades5= 9
valor5=37.9
final5=valor5+(valor5*extra)
producto6="chocolate mexicano"
unidades6= 2
valor6=88.8
final6=valor6+(valor6*extra)
print("{:^20}   {:<20}   {:<20}   {:<20}".format("producto","unidades","valor sin extra","final"))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto1,unidades1,valor1,final1))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto2,unidades2,valor2,final2))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto3,unidades3,valor3,final3))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto4,unidades4,valor4,final4))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto5,unidades5,valor5,final5))
print("{:^20}   {:<20}   {:<20}   {:<20,.2f}".format(producto6,unidades6,valor6,final6))
