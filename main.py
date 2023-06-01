import heapq

def parallel_processing(n, m, data): #Define 3 parametrus n thread skaits m darbu skaits data saraksts ar apstrades laikiem
    output = [] # tuksu sarakstu
    threads = [(0, i) for i in range(n)] # katrs thread pienem index 0 
    heapq.heapify(threads) #parvers sarakstu par heap(priority list)
    
    for i in range(m):
        t = data[i]
        completion_time, thread_idx = heapq.heappop(threads) #panem mazako vertibu no heap nemainot rindas kartibu
        output.append((thread_idx, completion_time)) #pievieno output sarakstam threadu indeksu un laiku kad darbs tika uzsakts
        heapq.heappush(threads, (completion_time + t, thread_idx)) #pusho jaunako vertibu heapa
    
    return output #atgriez output sarakstu ar threada indexiem un saksanas laiku 

def main():
   
    n, m = map(int, input().split()) #split atlauj inputot vairkas vertibas
    data = list(map(int, input().split())) # izlasa darba procesu laiku un saglaba tos list(saraksta)

  
    result = parallel_processing(n, m, data) #izsauc parallel proccessing funkciju un saglaba to result 
    
   
    for thread_idx, start_time in result:
        print(thread_idx, start_time) #izprinte threada indeksu un sakuma laiku katram darbam

if __name__ == "__main__": #cheko vai pasreizejais kods tiek vadits ka galvenais kods. Ja vins tiek vadits ka galvenais kods tiek izsaukta main funkcija
    main()

