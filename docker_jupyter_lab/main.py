import os
import sys

COMMAND = 'docker-compose up -d'
COMMAND_STOP = 'docker-compose down'
COMMAND_ADMIN = 'docker exec -it my-jupyter-lab  bash'

if __name__ == '__main__':
    args = sys.argv
    assert len(sys.argv) > 1, "use commands ['run', 'stop', 'admin']"
    if sys.argv[1] == 'run':
        os.system(COMMAND)
    elif sys.argv[1] == 'stop':
        os.system(COMMAND_STOP)
    elif sys.argv[1] == 'admin':
        os.system(COMMAND_ADMIN)
