var = {}
now = {}
save = []
start = False
input_true = True
print("csys interpreter alpha")
print("make september 20th 9:11(from korea)")
print("escape for #exit")
while True:
    if input_true == True:
        command = input("csys>").split(" ")
    input_true = True
    if command[0] == "0":
        if len(command) < 2:
            print("error!this is not command!")
        elif command[1] == "fun":
            esc1 = command[3].replace("\\n\\", "\n")
            if command[2] == "print":
                if command[3] == "var":
                    print(var[command[4]])
                else:
                    print(esc1.replace("\\s\\", " "))
            else:
                print("error!this is not command")
        elif command[1] == "var":
            if command[3] == "=":
                var[command[2]] = command[4]
                now[command[2]] = False
            else:
                print("error!this is not command!")
        elif command[1] == "com":
            if var[command[2]] == command[3] [1:]:
                now[command[2]] = True
            else:
                print("error!this is not command!")
        elif command[1] in now:
            if now[command[1]] == True:
                if command[3] == "ff":
                    start = True
                    now[command[1]] = False
                else:
                    print("haha!i don't know this!")
            elif now[command[1]] == False:
                print("why must me now?")
            else:
                print("i donot have this var")
            
        else:
            print("error!this is not command!")
    elif command[0] == "#exit":
        exit()
    elif command[0] == ";":
        save.append(command)
        if start == True:
            save[0] [0] = "0"
            command = save[0]
            save = []
            start = False
            input_true = False
            continue
    else:
        print("error!this is not command!")
