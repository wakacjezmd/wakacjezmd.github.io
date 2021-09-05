---
layout: page
permalink: /2021/egzamin/1/
---

## 2021 Egzamin - Pierwszy termin

### Zadanie 1

Dla \\(k,m,r \in \mathbb{N}\\), \\(r > 0\\), udowodnij tożsamość:

\\[ \sum_{i=1}^{k}\sum_{j=0}^{m}\binom{m}{j}{r\brace i}{m-j\brace k-i} i^j = {m+r\brace k} \\]

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <em>Interpretacja.</em> Bierzemy zbiór, który jest sumą rozłącznych zbiorów wielkości \(m\) i
      \(r\), a następnie dzielimy go na \(k\) niepustych bloków.
    </p>
    <p>
      <em>Prawa strona.</em> Zsumowany (\(m+r\))-zbiór dzielimy na \(k\) niepustych bloków.
    </p>
    <p>
      <em>Lewa strona.</em><br/>
      <ul>
        <li style="margin-bottom: 7px">
            \({r \brace i}\) – \(r\)-zbiór dzielimy na \(i\) bloków (gdzie \(i = 1{\ldots}k\));
        </li>
        <li style="margin-bottom: 7px">
            \(\binom{m}{j} \cdot i^j\) – wybieramy \(j\) elementów z \(m\)-zbioru, które rozdzielamy do \(i\) bloków (gdzie \(j = 1{\ldots}m\));
        </li>
        <li style="margin-bottom: 7px">
            \({m-j \brace k-j}\) – pozostałe \(m-j\) elementów z \(m\)-zbioru rozdzielamy do \(k-i\) bloków.
        </li>
      </ul>
    </p>
    <p>
      Czy w ten sposób uzyskamy wszystkie podziały i każdy dokładnie raz? Weźmy dowolny podział sumy
      \(m\) i \(r\) zbiorów. Zaznaczmy te bloki, w których występują elementy z \(r\) zbioru.
      Wyznacza nam to jednoznacznie wartość \(i\) z powyższego wzoru. Policzmy, ile w tych blokach
      znajduje się dołączonych elementów z \(m\) zbioru. Wyznacza nam to jednoznacznie wartość
      \(j\).
    </p>
  </div>
</div>

---

### Zadanie 2

Udowodnij, że współczynnikiem \\(x^k\\) w rozwinięciu \\((1+x+x^2+x^3)^n\\) jest \\(\sum_{j=0}^{n} \binom{n}{j} \binom{n}{k-2j}\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że \((1+x+x^2+x^3)^n = (1+x^2)^n (1+x)^n\). Na ile sposobów możemy uzyskać \(x^k\)
      z tego iloczynu? Jeśli z pierwszego nawiasu wybierzemy \(j\) razy czynnik \(x^2\), to
      pozostanie nam brakujący czynnik \(x^{k-2j}\). Możemy go uzyskać, wybierając \(k-2j\) razy
      czynnik \(x\) z drugiego nawiasu. Różnych sposobów wyboru z pierwszego nawiasu jest
      \(\binom{n}{j}\); z drugiego – \(\binom{n}{k-2j}\).
    </p>
  </div>
</div>

---

### Zadanie 3

Niech \\(\mathrm{fr}(x) = x− \lfloor x \rfloor\\) oznacza *część ułamkową* liczby rzeczywistej \\(x\\). Oblicz (bez wspomagania komputerowego) \\(\mathrm{fr}(998!/101^{10})\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że \( \mathrm{fr}\big( \frac{998!}{101^{10}} \big) = \mathrm{fr}\big(\frac{q}{101}\big) 
                     = \mathrm{fr}\big(\frac{q \bmod 101}{101}\big) \). Dalej rozpatrujemy kongruencję \(\text{mod }
                     101\) z licznika.

      \[ \begin{align*}
          q &\equiv \textstyle \frac{998!}{101^{9}} \\[3pt]
          q &\equiv (1 \cdots 100) \cdot 1 \cdot (102 \cdots 201) \cdot 2 \cdots 9 \cdot (910 \cdots 1009) \cdot (1009^{-1} \cdots 999^{-1}) \\[5pt]
          q &\equiv (1 \cdots 100)^{10} (1 \cdot 2 \cdots 9) (-1)^{-1} (-2)^{-1} \cdots (-11)^{-1}   \\[5pt]
         \end{align*}
      \]

    Liczba \(101\) jest pierwsza, więc z twierdzenia Wilsona mamy, że \(1 \cdots 100 \equiv -1 \; (\text{mod } 101)\). Z
    pierwszości \(101\) wynika też, że dla każdej liczby \(a \in \{1, 2, \ldots, 100\}\) istnieje jednoznaczna
    odwrotność \(\text{mod } 101\) z tego samego zbioru. Obydwa te fakty zostały dowiedzione na ćwiczeniach. Odnotujmy
    dodatkowo, że \(x^{-1} y^{-1} = (xy)^{-1}\) (co bardzo łatwo pokazać).

      \[ \begin{align*}
          q &\equiv (-1)^{20} \cdot (2 \cdot 12 \cdot 30 \cdot 56) \cdot (2 \cdot 12 \cdot 30 \cdot 56)^{-1} \cdot (9) \cdot (-9 \cdot 10 \cdot 11)^{-1} \\[3pt]
          q &\equiv 9 (20)^{-1} \\[3pt]
         \end{align*}
      \]

    Odwrotność \(\text{mod } 101\) liczby \(20\) możemy wyznaczyć, korzystając z rozszerzonego algorytmu Euklidesa.
    Otrzymujemy \( 1 = (-5) \cdot 20 + 101 \), więc odwrotność wynosi \( -5 \). Stąd \(q \equiv 9 \cdot (-5) \equiv 56 \; (\text{mod } 101)\).
      \[
         \mathrm{fr}\left(\frac{998!}{101^{10}}\right) = \frac{56}{101}
      \]
    </p>
  </div>
</div>

---

### Zadanie 4

Oblicz, na ile istotnie różnych sposobów można rozmieścić \\(n\\) nieatakujących się wież na planszy \\(n \times n\\),
jeśli utożsamimy takie rozmieszczenia, że jedno przechodzi na drugie:

<ol type="a">
  <li> przy obrocie planszy o \(180^\circ\); </li>
  <li> przy <em>dowolnym</em> obrocie planszy. </li>
</ol>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <ol type="a">
      <li style="margin-bottom: 20px">
        <p>
        Dana jest grupa przekształceń \( G = \{ \textrm{id}, 180^\circ\} \). Stałymi elementami zbioru względem
        przekształcenia \(\textrm{id}\) są oczywiście wszystkie spośród \(n!\) rozmieszczeń nieatakujących się wież.
        </p>

        <p>
        Rozważmy przekształcenie \(180^\circ\).
        </p>

        <p>
        <ul>
        <li>
            <p>
            Gdy \(n\) jest nieparzyste, wówczas środkowy wiersz (i środkowa kolumna)
            są <q>odbite</q> w centralnym elemencie, tzn. jeśli wieża jest na pozycji \(\big(\frac{n+1}{2}, k\big)\), to
            jest również na pozycji \(\big(\frac{n+1}{2}, n-k+1\big)\). To znaczy, że jedynym <q>nieatakującym</q> ułożeniem
            wieży w środkowym wierszu i w środkowej kolumnie jest \(\big(\frac{n+1}{2}, \frac{n+1}{2}\big)\).
            </p>

            <p>
            Po umieszczeniu środkowej wieży, do rozmieszczenia pozostało jeszcze \(n-1\). Ułożenie \(\frac{n-1}{2}\) wież w
            górnych wierszach wyznacza nam jednoznacznie ułożenie w dolnych wierszach. Należy uważać, by nie ułożyć
            w tym samym czasie wieży w kolumnie \(k\)-tej i w kolumnie (\(n-k+1\))-szej; odbicie wymagane przez obrót
            spowoduje wówczas kolizję.  Idąc kolumnami \(k=1\ldots \frac{n-1}{2}\), dla każdej wieży mamy do wyboru
            \(\big(\frac{n-1}{2}, \frac{n-3}{2}, \ldots, 1\big)\) wierszy i (zawsze) dwie kolumny (tzn. \(k\)-tą i
            \(n-k+1\)-szą), co daje nam w sumie:

            \[
                \textstyle  2^{(n-1)/2} \cdot \big( \frac{n-1}{2} \big)!
            \]

            punktów stałych przekształcenia \(180^\circ\) dla \(n\) nieparzystego.
            </p>
        </li>
        <li style="margin-top: 20px">
            <p>
            Gdy \(n\) jest parzyste, sytuacja jest analogiczna jak w przypadku \(n\) nieparzystego, ale nie musimy
            rozważać środkowego wiersza i środkowej kolumny (ponieważ środkiem obrotu będzie punkt pomiędzy dwoma
            środkowymi wierszami i dwiema środkowymi kolumnami). Otrzymujemy:

            \[
                \textstyle 2^{n/2} \cdot \big(\frac{n}{2}\big)!
            \]

            rozmieszczeń.
            </p>
        </li>
        </ul>
        </p>

        <p style="margin-top: 20px">
        Obliczyliśmy, że: \(
          \sum_{g \in G} \textrm{fix}(g) = n! + \textstyle 2^{\lfloor n/2 \rfloor} \big\lfloor\frac{n}{2}\big\rfloor!
        \). Z lematu Burnside'a wiemy, że:

        \[
          \sum_{g \in G} \textrm{fix}(g) = 2 \cdot |\textrm{Orb}(X)|
            \implies
          |\textrm{Orb}(x)| = \frac{n! + \textstyle 2^{\lfloor n/2 \rfloor} \big\lfloor\frac{n}{2}\big\rfloor!}{2}
        \]

        gdzie orbity oznaczają liczbę nieizomoricznych rozmieszczeń względem grupy przekształceń.

        </p>

    </li>

    <li>
        <p>
        Dana jest grupa przekształceń \( G = \{ \textrm{id}, 90^\circ, 180^\circ, 270^\circ\} \). Stałymi elementami
        zbioru względem przekształcenia \(\textrm{id}\) są oczywiście wszystkie spośród \(n!\) rozmieszczeń
        nieatakujących się wież. Przekształcenie \(180^\circ\) rozważyliśmy w poprzednim podpunkcie.
        </p>

        <p>
        Rozważmy jednocześnie przekształcenie \(90^\circ\) i równoważne jemu pod względem orbit przekształcenie
        \(270^\circ\). Rozważmy \(n\)-planszę taką, że \(2 \mid n\). Ponumerujmy planszę, jak poniżej.
        </p>

        <p style="margin-top:30px; margin-bottom: 30px">
        <img src="/images/2021_4_b.svg" style="display:block; margin-left:auto; margin-right:auto; width:50%">
        </p>

        <p>
        Odnotujmy, że jeśli na polu \((a,b)\) zostanie postawiona wieża, to nie może ona pojawić się na żadnym z pól
        \((a,\star), (\star, b), (b, \star), (\star, a)\) (gdzie \(\star\) to dowolny element). Wieże nie zbijają się za
        to, gdy stoją na polach \((k_1, k_2), (k_3, k_4), \ldots, \big(k_{\lfloor\frac{n}{4}\rfloor-1},
        k_{\lfloor\frac{n}{4}\rfloor}\big)\), gdzie \(k_1 \neq k_2 \neq \ldots \neq k_{\lfloor\frac{n}{4}\rfloor}\).
        </p>

        <p>
        Widać jasno, że jeśli \(4 \not\mid n\), to nie uda się rozstawić \(n\) wież, bo każda wieża pojawia się
        \(4\) razy. W przeciwnym wypadku wzór na liczbę unikalnych rozstawień wież wynosi:

        \[
            \frac{(n/2)!}{(n/4)!}
        \]

        To znaczy, permutujemy \(n!\) elementów, łączymy je w pary po dwa, i usuwamy powtarzające się pogrupowania
        (tzn. dzielimy liczbę permutacji elementów przez liczbę permutacji par).
        </p>

        <p>
        W przypadku gdy \(2 \not\mid n\), na polu \(\frac{n-1}{2}\) musi pojawić się wieża. Wówczas
        sytuacja jest zupełnie analogiczna jak w przypadku parzystym, tzn. możliwych jest:

        \[
            \frac{\big(\frac{n-1}{2}\big)!}{\big(\frac{n-1}{4}\big)!}
        \]

        rozstawień, gdy \(4 \mid (n-1)\). Dla wygody notacyjnej zdefiniujmy:

        <ul>
        <li style="margin-bottom: 7px"> \(P_{1}(n) = n!\) </li>
        <li style="margin-bottom: 7px"> \(P_{2}(n) = 2^{n/2} \big( \frac{n}{2} \big)!\) </li>
        <li style="margin-bottom: 7px"> \(P_{3}(n) = \frac{(n/2)!}{(n/4)!}\) </li>
        </ul>

        I dalej mamy:

        \[
            |\textrm{Orb}(x)| = \frac{1}{4} \cdot
                \begin{cases}
                  P_1(n) + P_2(n) + 2P_3(n)       &\text{gdy $n \equiv 0 \mod 4$} \\[3pt]
                  P_1(n) + P_2(n-1) + 2P_3(n-1)   &\text{gdy $n \equiv 1 \mod 4$} \\[3pt]
                  P_1(n) + P_2(n)                 &\text{gdy $n \equiv 2 \mod 4$} \\[3pt]
                  P_1(n) + P_2(n-1)               &\text{gdy $n \equiv 3 \mod 4$} \\[3pt]
                \end{cases}
        \]
        </p>

    </li>
    </ol>
  </div>
</div>
