#Jeremy Madrigal Portilla - 2019258245
#Randall Gabriel Zumbado Huertas - 2019082664
#Randy Conejo Juárez - 2019066448

#Se debe iniciar con super usuario antes de ejecutar este archivo

#Ejecutar comandos automatizados en la terminal
import subprocess



#DOCKER COMPOSE PARA GENERAR LAS MÁQUINAS
subprocess.run(['iptables', '-P', 'FORWARD', 'ACCEPT'])
subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up', '-d', '--build'])

#GENERA EL ROUTER 1
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'yum', '-y','install','iptables-services'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'systemctl', 'start','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'systemctl', 'start','ip6tables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'systemctl', 'enable','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'systemctl', 'enable','ip6tables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-F'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-t', 'nat' , '-A', 'POSTROUTING', '-s', '10.0.0.0/24', '-o', 'eth0','-j','MASQUERADE'])

#REGLAS DE IPTABLES ROUTER 1
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'OUTPUT' , '-p', 'udp', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '80', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'OUTPUT' , '-p', 'tcp', '-m', 'tcp', '--dport', '80', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '443', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'OUTPUT' , '-p', 'tcp', '-m', 'tcp', '--dport', '443', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '3128', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '8443', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '53', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'INPUT' , '-p', 'udp', '-m', 'udp', '--sport', '53', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'tcp', '--dport', '80', '-d', '10.0.0.20', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'tcp', '--dport', '443', '-d', '10.0.0.20', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'tcp', '--dport', '3128', '-d', '10.0.0.7', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'tcp', '--dport', '8443', '-d', '10.0.1.0', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'tcp', '--dport', '53', '-d', '10.0.0.3', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-A', 'FORWARD' , '-i', 'eth0', '-p', 'udp', '--dport', '53', '-d', '10.0.0.3', '-j', 'ACCEPT'])

#NATEO DESDE EL ROUTER 1 PARA EL ROUTER 2
subprocess.run(['docker', 'exec', '-it', 'docker_router1_1', 'iptables', '-t', 'nat' , '-A', 'POSTROUTING', '-s', '10.0.0.2', '-o', 'eth0','-j','MASQUERADE'])

#CONFIGURACIÓN DNS
subprocess.run(['docker', 'exec', '-it', 'docker_dns_1', 'route', 'add','default','gw','10.0.0.1'])
subprocess.run(['docker', 'exec', '-it', 'docker_dns_1', 'chgrp', 'named','/var/named/directa.lan01.io','/var/nameddirecta.lan02.io','/var/named/directa.google.com'])
subprocess.run(['docker', 'exec', '-it', 'docker_dns_1', 'systemctl', 'start','named'])
subprocess.run(['docker', 'exec', '-it', 'docker_dns_1', 'systemctl', 'enable','named'])
subprocess.run(['docker', 'exec', '-it', 'docker_dns_1', 'firewall-cmd', '--zone=public','--permanent','--add-service=dns'])

#CONFIGURACIÓN DHCP1
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp1_1', 'route', 'add','default','gw','10.0.0.1'])


#CONFIGURACIÓN PROXY_REVERSO
subprocess.run(['docker', 'exec', '-it', 'docker_proxy_reverso_1', 'route', 'add','default','gw','10.0.0.1'])

#CONFIGURACIÓN WEB_SERVER_1
subprocess.run(['docker', 'exec', '-it', 'docker_web_server_1_1', 'route', 'add','default','gw','10.0.0.1'])

#CONFIGURACIÓN WEB_CACHE
subprocess.run(['docker', 'exec', '-it', 'docker_web_cache_1', 'route', 'add','default','gw','10.0.0.1'])

#GENERA EL ROUTER 2
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'route', 'add','default','gw', '10.0.0.1'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'yum', '-y','install','iptables-services'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'systemctl', 'start','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'systemctl', 'start','ip6tables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'systemctl', 'enable','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'systemctl', 'enable','ip6tables'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-F'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-t', 'nat' , '-A', 'POSTROUTING', '-s', '10.0.1.0/24', '-o', 'eth0','-j','MASQUERADE'])

#REGLAS DE IPTABLES ROUTER 2
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-A', 'OUTPUT' , '-p', 'icmp', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '80', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-A', 'OUTPUT' , '-p', 'tcp', '-m', 'tcp', '--dport', '80', '-j', 'ACCEPT'])

subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-A', 'INPUT' , '-p', 'tcp', '-m', 'tcp', '--sport', '443', '-j', 'ACCEPT'])
subprocess.run(['docker', 'exec', '-it', 'docker_router2_1', 'iptables', '-A', 'OUTPUT' , '-p', 'tcp', '-m', 'tcp', '--dport', '443', '-j', 'ACCEPT'])


#CONFIGURACIÓN WEB_SERVER_2
subprocess.run(['docker', 'exec', '-it', 'docker_web_server_2_1', 'route', 'add','default','gw','10.0.1.1'])

#CONFIGURACIÓN DHCP2
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp2_1', 'route', 'add','default','gw','10.0.1.1'])

#GENERA VPN
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'route', 'add','default','gw','10.0.1.1'])
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'yum', '-y','install','iptables-services'])
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'systemctl', 'start','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'systemctl', 'start','ip6tables'])
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'systemctl', 'enable','iptables'])
subprocess.run(['docker', 'exec', '-it', 'docker_vpn_1', 'systemctl', 'enable','ip6tables'])

#DHCP 1 CONFIGURACIÓN
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp1_1', 'systemctl', 'start','dhcpd'])
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp1_1', 'systemctl', 'enable','dhcpd'])
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp1_1', 'systemctl', 'enable','dhcpd'])

#DHCP 2 CONFIGURACIÓN
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp2_1', 'systemctl', 'start','dhcpd'])
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp2_1', 'systemctl', 'enable','dhcpd'])
subprocess.run(['docker', 'exec', '-it', 'docker_dhcp2_1', 'systemctl', 'enable','dhcpd'])



#SE CREA EL CLIENTE 1
subprocess.run(['docker', 'build', '-t', 'cliente', '.'])
subprocess.run(['docker', 'run', '-itd', '--privileged', '--network=LAN_Virtual_1', '--name', 'cliente1', 'cliente'])
subprocess.run(['docker', 'exec', '-it', 'cliente1', 'dhclient','eth0'])
subprocess.run(['docker', 'exec', '-it', 'cliente1', 'ip','a','del','10.0.0.5/24','dev','eth0'])

#SE CREA EL CLIENTE 2
subprocess.run(['docker', 'run', '-itd', '--privileged', '--network=LAN_Virtual_2', '--name', 'cliente2', 'cliente'])
subprocess.run(['docker', 'exec', '-it', 'cliente2', 'dhclient','eth0'])
subprocess.run(['docker', 'exec', '-it', 'cliente2', 'ip','a','del','10.0.1.2/24','dev','eth0'])


