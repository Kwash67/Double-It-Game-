import random

start_message ="Let's play a game of Two's!"
start_message += "\nInput 'quit' to end the game"
print(start_message)

x = [value*2 for value in range(0,20)]
K = "start"
while K == "start":
    try:
        n = "correct"
        points = 0
        old_points = points
        while n == "correct":
            num = random.choice(x)
            print(num)
            ans = input("Number times 2: ")
            if str(ans) == 'quit':
                n = 'wrong'
                print(f" You had {points} points")
                K = 'end'
            elif int(ans) == 2*num:
                n = "correct"
                points = points + 5
                if points == old_points +5:
                    print("New High Score Achieved!")
            else:
                n = 'wrong'
                print("Game Over!")
                print(f"{2*num} is the right answer")
                print(f"Total score : {points}")
                #Restart option and highscore
                restart = input("Restart? (y/n) ")
                if restart == 'n':
                    print("Goodbye!")
                    K = 'end'
                elif restart == 'y':
                    n = 'correct'
                    old_points = points
                    points = 0
                else:
                    print("Answer with y or n!")
    except ValueError:
        print("Oh no!  Integers only!!!")
    finally:
        if K == 'start':
            fail = input("Restart? (y/n) ")
            if fail == 'y':
                n = 'correct'
            else:
                break