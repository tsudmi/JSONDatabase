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
        buf.write(u"\36\u009f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2")
        buf.write(u"\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\5\3\63\n\3\3\4\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\3\4")
        buf.write(u"\5\4>\n\4\3\4\3\4\3\4\3\4\5\4D\n\4\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\7\5L\n\5\f\5\16\5O\13\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\7\6\\\n\6\f\6\16\6_\13\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7l\n\7\f\7\16")
        buf.write(u"\7o\13\7\3\7\3\7\3\7\3\7\3\7\5\7v\n\7\3\b\3\b\3\b\3\b")
        buf.write(u"\5\b|\n\b\3\t\3\t\3\t\7\t\u0081\n\t\f\t\16\t\u0084\13")
        buf.write(u"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\7\n\u008d\n\n\f\n\16\n")
        buf.write(u"\u0090\13\n\3\13\3\13\3\13\5\13\u0095\n\13\3\f\3\f\3")
        buf.write(u"\f\3\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20")
        buf.write(u"\22\24\26\30\32\2\5\3\2\25\26\3\2\27\27\3\2\30\31\u00a3")
        buf.write(u"\2!\3\2\2\2\4\62\3\2\2\2\6=\3\2\2\2\bE\3\2\2\2\nS\3\2")
        buf.write(u"\2\2\fd\3\2\2\2\16w\3\2\2\2\20}\3\2\2\2\22\u0087\3\2")
        buf.write(u"\2\2\24\u0094\3\2\2\2\26\u0096\3\2\2\2\30\u009a\3\2\2")
        buf.write(u"\2\32\u009c\3\2\2\2\34\35\5\4\3\2\35\36\7\3\2\2\36 \3")
        buf.write(u"\2\2\2\37\34\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2")
        buf.write(u"\"$\3\2\2\2#!\3\2\2\2$%\5\4\3\2%\3\3\2\2\2&\'\7\4\2\2")
        buf.write(u"\'\63\5\6\4\2()\7\5\2\2)\63\5\b\5\2*+\7\6\2\2+\63\5\n")
        buf.write(u"\6\2,-\7\7\2\2-\63\5\f\7\2./\7\b\2\2/\63\5\16\b\2\60")
        buf.write(u"\61\7\t\2\2\61\63\5\20\t\2\62&\3\2\2\2\62(\3\2\2\2\62")
        buf.write(u"*\3\2\2\2\62,\3\2\2\2\62.\3\2\2\2\62\60\3\2\2\2\63\5")
        buf.write(u"\3\2\2\2\64\65\7\32\2\2\65\67\7\n\2\2\66\64\3\2\2\2\67")
        buf.write(u":\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;")
        buf.write(u">\7\32\2\2<>\7\13\2\2=8\3\2\2\2=<\3\2\2\2>?\3\2\2\2?")
        buf.write(u"@\7\f\2\2@C\7\32\2\2AB\7\r\2\2BD\5\22\n\2CA\3\2\2\2C")
        buf.write(u"D\3\2\2\2D\7\3\2\2\2EF\7\16\2\2FG\7\32\2\2GH\7\17\2\2")
        buf.write(u"HM\7\20\2\2IJ\7\32\2\2JL\7\n\2\2KI\3\2\2\2LO\3\2\2\2")
        buf.write(u"MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7\32\2\2Q")
        buf.write(u"R\7\21\2\2R\t\3\2\2\2ST\7\22\2\2TU\7\32\2\2U]\7\23\2")
        buf.write(u"\2VW\7\32\2\2WX\7\24\2\2XY\5\24\13\2YZ\7\n\2\2Z\\\3\2")
        buf.write(u"\2\2[V\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2")
        buf.write(u"\2_]\3\2\2\2`a\7\32\2\2ab\7\24\2\2bc\5\24\13\2c\13\3")
        buf.write(u"\2\2\2de\7\32\2\2em\7\23\2\2fg\7\32\2\2gh\7\24\2\2hi")
        buf.write(u"\5\24\13\2ij\7\n\2\2jl\3\2\2\2kf\3\2\2\2lo\3\2\2\2mk")
        buf.write(u"\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq\7\32\2\2qr\7")
        buf.write(u"\24\2\2ru\5\24\13\2st\7\r\2\2tv\5\22\n\2us\3\2\2\2uv")
        buf.write(u"\3\2\2\2v\r\3\2\2\2wx\7\f\2\2x{\7\32\2\2yz\7\r\2\2z|")
        buf.write(u"\5\22\n\2{y\3\2\2\2{|\3\2\2\2|\17\3\2\2\2}\u0082\7\16")
        buf.write(u"\2\2~\177\7\32\2\2\177\u0081\7\n\2\2\u0080~\3\2\2\2\u0081")
        buf.write(u"\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2")
        buf.write(u"\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086")
        buf.write(u"\7\32\2\2\u0086\21\3\2\2\2\u0087\u0088\7\32\2\2\u0088")
        buf.write(u"\u0089\7\24\2\2\u0089\u008e\5\24\13\2\u008a\u008b\t\2")
        buf.write(u"\2\2\u008b\u008d\5\22\n\2\u008c\u008a\3\2\2\2\u008d\u0090")
        buf.write(u"\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write(u"\23\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0095\5\30\r\2")
        buf.write(u"\u0092\u0095\5\32\16\2\u0093\u0095\5\26\f\2\u0094\u0091")
        buf.write(u"\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write(u"\25\3\2\2\2\u0096\u0097\7\27\2\2\u0097\u0098\n\3\2\2")
        buf.write(u"\u0098\u0099\7\27\2\2\u0099\27\3\2\2\2\u009a\u009b\7")
        buf.write(u"\33\2\2\u009b\31\3\2\2\2\u009c\u009d\t\4\2\2\u009d\33")
        buf.write(u"\3\2\2\2\17!\628=CM]mu{\u0082\u008e\u0094")
        return buf.getvalue()
		

class DatabaseParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'SELECT'", u"'CREATE'", u"'INSERT'", 
                     u"'UPDATE'", u"'DELETE'", u"'DROP'", u"','", u"'*'", 
                     u"'FROM'", u"'WHERE'", u"'TABLE'", u"'VALUES'", u"'('", 
                     u"')'", u"'INTO'", u"'SET'", u"'='", u"'AND'", u"'OR'", 
                     u"'\"'", u"'true'", u"'false'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"NAME", u"NUMBER", u"LINE_COMMENT", u"BLOCK_COMMENT", 
                      u"WS" ]

    RULE_commands = 0
    RULE_command = 1
    RULE_selectStatement = 2
    RULE_createStatement = 3
    RULE_insertStatement = 4
    RULE_updateStatement = 5
    RULE_deleteStatement = 6
    RULE_dropStatement = 7
    RULE_where = 8
    RULE_value = 9
    RULE_string = 10
    RULE_number = 11
    RULE_boolean = 12

    ruleNames =  [ u"commands", u"command", u"selectStatement", u"createStatement", 
                   u"insertStatement", u"updateStatement", u"deleteStatement", 
                   u"dropStatement", u"where", u"value", u"string", u"number", 
                   u"boolean" ]

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
    NAME=24
    NUMBER=25
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 26 
                    self.command()
                    self.state = 27
                    self.match(DatabaseParser.T__0) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 34 
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
            self.state = 48
            token = self._input.LA(1)
            if token in [DatabaseParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(DatabaseParser.T__1)
                self.state = 37 
                self.selectStatement()

            elif token in [DatabaseParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(DatabaseParser.T__2)
                self.state = 39 
                self.createStatement()

            elif token in [DatabaseParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(DatabaseParser.T__3)
                self.state = 41 
                self.insertStatement()

            elif token in [DatabaseParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.match(DatabaseParser.T__4)
                self.state = 43 
                self.updateStatement()

            elif token in [DatabaseParser.T__5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(DatabaseParser.T__5)
                self.state = 45 
                self.deleteStatement()

            elif token in [DatabaseParser.T__6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.match(DatabaseParser.T__6)
                self.state = 47 
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
            self.state = 59
            token = self._input.LA(1)
            if token in [DatabaseParser.NAME]:
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 50
                        self.match(DatabaseParser.NAME)
                        self.state = 51
                        self.match(DatabaseParser.T__7) 
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 57
                self.match(DatabaseParser.NAME)

            elif token in [DatabaseParser.T__8]:
                self.state = 58
                self.match(DatabaseParser.T__8)

            else:
                raise NoViableAltException(self)

            self.state = 61
            self.match(DatabaseParser.T__9)
            self.state = 62
            self.match(DatabaseParser.NAME)
            self.state = 65
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 63
                self.match(DatabaseParser.T__10)
                self.state = 64 
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
            self.state = 67
            self.match(DatabaseParser.T__11)
            self.state = 68
            self.match(DatabaseParser.NAME)
            self.state = 69
            self.match(DatabaseParser.T__12)
            self.state = 70
            self.match(DatabaseParser.T__13)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(DatabaseParser.NAME)
                    self.state = 72
                    self.match(DatabaseParser.T__7) 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 78
            self.match(DatabaseParser.NAME)
            self.state = 79
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
            self.state = 81
            self.match(DatabaseParser.T__15)
            self.state = 82
            self.match(DatabaseParser.NAME)
            self.state = 83
            self.match(DatabaseParser.T__16)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self.match(DatabaseParser.NAME)
                    self.state = 85
                    self.match(DatabaseParser.T__17)
                    self.state = 86 
                    self.value()
                    self.state = 87
                    self.match(DatabaseParser.T__7) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 94
            self.match(DatabaseParser.NAME)
            self.state = 95
            self.match(DatabaseParser.T__17)
            self.state = 96 
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

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(DatabaseParser.NAME)
            else:
                return self.getToken(DatabaseParser.NAME, i)

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
            self.state = 98
            self.match(DatabaseParser.NAME)
            self.state = 99
            self.match(DatabaseParser.T__16)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self.match(DatabaseParser.NAME)
                    self.state = 101
                    self.match(DatabaseParser.T__17)
                    self.state = 102 
                    self.value()
                    self.state = 103
                    self.match(DatabaseParser.T__7) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 110
            self.match(DatabaseParser.NAME)
            self.state = 111
            self.match(DatabaseParser.T__17)
            self.state = 112 
            self.value()
            self.state = 115
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 113
                self.match(DatabaseParser.T__10)
                self.state = 114 
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
            self.state = 117
            self.match(DatabaseParser.T__9)
            self.state = 118
            self.match(DatabaseParser.NAME)
            self.state = 121
            _la = self._input.LA(1)
            if _la==DatabaseParser.T__10:
                self.state = 119
                self.match(DatabaseParser.T__10)
                self.state = 120 
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
            self.state = 123
            self.match(DatabaseParser.T__11)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 124
                    self.match(DatabaseParser.NAME)
                    self.state = 125
                    self.match(DatabaseParser.T__7) 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 131
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

        def value(self):
            return self.getTypedRuleContext(DatabaseParser.ValueContext,0)


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
            self.state = 133
            self.match(DatabaseParser.NAME)
            self.state = 134
            self.match(DatabaseParser.T__17)
            self.state = 135 
            self.value()
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    _la = self._input.LA(1)
                    if not(_la==DatabaseParser.T__18 or _la==DatabaseParser.T__19):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 137 
                    self.where() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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


        def string(self):
            return self.getTypedRuleContext(DatabaseParser.StringContext,0)


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
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 146
            token = self._input.LA(1)
            if token in [DatabaseParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143 
                self.number()

            elif token in [DatabaseParser.T__21, DatabaseParser.T__22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144 
                self.boolean()

            elif token in [DatabaseParser.T__20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145 
                self.string()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DatabaseParser.StringContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DatabaseParser.RULE_string

        def enterRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.enterString(self)

        def exitRule(self, listener):
            if isinstance( listener, DatabaseListener ):
                listener.exitString(self)




    def string(self):

        localctx = DatabaseParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(DatabaseParser.T__20)
            self.state = 149
            _la = self._input.LA(1)
            if _la <= 0 or _la==DatabaseParser.T__20:
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 150
            self.match(DatabaseParser.T__20)
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

        def NUMBER(self):
            return self.getToken(DatabaseParser.NUMBER, 0)

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
        self.enterRule(localctx, 22, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(DatabaseParser.NUMBER)
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
        self.enterRule(localctx, 24, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==DatabaseParser.T__21 or _la==DatabaseParser.T__22):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




