import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class VisitorInterp(ExprVisitor):
    def __init__(self):
        self.lv = 0
    # Visit a parse tree produced by ExprParser#start_.
    def visitStart_(self, ctx:ExprParser.Start_Context):
        print(" start")
        #return self.visitChildren(ctx)
        self.lv += 1
        self.visitChildren(ctx)
        self.lv -= 1


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext ):
        print(self.lv, " expr" , ctx.getText())
        #return self.visitChildren(ctx)
        self.lv += 1
        self.visitChildren(ctx)
        self.lv -= 1



    # Visit a parse tree produced by ExprParser#atom.
    def visitAtom(self, ctx:ExprParser.AtomContext ):
        print(self.lv," atom", ctx.getText())
        #return self.visitChildren(ctx)
        self.lv += 1
        self.visitChildren(ctx)
        self.lv -= 1


    """
    def visitAtom(self, ctx:ExprParser.AtomContext):
        return int(ctx.getText())

    def visitExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.getChild(1))
            op = ctx.getChild(1).getText()
            v1 = self.visit(ctx.getChild(0))
            v2 = self.visit(ctx.getChild(2))
            if op == "+":
                return v1 + v2
            if op == "-":
                return v1 - v2
            if op == "*":
                return v1 * v2
            if op == "/":
                return v1 / v2
            return 0
        if ctx.getChildCount() == 2:
            opc = ctx.getChild(0).getText()
            if opc == "+":
                return self.visit(ctx.getChild(1))
            if opc == "-":
                return - self.visit(ctx.getChild(1))
            return 0
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return 0

    def visitStart_(self, ctx:ExprParser.Start_Context):
        for i in range(0, ctx.getChildCount(), 2):
            print(self.visit(ctx.getChild(i)))
        return 0
    """
