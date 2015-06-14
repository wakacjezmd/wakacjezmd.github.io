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
      Zastosujmy kontrapozycje. Chcemy pokazać, że jeżeli istnieje taki kolor, że każdy jego wierzchołek ma sąsiadów, którzy nie wyczerpują wszystkich pozostałych kolorów, to \(G\) nie był kolorowany na \(\chi(G)\) kolorów.
    </p>
    <p>
    	Załóżmy, że istnieje taki kolor \(k\), że każdy wierzchołek tego koloru posiada sąsiadów, którzy nie wyczerpują wszystkich pozostałych kolorów.
    	Oznacza to, że każdy taki wierzchołek możemy przekolorować na inny kolor, który nie był wykorzystany wśród jego sąsiadów.
    	To z kolei oznacza, że w nowym kolorowaniu kolor \(k\) nie będzie w ogóle użyty. <br/>
    	Zatem wyjściowe kolorowanie wcale nie używało minimalnej możliwej liczby kolorów \(\chi(G)\).
    </p>
  </div>
</div>
