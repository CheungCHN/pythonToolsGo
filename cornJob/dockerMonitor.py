#-*- coding: UTF-8 -*-
import os
import threading
import time
import socket
import subprocess
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')
                   
def isOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def startDocker():
    if isOpen('127.0.0.1',8080):
        logging.info('    Docker Is Run')
        # logging.info('    当前线程数为{}'.format(threading.activeCount()))

    else: 
        logging.info('    Docker Is Down')
        try:
            subprocess.run(['ls', '-l'], cwd='/root')
            # subprocess.run(['docker-compose', 'down'], cwd='/root/docker')
            # subprocess.run(['docker-compose', 'up', '-d'], cwd='/root/docker')
            logging.info('    Creat Docker OK～ @@@休眠30min')
        except Exception as r:
            logging.error('    ' + str(r))
        time.sleep(10)

if __name__ == '__main__':
    logging.info('    Program Start')
    while True: 
        timer = threading.Timer(10, startDocker)
        # logging.info('当前线程数为{}'.format(threading.activeCount()))
        timer.start()
        timer.join()
        # logging.info('    after join')