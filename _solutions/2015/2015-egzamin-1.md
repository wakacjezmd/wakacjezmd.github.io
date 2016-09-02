---
layout: page
permalink: /2015/egzamin/1/
---

## 2015 Pierwszy termin

###Zadanie 1
Udowodnij tożsamość

$$\sum^{n}\_{k=0}k^m = \sum^{m}\_{k=1}{n+1 \choose k+1}{m\brace k}k! $$

dla \\(n, m \ge 1\\). WSKAZÓWKA: Rozważ funkcje
\\(f:\\left\\{1,...,m+1\\right\\} \rightarrow \\left\\{1,...,n+1\\right\\}\\)
takie, że \\(f(1) \gt f(i)\\) dla \\(i \gt 1\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Dość szybko można zauważyć że zarówno lewa jak i prawa strona sumy
      prawdopodobnie zlicza funkcje podane we wskazówce. Skoro te dwie sumy
      zliczają te same obiekty, to muszą być sobie równe. Udowodnijmy to.
    </p>
    <p>
      <b>Lewa strona równania:</b> na początku wybieramy jakieś \(k\). Wtedy
      ustalamy, że \(f(1)=k+1\), a do każdego z pozostałych \(m\) elementów
      dziedziny \(f\) można przyporządkować \(k\) liczb należących do zbioru
      \(\left\{1,...,k\right\}\).  Możliwości, na jakie można to zrobić jest
      \(k^m\). Sumując po wszystkich możliwych \(k\) otrzymamy liczbę wszystkich
      funkcji ze wskazówki.
    </p>
    <p>
      <b>Prawa strona równania:</b> Podobnie jak poprzednio wybieramy jakieś
      \(k \in \left\{1,...,m\right\}\) które będzie nam mówiło ile liczb
      występuje w zbiorze wartości \(f\). Następnie wybieramy \(k+1\) liczb
      z przeciwdziedziny, z których największa będzie wynikiem \(f(1)\).
      Pozostałe \(k\) liczb przypiszemy pozostałym elementom dziedziny. Można to
      zrobić dzieląc ją na \(k\) bloków i mieszając je na \(k!\) sposobów, a
      potem kolejno dawać tym blokom kolejne liczby.
    </p>
  </div>
</div>

---

###Zadanie 2
Niech \\(a\_n(k)\\) oznacza liczbę n-permutacji z powtórzeniami ze zbioru
\\(\\left\\{1,...,k\\right\\}\\), w których k występuje nieparzystą liczbę razy.
Znajdź zwarty wzór na \\(a\_n(k)\\) dla \\(k \gt 1\\).

---

###Zadanie 3
Znajdź wszystkie rozwiązania kongruencji \\(x^2 - 3x - 5\equiv 0\ (mod\ 343)\\).

---

###Zadanie 4
Znajdź liczbę istotnie różnych turniejów 5-wierzchołkowych, gdzie turnieje
\\(T\\) i \\(T'\\) utożsamiamy, jeśli \\(T'\\) jest izomorficzny z
\\(T\\) lub z turniejem otrzymanym z \\(T\\) przez odwrócenie kierunków
wszystkich strzałek.

---
