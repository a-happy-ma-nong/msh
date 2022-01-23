try:
    from msh.cat import *
    from msh.cd import *
    from msh.df import *
    from msh.cpufreq import *
    from msh.ls import *
except ImportError:
    from cat import *
    from cd import *
    from df import *
    from cpufreq import *
    from ls import *
import os
while True:
    input_print = "micropython %s $" % os.getcwd()
    command = str(input(input_print))
    if command == "exit":
        break
    elif command == "ls":
        ls()
    elif command == "cpufreq":
        cpufreq()
    elif command == "df":
        df()
    elif command == "cd":
        cd("/")
    elif command == "":
        pass
    else:
        print("msh: %s: No such file or directory" % command)