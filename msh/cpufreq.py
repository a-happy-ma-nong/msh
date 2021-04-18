def cpufreq():
    import machine
    print(str(int(machine.freq() / 1000000)) + 'MHz')
