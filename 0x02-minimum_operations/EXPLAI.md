
# ```Problem Understanding:```

>- You have a text file containing a single character 'H'.
>- Your text editor supports two operations: Copy All and Paste.
>- Given a number 'n', you need to find the minimum number of operations required to have exactly 'n' 'H' characters in the file.

## ```Approach:```

### To solve this problem efficiently, we can use dynamic programming. Here's how the approach works:

>- Initialize an array dp to store the minimum number of operations required to obtain 'i' 'H' characters in the file, where 'i' varies from 0 to 'n'.
>- We start by copying all the characters already present in the file. This counts as 1 operation.
>- For each subsequent 'i' from 2 to 'n', we iterate over all possible divisors of 'i' (except 1).
>- For each divisor 'j', we calculate the minimum number of operations required to reach 'i' by pasting 'dp[j]' characters 'i//j' times. This accounts for 'dp[j] + i//j' operations.
>- We update the minimum number of operations required for 'i' using the minimum found in step 4.
>- Finally, we return the minimum number of operations required to obtain 'n' 'H' characters.

## ```Code Explanation:```

>- We first handle the base case where 'n' is 1, which requires 0 operations.
>- We initialize the dynamic programming array dp with length 'n+1' because we need to consider 'n' as well.
>- We iterate over each number from 2 to 'n', calculating the minimum number of operations required for each.
>- Within this loop, we iterate over all possible divisors 'j' of 'i'.
>- For each divisor 'j', we calculate the minimum number of operations required to reach 'i' from 'j' and update 'dp[i]' accordingly.
>- Finally, we return dp[n], which contains the minimum number of operations required to obtain 'n' 'H' characters.

## ```Example:```

### Let's take 'n' as 4:

>- Initially, we have 'H' in the file, which requires 1 operation.
>- For 'i' = 2, the only divisor is 2 itself. So, we can paste the content once to get 2 'H's.
>- For 'i' = 3, the only divisor is 3 itself. So, we can paste twice to get 3 'H's.
>- For 'i' = 4, the divisors are 2 and 4. We can either paste twice (2 + 4//2 = 4) or paste once the content of 2 and then paste again (1 + 2 + 4//4 = 4). So, the minimum operations are 2.
