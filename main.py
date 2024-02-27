name = input("What is your name? ")
while True:
    try:
        age = int(input("What is your age? "))
        if age < 1:
            raise Exception()
        print(name.lower().title() + ',', "you are", age * 365, "days old!")
        break
    except:
        print("Invalid age!")

