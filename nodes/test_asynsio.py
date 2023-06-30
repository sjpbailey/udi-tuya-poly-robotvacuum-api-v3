import asyncio
import time

# Python 3.5
async def some_coroutine(*some_args, loop=None):
    while True:
        starttime = time.time()
        print("tick_tock")
        #self.SwStat(self)
        time.sleep(5 - ((time.time() - starttime) % 5))
        
        #[...]
        #result = await loop.run_in_executor(
        #    None,  # Use the default executor
        #    some_blocking_io_call, 
        #    *some_args)
        #[...]
    await print('ok')



loop = asyncio.get_event_loop()
coro = some_coroutine(loop=loop)
loop.run_until_complete(coro)
