import nmap

# Crea un objeto nmap
nm = nmap.PortScanner()

# Escanea la red local para buscar dispositivos conectados
nm.scan(hosts='192.168.1.0/24', arguments='-n -sP')

# Imprime los dispositivos encontrados
for host in nm.all_hosts():
    if 'mac' in nm[host]['addresses']:
        print('Dispositivo:', nm[host]['addresses']['ipv4'], nm[host]['vendor'][nm[host]['addresses']['mac']])
    else:
        print('Dispositivo:', nm[host]['addresses']['ipv4'])

