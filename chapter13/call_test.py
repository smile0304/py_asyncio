import asyncio
def callback(sleep_times):
    print("sleep {} success".format(sleep_times))

def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    #loop.call_soon(callback,2)
    #loop.call_soon(stoploop, loop)
    loop.call_at(now+2,callback,2)
    loop.call_later(2,callback,2)
    loop.call_later(1,callback,1)
    loop.call_later(3,callback,3)
    loop.call_soon(callback,4)
    loop.run_forever()
