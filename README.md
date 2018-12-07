# QUICKSORT AND MERGESORT REPORT
The aim of this report is to explain what has been done for this assignment.
Mergesort and quicksort are two algorithms, based on ‘divide and conquer’ strategy, that are used to sort provided lists of numbers.  I have tried to implement mergesort and quicksort functions, given in the slides. The main implementation I have thought is to write one function for mergesort and one for quicksort. 

# IN QUICKSORT
The first thing to do is to check if the given list has more than one element: if yes, the list has to be sorted; if not, the functions return the initial list, because there is no need of sorting it.
After checking that the list has more than one element, I choose a pivot element: in this case the first element of the given list. Therefore, I divide the initial list in two lists: all the elements smaller than the pivot go in the left list; all the elements larger or equal to the pivot go in the right one. Then the quicksort function has to be repeatedly applied to left and right lists because the two lists are not sorted yet: this means that left and right lists will be divided in two smaller lists, taking each time a new pivot as fixed element, until reaching one element per list, which is a list always sorted.                                      Finally, when all the left and right lists have been sorted, the function will return the larger left list, then put it together with the pivot and the larger right list.

# IN MERGESORT
The first thing to do is to check if the given list has more than one element: if yes, the list has to be sorted; if not, the functions return the initial list, because there is no need of sorting it.
After checking that the list has more than one element, the function split the unsorted initial list in two: a left and a right list. On both lists is repeatedly applied the mergesort function: this means that left and right lists will be splitted until reaching one element per list. Why so? Because a list of one element is always sorted. Then I initialize two variables, ‘i’ and ‘j’ that will be my indices for left and right lists, and a list ‘result’, my result list. Rather than iterating while one of the two, either left or right list, has elements, I iterate while both left and right list have elements. At the end of the loop, one of the two lists will be empty, but it can be either right or left: that is why I append them at the end of the result.      Therefore while both left and right are full, we compare elements in them: if the element of left list is smaller than the element of the right list, I append the smaller of the two to my result list: the element of left list; vice versa, if the element of right list is smaller than the element of the left list, I append the smaller of the two to my result list: the element of right list.  And then I increase my indices, ‘i’ and ‘j’, to make the function continues the iteration over all the elements present in the lists. Finally, when all the elements of the initial list have been added to my result list, the function will return it. The result list is the sorted version of my initial list.

# TIMEIT
The two functions need to be compared, in terms of performing time. To compare the performance of the two functions, I use them on random lists, made of 10, 100, 1000 and 10000 elements. To do so, I have to import ‘random’ package and use the ‘sample’ method to create the lists above mentioned, with a range bigger than the list length, in this case five times bigger. Then I have to import ‘timeit’ package and use the ‘Timer’ method. The Timer method needs two inputs: the string that contains the calling of the function on the desired list, and the setup, that is the statement to be executed once initially.  Finally I print the results and plot them.

# PLOT
To represent the result of the comparison between mergesort and quicksort functions, I need to plot the time periods obtained by running the above mentioned functions on random lists, made of 10, 100, 1000 and 10000 elements. The first thing to do is to import ‘matplotlib’ package: for simplification, I call it ‘plt’. Then I include the results of the previous step in two lists, to have a graphic representation for both functions. Then to have the graphs I use the ‘plot’ method, which takes one input, the numbers that have to be represented, and different default inputs that define characteristics of the graphs: I modify the line style, represented by a string, and the label of each graph. I put units on x axis, because the points of graphs have no indications about x coordinates. Then I labelled the x and y axis, which respectively represent the list length and the time, expressed in seconds. After that, I put a title to my plot and then insert the grid. In the end, I use the ‘show’ to visualize the complete plot.

# CONCLUSIONS
Quicksort is faster than mergesort. Mergesort uses extra space (requires a temporary array to merge the sorted lists), quicksort requires little space and an in-place sorting algorithm. In-place sorting means no additional storage space is needed to perform sorting. Actually they have the same average runtime: n*(log(n)); despite that, quicksort is considered better than mergesort.
