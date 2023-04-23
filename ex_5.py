import asyncio
import time

async def do_task(name, task_num, prep_time, def_time):
    print(f"{name} started the {task_num} task.")
    await asyncio.sleep(prep_time)
    print(f"{name} moved on to the defense of the {task_num} task.")
    await asyncio.sleep(def_time)
    print(f"{name} completed the {task_num} task.")

async def do_tasks(name, task_num, prep_time, def_time, rest_time):
    await do_task(name, task_num, prep_time, def_time)
    print(f"{name} is resting.")
    await asyncio.sleep(rest_time)

async def interviews(*applicants):
    tasks = []
    for name, task1_prep, task1_def, task2_prep, task2_def in applicants:
        tasks.append(do_tasks(name, 1, task1_prep, task1_def, task2_prep))
        await asyncio.gather(*tasks)
        tasks.append(do_tasks(name, 2, task2_prep, task2_def, 0))
        await asyncio.gather(*tasks)
