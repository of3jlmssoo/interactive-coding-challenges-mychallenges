"""
[参照]
https://loctv.wordpress.com/2019/12/14/knapsack-top-down-memoization-bottom-up/
"""

"""
public int solveKnapsack(int[] profits, int[] weights, int capacity) {
  return knapsackRecursive(profits, weights, capacity, 0);
}
-----------------------------------------------------------------------
public int solveKnapsack(int[] profits, int[] weights, int capacity) {
  Integer[][] dp = new Integer[profits.length][capacity + 1];
  return knapsackRecursive(dp, profits, weights, capacity, 0);
}
"""


def solveks(profits, weights, capacity):
    # print(profits, weights, capacity)
    dp = [[None] * (capacity + 1)] * len(profits)
    # print(dp)
    return ksr(dp, profits, weights, capacity, 0)


"""
private int knapsackRecursive(int[] profits, int[] weights, int capacity, int currentIndex) {
  // base checks
  if (capacity <= 0 || currentIndex >= profits.length)
    return 0;

  // recursive call after choosing the element at the currentIndex
  // if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
  int profit1 = 0;
  if( weights[currentIndex] <= capacity )
      profit1 = profits[currentIndex] + knapsackRecursive(profits, weights,
              capacity - weights[currentIndex], currentIndex + 1);

  // recursive call after excluding the element at the currentIndex
  int profit2 = knapsackRecursive(profits, weights, capacity, currentIndex + 1);

  return Math.max(profit1, profit2);
}
-----------------------------------------------------------------------
private int knapsackRecursive(Integer[][] dp, int[] profits, int[] weights, int capacity,
    int currentIndex) {

  // base checks
  if (capacity <= 0 || currentIndex >= profits.length)
    return 0;

  // if we have already solved a similar problem, return the result from memory
  if(dp[currentIndex][capacity] != null)
    return dp[currentIndex][capacity];

  // recursive call after choosing the element at the currentIndex
  // if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
  int profit1 = 0;
  if( weights[currentIndex] <= capacity )
      profit1 = profits[currentIndex] + knapsackRecursive(dp, profits, weights,
              capacity - weights[currentIndex], currentIndex + 1);

  // recursive call after excluding the element at the currentIndex
  int profit2 = knapsackRecursive(dp, profits, weights, capacity, currentIndex + 1);

  dp[currentIndex][capacity] = Math.max(profit1, profit2);
  return dp[currentIndex][capacity];
}
"""

called_num = 0


def ksr(dp, profits, weights, capacity, currentindex):
    global called_num
    called_num += 1
    if capacity <= 0 or currentindex >= len(profits):
        return 0
    if(dp[currentindex][capacity] is not None):
        return dp[currentindex][capacity]
    result1 = 0
    if (weights[currentindex] <= capacity):
        result1 = profits[currentindex] + ksr(dp, profits,
                                              weights,
                                              capacity - weights[currentindex],
                                              currentindex + 1)
    result2 = ksr(dp, profits, weights, capacity, currentindex + 1)

    dp[currentindex][capacity] = max(result1, result2)
    # print(f'will be returned {max(result1, result2)}')
    # return max(result1, result2)
    return dp[currentindex][capacity]


print('10 == ', solveks([4, 5, 3, 7], [2, 3, 1, 4], 5),
      called_num, ' times called')
""" https://www.cs.colostate.edu/~cs475/f15/more_progress/Lec04Knapsack.pdf """
print('40 == ', solveks([1, 6, 18, 22, 28], [1, 2, 5, 6, 7], 11),
      called_num, ' times called')
""" https://www.es.ele.tue.nl/education/5MC10/Solutions/knapsack.pdf """
print('90 == ', solveks([10, 40, 30, 50], [5, 4, 6, 3], 10),
      called_num, ' times called')
""" https://github.com/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/knapsack_01/knapsack_challenge.ipynb """
print('13 == ', solveks([2, 4, 6, 9], [2, 2, 4, 5], 8),
      called_num, ' times called')
