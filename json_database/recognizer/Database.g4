grammar Database;

commands
    :   (command ';')+
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
    :   ((NAME ',') NAME | '*') 'FROM' NAME ('WHERE' where)?
    ;

createStatement
    :   'TABLE' NAME 'VALUES' '(' (NAME TYPE ',')* NAME TYPE ')'
    ;

insertStatement
    :   'INTO' NAME 'SET' (NAME '=' VALUE ',')* NAME '=' VALUE
    ;

updateStatement
    :   NAME 'SET' (NAME '=' VALUE ',')* NAME '=' VALUE ('WHERE' where)?
    ;

deleteStatement
    :   'FROM' NAME ('WHERE' where)?
    ;

dropStatement
    :   'TABLE' (NAME ',')* NAME
    ;

where
    :   NAME '=' VALUE (('AND' | 'OR') where)*
    ;

NAME
    :   [0-9a-zA-Z$_]+
    ;

VALUE
    :   STRING
    |   NUMBER
    ;

STRING
    :   '"' .*? '"'
    ;

NUMBER
    :   [1-9] [0-9]* ('.' [0-9]+)?
    |   '0' ('.' [0-9]+)?
    ;

TYPE
    :   'int'
    |   'float'
    |   'varchar'
    |   'boolean'
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

