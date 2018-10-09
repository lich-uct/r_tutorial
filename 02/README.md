# Jupyter Notebook &ndash; letem světem

V tomto krátkém tutoriálu si ukážeme ty nejdůležitější praktické aspekty používaní prostředí Jupyter. Podíváme se na základní funkce interaktivních notebooků a zároveň si vyzkoušíme to nejjednodušší z jazyka R. V tomto tutoriálu se předpokládá, že již máte nainstalované vývojové prostředí a spuštěný notebook (popsáno v [předchozím tutoriálu](../01/)). Čili před sebou vidíte něco jako toto:

![notebook_empty.png](notebook_empty.png  "notebook_empty.png")

Jupyter notebooky fungují na systému buňek (*cells*), do kterých uživatel píše kód v jazyce R, který chce vykonat. Výstup z buňky je potom po vykonání příkazu zobrazen pod ní. Ukažme si tedy jak vykonat jeden z nejjednodušších příkazů historie programovacích jazyků a to vypsání libovolného textu do výstupu programu. V R toho docílíme následovně:

```R
print("Ahoj světe!")
```

Když tento příkaz napíšete do buňky a vykonáte její obsah pomocí kláves <kbd>Shift</kbd> + <kbd>Enter</kbd>, dostane se vám následující odezvy:

```
[1] "Ahoj světe!"
```

V notebooku pak vše vypadá takto:

![hello_world.png](hello_world.png  "hello_world.png")

Číslo 1 v hranatých závorkách je speciální vlastností funkce `print` a slouží ke snadnější navigaci. Číslo označuje aktuální pořadí prvku vypisovaného vektoru nebo číselné řady na začátku řádku. V R je tato notace poměrně běžná a zjednodušuje orientaci v dlouhých výstupech programu. V tomto tutoriálu tuto funkcionalitu ještě mnohokrát uvidíme i u jiných funkcí a datových typů.

K vypisování výstupu nemusíme vždy nutně využívat funkce `print`, ale lze též použít řetězec přímo:

![hello_world_simple.png](hello_world_simple.png  "hello_world_simple.png")

Toto funguje díky tomu, že každý objekt v R má většinou danou nějakou textovou reprezentaci. Jupyter se pak vždy po vyhodnocení buňky pokusí nějakým způsobem zobrazit výsledek každého příkazu, jehož výstupem je nějaká textově reprezentovatelná hodnota. Všimněte si též, že bez použití funkce `print` již není součástí výstupu čislo 1 v hranatých závorkách a i formátování je trochu jiné.

Vytvořme si nyní novou buňku (většinou je však již vytvořena automaticky po vykonání buňky aktuální). Nejjednodušším způsobem, jak vytvořit novou buňku je pomocí kombinace kláves <kbd>Esc</kbd> + <kbd>b</kbd>, která požádá program o vytvoření nové buňky pod tou aktuální (vždy označena rámečkem). Podobně funguje i zkratka <kbd>Esc</kbd> + <kbd>a</kbd>, která vytvoří novou buňku nad tou aktuální. Užitečná je i zkratka <kbd>Esc</kbd> + <kbd>d</kbd> + <kbd>d</kbd>, která smaže aktuální buňku. Mnohem více zkratek lze potom nalézt [zde](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/) nebo v nápovědě (menu položka *Help*).

Zkusme si teď nějaké základní věci v R. Nejčastějším úkonem je přiřazování do proměnných, což se [doporučuje](http://blog.revolutionanalytics.com/2008/12/use-equals-or-arrow-for-assignment.html) dělat operátorem `<-`:

```R
a <- "Čau."
```

Všechny proměnné (tedy i naše proměnná *a*), které v notebooku vytvoříte, žijí v kontextu tzv. *kernelu*. Kernel je je jiný název pro interaktivní interpreter porgramovacího jazyka R. Kernel si pamatuje všechny vaše proměnné nebo funkce, které jste si nadefinovali, a provádí nad nimi operace, které mu zadáte. Čili proměnné a příkazy v buňkách se vykonávají v globálním kontextu kernelu daného Jupyter notebooku. Jakmile si tedy někde nadefinujete proměnnou, máte k ní přístup z kterékoliv buňky v notebooku (až na vyjímky, ale o tom si řekneme později). Čili hodnotu proměnné *a* můžete klidně použít v další buňce:

![variables.png](variables.png  "variables.png")

Toto chování pro nás občas může představovat problém. Obzvlášť pokud uděláme chybu a omylem si do prostředí zapíšeme něco, co tam nechceme. Než chybu manuálně opravovat, je často lepší prostě jenom restartovat aktuální kernel a všechny buňky znovu vyhodnotit. Toho lze docílit pomocí položky *Kernel* na ovládacím panelu:

![kernel_restart.png](kernel_restart.png  "kernel_restart.png")

Můžeme si vybrat hned z několika možností, ale tou nejčastější je pravděpodobně *Restart & Run All*, kterou se zresetuje aktuálně běžící kernel a všechny buňky se vyhodnotí znovu. Pouhý *Restart* jen zresetuje kernel, ale vaše výstupy zůstanou beze změny. Všechny vaše proměnné však zmizí z aktuálního prostředí, takže již k nim nebudete mít přístup.

Toto tedy byly ty nejnutnější základy, kterým je třeba porozumět při práci s Jupyter Notebooky. Ostatní funkce jsou poměrně intuitivní a není je třeba moc vysvětlovat. Koncept *learning by doing* zde funguje docela dobře. Všechny další tutoriály již budou psány téměř výhradně ve formě Jupyter notebooků, do kterých lze vkládat formátované poznámky nebo i matematické vzorce. Například buňka přepnutá do formátu Markdown (pomocí dropdown menu *Code* na ovládacím panelu) s následujícím obsahem:

```Markdown
# Vzorečky

- Pythagorova věta: $c^2 = a^2 + b^2$
- Boltzmannova rovnice: ${\displaystyle {\frac {\partial f}{\partial t}}+{\frac {\partial f}{\partial \mathbf {x} }}\cdot {\frac {\mathbf {p} }{m}}+{\frac {\partial f}{\partial \mathbf {p} }}\cdot \mathbf {F} =\left.{\frac {\partial f}{\partial t}}\right|_{\mathrm {coll} }.}$
- Schrödingerova rovnice: ${\displaystyle \mathrm {i} \hbar {\frac {\partial \Psi }{\partial t}}=-{\frac {\hbar ^{2}}{2m}}\Delta \Psi +V\Psi }$
```

vygeneruje v [našem notebooku](02.ipynb) takovýto výstup:

![notes.png](notes.png  "notes.png")
