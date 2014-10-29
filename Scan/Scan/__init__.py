import sys

global charclass, lexlen, token, lexeme, nextchar, nexttoken

token = 0; nexttoken = 0; lexlen = 0; nextchar = ""; charclass = ""; lexeme = "";

global LETTER, DIGIT, UNKNOWN, EOF, INT_LIT, IDENT, ASSIGN_OP, ADD_OP, SUB_OP, MULT_OP, DIV_OP, LEFT_PAREN, RIGHT_PAREN, PARSE

LETTER = 0; DIGIT = 1; UNKNOWN = 99; EOF = -1; INT_LIT = 10; IDENT = 11; ASSIGN_OP = 20; ADD_OP = 21;
SUB_OP = 22; MULT_OP = 23; DIV_OP = 24; LEFT_PAREN = 25; RIGHT_PAREN = 26; PARSE = 0;

global input_file

def addchar():
    global lexeme , lexlen
    lexlen = lexlen + 1;
    if(lexlen <= 98):
        lexeme = lexeme + nextchar;
    else:
        print "Error : Lexeme is too Long"

def lookup(ch):
    global nexttoken, lexeme
    if (ch == "("):
        addchar();
        nexttoken = LEFT_PAREN;
    elif (ch == ")"):
        addchar();
        nexttoken = RIGHT_PAREN;
    elif (ch == "+"):
        addchar();
        nexttoken=ADD_OP;
    elif (ch == "-"):
        addchar();
        nexttoken=SUB_OP;
    elif (ch == "*"):
        addchar();
        nexttoken=MULT_OP;
    elif (ch == "/"):
        addchar();
        nexttoken=DIV_OP;
    else:
        addchar();
        nexttoken = EOF;
        lexeme = "EOF";
    return nexttoken
def getChar():
    global nextchar, charclass
    nextchar = input_file.read(1);
    if(nextchar != ""):
        if (nextchar.isalpha()):
            charclass = LETTER;
        elif nextchar.isdigit():
            charclass = DIGIT;
        else:
            charclass = UNKNOWN;
    else:
        charclass = EOF;

def getnonblank():
    while nextchar.isspace():
        getChar();

def lex():
    global nexttoken, lexeme
    lexeme = "";
    getnonblank();
    if (charclass == LETTER):
        addchar();
        getChar();
        while(charclass == LETTER or charclass == DIGIT):
            addchar();
            getChar();
        nexttoken = IDENT;
    elif (charclass == DIGIT):
        addchar();
        getChar();
        while(charclass == DIGIT):
            addchar();
            getChar();
        nexttoken = INT_LIT;
    elif (charclass == UNKNOWN):
        lookup(nextchar);
        getChar();
    elif (charclass == EOF):
        nexttoken = EOF;
        lexeme = "EOF";
    print "next token is:", nexttoken ,", next lexeme is:", lexeme
    return nexttoken;

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            input_file = open(sys.argv[1], "r");
            PARSE = 1;
        elif len(sys.argv) == 1:
            input_file = open("front.txt", "r")
            PARSE = 1;
        else:
            print "usage: \n python front.py [file to parse (optional, default=front.txt)]"
    except IOError:
        if len(sys.argv) == 2:
            print "file not found", sys.argv[1]
        else:
            print "file not found: front.txt"
    except:
        print "UnExpected error "
    if PARSE:
        getChar();
        lex();
        while (nexttoken != EOF):
            lex();
        input_file.close();
 
