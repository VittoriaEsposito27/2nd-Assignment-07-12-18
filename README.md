# QUICKSORT AND MERGESORT REPORT
# I have tried to implement mergesort and quicksort functions, given in the slides. The main implementation is to write one single function for both mergesort and quicksort. In both cases, the first thing to do is to check if the given list has more than one element: if yes, the list has to be sorted; if not, the functions return the initial list.
# IN QUICKSORT
# After checking that the list has more than one element, I choose a pivot element: in this case the first element of the given list. So I divide the initial list in two lists: in the left list go all the elements smaller than the pivot; in the right one, all the elements larger or equal to the pivot. Then the quicksort function has to be recursively applied to left and right lists: the two lists are not sorted yet: this means that left and right lists will be divided until reaching one element per list.                                      Finally, when the initial list is sorted, the function will return it.
# IN MERGESORT
# After checking that the list has more than one element, the function split the initial list in two: a left and a right list. On both lists is recursively applied the mergesort function: this means that left and right lists will be splitted until reaching one element per list.                                                                                                                                      Then I initialize two variables, ‘i’ and ‘j’ that will be my indices for left and right lists, and a list ‘result’, my result list. Rather than iterating while one of the two,  either left or right, has elements, I iterate while both left and right have elements. At the end of the loop, one of the two lists will be empty, but it can be either right or left: that is why I append them at the end of the result.      So while both left and right are full, we compare elements in them: if the element of left list is smaller than the element of the right list, I append the smaller of the two: the element of left list; vice versa, if the element of right list is smaller than the element of the left list, I append the smaller of the two: the element of right list.  And then I increase my indices, ‘i’ and ‘j’, to make the function continue the iteration over all the elements present in the lists. Finally, when the initial list is sorted, the function return the result list, that is the sorted initial list.
# TIMEIT
# The two functions need to be compared, in terms of performing time. I want to compare the performance of the two functions on random lists, made of 10, 100, 1000 and 10000 elements. I’ve imported random package and used the method random.sample() to create the lists above mentioned, with a range five times bigger than the list length. Then I’ve imported timeit package and used the method timeit.Timer(). The Timer method needs two inputs: the string, that contains the calling of the function on the desired list, and the setup, that is the statement to be executed once initially.  Finally I print the results and plot them.
# CONCLUSIONS
# Quicksort is faster than mergesort.
# Mergesort needs in total n*log(n) comparisons.
# Quicksort needs in total ∑[n*(n-1)]/2 comparisons, if the smallest or largest value are chosen as pivot; but if the pivot is the median, the number of comparisons is the same as mergesort, n*log(n).
