# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .DatabaseListener import DatabaseListener
else:
    from DatabaseListener import DatabaseListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"!\u00a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2")
        buf.write(u"\7\2&\n\2\f\2\16\2)\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\4\3\4\3\4\7\4")
        buf.write(u">\n\4\f\4\16\4A\13\4\3\4\3\4\5\4E\n\4\3\4\3\4\3\4\3\4")
        buf.write(u"\5\4K\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\7\6X\n\6\f\6\16\6[\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\7\7h\n\7\f\7\16\7k\13\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\5\7r\n\7\3\b\3\b\3\b\3\b\5\bx\n\b\3\t\3\t\3")
        buf.write(u"\t\3\t\7\t~\n\t\f\t\16\t\u0081\13\t\3\t\3\t\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\5\n\u008a\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\5\13\u0096\n\13\3\f\3\f\3\r\3\r")
        buf.write(u"\3\16\3\16\3\17\3\17\3\17\5\17\u00a1\n\17\3\20\3\20\3")
        buf.write(u"\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \2\5\4\2\21\21\24\30\3\2\35\36\3\2\31\32\u00a8")
        buf.write(u"\2\'\3\2\2\2\48\3\2\2\2\6D\3\2\2\2\bL\3\2\2\2\nO\3\2")
        buf.write(u"\2\2\f`\3\2\2\2\16s\3\2\2\2\20y\3\2\2\2\22\u0089\3\2")
        buf.write(u"\2\2\24\u0095\3\2\2\2\26\u0097\3\2\2\2\30\u0099\3\2\2")
        buf.write(u"\2\32\u009b\3\2\2\2\34\u00a0\3\2\2\2\36\u00a2\3\2\2\2")
        buf.write(u" \u00a4\3\2\2\2\"#\5\4\3\2#$\7\3\2\2$&\3\2\2\2%\"\3\2")
        buf.write(u"\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2")
        buf.write(u"\2\2*+\5\4\3\2+\3\3\2\2\2,-\7\4\2\2-9\5\6\4\2./\7\5\2")
        buf.write(u"\2/9\5\b\5\2\60\61\7\6\2\2\619\5\n\6\2\62\63\7\7\2\2")
        buf.write(u"\639\5\f\7\2\64\65\7\b\2\2\659\5\16\b\2\66\67\7\t\2\2")
        buf.write(u"\679\5\20\t\28,\3\2\2\28.\3\2\2\28\60\3\2\2\28\62\3\2")
        buf.write(u"\2\28\64\3\2\2\28\66\3\2\2\29\5\3\2\2\2:;\5\32\16\2;")
        buf.write(u"<\7\n\2\2<>\3\2\2\2=:\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3")
        buf.write(u"\2\2\2@B\3\2\2\2A?\3\2\2\2BE\5\32\16\2CE\7\13\2\2D?\3")
        buf.write(u"\2\2\2DC\3\2\2\2EF\3\2\2\2FG\7\f\2\2GJ\5\30\r\2HI\7\r")
        buf.write(u"\2\2IK\5\22\n\2JH\3\2\2\2JK\3\2\2\2K\7\3\2\2\2LM\7\16")
        buf.write(u"\2\2MN\5\30\r\2N\t\3\2\2\2OP\7\17\2\2PQ\5\30\r\2QY\7")
        buf.write(u"\20\2\2RS\5\32\16\2ST\7\21\2\2TU\5\34\17\2UV\7\n\2\2")
        buf.write(u"VX\3\2\2\2WR\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\")
        buf.write(u"\3\2\2\2[Y\3\2\2\2\\]\5\32\16\2]^\7\21\2\2^_\5\34\17")
        buf.write(u"\2_\13\3\2\2\2`a\5\30\r\2ai\7\20\2\2bc\5\32\16\2cd\7")
        buf.write(u"\21\2\2de\5\34\17\2ef\7\n\2\2fh\3\2\2\2gb\3\2\2\2hk\3")
        buf.write(u"\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\5\32")
        buf.write(u"\16\2mn\7\21\2\2nq\5\34\17\2op\7\r\2\2pr\5\22\n\2qo\3")
        buf.write(u"\2\2\2qr\3\2\2\2r\r\3\2\2\2st\7\f\2\2tw\5\30\r\2uv\7")
        buf.write(u"\r\2\2vx\5\22\n\2wu\3\2\2\2wx\3\2\2\2x\17\3\2\2\2y\177")
        buf.write(u"\7\16\2\2z{\5\30\r\2{|\7\n\2\2|~\3\2\2\2}z\3\2\2\2~\u0081")
        buf.write(u"\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3")
        buf.write(u"\2\2\2\u0081\177\3\2\2\2\u0082\u0083\5\30\r\2\u0083\21")
        buf.write(u"\3\2\2\2\u0084\u0085\5\24\13\2\u0085\u0086\7\22\2\2\u0086")
        buf.write(u"\u0087\5\22\n\2\u0087\u008a\3\2\2\2\u0088\u008a\5\24")
        buf.write(u"\13\2\u0089\u0084\3\2\2\2\u0089\u0088\3\2\2\2\u008a\23")
        buf.write(u"\3\2\2\2\u008b\u008c\5\32\16\2\u008c\u008d\5\26\f\2\u008d")
        buf.write(u"\u008e\5\34\17\2\u008e\u008f\7\23\2\2\u008f\u0090\5\24")
        buf.write(u"\13\2\u0090\u0096\3\2\2\2\u0091\u0092\5\32\16\2\u0092")
        buf.write(u"\u0093\5\26\f\2\u0093\u0094\5\34\17\2\u0094\u0096\3\2")
        buf.write(u"\2\2\u0095\u008b\3\2\2\2\u0095\u0091\3\2\2\2\u0096\25")
        buf.write(u"\3\2\2\2\u0097\u0098\t\2\2\2\u0098\27\3\2\2\2\u0099\u009a")
        buf.write(u"\7\33\2\2\u009a\31\3\2\2\2\u009b\u009c\7\33\2\2\u009c")
        buf.write(u"\33\3\2\2\2\u009d\u00a1\5\36\20\2\u009e\u00a1\5 \21\2")
        buf.write(u"\u009f\u00a1\7\34\2\2\u00a0\u009d\3\2\2\2\u00a0\u009e")
        buf.write(u"\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\35\3\2\2\2\u00a2\u00a3")
        buf.write(u"\t\3\2\2\u00a3\37\3\2\2\2\u00a4\u00a5\t\4\2\2\u00a5!")
        buf.write(u"\3\2\2\2\17\'8?DJYiqw\177\u0089\u0095\u00a0")
        return buf.getvalue()
		

class DatabaseParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'SELECT'", u"'CREATE'", u"'INSERT'", 
                     u"'UPDATE'", u"'DELETE'", u"'DROP'", u"','", u"'*'", 
                     u"'FROM'", u"'WHERE'", u"'TABLE'", u"'INTO'", u"'SET'", 
                     u"'='", u"'OR'", u"'AND'", u"'!='", u"'>'", u"'<'", 
                     u"'>='", u"'<='", u"'true'", u"'false'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"NAME", u"STRING", u"INT", u"FLOAT", 
                      u"LINE_COMMENT", u"BLOCK_COMMENT", u"WS" ]

    RULE_commands = 0
    RULE_command = 1
    RULE_selectStatement = 2
    RULE_createStatement = 3
    RULE_insertStatement = 4
    RULE_updateStatement = 5
    RULE_deleteStatement = 6
    RULE_dropStatement = 7
    RULE_where = 8
    RULE_whereAND = 9
    RULE_operator = 10
    RULE_tableName = 11
    RULE_columnName = 12
    RULE_value = 13
    RULE_number = 14
    RULE_boolean = 15

    ruleNames =  [ u"commands", u"command", u"selectStatement", u"createStatement", 
                   u"insertStatement", u"updateStatement", u"deleteStatement", 
                   u"dropStatement", u"where", u"whereAND", u"operator", 
                   u"tableName", u"columnName", u"value", u"number", u"boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    NAME=25
    STRING=26
    INT=27
    FLOAT=28
    LINE_COMMENT=29
    BLOCK_COMMENT=30
    WS=31

    def __init__(self, input):
        super(DatabaseParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class CommandsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.CommandsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def command(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.CommandContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.CommandContext,i)


        def getRuleIndex(self):
            return DatabaseParser.RULE_commands

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterCommands(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitCommands(self)




    def commands(self):

        localctx = DatabaseParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 32 
                    self.command()
                    self.state = 33
                    self.match(DatabaseParser.T__0) 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 40 
            self.command()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.CommandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def selectStatement(self):
            return self.getTypedRuleContext(DatabaseParser.SelectStatementContext,0)


        def createStatement(self):
            return self.getTypedRuleContext(DatabaseParser.CreateStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(DatabaseParser.InsertStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(DatabaseParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(DatabaseParser.DeleteStatementContext,0)


        def dropStatement(self):
            return self.getTypedRuleContext(DatabaseParser.DropStatementContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_command

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterCommand(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitCommand(self)




    def command(self):

        localctx = DatabaseParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 54
            token = self._input.LA(1)
            if token in [DatabaseParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(DatabaseParser.T__1)
                self.state = 43 
                self.selectStatement()

            elif token in [DatabaseParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(DatabaseParser.T__2)
                self.state = 45 
                self.createStatement()

            elif token in [DatabaseParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(DatabaseParser.T__3)
                self.state = 47 
                self.insertStatement()

            elif token in [DatabaseParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(DatabaseParser.T__4)
                self.state = 49 
                self.updateStatement()

            elif token in [DatabaseParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(DatabaseParser.T__5)
                self.state = 51 
                self.deleteStatement()

            elif token in [DatabaseParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(DatabaseParser.T__6)
                self.state = 53 
                self.dropStatement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.SelectStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DatabaseParser.TableNameContext,0)


        def columnName(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.ColumnNameContext,i)


        def where(self):
            return self.getTypedRuleContext(DatabaseParser.WhereContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_selectStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitSelectStatement(self)




    def selectStatement(self):

        localctx = DatabaseParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            token = self._input.LA(1)
            if token in [DatabaseParser.NAME]:
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 56 
                        self.columnName()
                        self.state = 57
                        self.match(DatabaseParser.T__7) 
                    self.state = 63
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 64 
                self.columnName()

            elif token in [DatabaseParser.T__8]:
                self.state = 65
                self.match(DatabaseParser.T__8)

            else:
                raise NoViableAltException(self)

            self.state = 68
            self.match(DatabaseParser.T__9)
            self.state = 69 
            self.tableName()
            self.state = 72
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 70
                self.match(DatabaseParser.T__10)
                self.state = 71 
                self.where()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.CreateStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DatabaseParser.TableNameContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_createStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterCreateStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitCreateStatement(self)




    def createStatement(self):

        localctx = DatabaseParser.CreateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_createStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(DatabaseParser.T__11)
            self.state = 75 
            self.tableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InsertStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.InsertStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DatabaseParser.TableNameContext,0)


        def columnName(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.ColumnNameContext,i)


        def value(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.ValueContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.ValueContext,i)


        def getRuleIndex(self):
            return DatabaseParser.RULE_insertStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitInsertStatement(self)




    def insertStatement(self):

        localctx = DatabaseParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_insertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(DatabaseParser.T__12)
            self.state = 78 
            self.tableName()
            self.state = 79
            self.match(DatabaseParser.T__13)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80 
                    self.columnName()
                    self.state = 81
                    self.match(DatabaseParser.T__14)
                    self.state = 82 
                    self.value()
                    self.state = 83
                    self.match(DatabaseParser.T__7) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 90 
            self.columnName()
            self.state = 91
            self.match(DatabaseParser.T__14)
            self.state = 92 
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UpdateStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.UpdateStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DatabaseParser.TableNameContext,0)


        def columnName(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.ColumnNameContext,i)


        def value(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.ValueContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.ValueContext,i)


        def where(self):
            return self.getTypedRuleContext(DatabaseParser.WhereContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_updateStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitUpdateStatement(self)




    def updateStatement(self):

        localctx = DatabaseParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self.tableName()
            self.state = 95
            self.match(DatabaseParser.T__13)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96 
                    self.columnName()
                    self.state = 97
                    self.match(DatabaseParser.T__14)
                    self.state = 98 
                    self.value()
                    self.state = 99
                    self.match(DatabaseParser.T__7) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 106 
            self.columnName()
            self.state = 107
            self.match(DatabaseParser.T__14)
            self.state = 108 
            self.value()
            self.state = 111
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 109
                self.match(DatabaseParser.T__10)
                self.state = 110 
                self.where()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.DeleteStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DatabaseParser.TableNameContext,0)


        def where(self):
            return self.getTypedRuleContext(DatabaseParser.WhereContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_deleteStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitDeleteStatement(self)




    def deleteStatement(self):

        localctx = DatabaseParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(DatabaseParser.T__9)
            self.state = 114 
            self.tableName()
            self.state = 117
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 115
                self.match(DatabaseParser.T__10)
                self.state = 116 
                self.where()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DropStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.DropStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tableName(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.TableNameContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.TableNameContext,i)


        def getRuleIndex(self):
            return DatabaseParser.RULE_dropStatement

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterDropStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitDropStatement(self)




    def dropStatement(self):

        localctx = DatabaseParser.DropStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dropStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(DatabaseParser.T__11)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120 
                    self.tableName()
                    self.state = 121
                    self.match(DatabaseParser.T__7) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 128 
            self.tableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhereContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.WhereContext, self).__init__(parent, invokingState)
            self.parser = parser

        def whereAND(self):
            return self.getTypedRuleContext(DatabaseParser.WhereANDContext,0)


        def where(self):
            return self.getTypedRuleContext(DatabaseParser.WhereContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_where

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterWhere(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitWhere(self)




    def where(self):

        localctx = DatabaseParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where)
        try:
            self.state = 135
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130 
                self.whereAND()
                self.state = 131
                self.match(DatabaseParser.T__15)
                self.state = 132 
                self.where()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134 
                self.whereAND()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhereANDContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.WhereANDContext, self).__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(DatabaseParser.ColumnNameContext,0)


        def operator(self):
            return self.getTypedRuleContext(DatabaseParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(DatabaseParser.ValueContext,0)


        def whereAND(self):
            return self.getTypedRuleContext(DatabaseParser.WhereANDContext,0)


        def getRuleIndex(self):
            return DatabaseParser.RULE_whereAND

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterWhereAND(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitWhereAND(self)




    def whereAND(self):

        localctx = DatabaseParser.WhereANDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whereAND)
        try:
            self.state = 147
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137 
                self.columnName()
                self.state = 138 
                self.operator()
                self.state = 139 
                self.value()
                self.state = 140
                self.match(DatabaseParser.T__16)
                self.state = 141 
                self.whereAND()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143 
                self.columnName()
                self.state = 144 
                self.operator()
                self.state = 145 
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatabaseParser.RULE_operator

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitOperator(self)




    def operator(self):

        localctx = DatabaseParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DatabaseParser.T__14) | (1 << DatabaseParser.T__17) | (1 << DatabaseParser.T__18) | (1 << DatabaseParser.T__19) | (1 << DatabaseParser.T__20) | (1 << DatabaseParser.T__21))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TableNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.TableNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DatabaseParser.NAME, 0)

        def getRuleIndex(self):
            return DatabaseParser.RULE_tableName

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterTableName(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitTableName(self)




    def tableName(self):

        localctx = DatabaseParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(DatabaseParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumnNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.ColumnNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DatabaseParser.NAME, 0)

        def getRuleIndex(self):
            return DatabaseParser.RULE_columnName

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterColumnName(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitColumnName(self)




    def columnName(self):

        localctx = DatabaseParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(DatabaseParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.ValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(DatabaseParser.NumberContext,0)


        def boolean(self):
            return self.getTypedRuleContext(DatabaseParser.BooleanContext,0)


        def STRING(self):
            return self.getToken(DatabaseParser.STRING, 0)

        def getRuleIndex(self):
            return DatabaseParser.RULE_value

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterValue(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitValue(self)




    def value(self):

        localctx = DatabaseParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_value)
        try:
            self.state = 158
            token = self._input.LA(1)
            if token in [DatabaseParser.INT, DatabaseParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155 
                self.number()

            elif token in [DatabaseParser.T__22, DatabaseParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156 
                self.boolean()

            elif token in [DatabaseParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(DatabaseParser.STRING)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(DatabaseParser.INT, 0)

        def FLOAT(self):
            return self.getToken(DatabaseParser.FLOAT, 0)

        def getRuleIndex(self):
            return DatabaseParser.RULE_number

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitNumber(self)




    def number(self):

        localctx = DatabaseParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==DatabaseParser.INT or _la==DatabaseParser.FLOAT):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.BooleanContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatabaseParser.RULE_boolean

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterBoolean(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitBoolean(self)




    def boolean(self):

        localctx = DatabaseParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==DatabaseParser.T__22 or _la==DatabaseParser.T__23):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




