def hauntedHouse():
    print ("Welcome to the Haunted House. Where you could die.")
    answer = raw_input("Type Continue(c) or Leave(l) and hit 'Enter'.").lower()
    if answer == "continue" or answer == "c":
        print "You enter deeper never to return!"
    elif answer == "leave" or answer == "l":
        print "You leave to see another day only to be haunted every night by the ghosts of that house."
    else:
        print "You didn't pick left or right! Try again."
        hauntedHouse()

hauntedHouse()