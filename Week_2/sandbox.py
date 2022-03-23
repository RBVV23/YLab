
red = '\033[31m'
blue = '\033[34m'

marks = ['\033[31m X\033[00m', '\033[34m O\033[00m']

CELL_WIDTH = 10

nim = 50
nim = 'srt'
nim = '\033[31mX'

print(f'{marks[0]:^{CELL_WIDTH}}', end='|')

for ind, i in enumerate(range(10), start=-2):
    print(f'{ind}: {i}')
