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
RUN echo 'DHCPDARGS="eth0"' >> /etc/sysconfig/dhcp;
COPY dhcpd2.conf /etc/dhcp/dhcpd.conf

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]