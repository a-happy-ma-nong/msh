def cat(file):
    try:
       with open(file,"r") as f:
                print(f.read())
    except OSError:
        print("cat: %s: No such file or directory" % file)
