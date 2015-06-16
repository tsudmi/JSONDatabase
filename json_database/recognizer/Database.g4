grammar Database;
options {
    language = Python;
}

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
    :   ((NAME ',')* NAME | '*') 'FROM' NAME ('WHERE' where)?
    ;

createStatement
    :   'TABLE' NAME 'VALUES' '(' (NAME ',')* NAME ')'
    ;

insertStatement
    :   'INTO' NAME 'SET' (NAME '=' value ',')* NAME '=' value
    ;

updateStatement
    :   NAME 'SET' (NAME '=' value ',')* NAME '=' value ('WHERE' where)?
    ;

deleteStatement
    :   'FROM' NAME ('WHERE' where)?
    ;

dropStatement
    :   'TABLE' (NAME ',')* NAME
    ;

where
    :   NAME '=' value (('AND' | 'OR') where)*
    ;

NAME
    :   [a-zA-Z] ([0-9a-zA-Z$_])+
    ;

value
    :   number
    |   boolean
    |   string
    ;

string
    :   '"' ~'"' '"'
    ;

number
    : NUMBER
    ;

NUMBER
    :   [1-9] [0-9]* ('.' [0-9]+)?
    |   '0' ('.' [0-9]+)?
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
