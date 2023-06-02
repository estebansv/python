from scapy.all import ARP, Ether, srp

# Define la dirección IP de la red local y la máscara de subred
network = '192.168.1.0/24'

# Crea una solicitud de ARP
arp = ARP(pdst=network)

# Crea una trama Ethernet
ether = Ether(dst='ff:ff:ff:ff:ff:ff')

# Combinamos la solicitud ARP y la trama Ethernet
packet = ether/arp

# Envía el paquete y obtiene la lista de respuestas
result = srp(packet, timeout=3, verbose=0)[0]

# Extrae las direcciones IP y MAC de los dispositivos conectados
devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

# Imprime la lista de dispositivos encontrados
print('Dispositivos conectados:')
for device in devices:
    print('  IP:', device['ip'], ' MAC:', device['mac'])

