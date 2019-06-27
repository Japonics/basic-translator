Dopuszczalne produkcje,
Parser
Sprawdzić poprawność strumienia tokenów.
W = wyrażenie
S = składnik
C = czynnik
Tokeny nieterminalne: W, S, C
Tokeny terminalne: identyfikator, liczba, +, -, *, /, (, )
Dopuszczalne produkcje:
W = W + S
W = W - S
W = S
S = S * C
S = S / C
S = C
C = liczba
C = identyfikator
C = ( W )


Ja zrozumiałem, że parser ma sprawdzać, czy dany ciąg tokenów jest zgodny z podanymi produkcjami, a więc musimy napisać metody: 
bool is_w_plus_s(IEnumerable<Token> tokens);
bool is_w_minus_s(IEnumerable<Token> tokens);
bool is_s(IEnumerable<Token> tokens); 
//itd.
Żeby nie było za łatwo, parser musi zwracać informację, w którym miejscu w ciągu tokenów jest błąd.
