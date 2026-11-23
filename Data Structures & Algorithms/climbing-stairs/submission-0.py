class Solution:
    def climbStairs(self, n: int) -> int:

        #The idea is using decision binary tree, at each step you can take either 1 step or 2 step. Let's say you start at step 0 and n=5, you either go to step 1 or step 2.

        #                 0
        #                / \
        #               1   2
        #              / \ / \
        #             2  3 3  4
        #            /\ /\ /\ /\ 
        #           3 4 4 54 55 6
        # and so on... and then each time we get 5 we can return that as a valid path

        #Dynamic programming is a technique to solve a problem by solving it's sub-problem first. In this case when we are at step 2, you solve for step 3 or step 4. If we can store these results of step3 and 4 and how many ways we can reach to n from step 3 and 4, step 2 could be just the sum of them. This is called memoization, that is storing results of a sub-problem so that you don't have to compute again. Using this, we don't have to compute step again for when we reach step 2 on the right side of the tree. Thus saving time, otherwise it will be a solution of O(2^n). With dynamic programming this decision tree becomes of time complexity O(n)
        

        # Now, a key point to analyze here is that the base case is when n=5, let's assume we start at n. we only have to hop once because we are at result itself, so number of ways is "1", when we are at 4, you either take 1 step to reach to 5 or take 2 steps to reach 6 (which is OOB), so number of ways is again "1". Now, when at 3, you just solve for subproblem, because you can either go to 4 or 5. And you have answer for both of those steps so you just add them which is 1+1=2, now you solve for 2, which is ans of step 3 and step 4 which is 2+1 = 3 and so on, till you solve for 0 and that is the number of ways you can climb the stairs from ground. Key point to note that whatever n is, the number of ways from last and second last is always 1 and 1. So you just have to loop for n-1 times and keep on computing and shifting and you will reach the answer.

        # -,-,-,-,1,1
        # -,-,-,2,1,1
        # -,-,3,2,1,1
        # -,5,3,2,1,1
        # 8,5,3,2,1,1

        #ans = 8 for n=5

        one, two = 1,1 #The ways to climb from last and second last steps.

        for i in range(n-1):
            temp = one #To temp store one's value
            one  = one + two # You add the number of ways for the 2 steps ahead and shift that two one
            two = temp # two becomes the new one

        return one