def cd(path):
    try:
        import os
        os.chdir(str(path))
    except FileNotFoundError:
        print("cd: %s: No such file or directory" % path)