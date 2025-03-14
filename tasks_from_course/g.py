commands_done = []
commands_done.append("1")
while 1>0:
    polecenie = input(">")
    commands_done.append(polecenie)
    for i in range(1, len(commands_done)):
        if commands_done[i - 1] == commands_done[i]:
            print("why do you run the same command two times in a row!?")
            break
    if polecenie == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif polecenie == "start":
        print("car started... ready to go!")
    elif polecenie == "stop":
        print("car stopped.")
    elif polecenie == "exit":
        break
    else:
        print("I don't understand this command...")