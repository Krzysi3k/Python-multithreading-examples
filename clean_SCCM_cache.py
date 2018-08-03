from os import path
import time
import glob
import shutil
import threading

# clean SCCM cache folders, perform cleanup in different threads

big_log = []
today = time.time()

def remove_sccm_cache(bos, time_stamp):
    sccm_dir = "\\\\%s\\C$\\Windows\\SysWOW64\\CCM\\Cache\\*" % bos
    all_folders = [f for f in glob.glob(sccm_dir) if path.isdir(f)]
    old_folders = [o for o in all_folders if path.getctime(o) < time_stamp]
    big_log.append(old_folders)
    for folder in old_folders:
        print(folder)
        shutil.rmtree(folder)

def main(days):
    time_stamp = today - (3600 * 24 * days)
    with open('C:\\testing\\multi_threading\\W8-PL.TXT', 'r') as boses:
        bos_machines = [b.strip() for b in boses]
    boses.close()
    threads = [threading.Thread(target=remove_sccm_cache, args=(bos, time_stamp)) for bos in bos_machines]
    [t.start() for t in threads]
    [t.join() for t in threads]
    with open('C:\\testing\\PY\\output.log', 'w') as logfile:
        for log in big_log:
            for line in log:
                logfile.write(line + '\n')
    logfile.close()


if __name__ == '__main__':
    day_num = 365
    main(day_num)
    print('time elapsed: ' + time.strftime('%H:%M:%S', time.gmtime(time.time() - today)))
