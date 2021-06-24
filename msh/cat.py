def cat(file):
    try:
       with open(file,"r") as f:
                print(f.read())
    except OSError:
        print("cat: file %s not found" % file)
