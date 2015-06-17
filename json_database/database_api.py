import json
from collections import OrderedDict
from os.path import exists, getsize
from sys import exit

from click import echo, style


class DatabaseAPI(object):
    def __init__(self, path):
        self.path = path
        self.data = self._get_data(path)

    def _get_data(self, path):
        if not exists(path):
            with open(path, 'a'):
                return OrderedDict()
        elif not getsize(path):
            return OrderedDict()

        with open(path) as data_file:
            try:
                return json.load(data_file, object_pairs_hook=OrderedDict)
            except ValueError:
                echo(style('This is not valid JSON database file.', fg='red'), err=True)
                exit()

    def write_data(self):
        with open(self.path, 'w+') as data_file:
            json.dump(self.data, data_file, sort_keys=True, indent=4, ensure_ascii=False)

    def get_table(self, table_name):
        try:
            return self.data[table_name]
        except KeyError:
            return None

    def create_table(self, table_name):
        self.data[table_name] = []
        echo(style('Table with name %s has been created.' % table_name, fg='green'))

    def insert_row(self, table_name, column_names, values):
        table = self.data[table_name]
        table.append(OrderedDict())

        for i in range(len(column_names)):
            table[-1][column_names[i]] = values[i]

        echo(style('Created row %s in table %s.' % (len(table), table_name), fg='green'))

    def update_rows(self, table_name, column_names, values, row_ids, is_where):
        table = self.data[table_name]
        if not row_ids and not is_where:
            row_ids = range(len(table))

        for i in row_ids:
            row = table[i]
            for j in range(len(column_names)):
                if column_names[j] in row.keys():
                    echo(style('Column %s in row %s in table %s has been updated.' %
                               (column_names[j], i, table_name), fg='green'))
                else:
                    echo(style('Column %s in row %s in table %s has been created.' %
                               (column_names[j], i, table_name), fg='green'))

                row[column_names[j]] = values[j]

    def drop_tables(self, table_names):
        for name in table_names:
            if name not in self.data:
                echo(style('Table with name %s does not exist.' % name, fg='red'), err=True)
            else:
                del self.data[name]
                echo(style('Table %s has been dropped.' % name, fg='green'))

    def delete_table_rows(self, table_name, row_ids, is_where):
        table = self.data[table_name]
        if not row_ids and not is_where:
            row_ids = range(len(table))

        for i in reversed(row_ids):
            table.pop(i)
            echo(style('Table %s row %s has been deleted.' % (table_name, i), fg='green'))

    def print_table_rows(self, table_name, column_names, row_ids, is_where):
        table = self.data[table_name]
        if not row_ids and not is_where:
            row_ids = range(len(table))

        p_data = OrderedDict()
        if not column_names:
            p_data[table_name] = [table[id] for id in row_ids]
            echo(json.dumps(p_data, sort_keys=True, indent=4, ensure_ascii=False))
            return

        p_data[table_name] = []
        for i in row_ids:
            row = table[i]

            p_row = OrderedDict()
            for name in column_names:
                if name in row.keys():
                    p_row[name] = row[name]

            p_data[table_name].append(p_row)

        echo(json.dumps(p_data, sort_keys=True, indent=4, ensure_ascii=False))
