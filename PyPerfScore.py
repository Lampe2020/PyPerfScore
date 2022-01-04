import time as t

runs_max = 1000000
runs_passed = 0
number = 0
time_at_start = t.time()
while runs_passed <= runs_max:
        if runs_passed < runs_max:
                print(number, end="\r")
                number +=1
                runs_passed += 1
        elif runs_passed == runs_max:
                print(number)
                time_at_finish = t.time()
                time_to_complete = time_at_finish - time_at_start
                print("Your computer needed " + str(round(time_to_complete, 3)) + " seconds to count from zero to " + str(runs_max) + " as fast as it could.")
                score = runs_max / time_to_complete
                print("So the score is " + str(round(score)) + ".")
                exit()
