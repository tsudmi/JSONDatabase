# JSON Database
Automata, Languages and Compilers course project

## Requirements
* Python 2.7+

## Installation guide
1. Clone this repo:
```
    $ git clone git@github.com:tsudmi/json-database.git
```    
2. Create virtualenv:
```
    $ cd json-database
    $ virtualenv venv
```

3. Install JSON Database in development mode:
```
    $ venv/bin/python setup.py develop
```

## Usage
* Run database commands with **--c** paramater directly:
```
    $ venv/bin/json-database --c 'SELECT * FROM Person'
```
* Run database command with prompt:
```
    $ venv/bin/json-database
    Command: 'SELECT * FROM Person'
```
* Run database commands with provided script path:
```
    $ venv/bin/json-database --f /path/to/the/file
```

## Script example
```
-- This is script file example!!!
CREATE TABLE Person;
INSERT INTO Person SET Name="John", age=25, married=true;
UPDATE Person SET age=28 WHERE Name="John";
SELECT * FROM Person
DELETE FROM Person WHERE Name="Carl";
DELETE FROM Person;
DROP TABLE Person
```
