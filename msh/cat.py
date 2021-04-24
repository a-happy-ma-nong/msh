def cat(file):
    try:
       with open(file,"r") as f:
                print(f.read())
    except OSError:
        print("Error!")
