def trafficlight():
    signal=input("enter the colour :")
    if (signal not in("red,yellow,greeen")):
        print("enter the traffic colour")
    else:
        value=light(signal)
        if(value==0):
            print("Stop")
        elif(value==1):
            print("Get ready to go!")
        else:
            print("Go!")            
def light(colour):
    if(colour=="red"):
        return(0)
    elif(colour=="yellow"):
        return(1)
    else:
        return(2)
trafficlight()
