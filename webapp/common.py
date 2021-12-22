import time
import asyncio


async def measure(coro, ref):
    t_start = time.time()
    print(f'{ref} start: {t_start:.2f}')
    result = await coro
    t_end = time.time()
    print(f'{ref} end: {t_end:.2f} | diff: {t_end - t_start:.2f}')
    return result


async def multitask(func, n):
    tasks = []
    for i in range(n):
        coro = func(i)
        task = asyncio.create_task(coro)
        tasks.append(task)
    return await asyncio.wait(tasks)
