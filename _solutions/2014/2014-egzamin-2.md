---
layout: page
permalink: /2014/egzamin/2/
---

## 2014 Egzamin poprawkowy

###Zadanie 2

Udowodnij, że podziałów liczby \\(n\\) na cztery części jest tyle samo co podziałów
liczby \\(3n\\) na cztery części rozmiaru co najwyżej \\(n - 1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Żeby udowodnijć to stwierdzenie wskażemy bijekcję między zbiorami podziałów.<br/>
      Weźmy dowolny podział \(n\) na liczby \( \left\{ a_1, a_2, a_3, a_4 \right\}\). Zachodzi:
      $$\sum_{i=1}^4 a_i = n $$
      Teraz rozważmy podział \(\left\{n - a_1, n - a_2, n - a_3, n - a_4\right\}\).
      $$(n - a_1) + (n - a_2) + (n - a_3) + (n - a_4) = 4n - \sum_{i=1}^4 a_i = 3n$$
      Dodatkowo \(\forall_{i}\ 1 \leq a_i \leq n - 1\), więc \(\forall_{i}\ 1 \leq n - a_i \leq n - 1\),
      więc wszystkie warunki są spełnione.
    </p>
  </div>
</div>

###Zadanie 3

Udowodnij, że w dowolnym kolorowaniu grafu \\(G\\) na \\(\chi(G)\\) kolorów istnieje wierzchołek każdego koloru, który ma sąsiadów we wszystkich pozostałych kolorach. 

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
	Załóżmy, że istnieje kolor, taki że każdy wierzchołek tego koloru posiada sąsiadów, którzy nie wyczerpują wszystkich pozostałych kolorów.
	Oznacza to, że każdy taki wierzchołek możemy przekolorować na kolor, który nie był wykorzystany wśród sąsiadów. 
	To z kolei oznacza, że w takim poprawionym kolorowaniu ten kolor nie będzie w ogóle użyty. <br/>
	Dochodzimy więc do sprzeczhości, ponieważ wyjściowe kolorowanie nie było kolorowaniem na minimalną ilość kolorów.	
    </p>
  </div>
</div>

###Zadanie 4

Uprość wyrażenie \\( \frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)}\\) gdzie \\(c(\pi)\\) to ilość cykli w permutacji \\(\pi\\).
<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
	Grupując elementy podanej sumy na grupki permutacji o takich samych ilościach cykli uzyskujemy, że
	$$ \sum\limits\_{\pi \in S\_k} n^{c(\pi)}=\\
	  \sum\limits\_{i=1}^{k} {k \brack i} n^i   $$
	Zauważmy, że ta suma zlicza nam ilość pokolorowań cykli wszystkich k-permutacji na n kolorów. 
	Spróbujmy generować takie kolorowania w inny sposób. Wstawiając pierwszy element do permutacji może on być pokolorowany na jeden z \\(n\\) kolorów. 
	Drugi element może tworzyć nowy cykl i być pokolorowany na jeden z \\(n\\) kolorów, bądź stać w cyklu na prawo od elementu pierwszego i mieć taki sam kolor jak on.
	Łatwo widać że w takim wypadku daje nam to \\(x+1\\) możliwości. Uogólniając to rozumowanie, uzyskujemy następującą równość:
	$$   \sum\limits\_{i=1}^{k} {k \brack i} n^i =  n^\overline{k} $$
	Daje nam to odpowiedź:
$$ 	\frac{1}{k!} \sum\limits\_{\pi \in S\_k} n^{c(\pi)} = \frac{n^\overline{k}}{k!} $$
	 </p>
  </div>
</div>
