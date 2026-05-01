import asyncio
import time


# -------- 同步 ----------
def make_coffee(customer: str) -> None:
    print(f"开始为 {customer} 煮咖啡...")
    time.sleep(5)
    print(f"{customer} 的咖啡好了")


def main_sync():
    start_time = time.time()
    make_coffee("顾客A")
    make_coffee("顾客B")
    make_coffee("顾客C")
    end_time = time.time()
    print(f"同步方式总耗时：{end_time - start_time}")


# -------- 异步 ----------
async def make_coffee_async(customer: str) -> str:
    print(f"开始为 {customer} 煮咖啡...")
    await asyncio.sleep(5)
    print(f"{customer} 的咖啡煮好了")
    return f"{customer} 的咖啡"


async def main_async():
    start_time = time.time()

    # 创建任务清单
    tasks = [
        make_coffee_async("顾客A"),
        make_coffee_async("顾客B"),
        make_coffee_async("顾客C"),
    ]
    results = await asyncio.gather(*tasks)
    print("所有咖啡都准备好了：", results)

    end_time = time.time()
    print(f"异步方式总耗时：{end_time - start_time}")


if __name__ == "__main__":
    # main_sync()
    asyncio.run(main_async())
