class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #create students and sandwiches into a deque so it is faster and easy to operate

        students_dq = deque(students)
        sandwiches_dq = deque(sandwiches)


        while True:

            #break condition (happy case) - if sandwiches are empty and students are also empty then return 0
            if not students_dq and not sandwiches_dq:
                return 0
            
            if students_dq[0] == sandwiches_dq[0]:
                students_dq.popleft()
                sandwiches_dq.popleft()
            else:
                #break condition (hungry case) - if the top sandwich has no takers in students queue that means remaining student go hungry, so break away from the loop.
                if not sandwiches_dq[0] in students_dq:
                    break
                
                students_dq.rotate(-1)

        return len(students_dq)
                