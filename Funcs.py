

def starttext():
    import Pyline as pyline
    print("Pyline [Version: Alpha-0.x]")
    keyinput = input("Please enter indev key>")
    while True:
        if keyinput == "japmADweTCECsqiY":
            print("Welcome to pyline",pyline.hostid,"from",pyline.hostip)
            break
        else:
            print("Wrong key. Try again.")
            keyinput = input("Please enter indev key>")