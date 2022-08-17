---
layout: page
permalink: /2017/egzamin/2/
---

## 2017 Egzamin poprawkowy

### Zadanie 1
<em>Uporządkowanym podziałem</em> dodatniej liczby całkowitej \\( n \\),
czyli <em>n-kompozycją</em> nazywamy przedstawienie \\( n \\) w postaci sumy
dodatnich składników, przy czym kolejność składników w tym przedstawieniu jest
istotna (np. wszystkie 3-kompozycje to: \\( 1 + 1 + 1, 1 + 2, 2 + 1, 3 \\)). Znajdź
liczbę n-kompozycji, w których <em>liczba składników parzystych jest parzysta.</em>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie I (dłuższe)</h4>
  <div class="solution">
    <p>
      Rozważmy następujący sposób generowania n-kompozycji.
	</p>
	<p>
	  <img src="https://i.imgur.com/Kbj4OrO.png" alt="Graficzne przedstawienie sposobu generowania n-kompozycji" />
	</p>
	<p>
	  <span style="white-space: nowrap">Wygenerujemy w ten sposób wszystkie n-kompozycje, ponieważ uzyskujemy je
	  z każdej k-kompozycji, gdzie \( k &lt; n \),</span>
	  dopisując na ich końce takie \( t \), żeby \( k + t = n \). Ponadto dzielimy je na dwie grupy, w zależności od
	  spełniania warunku parzystości podanego w treści zadania (dopisanie na koniec liczby nieparzystej nie zmienia spełnialności
	  warunku, zaś parzystej tak).
	</p>
	<p>
	  Możemy teraz przejść do policzenia interesującej nas wartości \( a_n \), która oznacza liczbę n-kompozycji,
	  w których liczba składników parzystych jest parzysta (nieparzysta dla \( b_n \)).
	  Sugerując się powyższą tabelką, spróbujemy udowodnić indukcyjnie, że
	  \( a_n = b_n = 2^{n - 2} \) dla \( n &gt; 1 \). Wzór na pewno jest prawdziwy
	  dla \( n = 2 \). Zakładamy, że zachodzi on również dla każdego \( k &lt; n \), gdzie \( n &gt; 2 \)
	  i \( k &gt; 1 \). Wiemy, że (przedstawione jest to także na tabelce)
	  $$a_n = a_{n - 1} + b_{n - 2} + a_{n - 3} + b_{n - 4} + \dots + [if \, n \, mod \, 2 = 0 \, then \, b_2 \, else \, a_2] + 1$$
	  $$b_n = b_{n - 1} + a_{n - 2} + b_{n - 3} + a_{n - 4} + \dots + [if \, n \, mod \, 2 = 0 \, then \, a_2 \, else \, b_2] + 1$$
	  lub bardziej formalnie
	  $$a_n = \sum_{i = 0}^{\lfloor (n - 3) / 2 \rfloor} a_{n - (2 i + 1)} + \sum_{i = 1}^{\lfloor (n - 2) / 2 \rfloor} b_{n - 2 i} + 1$$
	  $$b_n = \sum_{i = 0}^{\lfloor (n - 3) / 2 \rfloor} b_{n - (2 i + 1)} + \sum_{i = 1}^{\lfloor (n - 2) / 2 \rfloor} a_{n - 2 i} + 1$$
	  Korzystamy z założenia indukcyjnego.
	  $$a_n = 2^{n - 3} + 2^{n - 4} + 2^{n - 5} + 2^{n - 6} + \dots + [if \, n \, mod \, 2 = 0 \, then \, 2^0 \, else \, 2^0] + 1$$
	  $$b_n = 2^{n - 3} + 2^{n - 4} + 2^{n - 5} + 2^{n - 6} + \dots + [if \, n \, mod \, 2 = 0 \, then \, 2^0 \, else \, 2^0] + 1$$
	  lub bardziej formalnie
	  $$a_n = \sum_{i = 0}^{\lfloor (n - 3) / 2 \rfloor} 2^{n - 2 - (2 i + 1)} + \sum_{i = 1}^{\lfloor (n - 2) / 2 \rfloor} 2^{n - 2 - 2 i} + 1$$
	  $$b_n = \sum_{i = 0}^{\lfloor (n - 3) / 2 \rfloor} 2^{n - 2 - (2 i + 1)} + \sum_{i = 1}^{\lfloor (n - 2) / 2 \rfloor} 2^{n - 2 - 2 i} + 1$$
	  Widzimy już, że \( a_n = b_n \), więc dalej możemy rozważać już tylko \( a_n \). Nietrudno zauważyć, że w istocie zachodzą następujące równości.
	  $$a_n = 2^{n - 3} + 2^{n - 4} + 2^{n - 5} + 2^{n - 6} + \dots + [if \, n \, mod \, 2 = 0 \, then \, 2^0 \, else \, 2^0] + 1 =$$
	  $$= 2^{n - 3} + 2^{n - 4} + 2^{n - 5} + 2^{n - 6} + \dots + 2^0 + 1 = (\sum_{i = 0}^{n - 3} 2^i) + 1 = \frac{2^{n - 2} - 1}{2 - 1} + 1 = 2^{n - 2}$$
	  lub bardziej formalnie
	  $$a_n = \sum_{i = 0}^{\lfloor (n - 3) / 2 \rfloor} 2^{n - 2 - (2 i + 1)} + \sum_{i = 1}^{\lfloor (n - 2) / 2 \rfloor} 2^{n - 2 - 2 i} + 1
	  = (\sum_{i = 0}^{n - 3} 2^i) + 1 = 2^{n - 2}$$
	  W związku z tym, że wzór okazał się prawdziwy dla \( n \), to na mocy indukcji jest on prawdziwy dla każdego \( n &gt; 1 \).
	  Ostatecznie liczba n-kompozycji, w których liczba składników parzystych jest parzysta wynosi
	  \( 2^{n - 2} \) dla \( n &gt; 1 \) i \( 1 \) dla \( n = 1 \).
    </p>
  </div>
</div>

<div data-collapse="">
  <h4 class="collapsible">Rozwiązanie II (krótsze)</h4>
  <div class="solution">
	<p>
		Zauważmy, że ogólnie wszystkich n-kompozycji jest \(2^{n-1}\). Wystarczy wyobrazić sobie \(n\) piłek, pomiędzy każdą piłkę możemy włożyć przegródkę: dowolne ułożenie \(\leq n-1\) przegródek definuje kompozycję. 
	</p>
	<p>
		Niech Dobra Kompozycja, to kompozycja, której liczba składników parzystych jest parzysta, a z kolei kompozycja z nieparzystą liczbą składników parzystych będzie Złą kompozycją. Oczywiście zbiory Dobrych i Złych kompozycji są rozłączne, a ich suma to po prostu wszystkie n-kompozycje. 
		Pokażę, że istnieje bijekcja pomiędzy Dobrymi a Złymi kompozycjami.
	</p>
	<p>
		Weźmy Dobrą kompozycję: jeśli jej pierwszy element jest jedynką to dołączamy go do drugiego elementu; jeśli jest różny od jeden, to zabieramy z niego jedynkę i dodajemy ją jako nowy element na sam początek kompozycji. Łatwo widać, że ta operacja jest różnowartościowa, a przez to także na.  
	</p>
	<p>
		Skoro istnieje bijekcja pomiędzy Dobrymi kompozycjami a Złymi, to jest ich tyle samo, a skoro razem jest ich \(2^{n-1}\), to Dobrych jest \(2^{n-2}\) dla \(n>1\).
	</p>
  </div>
</div>

---

### Zadanie 2
Udowodnij, że zbiór wierzchołków grafu planarnego można przedstawić jako sumę
trzech zbiorów \\( S_1, S_2, S_3 \\), takich, że graf indukowany przez każde \\( S_i \\) jest lasem.

<div data-collapse="">
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
	<p>
	  Zadanie rozwiążemy indukcyjnie. Dla grafu o \( n \leq 3 \) wierzchołkach twierdzenie trywialnie
	  zachodzi. Zakładamy, że zachodzi ono również dla każdego grafu planarnego o \( n &gt; 3 \)
	  wierzchołkach. Rozważmy dowolny graf planarny o \( n + 1 \) wierzchołkach. Wiemy, że w każdym grafie planarnym
	  istnieje wierzchołek stopnia co najwyżej 5. Tymczasowo usuwamy go z rozważanego grafu, a pozostałe wierzchołki
	  dzielimy na 3 grupy, korzystając z założenia indukcyjnego. Skoro usunięty wierzchołek jest stopnia co najwyżej
	  5, to spośród tych 3 grup musi istnieć przynajmniej jedna taka, że co najwyżej 1 wierzchołek z niej
	  jest połączony krawędzią z tym usuniętym. Zatem, dołączenie go do tej grupy nie spowoduje powstania
	  cyklu i nadal graf indukowany przez ten zbiór wierzchołków będzie lasem. W związku z tym, twierdzenie
	  jest prawdziwe dla dowolnego planarnego o \( n + 1 \) wierzchołkach i na mocy indukcji także dla każdego
	  grafu planarnego, co kończy dowód.
	</p>
  </div>
</div>

---

### Zadanie 3
Niech \\( p > 2 \\) będzie liczbą pierwszą. Znajdź liczbę rozwiązań kongruencji
$$x^{p+1} \equiv 1 \pmod{p^{2017}}$$
w zbiorze \\( \\{ 0, 1, \dots, p^{2017} - 1 \\} \\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Wiemy, że 0 nie jest rozwiązaniem, zaś 1 tak. Rozważamy teraz \( x &gt; 1 \).
	  $$x^{p + 1} \equiv 1 \pmod{p^{2017}}$$
	  W takim razie
	  $$r_{Z^*_{p^{2017}}}(x) \vert p + 1$$
	  i
	  $$r_{Z^*_{p^{2017}}}(x) \perp p$$
	  Z tw. Lagrange'a
	  $$r_{Z^*_{p^{2017}}}(x) \vert \varphi(p^{2017})$$
	  $$r_{Z^*_{p^{2017}}}(x) \vert p^{2016}(p - 1)$$
	  Skoro \( r_{Z^*_{p^{2017}}}(x) \perp p \), to
	  $$r_{Z^*_{p^{2017}}}(x) \vert p - 1$$
	  Zatem dla pewnego \( n \in N \)
	  $$p - 1 = nr_{Z^*_{p^{2017}}}(x)$$
	  $$p = nr_{Z^*_{p^{2017}}}(x) + 1$$
	  Wracamy do pierwotnej kongruencji.
	  $$x^{p+1} \equiv 1 \pmod{p^{2017}}$$
	  $$x^{nr_{Z^*_{p^{2017}}}(x) + 1 + 1} \equiv 1 \pmod{p^{2017}}$$
	  $$x^{nr_{Z^*_{p^{2017}}}(x)}x^{2} \equiv 1 \pmod{p^{2017}}$$
	  $$x^{2} \equiv 1 \pmod{p^{2017}}$$
	  Korzystamy ze wzoru na liczbę elementów danego rzędu w grupie cyklicznej.
	  $$\varphi(2) = 1$$
	  Ostatecznie jedynymi rozwiązaniami podanej kongruencji w podanym zbiorze są liczba 1
	  (w danej grupie jest ona elementem o rzędzie 1) oraz jakaś liczba, która w danej grupie
	  jest elementem o rzędzie 2. Zatem liczba rozwiązań podanej kongruencji wynosi 2.
    </p>
  </div>
</div>

---

### Zadanie 4
Znajdź liczbę rozwiązań kongruencji \\( x_1 + x_2 + \dots + x_6 \equiv 0 \pmod{3} \\),
gdzie \\( x_i \in \\{ 0, 1, 2 \\} \\) dla \\( 1 \leq i \leq 6 \\), a dwa rozwiązania utożsamiamy,
jeśli jedno przechodzi na drugie przez przesunięcie cykliczne (np. \\( \langle 1, 1, 1, 0, 0, 0
\rangle \simeq \langle 0, 1, 1, 1, 0, 0 \rangle \not\simeq \langle 1, 0, 1, 1, 0, 0 \rangle \\)).

<div data-collapse="">
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
	<p>
	  Wymieniamy permutacje.
	  $$(1) \, (2) \, (3) \, (4) \, (5) \, (6)$$
	  $$(1, 4) \, (2, 5) \, (3, 6)$$
	  $$(1, 3, 5) \, (2, 4, 6)$$
	  $$(1, 5, 3) \, (2, 6, 4)$$
	  $$(1, 2, 3, 4, 5, 6)$$
	  $$(1, 6, 5, 4, 3, 2)$$
	  Tworzymy indeks cyklowy.
	  $$\frac{1}{6}(x_1^6 + x_2^3 + 2 x_3^2 + 2 x_6)$$
	  Korzystamy z teorii Polyi, gdzie \( a \) to \( 0 \), \( b \) - \( 1 \), zaś \( c \) - \( 2 \).
	  $$\frac{1}{6}((a + b + c)^6 + (a^2 + b^2 + c^2)^3 + 2 (a^3 + b^3 + c^3)^2 + 2 (a^6 + b^6 + c^6))$$
	  Liczymy współczynniki przy interesujących nas wyrazach.
	  $$2 (a^6 + b^6 + c^6) \longrightarrow 2 \times 3 = 6$$
	  $$2 (a^3 + b^3 + c^3)^2 \longrightarrow 2 \times 3 \times 3 = 18$$
	  $$(a^2 + b^2 + c^2)^3 \longrightarrow 3 \times 3 \times 1 = 9$$
	  Przypadek \( (a + b + c)^6 \) jest nieco bardziej skomplikowany. Zauważmy, że, aby kongruencja zachodziła,
	  suma \( x_1 + x_2 + \dots + x_6 \) musi wynosić: \( 0, 3, 6, 9 \) lub \( 12 \). W takim razie dla każdej
	  z 5 możliwości rozważmy wszystkie konfiguracje zmiennych \( a, b \) i \( c \) (czyli odpowiednio \( 0, 1 \) i \( 2 \))
	  w ramach 6 nawiasów.
	</p>
	<p>
	  Dla \( 0 \)
	  $$0 \, 0 \, 0 \, 0 \, 0 \, 0 \longrightarrow 1$$
	  Dla \( 3 \)
	  $$1 \, 1 \, 1 \, 0 \, 0 \, 0 \longrightarrow \binom{6}{3}
											= \frac{\not 6 \times 5 \times 4}{\not 2 \times \not 3} = 20$$
	  $$2 \, 1 \, 0 \, 0 \, 0 \, 0 \longrightarrow \binom{6}{2} \times 2
											= \frac{6 \times 5}{\not 2} \times \not 2 = 30$$
	  Dla \( 6 \)
	  $$1 \, 1 \, 1 \, 1 \, 1 \, 1 \longrightarrow 1$$
	  $$2 \, 1 \, 1 \, 1 \, 1 \, 0 \longrightarrow \binom{6}{2} \times 2 = 30$$
	  $$2 \, 2 \, 1 \, 1 \, 0 \, 0 \longrightarrow \frac{6!}{2! \times 2! \times 2!}
											= \frac{\not 2 \times 3 \times \not 4 \times 5 \times 6}{\not 2 \times \not 2 \times \not 2} = 90$$
	  $$2 \, 2 \, 2 \, 0 \, 0 \, 0 \longrightarrow \binom{6}{3} = 20$$
	  Dla \( 9 \)
	  $$2 \, 2 \, 2 \, 1 \, 1 \, 1 \longrightarrow \binom{6}{3} = 20$$
	  $$2 \, 2 \, 2 \, 2 \, 1 \, 0 \longrightarrow \binom{6}{2} \times 2 = 30$$
	  Dla \( 12 \)
	  $$2 \, 2 \, 2 \, 2 \, 2 \, 2 \longrightarrow 1$$
	  Zatem łącznie
	  $$(a + b + c)^6 \longrightarrow 1 \times 3 + 20 \times 3 + 30 \times 3 + 90 \times 1 = 243$$
	  I dla całego indeksu cyklowego
	  $$\frac{1}{6}((a + b + c)^6 + (a^2 + b^2 + c^2)^3 + 2 (a^3 + b^3 + c^3)^2 + 2 (a^6 + b^6 + c^6)) \longrightarrow$$
	  $$\longrightarrow \frac{1}{6}(243 + 9 + 18 + 6) = \frac{1}{6} \times 276 = \underline{46}$$
	</p>
  </div>
</div>

---
