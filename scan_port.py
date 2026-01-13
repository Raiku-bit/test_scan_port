import psutil
import time

def tranformar_mb(bytes_value):
    return round(bytes_value / (1024**2),2)

while True:
    #obtain global network statistics
    netword = psutil.net_io_counters()
    
    send_mb = tranformar_mb(netword.bytes_sent)
    received_mb = tranformar_mb(netword.bytes_recv)
    #Display data
    print(f'Total Enviado: {send_mb} MB | Total Recibido: {received_mb} MB', end='\r')
    time.sleep(1)

    
