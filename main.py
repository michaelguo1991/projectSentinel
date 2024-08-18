from cli.parser import parse_args
from cli.commands import list_commands

def main():
    args = parse_args()
    list_commands(args)

if __name__ == '__main__':
    main()
