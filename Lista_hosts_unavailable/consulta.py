# Código criado por Nathan Q. Silva
# O código tem o unico intuíto de conectar na API do zabbix 
# e trazer todos os hosts que estão acessíveis,
#
# Contato: contato@nathanqsilva.com.br
#
import apizabbix

api = apizabbix.connect()

hosts = api.host.get(
    output='extend',
    excludeSearch=False
)

print ("Lista de hosts sem comunicação:")

for host in hosts:
    available = host['available']
    if int(available) == 2:
        print(host['name'])

api.user.logout()