from heapq import heappush,heappop,heapify

listoflist = [[10,15,30],[12,15,30],[17,20,32]]

flat_list = [l for lst in listoflist for l in lst]

print(flat_list)


heap = [(lst[0],i,0) for i,lst in enumerate(listoflist) if lst]

heapify(heap)
print(heap)
heap =[]

for item in flat_list:
    heappush(heap,item)


mergedsortedlist = []
while heap:   
    mergedsortedlist.append(heappop(heap))

print(mergedsortedlist)

# Using iteration:

def merge(listoflist):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(listoflist) if lst]
    heapify(heap)

    while heap:
        val, list_ind, element_ind = heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(listoflist[list_ind]):
            next_tuple = (listoflist[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heappush(heap, next_tuple)
    return merged_list

print('merge result')
print(merge(listoflist))