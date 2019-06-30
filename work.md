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



w załączniku przesyłam wytyczne do projektu.
Jeśli chodzi o bardziej szczegółowy opis -
aplikacja powinna przeskanować tokeny, które przeszły analizę leksykalną,
 tzn. jeśli lekser odnalazł w danej linii błąd, linia nie powinna trafić już do analizy syntaktycznej.
Trzeba zczytać tokeny z jednej linii i rozłożyć je na "czynniki pierwsze".
 W załączonym pliku znajduje się lista "produkcji", czyli dozwolonych sposobów rozkładania wyrażenia.
Weźmy krótki przykład, np. linię x*y Tokenami są identyfikator x, operator * i identyfikator y.
Każdą linię z tekstu traktujemy jako W, czyli wyrażenie. W naszym przypadku "W" możemy rozłożyć na 3 sposoby:
W => W+S
W => W-S
W => S
Przyjmujemy, że naszym W jest x*y.
Możemy dokonać parsowania na różne sposoby. Ja wykorzystam parsowanie "od lewej".
 Pierwsze dwie produkcje nie pasują, ponieważ w ciągu nie ma symboli terminalnych + i -.
Ostatnią nadzieją jest ostatnia dozwolona produkcja. Przyjmujemy więc W => S, a więc naszym S jest x*y.
Symbol nieterminalny S możemy rozłożyć z produkcji S => S*C.
S => S * C
S =  x * y
W wyniku takiego rozkładu otrzymujemy 2 symbole nieterminalne - nowe S które zawiera tylko symbol x, i C,
 które zawiera symbol y. Symbole nieterminalne musimy rozkładać dalej.
  Operator mnożenia jest symbolem terminalnym, dlatego nie musimy go już dalej brać pod uwagę.
Z tego miejsca rozkład nie jest już skomplikowany:
S = x
Korzystamy z reguły S => C, a następnie C => identyfikator. 
Ta gałąź rozkładu zakończyła się symbolem terminalnym, więc wszystko jest w porządku.
Druga gałąź jest jeszcze krótsza.
C = y
Korzystamy z reguły C => identyfikator.
Udało się rozłożyć wyrażenie do symboli terminalnych, a więc wyrażenie jest poprawne.
Na zajęciach zalecałem stworzenie funkcji W(), S() i C(),
 które usiłują przetworzyć ciąg tokenów zgodnie z ustalonymi produkcjami. 
 Jeśli im się to uda - linia przechodzi analizę syntaktyczną.
Nie ukrywam, że trudno jest to wyjaśnić w mailu. Jeśli coś wciąż będzie niejasne, proszę się nie zniechęcać. 
Postaram się odpowiedzieć na wszystkie pytania.
Może Pan również zapoznać się samodzielnie z jedną z metod parsowania. Proszę poczytać o metodzie LALR.
Ciężko mi polecić jedno "najlepsze" źródło wiedzy na ten temat. Każda strona opisuje tą metodę nieco innymi słowami.