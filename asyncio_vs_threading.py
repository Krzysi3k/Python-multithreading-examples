# performance comparison between asyncio and multithreading

import time

def async_example():
    import asyncio
    import random

    async def myCoroutine(id):
        process_time = random.randint(1,5)
        await asyncio.sleep(process_time)
        print("Coroutine: {}, has successfully completed after {} seconds".format(id, process_time))

    async def main():
        tasks = [asyncio.ensure_future(myCoroutine(i)) for i in range(50)]
        await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()


def multithreading_example():
    import threading
    import random

    def threadCoroutine(id):
        process_time = random.randint(1,5)
        time.sleep(process_time)
        print("Coroutine: {}, has successfully completed after {} seconds".format(id, process_time))

    def thread_main():
        threads = [threading.Thread(target=threadCoroutine, args=(i,)) for i in range(50)]
        [t.start() for t in threads]
        [t.join() for t in threads]

    thread_main()



if __name__ == '__main__':
    t1 = time.time()
    multithreading_example()
    finished_threading = time.time()
    t2 = time.time()
    async_example()
    finished_async = time.time()
    print("multithreading finished in:",time.strftime("%H:%M:%S", time.gmtime(finished_threading - t1)))
    print("async finished in:", time.strftime("%H:%M:%S", time.gmtime(finished_async - t2)))


