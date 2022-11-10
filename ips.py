# -*- coding: utf-8 -*-
"""
    Correr direcciones IP para realizar programacion de equipos ELSTER A1800

@author: sfherrera
"""

import os
import pyodbc

conn = pyodbc.connect(
    'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\sfherrera\\Documents\\PROGRAMACION_ELSTER\\datos.accdb;')
cursor = conn.cursor()
cursor.execute(
    'select CUSTOMER_IDSERVICIO,MEDIDOR, PPAL_RESP, NOMBRE_CLIENTE, DIRECCION_IP from CLIENTES')
listado_ip = []
for row in cursor.fetchall():
    res = os.system('PING ' + row[4])
    if res == 0:
        listado_ip.append(
            (row[0] + '|' + row[1] + '|' + row[2] + '|' + row[3] + '|' + row[4] + '|OK'))
        os.system('cls')
        for datos in listado_ip:
            print(datos)
    else:
        listado_ip.append(
            (row[0] + '|' + row[1] + '|' + row[2] + '|' + row[3] + '|' + row[4] + '|PENDIENTE'))
        os.system('cls')
        for datos in listado_ip:
            print(datos)
