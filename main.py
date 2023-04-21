# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)] 
    heapq.heapify(threads) 
    
    for i in range(m):
        t = data[i]
        completion_time, thread_idx = heapq.heappop(threads)
        output.append((thread_idx, completion_time))
        heapq.heappush(threads, (completion_time + t, thread_idx))
    
    return output

def main():
   
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

  
    result = parallel_processing(n, m, data)
    
   
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()

