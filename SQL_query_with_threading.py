import time
import pyodbc
import threading

start_time = time.time()
query_output = []

def query_machine(machine):
    try:
        conn = pyodbc.connect('Driver={SQL Server};Server=%s,1444;Database=PMS;uid=pms;pwd=pms' % machine)
        cursor = conn.cursor()
        SQLCommand = """
            SELECT * FROM PMS__SETTING
            WHERE TAG = 'SITE_NAME_1'
            AND SVALUE NOT LIKE '%Circle%'
            """
        cursor.execute(SQLCommand)
        results = cursor.fetchall()
        for row in results:
            print(machine + ' ' + row[0] + ' ' + row[1])
            query_output.append(machine + ' ' + row[0] + ' ' + row[1])
        conn.close()
    except Exception as e:
        print('cannot connect to: %s error message: %s' % (machine, str(e)))

def main():
    file = "C:/testing/multi_threading/W8-PL.TXT"
    with open(file) as fp:
        machine_list = [line.strip() for line in fp]
    # create threads start them and wait for all to finish...
    threads = [threading.Thread(target=query_machine, args=(m,)) for m in machine_list]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print("dumping to file...")
    with open("C:/TEMP/query_result.log","w") as dump_log:
        [dump_log.write(item + "\n") for item in query_output]
        dump_log.write("row numbers: " + str(len(query_output)))
        dump_log.close()
    print("number of items: ",len(query_output))
    elapsed_time = time.time() - start_time
    print('time elapsed:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


if __name__ == '__main__':
    main()