from click import echo, style

from json_database.database_api import DatabaseAPI
from json_database.recognizer.DatabaseListener import DatabaseListener
from json_database.recognizer.DatabaseParser import DatabaseParser


def value_converter(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            if value == 'true':
                return True
            elif value == 'false':
                return False

            return value.strip('"')


class CommandParser(DatabaseListener):
    def __init__(self, database_path):
        self.api = DatabaseAPI(database_path)

    def exitSelectStatement(self, ctx):
        column_names, row_ids, table_name = [], [], ''
        is_where = False
        for child in ctx.children:
            if isinstance(child, DatabaseParser.ColumnNameContext):
                column_names.append(child.getText())
            elif isinstance(child, DatabaseParser.TableNameContext):
                table_name = child.getText()
                if self.api.get_table(table_name) is None:
                    echo(style('Table with name %s does not exist.' % table_name, fg='red'), err=True)
                    return
            elif isinstance(child, DatabaseParser.WhereContext):
                is_where = True
                table = self.api.get_table(table_name)
                for i in range(len(table)):
                    if self.is_acceptable(table[i], child):
                        row_ids.append(i)

        self.api.print_table_rows(table_name, column_names, row_ids, is_where)

    def exitCreateStatement(self, ctx):
        table_name = ctx.getChild(1).getText()
        if self.api.get_table(table_name):
            echo(style('Table with name %s already exists.' % table_name, fg='blue'))
        else:
            self.api.create_table(table_name)

    def exitInsertStatement(self, ctx):
        table_name = ctx.getChild(1).getText()
        if self.api.get_table(table_name) is None:
            echo(style('Table with name %s does not exist. Creating...' % table_name, fg='blue'))
            self.api.create_table(table_name)

        column_names, values = [], []
        for child in ctx.children:
            if isinstance(child, DatabaseParser.ColumnNameContext):
                column_names.append(child.getText())
            elif isinstance(child, DatabaseParser.ValueContext):
                values.append(value_converter(child.getText()))

        self.api.insert_row(table_name, column_names, values)

    def exitUpdateStatement(self, ctx):
        table_name = ctx.getChild(0).getText()
        if self.api.get_table(table_name) is None:
            echo(style('Table with name %s does not exist. Nothing to update.' % table_name, fg='red'), err=True)
            return

        column_names, values, row_ids = [], [], []
        is_where = False
        for child in ctx.children:
            if isinstance(child, DatabaseParser.ColumnNameContext):
                column_names.append(child.getText())
            elif isinstance(child, DatabaseParser.ValueContext):
                values.append(value_converter(child.getText()))
            elif isinstance(child, DatabaseParser.WhereContext):
                is_where = True
                table = self.api.get_table(table_name)
                for i in range(len(table)):
                    if self.is_acceptable(table[i], child):
                        row_ids.append(i)

        self.api.update_rows(table_name, column_names, values, row_ids, is_where)

    def exitDropStatement(self, ctx):
        table_names = []
        for child in ctx.children:
            if isinstance(child, DatabaseParser.TableNameContext):
                table_names.append(child.getText())

        self.api.drop_tables(table_names)

    def exitDeleteStatement(self, ctx):
        table_name = ctx.getChild(1).getText()
        if self.api.get_table(table_name) is None:
            echo(style('Table with name %s does not exist. Nothing to delete.' % table_name, fg='red'), err=True)
            return

        row_ids = []
        is_where = False
        for child in ctx.children:
            if isinstance(child, DatabaseParser.WhereContext):
                is_where = True
                table = self.api.get_table(table_name)
                for i in range(len(table)):
                    if self.is_acceptable(table[i], child):
                        row_ids.append(i)

        self.api.delete_table_rows(table_name, row_ids, is_where)

    def is_acceptable(self, table_row, ctx):
        if isinstance(ctx, DatabaseParser.WhereContext):
            left = self.is_acceptable(table_row, ctx.getChild(0))

            if ctx.getChildCount() >= 3:
                right = self.is_acceptable(table_row, ctx.getChild(2))
                return left or right

            return left
        elif isinstance(ctx, DatabaseParser.WhereANDContext):
            column = value_converter(ctx.getChild(0).getText())
            value = value_converter(ctx.getChild(2).getText())

            left = column in table_row.keys() and table_row[column] == value
            if ctx.getChildCount() >= 5:
                right = self.is_acceptable(table_row, ctx.getChild(-1))
                return left and right

            return left
