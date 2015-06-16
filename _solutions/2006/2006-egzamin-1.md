---
layout: page
permalink: /2006/egzamin/1/
---

## 2006 Pierwszy termin

###Zadanie 1

*Uporządkowany podział* liczby \\(n\\) to ciąg dodatnich liczb całkowitych \\( \langle s\_{1}, \ldots, s\_{k} \rangle \\) takich, że \\(\sum\_{i=1}^{k}s\_{i} = n \\). Na przykład, wszystkie
uporządkowane podziały liczby 3 to \\( \langle 1,1,1 \rangle \\), \\( \langle 1,2 \rangle \\),
\\( \langle 2,1 \rangle \\), \\( \langle 3 \rangle \\).

**(a)** Znajdź liczbę wszystkich uporządkowanych podziałów \\(n\\).<br/>
**(b)** Udowodnij, że dla \\( n \geq 4 \\) we wszystkich uporządkowanych podziałach \\(n\\) liczba \\(3n\\)
występuje dokłądnie \\( n2^{n-5} \\) razy.

---

###Zadanie 3

Udowodnij, że krawędzie dowolnego grafu nieskierowanego można skierować w taki sposób,
że dla każdego wierzchołka \\(v\\) będzie spełniony warunek \\( \left| deg\_{in}(v) - deg\_{out}(v) \right|  \leq 1 \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Zauważmy, że jeżeli graf \(G\) zawiera podgraf \(C\) będący cyklem, to krawędzie zawarte w \(C\) możemy
      zorientować tak, żeby zachodziło \(\forall{v \in V(C)}\ \left| deg_{in}(v) - deg_{out}(v) \right| = 0\),
      bo do dowolnego wierzchołka \(v\) wchodzą dokładnie dwie krawędzie.
    </p>
    <p>
      Możemy więc założyć, że w \(G\) nie ma już żadnych cykli, czyli że jest drzewem.
      Przeprowadźmy indukcje po liczbie wierzchołków.<br/>
      1. Jeżeli drzewo ma jeden wierzchołek, to spełnia on warunek.<br/>
      2. Załóżmy, że warunek jest prawdziwy dla wszystkich drzew \(n\)-wierzchołkowych.
         Weźmy dowolne drzewo o \(n+1\) wierzchołkach i wybierzmy jeden z jego liści.
         Możemy go usunąć i z założenia indukcyjnego skierować pozostałe krawędzie tak,
         żeby spełniały powyższy warunek. Następnie dodajemy go, a kierunek jego krawędzi zawsze możemy
         ustalić tak, żeby albo wyrównać stopnie wchodzące i wychodzące jego sąsiada (jeżeli ich różnica była inna niż 0),
         albo, jeżeli były równe, to po skierowaniu tej krawędzi ich różnica będzie wynosiła co najwyżej 1. Zatem
         takie drzewo też spełnia warunek zadania.
    </p>
  </div>
</div>
