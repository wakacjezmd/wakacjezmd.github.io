---
layout: page
permalink: /2014/egzamin/1/
---

## 2014 Pierwszy termin

###Zadanie 1
Udowodnij tożsamość

$$\sum_{k}{ n\brack k}{k\brace m} = {n\choose m}\frac{(n-1)!}{(m-1)!}$$

dla \\(n, m > 0\\)

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <b>LEWA:</b> Dzielimy \(n\) elementów na \(k\) cykli, a następnie cykle dzielimy na
      zbiory tak, że żaden zbiór nie może być pusty.
    </p>
    <p>
      <b>PRAWA:</b> Wybieramy \(m\) elementów, które będą początkami słów. Wyróżniamy jeden z nich
      i stawiamy go na pierwszym miejscu, a następnie permutujemy pozostałe \(n-1\) elementów.
      Następnie rozcinamy ten \(n\)-elementowy ciąg przed każdym z wybranych elementów i
      otrzymujemy ciąg \(m\) słów. Podzielenie przez \(m!\) przekształca ten ciąg w zbiór \(m\) słów.
      $${n\choose m}m\frac{(n-1)!}{m!} = {n\choose m}\frac{(n-1)!}{(m-1)!}$$
    </p>
    <p>
      Żeby udowodnić tę równość wskażę bijekcje pomiędzy obiema stronami. Jeżeli mamy już dany jakiś
      podział na cykle i ich zbiory, to popatrzmy na jeden ze zbiórów. Ustalmy że zapisujemy cykle tak,
      że zawsze pierwszy element cyklu jest najmniejszy ze wszystkich, które do niego należą (tak jak w zapisie kanonicznym),
      a w ramach całego zbioru ustawiamy je w kolejności malejącej względem pierwszego elementu.
      Starcie wszystkich nawiasów wyznacza bijekcje między zbiorem cykli, a słowem.
      $$(6)(358)(24) \mapsto 635824$$
      W drugą stronę, jeżeli mamy dane jakieś słowo, to możemy odzyskać zbiór cykli w następujący sposób:
      weźmy pierwszy element słowa i do jego cyklu dopisujmy po kolei następne elementy tak długo, aż
      któryś z nich nie będzie większy niż pierwszy element. Kiedy napotkamy taki, to w tym momencie kończymy cykl
      i powtarzamy procedurę zaczynając od napotkanego elementu.
      $$635824 \mapsto (6)35824 \mapsto (6)(358)24 \mapsto (6)(358)(24)$$
    </p>
</div>
</div>
###Zadanie 2
Znajdź liczbę 6-literowych słów złożonych z liter A, B, C, D, E w
któryc: każda z liter A, B występuje _co najwyżej raz_, a każda z liter 
C, D - _co najmniej raz_.

###Zadanie 3
Wierzchołki grafu \\(G\_n\\) to wszystkie liczby złożone ze zbioru
{1,...,n} a para {i,j} jest krawędzią wtedy i tylko wtedy gdy 
\\(i\perp j\\). Rozstrzygnij czy graf \\(G\_{1000}\\) jest:

a) planarny

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
     Nie, następujące względnie pierwsze liczby: 4, 9, 25, 36, 49
     (kwadraty kolejnych liczb pierwszych) 
     tworzą klikę \(K_5\) co z tw.
     Kuratowskiego oznacza że nie jest planarny.

  </div>
</div>

b) hamiltonowski

c) eulerowski

=======
###Zadanie 4

Uprość wyrażenie \\( \frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)}\\) gdzie \\(c(\pi)\\) to ilość cykli w permutacji \\(\pi\\).
<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
	Grupując elementy podanej sumy na grupki permutacji o takich samych ilościach cykli uzyskujemy, że
	$$ \sum\limits\_{\pi \in S\_k} n^{c(\pi)}=\\
	  \sum\limits\_{i=1}^{k} {k \brack i} n^i   $$
	Zauważmy, że ta suma zlicza nam ilość pokolorowań cykli wszystkich k-permutacji na n kolorów. <br><br>
	Spróbujmy generować takie kolorowania w inny sposób - tworząc permutacje w zapisie kanonicznym cyklowym z kolorom przypisanym cyklom.
	Elementy wstawiamy do cyklu w kolejności od najmniejszego do największego.
	Wstawiając pierwszy element do permutacji może on być pokolorowany na jeden z \\(n\\) kolorów.
	Drugi element może tworzyć nowy cykl i być pokolorowany na jeden z \\(n\\) kolorów,
	bądź stać w cyklu na prawo od elementu pierwszego i mieć taki sam kolor jak on.
	Łatwo widać że w takim wypadku daje nam to \\(n+1\\) możliwości. Uogólniając to rozumowanie, uzyskujemy następującą równość:
	$$   \sum\limits\_{i=1}^{k} {k \brack i} n^i =  n^\overline{k} $$
	Daje nam to odpowiedź:
$$ 	\frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)} = \frac{n^\overline{k}}{k!} $$
	 </p>
  </div>
</div>
