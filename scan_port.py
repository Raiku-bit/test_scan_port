import psutil
import time

def tranformar_mb(bytes_value):
    return round(bytes_value / (1024**2),2)

while True:
    #obtain global network statistics
    netword = psutil.net_io_counters()
    send_mb = tranformar_mb(netword.bytes_sent)
    received_mb = tranformar_mb(netword.bytes_recv)
    #Display Data
    print(f'Total Enviado: {send_mb} MB | Total Recibido: {received_mb} MB', end='\r')
    
    #conexion activated
    networkd_connections = psutil.net_connections()
    for connection in networkd_connections[:15]:
        laddr = f'{connection.laddr.ip}:{connection.laddr.port}'
        raddr = f'{connection.raddr.ip}:{connection.raddr.port}' if connection.raddr else "N/A"
        types = 'TCP' if connection.type == 1 else 'UDP'
        
        #Display Data       
        p, ip, port, st = 6, 22, 22, 15
        print(f"┌{'─'*p}┬{'─'*ip}┬{'─'*port}┬{'─'*st}┐")
        print(f"│ {'PROTO':<{p-1}}│ {'IP':<{ip-1}}│ {'PORT':<{port-1}}│ {'STATUS':<{st-1}}│")
        print(f"├{'─'*p}┼{'─'*ip}┼{'─'*port}┼{'─'*st}┤")
        print(f"│ {types:<{p-1}}│ {laddr:<{ip-1}}│ {raddr:<{port-1}}│ {connection.status:<{st-1}}│")
        print(f"└{'─'*p}┴{'─'*ip}┴{'─'*port}┴{'─'*st}┘")
    time.sleep(5)

    
