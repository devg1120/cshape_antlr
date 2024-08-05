
import sys
from antlr4 import *
from grammar.CSharpLexer import CSharpLexer
from grammar.CSharpParser import CSharpParser
#from .grammar import CSharpLexer 
#from .grammar import CSharpParser 
from _VisitorInterp import VisitorInterp


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
        vinterp = VisitorInterp()
        vinterp.visit(tree)

if __name__ == '__main__':
    main(sys.argv)



