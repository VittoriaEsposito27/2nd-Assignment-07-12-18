import timeit
setup = """
def merge_sort( lst ) :
    if len ( lst ) > 1 :
         left = merge_sort( lst [ 0 : len( lst ) // 2 ] )
         right = merge_sort( lst [ len( lst ) // 2 : ] )
         lst = []
         while len ( left ) > 0 and len ( right ) > 0 :
            if left [ 0 ] <= right [ 0 ] :
                 lst.append ( left.pop( 0 ) )
            else :
                 lst.append ( right.pop( 0 ) )
         while len ( left ) > 0 :
            lst.append ( left.pop( 0 ) )
         while len ( right ) > 0 :
            lst.append ( right.pop( 0 ) )
         return lst
    else:
         return lst
    

def quick_sort( lst ) :
    if len ( lst ) > 1 :
        pivot = lst [ 0 ]
        left = [i for i in lst[1:] if i < pivot ]
        right = [i for i in lst[1:] if i >= pivot ]
        return quick_sort ( left ) + [ pivot ] + quick_sort ( right )
    else:
        return lst

import random
my_randoms0 = random.sample ( range ( 50 ), 10 )
my_randoms1 = random.sample ( range ( 500 ), 100 )
my_randoms2 = random.sample ( range ( 5000 ), 1000 )
my_randoms3 = random.sample ( range ( 50000 ), 10000 )
"""


t0 = timeit.Timer('quick_sort ( my_randoms0 )', setup=setup)
t1 = timeit.Timer('quick_sort ( my_randoms1 )', setup=setup)
t2 = timeit.Timer('quick_sort ( my_randoms2 )', setup=setup)
t3 = timeit.Timer('quick_sort ( my_randoms3 )', setup=setup)
print ('QuickSort time:', t0.timeit(5))
print ('QuickSort time:', t1.timeit(5))
print ('QuickSort time:', t2.timeit(5))
print ('QuickSort time:', t3.timeit(5))


t4 = timeit.Timer('merge_sort ( my_randoms0 )', setup=setup)
t5 = timeit.Timer('merge_sort ( my_randoms1 )', setup=setup)
t6 = timeit.Timer('merge_sort ( my_randoms2 )', setup=setup)
t7 = timeit.Timer('merge_sort ( my_randoms3 )', setup=setup)
print ('MergeSort time:', t4.timeit(5))
print ('MergeSort time:', t5.timeit(5))
print ('MergeSort time:', t6.timeit(5))
print ('MergeSort time:', t7.timeit(5))
