"""
asyncio 모듈은 async/await 구문을 통해 동시성 코드를 작성할 수 있게해주는 모듈이다.
단일 스레드 작업을 병렬로 처리할 수 있다. (python ver >= 3.7)
"""

import time
 
def sleep():
    time.sleep(1)
     
def sum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        sleep()
        total += number
        print(f"working {name}, number={number}, total={total}")
    end = time.time()
    print(f"worked={name}, time={end-start}")
    
    return total
    
def main():
    start = time.time()
    
    result1 = sum("A", [1, 2])
    result2 = sum("B", [1, 2, 3])
    
    end = time.time()
    
    print(f"total={result1+result2}, 총시간={end-start}")
    
if __name__ == "__main__":
    main()
    