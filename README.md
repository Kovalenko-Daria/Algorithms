# Algorithms

## About
This is the implementation of simple algorithms using python with testing on a variety of input data.
***

## Algorithms

* _Sieve of Eratosthenes_<br>
The input data is a natural number greater than one. The function uses an algorithm to search for prime numbers from 2 to a given number inclusive and returns an array with them. In case of an input error, returns an error message.


* _Cycle shift_<br>
The input data is an array and integer. The function performs a shift to the left with a positive parameter n and a shift to the right if a negative number is passed. Returns modified array. In case of an input error, returns an error message.

* _Binary search_<br>
The input data is the minimum and maximum values at which the hidden number can be found. The function outputs a possible number, after which it expects a comment from the user, regardless of whether it is "Greater" or "Less" than the guessed one. Guessing continues until the user enters the phrase "Got it!" Doesn't return anything.

* _Sort_<br>
This file consists of 5 sorts, including insert sort, choice sort, bubble sort, fast sort, merge sort. Each of the sorts receives an unsorted array of numbers as an input value, and returns an array sorted in ascending order.

* _Generation of sequences_<br>
This file contains function which generates placements with repetitions and function which generates permutations without repetitions. Each of them receives an array of values as well as length of one combination and saves arrays with sequences in global array called "place".

* _Check of bracket sequences_<br>
This file contains a function that accepts a string with a bracket sequence of three types of brackets - (), {}, [] - as input and checks correctness of the bracket expression. In case of correctness, the Truth is returned, otherwise - False.

* _Subsequences_<br>
This file contains two functions that work with subsequences. The first one looks for the largest common subsequence of two sequences and is called lcs(). It takes two strings and returns the length of the desired subsequence. The second function works with a single sequence, in which it searches for the greatest increasing subsequence and is called gis. It takes a string and returns the length of the greatest increasing subsequence.

* _KMP_<br>
This file contains an implementation of the Knuth-Morris-Pratt algorithm for searching for a substring in a string. The KMP function receives a comma-separated string and substring as input, and returns an array with indexes of the occurrence of the substring in the string.