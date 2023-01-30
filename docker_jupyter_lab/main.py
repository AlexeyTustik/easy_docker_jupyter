import os
import sys

COMMAND = 'docker-compose up -d'
COMMAND_STOP = 'docker-compose down'

if __name__ == '__main__':
    args = sys.argv
    if sys.argv[1] == 'run':
        os.system(COMMAND)
    elif sys.argv[1] == 'stop':
        os.system(COMMAND_STOP)
