import unittest

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.InputStream import InputStream

from json_database.recognizer.DatabaseLexer import DatabaseLexer
from json_database.recognizer.DatabaseParser import DatabaseParser


class SyntaxErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise RuntimeError(msg)

class RecognizerTest(unittest.TestCase):
    def test_valid_select_commands_are_accepted(self):
        commands = [
            'SELECT ColumnName1 FROM TableName',
            'SELECT ColumnName1, ColumnName2 FROM TableName',
            'SELECT ColumnName1, ColumnName2, ColumnName3 FROM TableName',
            'SELECT * FROM TableName',
            'SELECT ColumnName1 FROM TableName WHERE Name1="Value"',
            'SELECT ColumnName1 FROM TableName;'
            'SELECT ColumnName2 FROM TableName2'
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_select_commands_are_not_accepted(self):
        commands = [
            'SELECT FROM TableName',
            'SELECT ColumnName1, FROM TableName',
            'SELECT ColumnName1 FROM TableName WHERE',
            'SELECT ColumnName1',
            'SELECT ColumnName1 FROM',
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_create_commands_are_accepted(self):
        commands = [
            'CREATE TABLE TableName',
            'CREATE TABLE TableName;'
            'CREATE TABLE TableName',
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_create_commands_are_not_accepted(self):
        commands = [
            'CREATE TBLE TableName',
            'CREATE TABLE TableName VALUES (ColumnName1,)',
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_insert_commands_are_accepted(self):
        commands = [
            'INSERT INTO TableName SET ColumnName1="Value1"',
            'INSERT INTO TableName SET ColumnName1="Value1", ColumnName2=1, ColumnName3=3.14, ColumnName4=true',
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_insert_commands_are_not_accepted(self):
        commands = [
            'INSERT INTO TableName SET ColumnName1=Value1',
            'INSERT INTO TableName SET ColumnName1="Value1", ColumnName2=1,',
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_update_commands_are_accepted(self):
        commands = [
            'UPDATE TableName1 SET ColumnName1="Value1"',
            'UPDATE TableName1 SET ColumnName1="Value1", ColumnName2=3, ColumnName3=3.14',
            'UPDATE TableName1 SET ColumnName2=3, ColumnName3=3.14 WHERE ColumnName="Value1";'
            'UPDATE TableName1 SET ColumnName1="Value1"'
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_update_commands_are_not_accepted(self):
        commands = [
            'UPDATE TableName1 SET ColumnName1=Value1',
            'UPDATE TableName1 SET ColumnName1="Value1", ColumnName2=3 ColumnName3=3.14',
            'UPDATE TableName1 SET ColumnName2=3, ColumnName3=3.14 WHERE ColumnName="Value1"'
            'UPDATE TableName1 SET ColumnName1="Value1"'
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_drop_commands_are_accepted(self):
        commands = [
            'DROP TABLE TableName1',
            'DROP TABLE TableName1, TableName2'
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_drop_commands_are_not_accepted(self):
        commands = [
            'DROP TABLE @TableName1',
            'DROP TABLE TableName1, TableName2,'
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_delete_commands_are_accepted(self):
        commands = [
            'DELETE FROM TableName1 WHERE ColumnName1="Value"',
            'DELETE FROM TableName1 WHERE ColumnName1="Value" AND ColumnName2=3.14',
            'DELETE FROM TableName1'
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_delete_commands_are_not_accepted(self):
        commands = [
            'DELETE FROM TableName1 WHERE ColumnName1=Value',
            'DELETE FROM TableName1 WHERE ColumnName1="Value", ColumnName2=3.14',
            'DELETE FROM TableName1;'
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    def test_valid_commands_with_where_statement_are_accepted(self):
        commands = [
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1="Value" AND Name2=3',
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1="Value" OR Name2=true',
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1="Value" OR Name2=false'
        ]

        for command in commands:
            self.ensure_command_is_accepted(command)

    def test_invalid_commands_with_where_statement_are_not_accepted(self):
        commands = [
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1="Value", Name2=3',
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1="Value" Name2=true',
            'SELECT ColumnName1, ColumnName2 FROM TableName WHERE Name1=ValueName Name2=false'
        ]

        for command in commands:
            self.ensure_command_is_not_accepted(command)

    # Helper methods
    def ensure_command_is_not_accepted(self, command):
        try:
            self.parse_with_exceptions(command)
            raise AssertionError('Following commands should not be accepted: %s' % command)
        except RuntimeError:
            pass

    def ensure_command_is_accepted(self, command):
        try:
            self.parse_with_exceptions(command)
        except RuntimeError as e:
            raise AssertionError('Following command should be accepted: %s' % command, 'Error: %s' % e.message)

    def parse_with_exceptions(self, commands):
        stream = InputStream(commands)

        lexer = DatabaseLexer(stream)
        lexer.addErrorListener(SyntaxErrorListener())

        tokens = CommonTokenStream(lexer)

        parser = DatabaseParser(tokens)
        parser.addErrorListener(SyntaxErrorListener())

        commands_tree = parser.commands()

        if not (parser or commands_tree.getChildCount()):
            raise RuntimeError('Problem with parsing')
        elif tokens.LA(1) != -1:
            raise RuntimeError('Some tokens left after parsing')
