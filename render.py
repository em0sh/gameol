import os, platform, time

# Find OS
if platform.system() == 'Darwin':
    clearscreen = 'clear'
else:
    clearscreen = 'cls'


class Figure():
    # Class for figure manipulation

    def plot(f):
    # Figure plotting
        os.system(clearscreen)
        # string to build
        s = ''
        for i in range(len(f)):
            for j in range(len(f[i])):
                if f[i][j] == 0:
                    s += ' '
                else:
                    s += 'x'
            #    s += str(f[i][j])
            print(str(s))
            s = ''
        time.sleep(.25)
