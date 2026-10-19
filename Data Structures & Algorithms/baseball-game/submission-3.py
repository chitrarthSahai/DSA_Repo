class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []

        #I am thinking of maintaining the second element from the top, so it's easy to do "+"
        wasTop = 0

        for operation in operations:
            match operation:
                case "+":
                    #add top and wasTop to get the sum
                    ans = scoreStack[-1] + wasTop
                    #Update wasTop to the current top
                    wasTop = scoreStack[-1]
                    #Add ans to top
                    scoreStack.append(ans)
                case "C":
                    scoreStack.pop() #Remove the actual top

                    #wasTop became the new top, but pop it so we can get the element behind it to store the new wasTop
                    newTop = scoreStack.pop() if scoreStack else 0

                    #Update new wasTop
                    wasTop = scoreStack[-1] if scoreStack else 0

                    #Add top again
                    scoreStack.append(newTop)
                case "D":
                    #Get the new top
                    top = scoreStack[-1]

                    #Update #wasTop
                    wasTop = top

                    #Add 2wice of top
                    scoreStack.append(2*top)
                case number:
                    #Updte wasTop, for first addition the list could be empty
                    wasTop = scoreStack[-1] if scoreStack else 0

                    scoreStack.append(int(number))

        return sum(scoreStack)
