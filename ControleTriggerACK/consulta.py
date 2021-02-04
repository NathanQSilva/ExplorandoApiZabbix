from pyzabbix import ZabbixAPI
import pprint

server =  #input("Digite seu servidor: ")
user =  #input("Digite seu usuário: ")
password =  #input("Digite sua senha: ")

zapi = ZabbixAPI(server)
zapi.login(user, password)

alerts = zapi.event.get(
    output= 'extend',
    #excludeSearch=True,
    #search='704245'
)

pprint.pprint(alerts)

zapi.user.logout()