


#########################################

https://github.com/antlr/antlr4/blob/master/doc/getting-started.md
https://github.com/antlr/antlr4/blob/4.6/doc/python-target.md


pip install antlr4-tools

$ antlr4 

pip install antlr4-python3-runtime

git clone https://github.com/antlr/grammars-v4

ls grammars-v4/csharp/*.g4

mkdir grammar

cp grammars-v4/csharp/*.g4 grammar

antlr4  -Dlanguage=Python3 grammar/*.g4
$ ls -1 grammar/*.py
grammar/CSharpLexer.py
grammar/CSharpParser.py
grammar/CSharpParserListener.py
grammar/CSharpPreprocessorParser.py
grammar/CSharpPreprocessorParserListener.py


$ antlr4 -visitor -listener -Dlanguage=Python3 grammar/*.g4
$  ls -1 grammar/*.py
grammar/CSharpLexer.py
grammar/CSharpParser.py
grammar/CSharpParserListener.py
grammar/CSharpParserVisitor.py
grammar/CSharpPreprocessorParser.py
grammar/CSharpPreprocessorParserListener.py
grammar/CSharpPreprocessorParserVisitor.py

 1062  python _Driver-Listener.py ./ObjectEditor.cs
 1063  python _Driver-Visitor.py ./ObjectEditor.cs

