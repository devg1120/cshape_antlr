import sys
from antlr4 import *
#from ExprLexer import ExprLexer
#from ExprParser import ExprParser
from grammar.CSharpLexer import CSharpLexer
from grammar.CSharpParser import CSharpParser

from _ListenerInterp import ListenerInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)
    #tree = parser.start_()
    tree = parser.compilation_unit()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        linterp = ListenerInterp()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)

if __name__ == '__main__':
    main(sys.argv)

