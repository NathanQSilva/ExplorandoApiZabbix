# Código criado por Nathan Q. Silva
# O código tem o unico intuíto de conectar na API do zabbix 
# e trazer todos os hosts que estão acessíveis,
#
# Contato: contato@nathanqsilva.com.br
#

import apizabbix
from pprint import pprint

api = apizabbix.connect()

groups = api.hostgroup.get(
    output='extend',
    excludeSearch=True,
    search={
        'name': 'Templates'
    },
    selectHosts=[
        'name',
        'host',
        'available'
    ]
)

hosts = api.host.get(
    output='extend',
    excludeSearch=False
)

print("GRUPO;AVAILABLE;NOT AVAILABLE;UNKNOWN")

for group in groups:
    Available = 0
    NotAvailable = 0
    Unknown = 0
    
    for host in group['hosts']:
        AvailableStatus = host['available']
        if AvailableStatus == '0':
            Unknown+=1
        if AvailableStatus == '1':
            Available+=1
        if AvailableStatus == '2':
            NotAvailable+=1
    
    print(group['name']+";"+str(Available)+";"+str(NotAvailable)+";"+str(Unknown))
    
api.user.logout()
q