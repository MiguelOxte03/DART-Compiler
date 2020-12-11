import sys
import ply.lex as lex

# TOKENS
tokens = (
    # Reserverd Words
    # https://dart.dev/guides/language/language-tour
    "CASE",
    "CLASS",
    "CONST",
    "PRINT",
    "DO",
    "BREAK",
    "FOR",
    "SWITCH",
    "WHILE",
    "IF",
    "ELSE",
    "STRING",
    "STATIC",
    "RETURN",
    "MAIN",
    "VAR",
    # Boolean
    "TRUE",
    "FALSE",
    # Type of data
    # Symbols
    "PLUS",
    "PLUSPLUS",
    "PLUSEQUAL",
    "MINUS",
    "MINUSMINUS",
    "MINUSEQUAL",
    "TIMES",
    "DIVIDE",
    "LESS",
    "LESSEQUAL",
    "GREATER",
    "GREATEREQUAL",
    "EQUAL",
    "DEQUAL",
    "DISTINT",
    "ISEQUAL",
    "SEMI",
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "LBLOCK",
    "RBLOCK",
    "COLON",
    "DOT",
    "QUOTES",
    "APOSTROPHE",
    # Others
    "COMMENTS",
    "COMMENTS_C99",
    "ID",
    "IDVAR",
    "NUM",
    "VOID",
)
# Ignore Characters
t_ignore = "\t"


def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")


def t_VOID(t):
    r"void|VOID"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Illegal character" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)


# RE Tokens
# palabras reservadas
def t_CASE(t):
    r"case"
    return t


def t_CLASS(t):
    r"class"
    return t


def t_CONST(t):
    r"conts"
    return t


def t_PRINT(t):
    r"print"
    return t


def t_DO(t):
    r"do"
    return t


def t_FOR(t):
    r"for"
    return t


def t_BREAK(t):
    r"break"
    return t


def t_SWITCH(t):
    r"switch"
    return t


def t_WHILE(t):
    r"while"
    return t


def t_IF(t):
    r"if"
    return t


def t_ELSE(t):
    r"else"
    return t


def t_STATIC(t):
    r"static"
    return


def t_RETURN(t):
    r"return"
    return t


def t_MAIN(t):
    r"main"
    return t


def t_VAR(t):
    r"var"
    return


#  RE SÍMBOLOS
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_EQUAL = r"="
t_DISTINT = r"!"
t_LESS = r"<"
t_GREATER = r">"
t_SEMI = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBLOCK = r"{"
t_RBLOCK = r"}"
t_COLON = r":"
t_DOT = r"\."
t_QUOTES = r"\""
t_APOSTROPHE = r"\' "


def t_LESSEQUAL(t):
    r"<="
    return t


def t_GREATEREQUAL(t):
    r">="
    return t


def t_DEQUAL(t):
    r"!="
    return t


def t_ISEQUAL(t):
    r"=="
    return t


def t_MINUSMINUS(t):
    r"--"
    return t


def t_PLUSPLUS(t):
    r"\+\+"
    return t


# RE OTHERS
def t_COMMENTS(t):
    r"\/\*([^*]|\*[^\/])*(\*)+\/"
    t.lexer.lineno += t.value.count("\n")


def t_COMMENTS_C99(t):
    r"(\/\/|\#)(.)*?\n"
    t.lexer.lineno += 1


def t_IDVAR(t):
    r"\$\w+(\d\w)*"
    return t


def t_NUM(t):
    r"\d+(\.\d+)?"
    t.valor = float(t.value)
    return t


def t_ID(t):
    r"\w+(\w\d)*"
    return t


def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]

        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27) + "[0;36m" + "INICIA ANALISIS LEXICO" + chr(27) + "[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(
                "\t"
                + str(i)
                + " - "
                + "Line: "
                + str(tok.lineno)
                + "\t"
                + str(tok.type)
                + "\t-->  "
                + str(tok.value)
            )
            i += 1

        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")

    else:
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp DART como parametro")
        print(
            chr(27)
            + "[0;36m"
            + "\t$ python DART-Compiler.py"
            + chr(27)
            + "[1;31m"
            + " <filename>.dart"
            + chr(27)
            + "[0m"
        )