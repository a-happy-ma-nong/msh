def cat(file):
    try:
        if file != 'no':
            with open(file,"r") as f:
                print(f.read())
    except OSError:
        print("Error!")