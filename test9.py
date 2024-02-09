#weather = str(input("Please enter the weather: "))
#
#if weather == "rain":
#    print("Use Umbrella")
#else:
#    print("Enjoy the sunny day")


def bigger_guy(a, b) -> None:
    

    if a > b:
        print(a, "is bigger than", b)
    else:
        print(b, "is bigger than", a)


bigger_guy(45, 40)
