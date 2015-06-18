from ast import literal_eval
import os.path
import unittest

from antlr4 import CommonTokenStream, ParseTreeWalker
from antlr4.InputStream import InputStream

from json_database.parser.parser import CommandParser
from json_database.recognizer.DatabaseLexer import DatabaseLexer
from json_database.recognizer.DatabaseParser import DatabaseParser


class CommandsTest(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.json')

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_one_create_statement(self):
        command = 'CREATE TABLE Isik'
        result = self.execute_command(command, self.db_path)
        self.assertEqual(result, {'Isik': []})

    def test_multiple_create_statements(self):
        command = 'CREATE TABLE Isik; CREATE TABLE Isik1; CREATE TABLE Isik2'
        result = self.execute_command(command, self.db_path)
        self.assertEqual(result, {'Isik': [], 'Isik1': [], 'Isik2': []})

    def test_create_statement_with_existing_table(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write('{"Isik":[]}')

        command = 'CREATE TABLE Isik'
        result = self.execute_command(command, self.db_path)
        self.assertEqual(result, {'Isik': []})

    def test_insert_statement_with_one_value(self):
        command = 'INSERT INTO Isik SET Nimi="John"'
        result = self.execute_command(command, self.db_path)
        self.assertEqual(result, {'Isik': [{'Nimi': 'John'}]})

    def test_insert_statement_with_multiple_values(self):
        command = 'INSERT INTO Isik SET Nimi="John", age=25, married=true'
        result = self.execute_command(command, self.db_path)

        self.assertEqual(result, {'Isik': [{'Nimi': 'John', 'age': 25, 'married': True}]})

    def test_insert_statement_with_multiple_statements(self):
        command = 'INSERT INTO Isik SET Nimi="John"; INSERT INTO Isik SET Nimi="Paul"'
        result = self.execute_command(command, self.db_path)

        self.assertEqual(result, {'Isik': [{'Nimi': 'John'}, {'Nimi': 'Paul'}]})

    def test_update_statement_without_where_statement(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'UPDATE Cars SET age=2'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        expected['Cars'][0]['age'] = 2
        expected['Cars'][1]['age'] = 2

        self.assertEqual(result, expected)

    def test_update_statement_with_where_statement(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'UPDATE Person SET age=25 WHERE Name="John"'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        expected['Person'][0]['age'] = 25

        self.assertEqual(result, expected)

    def test_delete_statement_without_where_statement(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'DELETE FROM Person'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        expected['Person'] = []

        self.assertEqual(result, expected)

    def test_delete_statement_with_where_statement(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'DELETE FROM Person WHERE Name="Carl"'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        del expected['Person'][1]

        self.assertEqual(result, expected)

    def test_drop_statement_with_one_table_name(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'DROP TABLE Person'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        del expected['Person']

        self.assertEqual(result, expected)

    def test_drop_statement_with_multiple_table_names(self):
        with open(self.db_path, 'w+') as db_file:
            db_file.write(self.generate_sample_data())

        command = 'DROP TABLE Person, Cars'
        result = self.execute_command(command, self.db_path)

        expected = literal_eval(self.generate_sample_data())
        del expected['Person']
        del expected['Cars']

        self.assertEqual(result, expected)

    # Helper methods
    def execute_command(self, command, db_path):
        stream = InputStream(command)
        lexer = DatabaseLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = DatabaseParser(tokens)
        tree = parser.commands()

        command_parser = CommandParser(db_path)
        walker = ParseTreeWalker()
        walker.walk(command_parser, tree)

        return command_parser.api.data

    def generate_sample_data(self):
        return """{
            "Person": [
                {
                    "Name": "John",
                    "age": 23,
                    "married": "false"
                },
                {
                    "Name": "Carl",
                    "Surname": "Paul",
                    "age": 23,
                    "married": "false"
                }
            ],
            "Cars": [
                {
                    "Mark": "Audi",
                    "age": 23
                },
                {
                    "Mark": "Mercedez-Benz",
                    "age": 1,
                    "crashed": "false"
                }
            ]
        }"""
