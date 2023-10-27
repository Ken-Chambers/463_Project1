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
| Test Number | insertionSort | mergeSort | hybridSort |
| ----------- | ------- | ------- | ------- |
| Test 1      | 0.02251911163330078    | 0.0020008087158203125    | 0.0020017623901367188    |
| Test 2      | 0.02101755142211914    | 0.0020017623901367188    | 0.001501321792602539    |
| Test 3      | 0.01951742172241211    | 0.0020017623901367188    | 0.0020017623901367188    |
| Test 4      | 0.022019624710083008    | 0.002001523971557617    | 0.002001523971557617    |
| Test 5      | 0.020517349243164062    | 0.0020017623901367188    | 0.0020008087158203125    |
| Test 6      | 0.020517349243164062    | 0.0020020008087158203    | 0.0020017623901367188    |
| Test 7      | 0.02051854133605957    | 0.002001047134399414    | 0.0020003318786621094    |
| Test 8      | 0.020016908645629883    | 0.0015006065368652344    | 0.0020024776458740234    |
| Test 9      | 0.020517587661743164    | 0.0015010833740234375    | 0.0019049644470214844    |
| Test 10     | 0.02251911163330078    | 0.002002239227294922    | 0.0015027523040771484    |


## Numerical Discussion
### assdfgsd
