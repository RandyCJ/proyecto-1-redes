$TTL 3H
@     IN SOA @ srvcentos.lan02.io. (
                                      0       ; serial
                                      1D      ; refresh
                                      1H      ; retry
                                      1W      ; expire
                                      3H )    ; minimum
               NS     srvcentos.lan02.io.
srvcentos      A      10.0.0.3
@              A      10.0.0.3
www            CNAME  srvcentos
web            CNAME  srvcentos
ftp            CNAME  srvcentos