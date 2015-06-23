grammar Database;

commands
    :   (command ';')* command
    ;

command
    :   'SELECT' selectStatement
    |   'CREATE' createStatement
    |   'INSERT' insertStatement
    |   'UPDATE' updateStatement
    |   'DELETE' deleteStatement
    |   'DROP'   dropStatement
    ;

selectStatement
    :   ((columnName ',')* columnName | '*') 'FROM' tableName ('WHERE' where)?
    ;

createStatement
    :   'TABLE' tableName
    ;

insertStatement
    :   'INTO' tableName 'SET' (columnName '=' value ',')* columnName '=' value
    ;

updateStatement
    :   tableName 'SET' (columnName '=' value ',')* columnName '=' value ('WHERE' where)?
    ;

deleteStatement
    :   'FROM' tableName ('WHERE' where)?
    ;

dropStatement
    :   'TABLE' (tableName ',')* tableName
    ;

where
    :   whereAND 'OR' where
    |   whereAND
    ;

whereAND
    :   columnName operator value 'AND' whereAND
    |   columnName operator value
    ;

operator
    :   '=' | '!=' | '>' | '<' | '>=' | '<='
    ;

tableName
    :   NAME
    ;

columnName
    :   NAME
    ;

NAME
    :   [a-zA-Z] [0-9a-zA-Z$_]*
    ;

value
    :   number
    |   boolean
    |   STRING
    ;

STRING
    :   '"' ~["\r\n]*? '"'
    ;

number
    : INT
    | FLOAT
    ;

INT
    :   '-'? [1-9] [0-9]* ('.' [0-9]+)?
    ;

FLOAT
    :   '-'? '0' ('.' [0-9]+)?
    ;

boolean
    : 'true'
    | 'false'
    ;

LINE_COMMENT
    :   ('--' | '#') ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    :   '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
