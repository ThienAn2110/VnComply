"""
Quán phở đồng bộ:
1 nhân viên
phục vụ khách A ; Đợi xong khách A -> B
A gọi 1 phở -> Nhân viên nấu phở -> Phở xong -> Nhân viên mang phở cho A
phục vụ khách B ; Đợi xong khách B -> C
A -> B -> C -> ...
=> Sync(hronous)
chờ 10' -> 100'


Quán phở bất đồng bộ:
1 nhân viên
phục vụ khách A ; Đợi xong khách A -> B
A gọi 1 phở -> Nhân viên nấu phở (Giao việc cho bếp) -> Phở xong -> Nhân viên mang phở cho A
Trong lúc chờ phở A, nhân viên phục vụ khách B ; Đợi xong khách B -> C
=> Async(Asynchronous)
"""

#Async Await
import asyncio
import time

async def cook_pho(name, cook_time):
    print(f"{name} is ordering pho...")
    await asyncio.sleep(cook_time)
    print(f"{name}'s pho is ready!")
    return f"{name}'s pho"

async def serve_customer(name, cook_time):
    pho = await cook_pho(name, cook_time)
    print(f"Serving {pho} to {name}")
async def main():
    customers = [("Alice", 6), ("Bob", 1), ("Charlie", 0.5)]
    tasks = [serve_customer(name, cook_time) for name, cook_time in customers]
    await asyncio.gather(*tasks)
start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")








