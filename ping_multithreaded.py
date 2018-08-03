import subprocess
import time
import threading

start_time = time.time()
print('started: ', time.strftime("%X", time.localtime(start_time)))


def ping_machines(hostname):
    state = ''
    for i in range(0,4):
        ping_request = subprocess.call(['ping', '-n', '1', hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ping_request == 0:
            state = 'ping ok'
            break
        else:
            state = 'request timed out'
    print(hostname + " " + state)

def main():
    with open("C:/testing/multi_threading/W8-PL.TXT") as files:
        new_list = [line.strip() for line in files]
        for i in new_list:
            threading.Thread(target=ping_machines, args=(i,)).start()


if __name__ == '__main__':
    thread_counter = threading.active_count()
    main()
    while threading.active_count() > thread_counter:
        time.sleep(0.1)
    ended_time = time.time()
    elapsed_time = ended_time - start_time
    print('elapsed time: ', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
