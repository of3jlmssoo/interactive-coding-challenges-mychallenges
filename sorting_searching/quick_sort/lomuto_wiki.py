""" [summary]
algorithm quicksort(A, lo, hi) is
    // first we check if the lo and hi
    // are natural numbers (without this check, you
    // will get an overflow error because, at some point
    // the program will access something like A[-1]
    // which does not exists !
    if lo >= 0 && hi >= 0 then
         // if the indexes are in correct order, continue
         if lo < hi then
              // we find the index of the pivot and... 
              p := partition(A, lo, hi)
              // ...apply quicksort for the left side and the
              // right side of the array
              quicksort(A, lo, p - 1)
              quicksort(A, p + 1, hi)

                                            partition(arr,0,7)
algorithm partition(A, lo, hi) is
    // we set the pivot value to the
    // final value of the array 
    pivot := A[hi]
    // we set the pivotIndex (i) to
    // the start of the array
    // ! NOTICE that A[i] != pivot
    // aka. A[pivotIndex] != pivotValue
    i := lo - 1
    // we traverse the array from the start
    // to the end (inclusive) aka. we traverse
    // the array in this interval: [lo, hi]
    for j := lo to hi do
        // if the current element is
        // less than the value of the pivot
        // (or equal to it), then increment the i
        // and swap it with the element at i (pivotIndex)
        // ! NOTICE that j is automatically incremented 
        if A[j] <= pivot then
            i := i + 1
            swap A[i] with A[j]         j=1 i=0  arr[0] arr[1]
    return i

"""
