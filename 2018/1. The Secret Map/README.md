# 1. The Secret Map
Neo got the secret map which tells where the Frodo's nest egg. This secret map is encoded, so it is necessary to decode it. Luckily, there is a memo about how to decode the secret map.

1. The map is a n x n square, and each element consists of the blank(" ") or the wall("#").
2. There are two maps(named "map 1" and "map 2") which need to be piled up. For each element, it's a wall("#") if at least one element of map 1 or map 2 is a wall("#"), If both elements of map 1 and map 2 is a blank(" "), it's a blank(" ").
3. Both of map 1 and map 2 is encoded in the form of the integer array.
4. The encoded array is the array of the value of the binary number which is converted a wall("#") to 1, and a blank(" ") to 0 for each row of the square.

To help Neo get the Frodo's nest egg, develop the program decoding the secret map.

## input
A size of the secret map *n*, and two integer array *arr1*, *arr2*
- 1 <= *n* <= 16
- *arr1* and *arr2* are the arry of the integer where the length of *arr1*, and *arr2* is *n*.
- 0 <= *x* <= 2^n - 1

## output
The array of the string which consists of "#" and " ".

## example
1.
- *n* = 5
- *arr1* = [9, 20, 28, 18, 11]
- *arr2* = [30, 1, 21, 17, 28]
- output = [["#####", "# # #", "### #", "#  ##", "#####"]

2.
- *n* = 6
- *arr1* = [46, 33, 33, 22, 31, 50]
- *arr2* = [27, 56, 19, 14, 14, 10]
- output = ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
