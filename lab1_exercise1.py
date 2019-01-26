fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
confidence = float(input("Enter your confidence in programmers from 0-100%: ")) / 100
dog_age = age * 7
print("Hello", fname, lname+", nice to meet you! You might be", str(age)+" in human years, but in dog years you are", str(dog_age)+".")
if confidence < 0.5:
    print("I agree, programmers can't be trusted!")
else:
    print("Writing good code takes hard work!")
