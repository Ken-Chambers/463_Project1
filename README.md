# An In-Depth Look into Hybrid Sorting Algorithms and Their Effectiveness


## Project Goals:
### To develop an algorithm that combines Insertion sort and Merge sort to effectively handle different lengths of data that gets inputted into it.
### Using this combination of algorithms, I plan to create a new algorithm that performs better than its components most of the time.
### From this experimentation, learn more about sorting algorithms and how to use them to be most effective because all sorting algorithms of a range of when they are most effective.

## Algorithm Description:
### By using both Insertion and Merge sort, I can create an algorithm which is good at dealing with data that is both short and long.
### The way that it works is it calls on either the Insertion sort or Merge sort function depending on what length of data is being loaded into the hybridSort
### If the length of the array that is inserted into the hybridSort function is less than 16, it uses Insertion sort but otherwise it uses Merge sort until this length of 16 threshold is hit, and then the algorithm switches back to the Insertion sort portion.


## Benchmarking Results:
### 500 Item length
| Test Number | insertionSort | mergeSort | hybridSort |
| ----------- | ------- | ------- | ------- |
| Test 1      | 0.004503726959228516    | 0.0010006427764892578    | 0.0010008811950683594    |
| Test 2      | 0.005003690719604492    | 0.0010008811950683594    | 0.0010006427764892578    |
| Test 3      | 0.005504608154296875    | 0.0010006427764892578    | 0.0010008811950683594    |
| Test 4      | 0.004503011703491211    | 0.001001119613647461     |  0.001001119613647461    |
| Test 5      | 0.004503726959228516    | 0.0010006427764892578    | 0.0010006427764892578    |


### 1000 Item length
| Test Number | insertionSort | mergeSort | hybridSort |
| ----------- | ------- | ------- | ------- |
| Test 1      | 0.02251911163330078    | 0.0020008087158203125    | 0.0020017623901367188    |
| Test 2      | 0.02101755142211914    | 0.0020017623901367188    | 0.001501321792602539    |
| Test 3      | 0.01951742172241211    | 0.0020017623901367188    | 0.0020017623901367188    |
| Test 4      | 0.022019624710083008    | 0.002001523971557617    | 0.002001523971557617    |
| Test 5      | 0.020517349243164062    | 0.0020017623901367188    | 0.0020008087158203125    |


## Numerical Discussion
### After running 10 total difference test (5 and 5 ) with randomized data set which had 500 items and items going from 1 to 10,000 and 1000 different numbers in it which ranged from 1 to 10,000, a result was decided based on the results on the data. In the end, it seems that my hybridSort was on par with mergeSort for the most part. When this wasn't the case however, mergeSort was slightly faster when compared to hybridSort. As for insertionSort however, it got completely blown out of the water between hybridSort and mergeSort. Going back to hybridSort vs mergeSort however, one thing to note about hybridSort is that it always used less memory when compared to mergeSort. During all of the tests, hybridSort only used 176 bytes of data in all of its tests, but when compared to the 560 bytes of data that mergeSort used in the second half of testing.

## Conclusion
### During all of the testing that I have ran in regards to the how well the 3 of these algorithms did when compared to each other and how we got to this point, one truth has been discovered: hybridSort ended being a great conbination of insertionSort and mergeSort. Although it didn't always beat out mergeSort, it took what makes both of these sorting algorithms great and combined them into a new sorting which has the speed and efficiency of mergeSort with the low memory costs of insertionSort along with how well it works with smaller data sets.







