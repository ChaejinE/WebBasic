"""
asyncio 모듈은 async/await 구문을 통해 동시성 코드를 작성할 수 있게해주는 모듈이다.
단일 스레드 작업을 병렬로 처리할 수 있다. (python ver >= 3.7)
비동기와 동기의 실행시간을 비교해보자
"""

import asyncio
import time

# 함수앞에 async 문자을 삽입하면 딘다. (비동기 함수 만들기 -> 이를 코루틴이라고 부른다.)
async def sleep():
    # 코루틴 안의 함수에서 또다른 코루틴을 부르기 위해서는 await co-routine으로 호출해야한다.
    # 코루틴 수행 중 코루틴을 만나면 await으로 호출한 코루틴이 종료될 때 까지 기다리지 않고,
    # 메인 스레드나 다른 코루틴으로 넘긴다. (Non-blocking)
    # 호출한 코루틴이 종료되면 이벤트에 의해 다시 그 이후 작업이 수행된다.
    # time.time()은 코루틴이 아니므로 코루틴의 sleep을 호출한다.
    await asyncio.sleep(1)
    
async def sum(name, numbers):
    start = time.time()
    total = 0
    
    for number in numbers:
        await sleep()
        total += number
        print(f"working {name}, number={number}, total={total}")
    end = time.time()
    print(f"worked={name}, time={end-start}")
    
    return total

async def main():
    start = time.time()
    
    # 코루틴 작업을 생성한다.
    # 코루틴 작업이 생성될 뿐, 코루틴이 수행되는 것은 아니다.
    # 코루틴을 동시에 시작하기 위해 필요한 작업이다.
    task1 = asyncio.create_task(sum("A", [1, 2]))
    task2 = asyncio.create_task(sum("B", [1, 2, 3]))
    
    # 코루틴의 수행은 await Task에 의해 실행된다.
    await task1
    await task2
    
    # 코루틴의 수행 결과는 .result()로 얻을 수 있다.
    result1 = task1.result()
    result2 = task2.result()
    
    end = time.time()
    
    print(f"total={result1+result2}, 총시간={end-start}")
    
if __name__ == "__main__":
    # run loop을 생성해서 main 코루틴을 실행한다.
    # 코루틴 실행하기 위해서 런 루프가 반드시 필요하다.
    # 코루틴 모두 비동기적으로 실행되므로 그 시작과 종료를 감지할 수 있는 이벤트 루프는
    # 반드시 필요하기 때문이다.
    asyncio.run(main())
    
    """
    https://docs.python.org/ko/3/library/asyncio.html
    https://docs.python.org/ko/3/library/asyncio-task.html
    """