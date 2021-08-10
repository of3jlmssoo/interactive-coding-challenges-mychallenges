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
-----------------------------------------------------------------------
public int solveKnapsack(int[] profits, int[] weights, int capacity) {
  // basic checks
  if (capacity &lt;= 0 || profits.length == 0 || weights.length != profits.length)
    return 0;

  int n = profits.length;
  int[][] dp = new int[n][capacity + 1];

  // populate the capacity=0 columns, with '0' capacity we have '0' profit
  for(int i=0; i &lt; n; i++)
    dp[i][0] = 0;

  // if we have only one weight, we will take it if it is not more than the capacity
  for(int c=0; c &lt;= capacity; c++) {
    if(weights[0] &lt;= c)
      dp[0][c] = profits[0];
  }

  // process all sub-arrays for all the capacities
  for(int i=1; i &lt; n; i++) {
    for(int c=1; c &lt;= capacity; c++) {
      int profit1= 0, profit2 = 0;
      // include the item, if it is not more than the capacity
      if(weights[i] &lt;= c)
        profit1 = profits[i] + dp[i-1][c-weights[i]];
      // exclude the item
      profit2 = dp[i-1][c];
      // take maximum
      dp[i][c] = Math.max(profit1, profit2);
    }
  }

  // maximum profit will be at the bottom-right corner.
  return dp[n-1][capacity];
}
"""


def solveks(profits, weights, capacity):
    print('P:', profits, 'W:', weights, 'C:', capacity)
    if (capacity <= 0 or len(profits) == 0 or len(weights) != len(profits)):
        return 0
    print('P:', profits, 'W:', weights, 'C:', capacity)

    n = len(profits)
    # dp = [[None] * (capacity + 1)] * len(profits)
    W = [[None for j in range(capacity + 1)] for i in range(len(profits)+1)]
    print('W(0) ', W)

    for w in range(capacity+1):
      W[0][w] = 0
    print('W(1) ', W)

    for i in range(1,len(profits)+1):
      for w in range(capacity+1):
        print(f'i:{i}, w:{w} --- ',end='')
        if weights[i-1] > w:
          print(f'then: weights[i-1]:{weights[i-1]} > w:{w} --- ', end='')
          print(f'W[{i}][{w}] = W[{i-1}][{w}]')
          W[i][w] = W[i-1][w]
        else:
          print(f'else:                          W[{i}][{w}] = max(W[{i-1}][{w}], profits[{i-1}]+W[{i-1}][{w}-weights[{i-1}]]) --- max( {W[i-1][w]}, {profits[i-1]}+{W[i-1][w-weights[i-1]]} ) ')
          W[i][w] = max(W[i-1][w], profits[i-1]+W[i-1][w-weights[i-1]])
          # W[i][w] = max(W[i-1][w], profits[i-1]+W[i][w-weights[i-1]])

    print('W(2) ', W)
    print(f'{len(profits)}, {capacity}')
    return W[len(profits)][capacity]

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


# def ksr(dp, profits, weights, capacity, currentindex):
#     global called_num
#     called_num += 1
#     if capacity <= 0 or currentindex >= len(profits):
#         return 0
#     if(dp[currentindex][capacity] is not None):
#         return dp[currentindex][capacity]
#     result1 = 0
#     if (weights[currentindex] <= capacity):
#         result1 = profits[currentindex] + ksr(dp, profits,
#                                               weights,
#                                               capacity - weights[currentindex],
#                                               currentindex + 1)
#     result2 = ksr(dp, profits, weights, capacity, currentindex + 1)

#     dp[currentindex][capacity] = max(result1, result2)
#     # print(f'will be returned {max(result1, result2)}')
#     # return max(result1, result2)
#     return dp[currentindex][capacity]


# print('10 == ', solveks([4, 5, 3, 7], [2, 3, 1, 4], 5),
#       called_num, ' times called')
# """ https://www.cs.colostate.edu/~cs475/f15/more_progress/Lec04Knapsack.pdf """
print('40 == ', solveks([1, 6, 18, 22, 28], [1, 2, 5, 6, 7], 11),
      called_num, ' times called')
# """ https://www.es.ele.tue.nl/education/5MC10/Solutions/knapsack.pdf """
# print('90 == ', solveks([10, 40, 30, 50], [5, 4, 6, 3], 10),
#       called_num, ' times called')
# """ https://github.com/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/knapsack_01/knapsack_challenge.ipynb """
# print('13 == ', solveks([2, 4, 6, 9], [2, 2, 4, 5], 8),
#       called_num, ' times called')

print('14 == ', solveks([1, 3,7], [1, 2, 4], 8),
      called_num, ' times called')

"""
P: [1, 6, 18, 22, 28] W: [1, 2, 5, 6, 7] C: 11
P: [1, 6, 18, 22, 28] W: [1, 2, 5, 6, 7] C: 11
W(0)  [[None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]
W(1)  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]



i:1, w:0 --- then: weights[i-1]:1 > w:0 --- W[1][0] = W[0][0]
i:1, w:1 --- else:                          W[1][1] = max(W[0][1], profits[0]+W[0][1-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:2 --- else:                          W[1][2] = max(W[0][2], profits[0]+W[0][2-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:3 --- else:                          W[1][3] = max(W[0][3], profits[0]+W[0][3-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:4 --- else:                          W[1][4] = max(W[0][4], profits[0]+W[0][4-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:5 --- else:                          W[1][5] = max(W[0][5], profits[0]+W[0][5-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:6 --- else:                          W[1][6] = max(W[0][6], profits[0]+W[0][6-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:7 --- else:                          W[1][7] = max(W[0][7], profits[0]+W[0][7-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:8 --- else:                          W[1][8] = max(W[0][8], profits[0]+W[0][8-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:9 --- else:                          W[1][9] = max(W[0][9], profits[0]+W[0][9-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:10 --- else:                          W[1][10] = max(W[0][10], profits[0]+W[0][10-weights[0]]) --- max( 0, 1+0 ) 
i:1, w:11 --- else:                          W[1][11] = max(W[0][11], profits[0]+W[0][11-weights[0]]) --- max( 0, 1+0 ) 


i:2, w:0 --- then: weights[i-1]:2 > w:0 --- W[2][0] = W[1][0]
i:2, w:1 --- then: weights[i-1]:2 > w:1 --- W[2][1] = W[1][1]
i:2, w:2 --- else:                          W[2][2] = max(W[1][2], profits[1]+W[1][2-weights[1]]) --- max( 1, 6+0 ) 
i:2, w:3 --- else:                          W[2][3] = max(W[1][3], profits[1]+W[1][3-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:4 --- else:                          W[2][4] = max(W[1][4], profits[1]+W[1][4-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:5 --- else:                          W[2][5] = max(W[1][5], profits[1]+W[1][5-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:6 --- else:                          W[2][6] = max(W[1][6], profits[1]+W[1][6-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:7 --- else:                          W[2][7] = max(W[1][7], profits[1]+W[1][7-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:8 --- else:                          W[2][8] = max(W[1][8], profits[1]+W[1][8-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:9 --- else:                          W[2][9] = max(W[1][9], profits[1]+W[1][9-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:10 --- else:                          W[2][10] = max(W[1][10], profits[1]+W[1][10-weights[1]]) --- max( 1, 6+1 ) 
i:2, w:11 --- else:                          W[2][11] = max(W[1][11], profits[1]+W[1][11-weights[1]]) --- max( 1, 6+1 ) 

i:3, w:0 --- then: weights[i-1]:5 > w:0 --- W[3][0] = W[2][0]
i:3, w:1 --- then: weights[i-1]:5 > w:1 --- W[3][1] = W[2][1]
i:3, w:2 --- then: weights[i-1]:5 > w:2 --- W[3][2] = W[2][2]
i:3, w:3 --- then: weights[i-1]:5 > w:3 --- W[3][3] = W[2][3]
i:3, w:4 --- then: weights[i-1]:5 > w:4 --- W[3][4] = W[2][4]
i:3, w:5 --- else:                          W[3][5] = max(W[2][5], profits[2]+W[2][5-weights[2]]) --- max( 7, 18+0 ) 
i:3, w:6 --- else:                          W[3][6] = max(W[2][6], profits[2]+W[2][6-weights[2]]) --- max( 7, 18+1 ) 
i:3, w:7 --- else:                          W[3][7] = max(W[2][7], profits[2]+W[2][7-weights[2]]) --- max( 7, 18+6 ) 
i:3, w:8 --- else:                          W[3][8] = max(W[2][8], profits[2]+W[2][8-weights[2]]) --- max( 7, 18+7 ) 
i:3, w:9 --- else:                          W[3][9] = max(W[2][9], profits[2]+W[2][9-weights[2]]) --- max( 7, 18+7 ) 
i:3, w:10 --- else:                          W[3][10] = max(W[2][10], profits[2]+W[2][10-weights[2]]) --- max( 7, 18+7 ) 
i:3, w:11 --- else:                          W[3][11] = max(W[2][11], profits[2]+W[2][11-weights[2]]) --- max( 7, 18+7 ) 

i:4, w:0 --- then: weights[i-1]:6 > w:0 --- W[4][0] = W[3][0]
i:4, w:1 --- then: weights[i-1]:6 > w:1 --- W[4][1] = W[3][1]
i:4, w:2 --- then: weights[i-1]:6 > w:2 --- W[4][2] = W[3][2]
i:4, w:3 --- then: weights[i-1]:6 > w:3 --- W[4][3] = W[3][3]
i:4, w:4 --- then: weights[i-1]:6 > w:4 --- W[4][4] = W[3][4]
i:4, w:5 --- then: weights[i-1]:6 > w:5 --- W[4][5] = W[3][5]
i:4, w:6 --- else:                          W[4][6] = max(W[3][6], profits[3]+W[3][6-weights[3]]) --- max( 19, 22+0 ) 
i:4, w:7 --- else:                          W[4][7] = max(W[3][7], profits[3]+W[3][7-weights[3]]) --- max( 24, 22+1 ) 
i:4, w:8 --- else:                          W[4][8] = max(W[3][8], profits[3]+W[3][8-weights[3]]) --- max( 25, 22+6 ) 
i:4, w:9 --- else:                          W[4][9] = max(W[3][9], profits[3]+W[3][9-weights[3]]) --- max( 25, 22+7 ) 
i:4, w:10 --- else:                          W[4][10] = max(W[3][10], profits[3]+W[3][10-weights[3]]) --- max( 25, 22+7 ) 
i:4, w:11 --- else:                          W[4][11] = max(W[3][11], profits[3]+W[3][11-weights[3]]) --- max( 25, 22+18 ) 

i:5, w:0 --- then: weights[i-1]:7 > w:0 --- W[5][0] = W[4][0]
i:5, w:1 --- then: weights[i-1]:7 > w:1 --- W[5][1] = W[4][1]
i:5, w:2 --- then: weights[i-1]:7 > w:2 --- W[5][2] = W[4][2]
i:5, w:3 --- then: weights[i-1]:7 > w:3 --- W[5][3] = W[4][3]
i:5, w:4 --- then: weights[i-1]:7 > w:4 --- W[5][4] = W[4][4]
i:5, w:5 --- then: weights[i-1]:7 > w:5 --- W[5][5] = W[4][5]
i:5, w:6 --- then: weights[i-1]:7 > w:6 --- W[5][6] = W[4][6]
i:5, w:7 --- else:                          W[5][7] = max(W[4][7], profits[4]+W[4][7-weights[4]]) --- max( 24, 28+0 ) 
i:5, w:8 --- else:                          W[5][8] = max(W[4][8], profits[4]+W[4][8-weights[4]]) --- max( 28, 28+1 ) 
i:5, w:9 --- else:                          W[5][9] = max(W[4][9], profits[4]+W[4][9-weights[4]]) --- max( 29, 28+6 ) 
i:5, w:10 --- else:                          W[5][10] = max(W[4][10], profits[4]+W[4][10-weights[4]]) --- max( 29, 28+7 ) 
i:5, w:11 --- else:                          W[5][11] = max(W[4][11], profits[4]+W[4][11-weights[4]]) --- max( 40, 28+7 ) 
W(2)  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7], [0, 1, 6, 7, 7, 18, 19, 24, 25, 25, 25, 25], [0, 1, 6, 7, 7, 18, 22, 24, 28, 29, 29, 40], [0, 1, 6, 7, 7, 18, 22, 28, 29, 34, 35, 40]]
5, 11
40 ==  40 0  times called

"""
