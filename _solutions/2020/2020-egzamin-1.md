---
layout: page
permalink: /2020/egzamin/1/
---

## 2020 Egzamin - Pierwszy termin

### Zadanie 1

<div>
W jednym kroku <em>spaceru po kracie</em> \(\mathbb{Z}^2\) z punktu \((x,y)\)
możemy przejść do \((x \pm 1, y)\) lub \((x, y \pm 1)\). Znajdź zwarty wzór na
liczbę spacerów złożonych z \(n\) kroków, które zaczynają się i kończą w punkcie
\((0,0)\).
</div>


<div data-collapse>
  <h4 class="collapsible">Wskazówka wakacyjna</h4>
  <div class="tip">
    Zadanie da się zrobić interperetacją, w której dwukrotnie wybiera się te samą liczbę. W interpretacji nie ma żadnego sumowania.
  </div>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <p>
        Zauważmy, że ciąg złożny z \(L, P, G, D\) jest spacerem wtedy i tylko wtedy, gdy \(\#L\) = \(\#P\) oraz \(\#G\) = \(\#D\). Dzieje się tak, bo żeby zacząć i skończyć w \((0, 0)\) potrzebujemy tyle samo skrętów w prawo co lewo itd. 
      </p>
      <p>
        <em>Zliczanie</em>: 
        Wybierzmy połowę miejsc. W wybrane miejsca wstawmy \(L\). Ponownie wybierzmy połowę miejsc (z \(n\) - miejsca z dwóch wyborów mogą się pokrywać). W wybrane miejsca wstawiamy \(P\). Wybór miejsc rozumiemy podług tej tabelki (pierwsze miejsce reprezentuje pierwszy wybór, drugie - analogicznie):
        </p>
        <p>
          \(\_P = P\)
        </p>
        <p>
          \(LP = D\)
        </p>
          \(\_\_ = G\)
        <p>
          \(L\_ = L\)
        </p>

      <p>
        Czyli na przykład: \(n = 4\), pierwszy wybór: \(L\_L\_\). Drugi wybór: \(PP\_\_\). Sumarycznie: \(DPLG\).

        Twierdzę, że takie wybory zliczają spacery.
      </p>

    <p>
      <em>Prawidłowość wyboru</em>:

      \(n\) dowolne, z pierwszego wyboru mamy \(\frac{n}{2}\) \(L\), z drugiego \(\frac{n}{2}\) \(P\). Niech \(x\) to będzie liczba pokrywających się miejsc. Policzmy teraz liczbę poszczególnych kierunków:
      <p>
        \(\#L = \frac{n}{2} - x \) (\(\frac{n}{2}\) było na starcie, zabieramy \(x\), bo tyle się pokrywa)
      </p>

      <p>
        \(\#P = \frac{n}{2} - x\) (Skoro po drugim wyborze \(x\) miejsc się pokrywa, a wybieraliśmy z \(\frac{n}{2}\), to na \(\frac{n}{2} - x \) stoi samo \(P\))
      </p>

      <p>
        \(\#D = x\) (Bo \(x\) się pokrywa)
      </p>

      <p>
        \(\#G = x \) (Bo na \(\frac{n}{2}\) coś stoi z pierwszego wyboru, wiemy, że \(x\) się pokrywa z drugim, czyli z drugiego wyboru mamy \(\frac{n}{2} - x\) nowych miejsc [niepokrywających się z pierwszym wyborem]. Czyli \(\frac{n}{2} + \frac{n}{2} - x \) to liczba miejsc, na którym coś stoi. Odejmujemy od \(n\), żeby otrzymać liczbę miejsc pustych i wychodzi \(x\)).
      </p>

      <p>
        Czyli ten sposób zawsze wybiera prawidłowe spacery.
      </p>

    </p>

    <p>
      <em>Zlicza każdy spacer</em>:

      Niech \(S\) będzie dowolnym spacerem z zadania. \(A, B, C, D\) to odpowiednio zbiory pozycji \(L, P, G, D\) tego spaceru.

      Z pierwszego wyboru niech wszystkie \(L\) padną na pozycję z \(A\). To ustawia wszystkie \(L\) jak trzeba.

      Z drugiego, niech \(\|D\|\) \(P\) padnie na pozycję z \(D\). To ustawia wszystkie \(D\) jak trzeba. 

      Pozostałe \(P\) z drugiego wybour \((\frac{n}{2} - \|D\|\)) niech padną na puste pozycje. To ustawia \(P\) i zarazem \(G\).
    </p>

    <p>
      <em>Różnowartościowość wyboru:</em>
      Tabelka zdefiniowana na początku pozwala uzyskać dany skręt na dokładnie jeden sposób, więc dwa różne wybory muszą dać różne podziały.
    </p> 

    <p>
      <em> Wzór:  </em>
        <p>
          Dwa razy wybieramy połowę z \(n\): \(\binom{n}{\frac{n}{2}}^2\)
        </p>
    </p>
  </p>
  </div>
</div>

### Zadanie 2

<div>
<p style="margin-bottom: 15px">
Niech \(D(d_1, d_2, \ldots, d_k)\) oznacza liczbę <em>nieporządków
multizbioru</em>, w którym jest \(d_i\) egzemplarzy elementów \(i\)-tego
rodzaju, dla \(i=1,\ldots,k\), czyli takich ustawień elementów tego multizbioru
w ciąg, że na pierwszych \(d_1\) pozycjach nie ma żadnego elementu pierwszego
rodzaju, na kolejnych \(d_2\) pozycjach nie ma żadnego elementu drugiego
rodzaju, itd. Na przykład \(D(1,2) = 0\), \(D(2,2) = 1\), \(D(1,1,2)=2\) (jedyne
nieporządki multizbioru \(\{ a,b,c,d \}\) to \(\langle c,c,a,b \rangle\) oraz
\(\langle c,c,b,a \rangle\)).
</p>

<p style="margin-bottom: 15px">
Oblicz \(D(2,2,2,3)\).
</p>

<p>
<em>Wskazówka: </em> W obliczeniach może się okazać przydatne oprogramowanie
takie jak serwis WolframAlpha lub pakiet do obliczeń symbolicznych.
</p>

</div>

---

### Zadanie 3

<div>
<p style="margin-bottom: 15px">
Niech \(n\) będzie dodatnią liczbą nieparzystą i niech
\(X_n = \{ 1 \leq x \leq n \mid x \perp n \,\wedge\, (x+1) \perp n \}\).
</p>
<p style="margin-bottom: 15px">
Udowodnij, że \((\prod_{x \in X_n} x) \equiv 1 \bmod n\).
</p>
</div>

<div data-collapse>
  <h4 class="collapsible">Wskazówka wakacyjna</h4>
  <div class="tip">
    Zastanów się nad odwrotnościami multiplikatywnymi modulo \(n\).
  </div>
</div>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Pokażemy, że każdy element w \(X_n\) ma także w tym zbiorze swoją odwrotność multiplikatywną \(\bmod n\). Korzystamy z faktu, że jeśli odwrotność multiplikatywna istnieje, to istnieje dokładnie jedna, unikalna dla każdego elementu.
    </p>
    <p>
      Niech \(a\in X_n\). Oczywiście \(a \perp n\). Jest to warunek konieczny i wystarczający istnienia odwrotności multiplikatywnej \(a\). Pokażemy, że \(a^{-1} \in X_n\).
    </p>
    <p>
      <p>
        <em> Czy  \(a^{-1} \perp n\)? </em>
      </p>
      Załóżmy, że tak nie jest. Oznacza to, że istnieje takie \(p\), że \(p \mid n \wedge p \mid a^{-1}\).
      Ale z definicji odwrotności mamy: \(aa^{-1} \equiv 1 \bmod n\). Ta kongruencja znaczy tyle co: \(n \mid aa^{-1}-1\).
      Jednak \(p \mid n\), ale \(p \nmid aa^{-1} -1\) - sprzeczność. Oznacza to, że takie \(p\) nie może istnieć.
    </p>
    <p>
      <em> Czy  \(a^{-1}+1 \perp n\)? </em>
    </p>
    <p>
      Wiemy, że \(a+1 \perp n\) oraz \(a^{-1} \perp n\). Zachodzi także \((a+1)(a^{-1}) \perp n\). Ta własność to nic innego jak: \(NWD(aa^{-1}+a^{-1}, n) = 1\). Z własności \(NWD\), możemy wziąć pierwszy argument modulo drugi, nie zmieniając wyniku: \(NWD(aa^{-1}+a^{-1}, n) = NWD(1+a^{-1}, n) = 1\). Czyli \(a^{-1} + 1 \perp n\).
    </p>
    <p>
      Pokazaliśmy, że dla dowolnego elementu z \(X_n\), jego odwrotność także należy do tego zbioru. Możemy teraz połączyć każdy element z jego odwrotnością, co daje \(1\) licząc modulo \(n\). Finalnie mamy iloczyn samych jednynek modulo \(n\), co kończy zadanie.
    </p>
  </div>
</div>

### Zadanie 4


<div>
<p style="margin-bottom: 15px">
Znajdź liczbę istotnie różnych naszyjników złożonych z \(15\) paciorków w
kolorach zielonym lub czerwonym, przy czym <em>żadne dwa czerwone paciorki nie
są sąsiednie</em>. Dwa naszyjniki utożsamiamy, jeśli jeden przechodzi na drugi
przez pewien obrót lub symetrię osiową.
</p>
<p style="margin-bottom: 15px">
<em>Wskazówka:</em> W obliczeniach przydatny okazać się może arkusz
kalkulacyjny.
</p>
</div>
