score = 0


print("What kind of animal is a Python?")
print("A. A dog")
print("B. A fish")
print("C. A snake")
print("D. A bird")
choice = input("Type in a letter to guess: ")

if choice == "C" or choice == "c":
    print("Well done, that's right!")
    score = score + 1
else:
    print("Wrong, wrong, wrong!")

print("\n")

print("Which subject is NOT usually taught in schools?")
print("A. Maths")
print("B. Boxing ")
print("C. English")
print("D. Computing")
choice = input("Type in a letter to guess: ")

if choice == "B" or choice == "b":
    print("Well done, that's right!")
    score = score + 1
else:
    print("Wrong, wrong, wrong!")

print("\n")


print("Whats the right way to print a string?")
print("A. PRINT: Hello")
print("B. print(Hello)")
print("C. Print: hello")
print("D. print()")
choice = input("Type in a letter to guess: ")

if choice == "D" or choice == "d":
    print("Well done, that's right!")
    score = score + 1
else:
    print("Wrong, wrong, wrong!")

print("\n")

print("The end! You scored " + str(score), "out of 3")

input("\nPress ENTER to exit program")
