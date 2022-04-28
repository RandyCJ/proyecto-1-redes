FROM centos:7
ENV container docker
RUN yum -y update; yum clean all
RUN yum -y install systemd; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
RUN yum -y install traceroute;
RUN yum -y install net-tools;
RUN yum -y install iproute;
RUN yum -y install nano;
RUN yum -y install dhcp;
RUN yum -y install firewalld;
RUN yum -y install bind bind-utils;
COPY named.conf /etc/named.conf

RUN cat /dev/null > /var/named/directa.lan01.io;
RUN cat /dev/null > /var/named/directa.lan02.io;
RUN cat /dev/null > /var/named/directa.google.com;

COPY directa.lan01.io /var/named/directa.lan01.io
COPY directa.lan02.io /var/named/directa.lan02.io
COPY directa.google.com /var/named/directa.google.com

RUN cat /dev/null > /etc/resolv.conf;
RUN echo 'search localdomain lan01.io' >> /etc/resolv.conf ;
RUN echo 'search localdomain lan02.io' >> /etc/resolv.conf;
RUN echo 'search localdomain google.com' >> /etc/resolv.conf;
RUN echo 'nameserver 10.0.0.3' >> /etc/resolv.conf;
RUN echo '10.0.0.3 srvcentos.lan01.io' >> /etc/hosts;
RUN echo '10.0.0.3 srvcentos.lan02.io' >> /etc/hosts;
RUN echo '10.0.0.3 srvcentos.google.com' >> /etc/hosts;

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]