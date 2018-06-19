import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

#1.loop会被放到future中
#2.取消future(task)
async def get_html(sleep_time):
    print("Waiting")
    await asyncio.sleep(sleep_time)
    print("done after {}s".format(sleep_time))

if __name__ == "__main__":
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)

    tasks = [task1,task2,task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("calcel")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
