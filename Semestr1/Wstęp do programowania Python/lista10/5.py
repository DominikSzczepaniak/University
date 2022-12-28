import more_itertools as mit
def partition2():
    lst = list(map(int, input().split()))
    for i in [podzial for ilosc in range(1, len(lst) + 1) for podzial in mit.set_partitions(lst, ilosc)]:
        yield sorted(i)
for i in partition2():
    print(i)
