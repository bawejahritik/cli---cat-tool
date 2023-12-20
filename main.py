import click
import sys

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('-n', '--lines', 'linenumbers', is_flag=True, help="To display the line number")
@click.option('-b', '--blank', 'blanks', is_flag=True, help="To not number blank lines")
def main(filenames, linenumbers, blanks):
    if not filenames:
        sys.stdin.reconfigure(encoding='utf-8')
        data = sys.stdin.read()
        data = data.splitlines()
        count = 1
        for i, line in enumerate(data):
            if not blanks:
                if linenumbers:
                    sys.stdout.write(str(i+1) + " " +line + "\n")
                else:
                    sys.stdout.write(line + "\n")
            else:
                if line !="":
                    sys.stdout.write(str(count) + " " +line + "\n")
                    count += 1
                else:
                    sys.stdout.write(line +"\n")
    else:
        lines = []
        for filename in filenames:
            with open(filename, "r", encoding="utf-8") as f:
                data = f.readlines()
                for line in data:
                    # sys.stdout.write(line)
                    lines.append(line)
        count = 1
        for i, line in enumerate(lines):
            if not blanks:
                if linenumbers:
                    sys.stdout.write(str(i+1) + " " +line)
                else:
                    sys.stdout.write(line)
            else:
                if line !="\n":
                    sys.stdout.write(str(count) + " " +line)
                    count += 1
                else:
                    sys.stdout.write(line)

if __name__ == '__main__':
    main()