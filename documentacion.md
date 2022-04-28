**Instituto Tecnológico de Costa Rica**

**Proyecto 1**

**Redes**

**Número de Grupo: 20**

Elaborado por:

Jeremy Madrigal Portilla - 2019258245

Randall Gabriel Zumbado Huertas - 2019082664

Randy Conejo Juárez - 2019066448

Profesor:

Gerardo Nereo Campos Araya

Alajuela, 29 de abril de 2022

## Instrucciones de ejecución

El proyecto fue implementado en un sistema Ubuntu 20.04, por lo que se
recomienda utilizar este sistema para replicar las instrucciones de
forma correcta.

Como primer paso instalamos Docker

`
  $ sudo apt install docker.io
`

También necesitamos instalar python

`
  $ sudo apt install python3
`

Ahora iniciamos Portainer, que es una interfaz gráfica para monitorear
los servicios que creemos con Docker-compose.

  ```
  $ sudo docker run -d -p 8000:8000 -p 9000:9000 \--name=portainer \--restart=always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer-ce
  ```

Instalamos también docker-compose

`  $ sudo apt install docker-compose
`

Abrimos nuestro navegador web de preferencia e ingresamos a
localhost:9000
![image19](https://user-images.githubusercontent.com/61055501/165863460-bfe00551-c8bd-4d07-a595-28ef80b109fa.png)



Aquí definimos una contraseña, tiene que ser de mínimo 8 caracteres.

Una vez definida ingresamos a Get Started
![image17](https://user-images.githubusercontent.com/61055501/165863502-8a45aa35-37c1-429f-ba34-c1655e7a7785.png)


Aquí seleccionamos local
![image20](https://user-images.githubusercontent.com/61055501/165863529-263b72fa-762b-4337-bdc6-d2aec2b3e78f.png)


Aquí nos saldrá el dashboard, donde podremos ver todos los contenedores
y redes que vayamos levantando.
![image6](https://user-images.githubusercontent.com/61055501/165863543-e679ead8-7061-4c7c-bbfa-f593008bce10.png)


Ahora entramos a la terminal y nos colocamos en la ruta del proyecto,
ingresamos como administrador.

  `
  $ sudo su
  `

Una vez ahí ejecutamos el script de python, con esto se construirán y
levantarán automáticamente los servicios definidos en el
docker-compose.yml.

  `
  $ python docker_run.py
  `

La primera vez que ejecutemos este script durará un rato pues tiene que
instalar las dependencias y aplicaciones necesarias en cada servicio
para realizar las pruebas, una vez terminado el script volvemos al
navegador y seleccionamos Containers y Networks, deberíamos poder ver
todos estos contenedores y redes levantadas y corriendo.
![image18](https://user-images.githubusercontent.com/61055501/165863617-6962092b-ed93-4b8d-9208-0e9048a3301c.png)

![image25](https://user-images.githubusercontent.com/61055501/165863622-24520241-fe26-4ee7-a19d-d6316a2c83a3.png)


Una vez llegados aquí el proyecto se levantó correctamente.

## Pruebas realizadas

Cabe recalcar que todas las máquinas virtuales usadas con docker corren
en un sistema operativo CentOS 7, exceptuando el proxy reverso y los web
servers externos, además una vez ejecutamos las pruebas de cada máquina
podemos utilizar el siguiente comando para salir de dicha máquina:

`  $ exit
  `
  
![image1](https://user-images.githubusercontent.com/61055501/165863668-4782021b-2eeb-4800-8695-2e9b5b5936d4.png)


### Router 1

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it docker_router1_1 /bin/bash
  `

Verificamos la IP del router 1 este contenido en la LAN \#1 y con la ip
10.0.0.1 con el siguiente comando:

  `
  $ ip a
  `
  
![image21](https://user-images.githubusercontent.com/61055501/165863878-8b605080-a1ed-46e2-ad2d-dc61e2fde36c.png)


Verificamos que haya conexión hacia internet por medio del siguiente
comando:

  `
  $ ping www.google.com
  `
  
![image5](https://user-images.githubusercontent.com/61055501/165863892-ff7489f8-5e1f-47c2-8e1c-682f2fe90b7d.png)


Verificamos la ruta por el cúal pasan los paquetes del router, en este
caso debería ir directo hacia el host y después a internet ya que el
router de la LAN \#1 se encuentra directamente conectado al host, para
probar esto utilizamos el siguiente comando:

  `
  $ traceroute www.google.com
  `
  
![image8](https://user-images.githubusercontent.com/61055501/165863915-acccc950-00a7-4f36-b89f-125f5a716276.png)


Verificamos las reglas del router, primero las reglas que creamos, para
esto ejecutamos el siguiente comando:

  `
  $ iptables -nL
  `
  
![image7](https://user-images.githubusercontent.com/61055501/165863948-5d5a22d2-b1cb-4a63-b2da-287343fdb52c.png)


Verificamos las reglas NAT del router ya que debería tener tanto una
conexión con todos los contenedores internos como un NAT hacia el router
de la LAN\#2, para esto ejecutamos el siguiente comando:

  `
  $ iptables -t nat -nL
  `
  
![image23](https://user-images.githubusercontent.com/61055501/165863980-730c3304-cab2-4cfd-925b-a45188e85135.png)


### Router 2

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
 $ docker exec -it docker_router2_1 /bin/bash
  `

Verificamos la IP del router 2 este contenido en la LAN \#2 y con la ip
10.0.1.1 además también deberá estar contenido en la LAN \#1 con la ip
10.0.0.2, verificamos con el siguiente comando:

  `
  $ ip a
  `

![image10](https://user-images.githubusercontent.com/61055501/165864039-526b4b7d-9317-4774-8edc-1537120cfda9.png)


Verificamos que haya conexión hacia internet por medio del siguiente
comando:

  `
  $ ping www.google.com
  `

![image16](https://user-images.githubusercontent.com/61055501/165864063-9e3af010-22f3-43f6-b05c-3b2efb61584f.png)


Verificamos la ruta por el cúal pasan los paquetes del router, en este
caso debería ir directo hacia el router en la LAN \#1 y después a
internet ya que el router de la LAN \#2, para probar esto utilizamos el
siguiente comando:

  `
  $ traceroute www.google.com
  `

![image24](https://user-images.githubusercontent.com/61055501/165864083-205585a0-152b-447f-b1e7-f2fa7d166d5c.png)


Verificamos las reglas del router, primero las reglas que creamos, para
esto ejecutamos el siguiente comando:

  `
  $ iptables -nL
  `

![image3](https://user-images.githubusercontent.com/61055501/165864107-0dc146dd-41b2-495b-af5a-0136933f8fcd.png)


Verificamos las reglas NAT del router ya que debería tener una conexión
con todos los contenedores internos, para esto ejecutamos el siguiente
comando:

  `
  $ iptables -t nat -nL
  `

![image14](https://user-images.githubusercontent.com/61055501/165864125-889e34b9-afd5-4b37-bde3-e136e8c3431e.png)


### DHCP1

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it docker_dhcp1_1 /bin/bash
  `

Para verificar que nuestro DHCP1 se encuentra configurado y encendido
utilizamos el siguiente comando:

  `
  $ systemctl status dhcpd
  `

![image12](https://user-images.githubusercontent.com/61055501/165864183-efd59b26-caed-4c15-843d-ab6da12174c1.png)


### DHCP 2

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it docker_dhcp2_1 /bin/bash
  `

Para verificar que nuestro DHCP 2 se encuentra configurado y encendido
utilizamos el siguiente comando:

  `
  $ systemctl status dhcpd
  `

![image15](https://user-images.githubusercontent.com/61055501/165864224-f8742387-3743-48f9-99a0-163a230a92ef.png)


### DNS

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it docker_dns_1 /bin/bash
  `

Para verificar que nuestro DNS se encuentra configurado y encendido
utilizamos el siguiente comando:

  `
  $ systemctl status named
  `

![image22](https://user-images.githubusercontent.com/61055501/165864250-694e325c-d777-40cd-88d0-1b2128d281e4.png)


### Cliente 1 - DNS

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it cliente1 /bin/bash
  `

Verificamos que el DHCP haya asignado correctamente el DNS hacia nuestra
máquina cliente de la LAN\#1, lo que veremos es la ip de nuestro
servidor DNS, para esto ejecutamos el siguiente comando:

  `
  $ nslookup
  `

  `
  \>server
  `

![image9](https://user-images.githubusercontent.com/61055501/165864299-3ca9188f-aff0-4630-be67-6a56759171b3.png)


### Cliente 1 - DHCP

En la misma máquina que nos encontramos vamos a verificar la ip que nos
asignó nuestro servidor dhcp en este caso el que se encuentra en la
LAN\#1, para esto ejecutamos el siguiente comando:

  `
  $ ip a
  `
  
![image11](https://user-images.githubusercontent.com/61055501/165864327-06e97862-8b70-4353-92c6-b4d162d3bf8b.png)


### Cliente 2 - DNS

Ejecutamos como super usuario en una terminal el siguiente comando:

  `
  $ docker exec -it cliente2 /bin/bash
  `

Verificamos que el DHCP haya asignado correctamente el DNS hacia nuestra
máquina cliente de la LAN\#1, lo que veremos es la ip de nuestro
servidor DNS, para esto ejecutamos el siguiente comando:

  `
  $ nslookup
  `

  `
  \>server
  `

![image9](https://user-images.githubusercontent.com/61055501/165864370-348a058b-5823-41b2-982b-1c6e7bbf82be.png)


### Cliente 2 - DHCP

En la misma máquina que nos encontramos vamos a verificar la ip que nos
asignó nuestro servidor dhcp en este caso el que se encuentra en la
LAN\#2, para esto ejecutamos el siguiente comando:

  `
  $ ip a
  `

![image4](https://user-images.githubusercontent.com/61055501/165864396-e2831aac-fa26-4610-9d45-b7a149a665bc.png)


### Proxy reverso y Web Servers

Entramos al navegador web e ingresamos a localhost/web1, deberíamos ver
la siguiente página, que corresponde al Web Server 1.


![image2](https://user-images.githubusercontent.com/61055501/165864414-b163f02e-71bf-426d-a083-b05b703a803c.png)


Si ahora ingresamos a localhost/web2, deberíamos ver la siguiente
página, que corresponde al Web Server 2.

![image13](https://user-images.githubusercontent.com/61055501/165864427-25cc3456-f23e-4f84-b6e9-1bf5debcf458.png)


## Conclusiones

-   Se concluye que existen bibliotecas libres (iptables, bind,
    named...) que ayudan a poder configurar servicios como el router,
    dhcp, dns, entre muchos otros.

-   Se puede concluir que a lo largo de la realización de todo el
    proyecto, se adquirió un amplio conocimiento en cuanto a los
    servicios que contiene un red y cómo estas conexiones ocurren
    entre los sistemas.

-   Se concluye que la automatización es fundamental para poder realizar
    las configuraciones de los servicios del proyecto, esto ayudará a
    que se ejecuten todas y poder por medio de un comando una red
    configurada.

-   Se concluye que se pudo aprender gran parte en la administración de
    máquinas virtuales y como docker complementa esto para poder
    generar varias, ayudando a poder realizar redes como la creada en
    este proyecto como a poder ejecutar varias máquinas y realizar
    pruebas internamente.

-   Se concluye que aunque no se haya completado satisfactoriamente
    todos los puntos del proyecto, se pudo tener experiencia en
    herramientas nuevas para nosotros y tener un primer acercamiento a
    cómo se realizan las configuraciones internas dándonos una visión
    de esta.

-   Se concluye que las redes en general son importantes a la hora de
    poder crear conexiones y a su vez tener comunicación entre
    diferentes dispositivos para poder transmitir información entre
    varias partes, esto aplica tanto para dispositivos en una misma
    zona como en zonas muy lejanas, permitiendo la globalización.

-   Se concluye que los router en su gran parte permiten o deniegan
    diferentes paquetes, además pueden convertir estos paquetes para
    poder enviarlos hacia el exterior (internet) esto permite que se
    pueda crear seguridad y administrar que es lo que queremos recibir
    además de poder controlar los datos que envía nuestra computadora.

-   Se puede concluir que el DHCP permite nombrar equipos en este caso
    para una LAN, este nombramiento se da con base a una IP que es
    como identificar un equipo en una red, esto permite poder
    administrar y dar conexión a los diferentes equipos que se
    conecten en una misma lan e identificarlos.

-   Se concluye que el DNS permite el nombramiento y direccionamiento de
    algún equipo en particular hacia una ip por medio de nombres,
    igualmente se aprendió cómo se puede administrar un DNS interno y
    poder realizar nombramiento hacia otras ips tanto internas como
    externas.

-   Se puede concluir que el proxy reverso es una medida de seguridad
    para poder evitar una excesiva carga de clientes que quieran
    acceder a los servidores, permitiendo dividir la carga de acceso a
    los servidores.

## Recomendaciones

-   Se recomienda realizar el proyecto en el sistema operativo Ubuntu
    20.04, tomando este como host para docker.

-   Se recomienda utilizar docker-compose para automatizar la creación
    de servicios.

-   Se recomienda utilizar el driver macvlan en las redes, ya que este
    establece un gateway por defecto, y permite setear un gateway a
    los demás servicios hacia el router.

-   Para web servers sencillos, se recomienda utilizar la imagen
    python:3.7-alpine y utilizar la biblioteca Flask para enviar el
    html al puerto determinado.

-   Se recomienda la instalación de Portainer, de esta forma podemos ver
    de manera gráfica que está pasando con nuestros contenedores y
    redes, y manejarlos sencillamente.

-   Para los routers se recomienda utilizar la imagen de CentOS:7, dado
    que es muy ligera y estable.

-   Para el proxy reverso se recomienda utilizar la imagen de
    nginx:1.17.10, dado que esta cuenta con páginas web en caso de
    respuestas 404 Not Found y errores internos.

-   Para mayor seguridad en las conexiones, se recomienda utilizar
    iptables para denegar todos los servicios, y solo dejar activos
    los necesarios para el funcionamiento correcto de toda la red, de
    esta manera evitamos el uso indebido de los servicios.

-   Se recomienda utilizar traceroute para asegurar que los paquetes
    enviados están viajando y siguiendo el camino de servicios que
    debería seguir.

-   Se recomienda el uso de archivos de configuración .dockerfile, para
    que cuando se estén creando los servicios sigan todas las reglas.

## Bibliografía

Anicas, M. (2021, 9 julio). *Iptables Essentials: Common Firewall Rules
and Commands*. DigitalOcean Community. Recuperado 18 de abril de 2022,
de
https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands

Atienza -, J., -, I., Atienza -, J., Content -, S., Atienza -, J.,
Atienza -, J., Upadhyay -, R., -, I., Atienza -, J., & Content -, S.
(2022, 11 febrero). *Setting Up DNS Server On CentOS 7 \| Install DNS
Server On CentOS 7*. Unixmen. Recuperado 20 de abril de 2022, de
https://www.unixmen.com/setting-dns-server-centos-7/

Docker. (s. f.). *Docker Hub*. Hub.Docker. Recuperado 10 de abril de
2022, de
https://hub.docker.com/

Docker. (s. f.). *Overview of Docker Compose*. Docker Documentation.
Recuperado 10 de abril de 2022, de
https://docs.docker.com/compose/

Doyle. (2020, May 11). *Docker and Nginx Reverse Proxy* \[Video\].
Youtube.
https://www.youtube.com/watch?v=hxngRDmHTM0

Systemas, S. (2018, 3 diciembre). *Cómo configurar DHCP Servidor y
Cliente en CentOS 7 o Ubuntu 18.04*. Solvetic. Recuperado 18 de abril de
2022, de
https://www.solvetic.com/tutoriales/article/6456-como-configurar-dhcp-servidor-y-cliente-en-centos-7-o-ubuntu-1804/
