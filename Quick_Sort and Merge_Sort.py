import timeit
setup = """
def quick_sort( lst ) :
    if len ( lst ) > 1 :
        pivot = lst [ 0 ]
        left = quick_sort( [ i for i in lst[ 1 : ] if i < pivot ] )
        right = quick_sort( [ i for i in lst[ 1 : ] if i >= pivot ] )
        return left + [ pivot ] + right
    else:
        return lst
        
        
        
def merge_sort( lst ) :
    if len ( lst )  > 1 :
        result = []
        left = merge_sort( lst [ : len( lst ) // 2 ] )
        right = merge_sort( lst [ len( lst ) // 2 : ] )
        i = j = 0
        while i < len(left) and j < len(right):
            if left [ 0 ] < right [ 0 ]:
                result.append( left[ i ] )
                i += 1
            else:
                result.append( right[ i ] )
                j += 1
        result += left [ i : ]
        result += right [ j : ]
        return result
    else:
        return lst
    


import random
my_randoms0 = random.sample ( range ( 50 ), 10 )
my_randoms1 = random.sample ( range ( 500 ), 100 )
my_randoms2 = random.sample ( range ( 5000 ), 1000 )
my_randoms3 = random.sample ( range ( 50000 ), 10000 )
"""


t1 = timeit.Timer('quick_sort ( my_randoms0 )', setup=setup)
t2 = timeit.Timer('quick_sort ( my_randoms1 )', setup=setup)
t3 = timeit.Timer('quick_sort ( my_randoms2 )', setup=setup)
t4 = timeit.Timer('quick_sort ( my_randoms3 )', setup=setup)
print ('QuickSort time for 10 elements:', t1.timeit(5))
print ('QuickSort time for 100 elements:', t2.timeit(5))
print ('QuickSort time for 1000 elements:', t3.timeit(5))
print ('QuickSort time for 10000 elements:', t4.timeit(5))


t5 = timeit.Timer('merge_sort ( my_randoms0 )', setup=setup)
t6 = timeit.Timer('merge_sort ( my_randoms1 )', setup=setup)
t7 = timeit.Timer('merge_sort ( my_randoms2 )', setup=setup)
t8 = timeit.Timer('merge_sort ( my_randoms3 )', setup=setup)
print ('MergeSort time for 10 elements:', t5.timeit(5))
print ('MergeSort time for 100 elements:', t6.timeit(5))
print ('MergeSort time for 1000 elements:', t7.timeit(5))
print ('MergeSort time for 10000 elements:', t8.timeit(5))
