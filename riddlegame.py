i = 0


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


lst = [None] * 9

lst[0] = "If u multiply this number by any number, the answer will always be the same.What number is this?"
lst[1] = "How many times can you substract the numbr 5 from 25?"
lst[2] = "If there are three apples and u take away two, how many apples do u have?"
lst[3] = "What do mathematics teachers like to eat?"
lst[
    4] = "There are 2 ants in front of 2 other ants, 2 ants behind 2 ants and 2 ants next 2 ants. How many total ants are there?"
lst[5] = "Ram has 5 sons. Each of his sons has a sister. If so how many children does Mr.Ram have?"
lst[6] = "I am an odd number. Take away a letter and I become even. What number am I?"
lst[7] = "If two's a company and three's a crowd, what are four and five?"
lst[8] = "Suppose 1+9+8=1, then what can be 2+8+9= ?"


def printPostorder(root):
    global i

    if root:

        printPostorder(root.left)

        printPostorder(root.right)

        print(lst[i])
        i = i + 1
        flag = 0
        while flag != 3:

            ans = float(input("Enter ur answer here : "))

            if ans == root.val:

                print("Your answer is correct")
                if ans == 10:
                    print("GOOD JOB..U WON")
                    break

                break
            else:
                print("Wrong answer..try again")
                flag += 1
                if flag == 3:
                    print("Maximum limit exceeded")
                    exit()


root = Node(10)
root.left = Node(3.14)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(7)
root.left.left.left = Node(0)
root.right.right.right = Node(6)

print("ALL THE BEST..")
printPostorder(root)

