import sys
sys.stderr.write('Usage: \ntype inputfile.txt | python.exe convert.py > newinputfile.txt\n')
ogdata = sys.stdin.read()
if ogdata.__contains__('\t'):
    splitdata = ogdata.splitlines()
    for line in  splitdata:
        linesplit = line.split('\t')
        if linesplit[0] == 'C':
            sys.stdout.write('C\n'+linesplit[1]+'\n'+linesplit[2]+'\n'+linesplit[3]+'\n'+linesplit[4]+'\n')
        elif linesplit[0] == 'K':
            sys.stdout.write('K\n'+linesplit[1]+'\n'+linesplit[2]+'\n')
        elif linesplit[0] == 'M':
            sys.stdout.write('M\n'+linesplit[1]+'\n'+linesplit[2]+'\n')
        elif linesplit[0] == 'W':
            sys.stdout.write('W\n'+linesplit[1]+'\n')
        elif linesplit[0] == 'F':
            sys.stdout.write('F\n'+linesplit[1]+'\n')
        elif linesplit[0] == 'V':
            sys.stdout.write('V\n'+linesplit[1]+'\n')
        else:
            for parameter in linesplit:
                sys.stdout.write(parameter+'\n')
else:
    pointer = 0
    splitdata = ogdata.splitlines()
    while pointer < splitdata.__len__():
        if splitdata[pointer][0] == 'C':
            sys.stdout.write('C\t'+splitdata[pointer+1]+'\t'+splitdata[pointer+2]+'\t'+splitdata[pointer+3]+'\t'+splitdata[pointer+4]+'\n')
            pointer += 5
        elif splitdata[pointer][0] == 'K':
            sys.stdout.write('K\t'+splitdata[pointer+1]+'\t'+splitdata[pointer+2]+'\n')
            pointer += 3
        elif splitdata[pointer][0] == 'M':
            sys.stdout.write('M\t' + splitdata[pointer + 1] + '\t' + splitdata[pointer + 2]+'\n')
            pointer += 3
        elif splitdata[pointer][0] == 'W':
            sys.stdout.write('W\t' + splitdata[pointer + 1]+'\n')
            pointer += 2
        elif splitdata[pointer][0] == 'F':
            sys.stdout.write('F\t' + splitdata[pointer + 1]+'\n')
            pointer += 2
        elif splitdata[pointer][0] == 'V':
            sys.stdout.write('V\t' + splitdata[pointer + 1]+'\n')
            pointer += 2
        else:
            sys.stdout.write(splitdata[pointer]+'\n')
            pointer += 1
