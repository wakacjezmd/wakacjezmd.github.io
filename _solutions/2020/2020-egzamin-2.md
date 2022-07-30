---
layout: page
permalink: /2020/egzamin/2/
---

## 2020 Egzamin poprawkowy

### Zadanie 1

Niech \\(p_{n,k}\\) oznacza liczbę \\(n\\)-permutacji mających dokładnie \\(k\\) punktów stałych i niech \\(r\\) będzie ustaloną
dodatnią liczbą naturalną. Udowodnij tożsamość:

\\[
    \sum_{k=0}^{n} k^r p_{n,k} = n! \sum_{t=1}^{r} {r \brace t} \quad \text{dla $n \geq r$.}
\\]

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie (trudniejsze)</h4>
  <div class="solution">
  <p>
    Zadanie z gatunku tych raczej trudniejszych, niż prostszych &#x1F605;.
  </p>
  <ul>
    <li> <p> (\(r = 0\)). Proste. </p> </li>
    <li>
      <p>
        (\(r = 1\)). Rozważmy działanie grupy \(s_n\) na zbiorze \(\{1, 2, 3, 4, \ldots, n\}\), gdzie \(s_n\) to grupa
        \(n\)-permutacji. (Przykładowo weźmy grupę \(s_6\). Dla pewnej permutacji \(\sigma \in s_6\), \(\sigma = (1\,
        5)(3\, 4\, 2)(6)\), mamy \(\sigma(5) = 1\), \(\sigma(4) = 2\), \(\sigma(6) = 6\) i tak dalej).
      </p>

      <p>
        Ile jest elementów w grupie \(s_n\)? Oczywiście \((n!)\).
        Ile mamy orbit działania grupowego? Oczywiście każdy element zbioru może przejść przy pewnej permutacji na
        dowolny inny (co daje nam jedną orbitę), stąd \(|\textrm{Orb}_{s_n}(X)| = 1\). 
        Ile mamy punktów stałych działania grupowego? Odnotujmy, że:
        \[
          \sum_{\sigma \in s_n} |\textrm{fix}(\sigma)| = \sum_{k=0}^{n} p_{n,k} k
        \]
        Skąd to wynika? Pogrupowaliśmy permutację po punktach stałych. Dla każdej permutacji o \(k\) punktach stałych
        mamy – bez zaskoczenia – \(k\) punktów stałych. Po podstawieniu wyliczonych wartości do lematu Burnside'a,
        otrzymujemy szukaną tożsamość:
        \[
          \sum_{k=0}^{n} k \, p_{n,k} = |s_n| |\textrm{Orb}_{s_n}(X)| =  n!
        \]
      </p>
    </li>
    <li>
      <p>
        (\(r\) dowolne). Rozważmy działanie <em>diagonalne</em> grupy \(s_n\) na zbiorze <em>\(r\)-krotek:</em> \(\{1,
        2, 3, 4, \ldots, n\}^{r}\).  <em>Diagonalne</em>, czyli takie, że dla \(\sigma \in s_n\) mamy \(\sigma(k_1, k_2,
        \ldots, k_r) = (\sigma k_1, \sigma k_2, \ldots, \sigma k_r)\). Zacznijmy od znalezienia liczby punktów stałych.
        Mamy:
        \[
          \sum_{\sigma \in s_n} |\textrm{fix}(\sigma)| = \sum_{k=0}^{n} p_{n,k} k^r
        \]
        Skąd wynika ten wzór? Jeśli permutacja ma \(k\) punktów stałych na zbiorze \(X\), to  każdy z tych punktów może
        pojawić się na dowolnej pozycji w pojedynczej \(r\)-krotce, stanowiącej punkt stały na \(X^r\). Stąd
        \(k^r\). Jeśli chodzi o orbity, mamy:
        \[
          n! \cdot |\textrm{Orb}_{s_n}(X)| = n! \cdot B_r,
        \]
        gdzie \(B_r\) jest \(r\)-tą liczbą Bella (liczbą podziałów \(r\)-zbioru na dowolną liczbę bloków).
      </p>
      <p>
        Skąd wynika ten wzór? Rozważmy krotki postaci \((a, a, \ldots, a)\). Oczywiście przy dowolnej permutacji taka
        krotka przejdzie na \((b, b, \ldots, b)\) – krotki z tym samym elementem na wszystkich \(r\) pozycjach
        stanowią oddzielną orbitę i odpowiadają podziałowi \(r\)-zbioru na jeden blok.
      </p>
      <p>
        Generalizując, \(r\) pozycji w krotce grupujemy w dowolny sposób. W każdej grupie znajdują się nierozróżnialne
        elementy, które przy dowolnej permutacji przejdą na (inne lub te same) nierozróżnialne elementy. Ostatecznie, z
        lematu Burnside'a, otrzymujemy szukany wzór:
        \[
          \sum_{k=0}^{n} k^r p_{n,k} = n! \cdot B_r
        \]
      </p>
    </li>
  </ul>
  </div>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie (prostsze)</h4>
  <div class="solution">

    Zliczamy pary \(n-\)permutacji oraz \(r-\)ciągów z powtórzeniami puntków stałych permutacji. 
    <p>
      <em> Lewa strona: </em>
      <br>
      Dla każdej permutacji mamy dokładnie \(k^r\) ciągów.
    </p>
    <p>
      <em> Prawa strona: </em>
      <br>
      Najpierw wybieramy ciąg punktów stałych. Robimy to poprzez podzielenie \(r\) na \(t\) bloków. Miejsca w tym samym bloku będą zajętę przez ten sam punkt stały, bloki są parami zajęte przez różne punkty stałe.
      Bloki możemy uzyskać na \(r \brace t\) sposobów. Pozostaje wybrać owe punkty stałe. Jest ich oczywiście \(t\), każdy może być dowolny, ale wszystkie mają być parami różne, więc: \((n)*(n-1)*(...)*(n-t+1)\) (wybrane bloki dostają punkty stałej w następującej kolejnośći: najwcześniej zaczynając się blok dostaje pierwszy wybór z iloczynu, drugi po nim drugi z iloczynu i tak dalej).
      Permutację konstruujemy tak: jej punkty stałe już wybraliśmy, pozostaje elementy możemy ułożyć na \((n-t)!\) sposobów.
      <p> 
        Dwa różne wyżej opisane wybory dadzą dwie różne pary. Jeśli dwa ciągi są sobie równe, to znaczy, że musiały zostać podzielone na te same bloki. 
        Ponadto punkty stały w obydwu ciągach musiały zostać wybrane także te same w tej samej kolejności. Finalnie sam ciąg musiał także zostać dopełniony w ten sam sposób: wybory były więc identyczne.
        Nietrudno zauważyć, że te wybory pozwalają uzyskać dowolną parę (pamiętajmy, że permutacja ma co najmniej tyle punktów stałych, ile jest różnych wartości w ciągu).
      </p>
      <p>
        <em> Przykład: </em>
        <br>
        \(r=4, t=2, n=10\).
        Dzielimy na przykład tak: \(ABAB\). Wybieramy dwa punkty stałe (bo \(t=2\)): \(2, 8\). Mamy już ciąg: \(2828\). 
        W permutacji mamy wybrane punkty stałe, następnie dobieramy permutację reszty elementów: \([1,5][2][3,6][4][7,9][8][10]\). 
      </p>
      
    </p>


  </div>
</div>

---

### Zadanie 2

Znajdź współczynnik \\(x_1 x_2 \cdots x_6\\) przy wyrażeniu:

\\[
    (X - x_2) (X - x_5) \prod_{i=1}^{5} (X - x_{i-1} - x_{i+1}),
\\]

gdzie \\( X = x_1 + x_2 + \cdots + x_6 \\). *Uwaga:* to zadanie należy rozwiązać bez wspomagania komputerowego.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Przyjmijmy \(D := X\). Po rozpisaniu otrzymujemy:

      \[
          \underbrace{(D-x_2)(D-x_2-x_4)(D-x_4-x_6)}_{\text{grupa } A} \; \underbrace{(D-x_5)(D-x_1-x_3)(D-x_3-x_5)}_{\text{grupa } B}.
      \]

      Rozpiszmy składniki jednej grupy, w każdym kroku usuwając jednak składniki, w których zmienne się dublują (np. \(x_4 x_4\)),
      co uniemożliwia <q>zwinięcie</q> się do szukanego wyrażenia.

      \[
          \begin{align}
                  &\; (D-x_2)(D-x_2-x_4)(D-x_4-x_6) \\
          \approx &\; (D - x_2)(D^2 - D[2x_2 + 2x_4 + x_6] + x_2 x_4 + x_2 x_6 + x_4 x_6) \\
          \approx &\; (D^3 - D^2[2x_2 + 2x_4 + x_6] + D[3 x_4 x_2 + 2 x_6 x_2 + x_4 x_6] - x_2 x_4 x_6)
          \end{align}
      \]

      Szczęśliwie dla nas, grupy \(A\) i \(B\) są <q>symetryczne</q>, mamy więc \(x_2 \mapsto x_5\), \(x_4 \mapsto
      x_3\), \(x_6 \mapsto x_1\). Czyli szukamy współczynnika przy \(x_1 x_2 \cdots x_6\) w poniższym wyrażeniu.

      \[
          \begin{align}
                &\; (D^3 - D^2[2x_2 + 2x_4 + x_6] + D[3 x_4 x_2 + 2 x_6 x_2 + x_4 x_6] - x_2 x_4 x_6) \\
          \cdot &\; (D^3 - D^2[2x_5 + 2x_3 + x_1] + D[3 x_3 x_5 + 2 x_1 x_5 + x_3 x_1] - x_5 x_3 x_1)
          \end{align}
      \]

      Dalej możemy po prostu obliczyć współczynniki przy szukanym iloczynie, patrząc na ile sposobów (i z jakim znakiem) można go uzyskać
      w kolejnych parach (np. dla \(D^3 D^3\) jest to \(6!\)).

      \[
          \begin{align}
            &6! + 2(- 5 \cdot 5! + (3+2+1) 4! - 3!)                     \\
          +\; &4! \cdot 5^2 + 2(-(3+2+1) \cdot 5 \cdot 3! + 5 \cdot 2!) \\
          +\; &(3+2+1)^2 \cdot 2! - 2 \cdot 6                           \\
          +\; &1                                                        \\
          \end{align}
      \]

      Wynikiem tego długiego wyrażenia jest \(117\). Dla potwierdzenia <a href="/downloads/2020_egzamin2_3.py" download>brut w Pythonie</a>.
    </p>
  </div>
</div>

---

### Zadanie 3

Udowodnij, że w \\(n\\)-wierzchołkowym grafie spójnym \\(G\\) zachodzi oszacowanie:

\\[
    \chi(G) + \textrm{diam}(G) \leq n+1.
\\]

Pokaż, że dla każdego \\(d > 0\\) i dostatecznie dużego \\(n\\) istnieje graf \\(n\\)-wierzchołkowy o średnicy \\(d\\),
dla którego to oszacowanie jest dokładne.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  Rozważmy najdłuższą ścieżkę w grafie pomiędzy wierzchołkami \(v_s\), \(v_e\). Da się ją pokolorować na dwa kolory; w
  przeciwnym razie pomiędzy niesąsiednimi wierzchołkami na ścieżce istnieje krawędź, czyli istnieje krótsza ścieżka z
  \(v_s\) do \(v_e\) – sprzeczność. Pozostałych wierzchołków jest \(n-(\mathrm{diam}(G)+1)\), co daje nam górne
  oszacowanie na minimalną liczbę ich kolorowań, stąd otrzymujemy:

  \[
      \chi(G) + \mathrm{diam}(G) \leq 2 + n-(\mathrm{diam}(G)+1) + \mathrm{diam}(G) = n + 1.
  \]

  Przykładem grafu, dla którego to oszacowanie jest dokładne, jest ścieżka \(n\)-elementowa, którą oczywiście można
  pokolorować na minimalnie dwa kolory, a której średnica wynosi \(d=n-1\). Jeśli chcemy znaleźć taki \(n\)-graf dla
  dowolnego \(d\) i dowolnego \(n \geq d+1\), to rozważmy ścieżkę (\(d+1\))-elementową, której dwa ostatnie wierzchołki są również
  wierzchołkami \((n -(d+1)+ 2)\)-kliki. Klikę w tym grafie możemy pokolorować na minimalnie \(n - d + 1\) kolorów,
  natomiast pozostałe wierzchołki ścieżki na dowolne dwa kolory, na które pokolorowana została klika. Mamy więc
  \(\chi(G) + \mathrm{diam}(G) = n - d + 1 - d = n+1\), czyli oszacowanie jest dokładne.
  </div>
</div>

---

### Zadanie 4


Znajdź liczbę uporządkowanych par liczb naturalnych \\(\langle a,b \rangle\\) takich, że \\(\text{NWW}(a,b) = 10!\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że:

      \[
          10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1
      \]

      Wiadomo (m.in. z wykładu), że jeśli \(a = p_1^{\alpha_1} p_2^{\alpha_2} \ldots p_k^{\alpha_k}\) oraz
      \(b = p_1^{\beta_1} p_2^{\beta_2} \ldots p_k^{\beta_k}\), to wówczas:

      \[
          \mathrm{NWW}(a,b) = p_1^{\max(\alpha_1, \beta_1)} p_2^{\max(\alpha_2, \beta_2)} \ldots\, p_k^{\max(\alpha_k, \beta_k)}.
      \]

      Czyli żadna z liczb \(\langle a,b \rangle\) nie może mieć dzielnika różnego od \(2, 3, 5, 7\), a jedna z nich musi
      mieć go w potędze takiej, jak \(10!\).
    </p>

    <p>
      Zamiast par liczb \(a, b\) możemy więc rozpatrywać więc pary ciągów
      \((q_1, q_2, q_3, q_4),\, (t_1, t_2, t_3, t_4)\) takie, że \( (\max(q_1, t_1), \ldots, \max(q_4,
      t_4)) = (8, 4, 2, 1)\). Nietrudno zauważyć, że takich ciągów jest:

      \[
          \prod_{i \in \{ 8, 4, 2, 1 \}}  \left( 2i + 1 \right) = 2295.
      \]

      (Jeśli np. liczba \(q_1 = 0\ldots7\), wówczas \(t_1 = 8\), i na odwrót, co daje nam \(2i\), a także może być \(q_1
      = t_1 = 8\), co daje nam \(1\)).
    </p>
  </div>
</div>
