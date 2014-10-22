package Toyscanner;

import java.io.FileReader;
import java.io.IOException;

public class scan extends Codes {
	
	


	 static FileReader inputStream=null;
	    
		 public static void file(FileReader f)
		 {
			 inputStream=f;
			 try {
					getChar();
					   do{
						     lex();                                          
						    }while(nextToken!=EOF);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} 
		 }
	
	public static void addChar()
    {
        
            lexeme=lexeme + nextChar;
        }
    public static void getChar()throws IOException
    {
         nextChar=(char)inputStream.read();  
        if((nextChar)!=EOF) 
     {
      if(Character.isLetter(nextChar))
          charClass=LETTER;
      else if(Character.isDigit(nextChar))
          charClass=DIGIT;
      else charClass=UNKNOWN;
     }
     else charClass=EOF;
    }
    public static void getNonBlank() throws IOException
    {
        while(Character.isSpaceChar(nextChar))
        {
            getChar();
        }
    }

    
    public static int lookup(char ch)
    {
        switch(ch)
        {
                case'(':
                addChar();
                nextToken=LEFT_PAREN;
                break;
                case')':
                addChar();
                nextToken=RIGHT_PAREN;
                break;
                case'+':
                addChar();
                nextToken=ADD_OP;
                break;
                case'-':
                addChar();
                nextToken=SUB_OP;
                break;
                case'*':
                addChar();
                nextToken=MULT_OP;
                break;
                case'/':
                addChar();
                nextToken=DIV_OP;
                break;
                default:
                addChar();
                nextToken=EOF;
                break;
        }
        return nextToken;
    }
	  public static int lex() throws IOException
	    {
	        lexeme="";
	        getNonBlank();
	        switch(charClass)
	        {
	                case LETTER:
	                addChar();
	                getChar();
	                while(charClass==LETTER||charClass==DIGIT){
	                    addChar();
	                    getChar();
	                }
	                nextToken=IDENT;
	                break;
	                case DIGIT:
	                addChar();
	                getChar();
	                while(charClass==DIGIT){
	                    addChar();
	                    getChar();
	                }
	                nextToken=INT_LIT;
	                break;
	                case UNKNOWN:
	                lookup(nextChar);
	                getChar();
	                break;
	                case EOF:
	                nextToken=EOF;
	                lexeme="?";    
	        }
	        System.out.println("Next Token is:"+nextToken+"\tNextLexeme is:"+lexeme);
	        return nextToken;
	        
	    }
}