alphabet [A-Za-z]
digit [0-9]

%%
[ \t] ;
"{" 	{open1(); return '{';}
"}"	{close1(); return '}';}
void	{yylval.ival = VOID; return VOID;}
int	{yylval.ival = INT; return INT;}
float	{yylval.ival = FLOAT; return float;}
else	return ELSE;
do	return DO;
if	retrurn IF;
struct	return STRUCT;
^"#include ".+	return PREPROC;
while	return WHILE;
for 	return FOR; 
return 	return RETURN;
printf	return PRINT;
{alpha}({alpha}|{digit}*{yylval.str=strdup(yytext);	return ID;}
{digit}+	{yylval.str=strdup(yytext);		return NUM;}
{digit}+\.{digit}+	{yylval.str=strdup(yytext);	return REAL;}
"<="		return LE;
">=

\n {yylineno++;}
