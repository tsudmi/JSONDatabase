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
        buf.write(u"\36\u0083\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\6\2\30\n\2\r")
        buf.write(u"\2\16\2\31\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\5\3(\n\3\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\4\3\4")
        buf.write(u"\3\4\3\4\5\4\65\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5>")
        buf.write(u"\n\5\f\5\16\5A\13\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\7\6N\n\6\f\6\16\6Q\13\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\7\3\7\3\7\3\7\3\7\3\7\7\7]\n\7\f\7\16\7`\13\7\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\5\7g\n\7\3\b\3\b\3\b\3\b\5\bm\n\b\3\t")
        buf.write(u"\3\t\3\t\7\tr\n\t\f\t\16\tu\13\t\3\t\3\t\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\7\n~\n\n\f\n\16\n\u0081\13\n\3\n\2\2\13\2\4")
        buf.write(u"\6\b\n\f\16\20\22\2\3\3\2\25\26\u0088\2\27\3\2\2\2\4")
        buf.write(u"\'\3\2\2\2\6.\3\2\2\2\b\66\3\2\2\2\nF\3\2\2\2\fV\3\2")
        buf.write(u"\2\2\16h\3\2\2\2\20n\3\2\2\2\22x\3\2\2\2\24\25\5\4\3")
        buf.write(u"\2\25\26\7\3\2\2\26\30\3\2\2\2\27\24\3\2\2\2\30\31\3")
        buf.write(u"\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\34")
        buf.write(u"\7\4\2\2\34(\5\6\4\2\35\36\7\5\2\2\36(\5\b\5\2\37 \7")
        buf.write(u"\6\2\2 (\5\n\6\2!\"\7\7\2\2\"(\5\f\7\2#$\7\b\2\2$(\5")
        buf.write(u"\16\b\2%&\7\t\2\2&(\5\20\t\2\'\33\3\2\2\2\'\35\3\2\2")
        buf.write(u"\2\'\37\3\2\2\2\'!\3\2\2\2\'#\3\2\2\2\'%\3\2\2\2(\5\3")
        buf.write(u"\2\2\2)*\7\27\2\2*+\7\n\2\2+,\3\2\2\2,/\7\27\2\2-/\7")
        buf.write(u"\13\2\2.)\3\2\2\2.-\3\2\2\2/\60\3\2\2\2\60\61\7\f\2\2")
        buf.write(u"\61\64\7\27\2\2\62\63\7\r\2\2\63\65\5\22\n\2\64\62\3")
        buf.write(u"\2\2\2\64\65\3\2\2\2\65\7\3\2\2\2\66\67\7\16\2\2\678")
        buf.write(u"\7\27\2\289\7\17\2\29?\7\20\2\2:;\7\27\2\2;<\7\33\2\2")
        buf.write(u"<>\7\n\2\2=:\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B")
        buf.write(u"\3\2\2\2A?\3\2\2\2BC\7\27\2\2CD\7\33\2\2DE\7\21\2\2E")
        buf.write(u"\t\3\2\2\2FG\7\22\2\2GH\7\27\2\2HO\7\23\2\2IJ\7\27\2")
        buf.write(u"\2JK\7\24\2\2KL\7\30\2\2LN\7\n\2\2MI\3\2\2\2NQ\3\2\2")
        buf.write(u"\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\7\27\2\2")
        buf.write(u"ST\7\24\2\2TU\7\30\2\2U\13\3\2\2\2VW\7\27\2\2W^\7\23")
        buf.write(u"\2\2XY\7\27\2\2YZ\7\24\2\2Z[\7\30\2\2[]\7\n\2\2\\X\3")
        buf.write(u"\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_a\3\2\2\2`^\3\2")
        buf.write(u"\2\2ab\7\27\2\2bc\7\24\2\2cf\7\30\2\2de\7\r\2\2eg\5\22")
        buf.write(u"\n\2fd\3\2\2\2fg\3\2\2\2g\r\3\2\2\2hi\7\f\2\2il\7\27")
        buf.write(u"\2\2jk\7\r\2\2km\5\22\n\2lj\3\2\2\2lm\3\2\2\2m\17\3\2")
        buf.write(u"\2\2ns\7\16\2\2op\7\27\2\2pr\7\n\2\2qo\3\2\2\2ru\3\2")
        buf.write(u"\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\27\2")
        buf.write(u"\2w\21\3\2\2\2xy\7\27\2\2yz\7\24\2\2z\177\7\30\2\2{|")
        buf.write(u"\t\2\2\2|~\5\22\n\2}{\3\2\2\2~\u0081\3\2\2\2\177}\3\2")
        buf.write(u"\2\2\177\u0080\3\2\2\2\u0080\23\3\2\2\2\u0081\177\3\2")
        buf.write(u"\2\2\r\31\'.\64?O^fls\177")
        return buf.getvalue()
		

class DatabaseParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'SELECT'", u"'CREATE'", u"'INSERT'", 
                     u"'UPDATE'", u"'DELETE'", u"'DROP'", u"','", u"'*'", 
                     u"'FROM'", u"'WHERE'", u"'TABLE'", u"'VALUES'", u"'('", 
                     u"')'", u"'INTO'", u"'SET'", u"'='", u"'AND'", u"'OR'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"NAME", u"VALUE", u"STRING", u"NUMBER", 
                      u"TYPE", u"LINE_COMMENT", u"BLOCK_COMMENT", u"WS" ]

    RULE_commands = 0
    RULE_command = 1
    RULE_selectStatement = 2
    RULE_createStatement = 3
    RULE_insertStatement = 4
    RULE_updateStatement = 5
    RULE_deleteStatement = 6
    RULE_dropStatement = 7
    RULE_where = 8

    ruleNames =  [ u"commands", u"command", u"selectStatement", u"createStatement", 
                   u"insertStatement", u"updateStatement", u"deleteStatement", 
                   u"dropStatement", u"where" ]

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
    NAME=21
    VALUE=22
    STRING=23
    NUMBER=24
    TYPE=25
    LINE_COMMENT=26
    BLOCK_COMMENT=27
    WS=28

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18 
                self.command()
                self.state = 19
                self.match(DatabaseParser.T__0)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DatabaseParser.T__1) | (1 << DatabaseParser.T__2) | (1 << DatabaseParser.T__3) | (1 << DatabaseParser.T__4) | (1 << DatabaseParser.T__5) | (1 << DatabaseParser.T__6))) != 0)):
                    break

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
            self.state = 37
            token = self._input.LA(1)
            if token in [DatabaseParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(DatabaseParser.T__1)
                self.state = 26 
                self.selectStatement()

            elif token in [DatabaseParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(DatabaseParser.T__2)
                self.state = 28 
                self.createStatement()

            elif token in [DatabaseParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(DatabaseParser.T__3)
                self.state = 30 
                self.insertStatement()

            elif token in [DatabaseParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(DatabaseParser.T__4)
                self.state = 32 
                self.updateStatement()

            elif token in [DatabaseParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.match(DatabaseParser.T__5)
                self.state = 34 
                self.deleteStatement()

            elif token in [DatabaseParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.match(DatabaseParser.T__6)
                self.state = 36 
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

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
            self.state = 44
            token = self._input.LA(1)
            if token in [DatabaseParser.NAME]:
                self.state = 39
                self.match(DatabaseParser.NAME)
                self.state = 40
                self.match(DatabaseParser.T__7)
                self.state = 42
                self.match(DatabaseParser.NAME)

            elif token in [DatabaseParser.T__8]:
                self.state = 43
                self.match(DatabaseParser.T__8)

            else:
                raise NoViableAltException(self)

            self.state = 46
            self.match(DatabaseParser.T__9)
            self.state = 47
            self.match(DatabaseParser.NAME)
            self.state = 50
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 48
                self.match(DatabaseParser.T__10)
                self.state = 49 
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

        def TYPE(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.TYPE)
            else:
                return self.getToken(DatabaseParser.TYPE, i)

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
            self.state = 52
            self.match(DatabaseParser.T__11)
            self.state = 53
            self.match(DatabaseParser.NAME)
            self.state = 54
            self.match(DatabaseParser.T__12)
            self.state = 55
            self.match(DatabaseParser.T__13)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 56
                    self.match(DatabaseParser.NAME)
                    self.state = 57
                    self.match(DatabaseParser.TYPE)
                    self.state = 58
                    self.match(DatabaseParser.T__7) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 64
            self.match(DatabaseParser.NAME)
            self.state = 65
            self.match(DatabaseParser.TYPE)
            self.state = 66
            self.match(DatabaseParser.T__14)
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

        def VALUE(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.VALUE)
            else:
                return self.getToken(DatabaseParser.VALUE, i)

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
            self.state = 68
            self.match(DatabaseParser.T__15)
            self.state = 69
            self.match(DatabaseParser.NAME)
            self.state = 70
            self.match(DatabaseParser.T__16)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(DatabaseParser.NAME)
                    self.state = 72
                    self.match(DatabaseParser.T__17)
                    self.state = 73
                    self.match(DatabaseParser.VALUE)
                    self.state = 74
                    self.match(DatabaseParser.T__7) 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 80
            self.match(DatabaseParser.NAME)
            self.state = 81
            self.match(DatabaseParser.T__17)
            self.state = 82
            self.match(DatabaseParser.VALUE)
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

        def VALUE(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.VALUE)
            else:
                return self.getToken(DatabaseParser.VALUE, i)

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
            self.state = 84
            self.match(DatabaseParser.NAME)
            self.state = 85
            self.match(DatabaseParser.T__16)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(DatabaseParser.NAME)
                    self.state = 87
                    self.match(DatabaseParser.T__17)
                    self.state = 88
                    self.match(DatabaseParser.VALUE)
                    self.state = 89
                    self.match(DatabaseParser.T__7) 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 95
            self.match(DatabaseParser.NAME)
            self.state = 96
            self.match(DatabaseParser.T__17)
            self.state = 97
            self.match(DatabaseParser.VALUE)
            self.state = 100
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 98
                self.match(DatabaseParser.T__10)
                self.state = 99 
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

        def NAME(self):
            return self.getToken(DatabaseParser.NAME, 0)

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
            self.state = 102
            self.match(DatabaseParser.T__9)
            self.state = 103
            self.match(DatabaseParser.NAME)
            self.state = 106
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 104
                self.match(DatabaseParser.T__10)
                self.state = 105 
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

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
            self.state = 108
            self.match(DatabaseParser.T__11)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self.match(DatabaseParser.NAME)
                    self.state = 110
                    self.match(DatabaseParser.T__7) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 116
            self.match(DatabaseParser.NAME)
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

        def NAME(self):
            return self.getToken(DatabaseParser.NAME, 0)

        def VALUE(self):
            return self.getToken(DatabaseParser.VALUE, 0)

        def where(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DatabaseParser.WhereContext)
            else:
                return self.getTypedRuleContext(DatabaseParser.WhereContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(DatabaseParser.NAME)
            self.state = 119
            self.match(DatabaseParser.T__17)
            self.state = 120
            self.match(DatabaseParser.VALUE)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 121
                    _la = self._input.LA(1)
                    if not(_la==DatabaseParser.T__18 or _la==DatabaseParser.T__19):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 122 
                    self.where() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




