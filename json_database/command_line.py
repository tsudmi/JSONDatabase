from os.path import dirname, realpath, join, isfile

from antlr4 import CommonTokenStream, ParseTreeWalker
from antlr4.InputStream import InputStream
from antlr4.FileStream import FileStream
from click import command, option, echo, prompt, style

from json_database.parser.parser import CommandParser
from json_database.recognizer.DatabaseLexer import DatabaseLexer
from json_database.recognizer.DatabaseParser import DatabaseParser


@command()
@option('--db', default=join(dirname(realpath(__file__)), 'database.json'),
        help='JSON database path.')
@option('--f', default=None, help='Commands file path.')
@option('--c', default=None, help='Command to execute.')
def main(db, f, c):
    """Command line tool for JSON database manipulation."""

    if f is not None:
        if not isfile(f):
            echo(style('Specified file path does not exist.', fg='red'), err=True)
            return
        else:
            stream = FileStream(f)
    elif c is not None:
        stream = InputStream(c)
    else:
        c = prompt('Command')
        stream = InputStream(c)

    lexer = DatabaseLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = DatabaseParser(tokens)
    tree = parser.commands()

    command_parser = CommandParser(db)
    walker = ParseTreeWalker()
    walker.walk(command_parser, tree)
    command_parser.api.write_data()

if __name__ == '__main__':
    main()
