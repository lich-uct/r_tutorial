# Instalace a první spuštění R

V tomto tutoriálu si ukážeme, jak získat distribuci jazyka R a podíváme se na software, který nám usnadní práci při jeho používání (tzv. vývojová prostředí). Kupodivu je aplikací celá řada a všechny jsou v podstatě zdarma, takže v tomto ohledu máme štěstí. Pojďme se tedy do toho pustit.

## R jako takové

Implementace jazyka R je (včetně jednoduchého vývojového prostředí) distribuována jako open source software pod licencí [GPL](https://github.com/wch/r-source/blob/trunk/COPYING). To znamená, že ho může používat v podstatě kdokoliv a zdarma (dokonce i pro komerční účely), pokud neporušuje konkrétní podmínky licence. Stačí si pouze na [stránkách projektu](https://cloud.r-project.org/) stáhnout verzi pro váš systém a můžete začít.

Nejčastěji asi budeme chtít používat R pod systémem Windows, takže se v tomto tutoriálu omezíme pouze na tuto variantu, ale pro ostatní operační systémy je postup též jednoduchý.

 1. Ze [stránek](https://cloud.r-project.org/) stáhneme instalační soubor. Z nabídky různých binárek vybereme možnost 'base', což je holá instalace, která v sobě obsahuje ty nejzákladnější funkce jazyka, což je pro nás více než dostačující.
 2. Soubor spustíme a zobrazí se instalační dialog. Podle potřeby si upravíme nastavení a klikáme na příslušná tlačítka dokud se R nenainstaluje.
 3. Po spuštění přes zástupce v nabídce start by se nám mělo zobrazit okno s příkazovou řádkou, které bude vypadat asi takto:
    
![R_command_line.png](R_command_line.png  "R_command_line.png")

Do tohoto rozhranní již můžete začít psát první příkazy. Můžete například začít zavoláním funkce `help()`, která zobrazí nápovědu, nebo `q()`, která aktuální sezení ukončí a zavře vývojové prostředí.

## Vývojová prostředí

Jak jste už asi zjistili při instalaci a prvním spuštění holého R, tak tato verze R vám opravdu nenabízí velké pohodlí při psaní příkazů a zobrazování výsledků vašich výpočtů. Nejste jediní, komu se zdá, že R potřebuje propracovanější uživatelské rozhranní, a proto vzniklo několik vývojových prostředí pro tento jazyk. My si zde ukážeme dvě z nich momentálně nejpoužívanější.

### RStudio

[RStudio](https://www.rstudio.com) lze získat v open source verzi opět pro celou řadu platforem [zde](https://www.rstudio.com/products/rstudio/download/#download). Pro použití RStudia je třeba již mít nainstalovanou základní distribuci R, jak jsme si ukázali výše. 

Instalace je obdobná a pokud vše proběhlo, jak mělo, tak se vám po nastartování RStudia otevře následující uživatelské rozhranní, které je již na první pohled o něco bohatší:

![RStudio.png](RStudio.png  "RStudio.png")

Co všechno RStudio umí a jak v něm pracovat je nad rámec tohoto krátkého tutoriálu, ale jedná se o velice intuitivní nástroj, jehož základní funkce lze pochopit během několika minut. Práce zpravidla spočívá v tom, že příkazy buď píšete do konzole, nebo pomocí vestavěného editoru vytvoříte krátký skirpt, který se pak příkaz po příkazu v konzoli spustí. V konzoli se pak zobrazují jednoduché textové výsledky, zatímco grafy, nápověda, obsah prostředí a další komplexnější informace se pak zobrazují v ostatních panelech.

Stojí za to ještě zmínit, že je k dispozici i tzv. "portable" verze RStudia, kterou není třeba instalovat. Je tak možné ji využít například na univerzitních počítačích, kde nemá uživatel dostatek práv pro instalaci nového software. Portable RStudio je dostupné pod [stejným odkazem jako běžná verze](https://www.rstudio.com/products/rstudio/download/). Stačí jenom zvolit verzi ze sekce "Zip/tar archives" místo "Installers". Po rozbalení archivu pak stačí jen najít spouštěcí soubor (pro Windows je to `rstudio.exe` ve složce `bin`).

### Anaconda a Jupyter Notebook

V poslední době se postupně rozšiřuje pro práci s daty platforma Jupyter. Tento software se v podstatě snaží imitovat prostředí nástrojů jako je Matlab, Maple nebo Wolfram Mathematica, ale je též open source a tedy úplně zdarma. [Jupyter](http://jupyter.org/) byl původně vytvořen jako prostředí pro jazyk Python, který je v oblasti datové analýzy též velice populární, ale postupně vznikaly i rozšíření na další jazyky včetně R. Instalace tohoto software již vyžaduje větší snahu, neboť je třeba skloubit dohromady více nástrojů. 

V první řadě je třeba instalace interpreteru pro jazyk [Python](https://www.python.org/), ve kterém je uživatelské rozhranní napsáno. My si v tomto tutoriálu ukážeme, jak si toto vývojové prostředí rozhýbat na systému Windows, ale i na jiných platformách je postup téměř identický. K instalaci Pythonu, ale i samotného R budeme používat distribuci jazyka Python a balíčkovací manažer [Anaconda](https://www.continuum.io/anaconda), který nemá s R nebo statistickou analýzou dat na první pohled nic společného, ale je velice užitečný při spravování programů a dalšího software. Do tzv. virtuálního prostředí lze nainstalovat téměř cokoliv, co se nachází v [oficiálním repozitáři balíčků](https://anaconda.org/) (včetně samotného [R a RStudia](https://anaconda.org/r)). Pomocí tohoto integrovaného balíčkovacího systému tak dává uživateli možnost vytvořit si vývojové prostředí na míru a bez zbytečného 'zaplevelení' operačního systému programy, které budete využívat jen pro jeden projekt (nebo absolvování tohoto předmětu) a dále už třeba nikdy.

My v našem tutoriálu budeme používat zmenšenou verzi Anacondy, Minicondu, která je k dispozici pro Windows hned v několika verzích. Jak si můžete všimnout při otevření [stránky pro download](https://conda.io/miniconda.html), Miniconda již má v sobě integrovaný jazyk Python a to jak verzi 3, tak starší verzi 2. V dnešní době již v podstatě až na vyjímečné případy není důvod používat verzi 2, takže my sáhneme po verzi 3.

Při instalaci Minicondy budeme dotázáni, zda chceme přidat naší distribuci do systémové proměnné PATH. Tahle proměnnná rozhoduje o tom, kde hledat spouštěcí soubory různých nástrojů v našem systému. My ji při instalaci modifikovat nechceme, a proto necháme zaškrtávací tlačítko tak, jak je (nezaškrtnuté), aby nedošlo ke konfliktům se softwarem, který je již na systému nainstalován. Ke spuštění nástroje použijeme tzv. Anaconda Prompt, který by měl být po instalaci dostupný z nabídky Start. Tento krok je specifický pouze pro systém Windows. Na ostatních platformách je možné používat rozhranní Minicondy přímo z vaší příkazové řádky.

Anaconda prompt je obyčejná příkazová řádka, která je ovšem obohacená o všechen software, který nám prostředí Miniconda nabízí. Vzhledem k tomu, že Miniconda je redukovaná v počtu balíčků, který si s sebou nese, tak ho zatím není mnoho. Aktuálně nainstalované balíčky si lze zobrazit příkazem `conda list`:

```no-highlight
(C:\Users\user\Miniconda3) C:\Users\user>conda list
# packages in environment at C:\Users\user\Miniconda3:
#
asn1crypto                0.22.0                   py36_0
cffi                      1.10.0                   py36_0
conda                     4.3.21                   py36_0
conda-env                 2.6.0                         0
console_shortcut          0.1.1                    py36_1
cryptography              1.8.1                    py36_0
idna                      2.5                      py36_0
menuinst                  1.4.7                    py36_0
openssl                   1.0.2l                   vc14_0  [vc14]
packaging                 16.8                     py36_0
pip                       9.0.1                    py36_1
pycosat                   0.6.2                    py36_0
pycparser                 2.17                     py36_0
pyopenssl                 17.0.0                   py36_0
pyparsing                 2.1.4                    py36_0
python                    3.6.1                         2
pywin32                   220                      py36_2
requests                  2.14.2                   py36_0
ruamel_yaml               0.11.14                  py36_1
setuptools                27.2.0                   py36_1
six                       1.10.0                   py36_0
vs2015_runtime            14.0.25123                    0
wheel                     0.29.0                   py36_0
```

Toto v podstatě znamená výběr toho nejnutnějšího a představuje balíčky nainstalované v implicitním prostředí (root nebo base), které je aktuálně aktivní. Seznam prostředí, která se na systému momentálně nachází, lze získtat příkazem `conda env list`:

```no-highlight
(C:\Users\user\Miniconda3) C:\Users\user>conda env list
# conda environments:
#
base                  *  C:\Users\user\Miniconda3
```

Jak vidíme, zatím máme jen defaultní prostředí *base*, které je pro nás momentálně celkem nezajímavé. Čili si vytvoříme nové prostředí, do kterého budeme instalovat všechen software, který budeme v tomto tutoriálu potřebovat. Stačí nám na to pouze jeden příkaz: `conda create -n statistika r rstudio`. Vypíše se nám dlouhý seznam balíčků, které budou do daného prostředí nainstalovány. Po odsouhlasení stiskem <kbd>y</kbd> se balíčky stáhnou a nainstalují (může chvíli trvat v závislosti na vašem hardware a internetovém připojení). Po úspěšné instalaci nám nástroj navrhne příkaz pro přístup do nového prostředí:

```no-highlight
#
# To activate this environment, use:
# > activate statistika
#
# To deactivate this environment, use:
# > deactivate statistika
#
# * for power-users using bash, you must source
#
```

Když tak učiníme, přenese nás nástroj do nově vytvořeného prostředí:

```no-highlight
(C:\Users\user\Miniconda3) C:\Users\user>activate statistika

(statistika) C:\Users\user>
```

Všimněte si změny tvaru příkazové řádky, která teď obsahuje jméno našeho prostředí, které jsme výše specifikovali pomocí parametru `-n statistika`. Po zadání příkazu `conda env list` již také vidíme naše prostředí v seznamu:

```no-highlight
(statistika) C:\Users\user>conda env list
# conda environments:
#
statistika            *  C:\Users\user\Miniconda3\envs\statistika
root                     C:\Users\user\Miniconda3
```

Jelikož se nyní jedná o aktivní prostředí, je v seznamu označeno hvězdičkou společně z cestou, kde jsou uloženy všechny soubory a software. V tomto právě spočívá hlavní výhoda Anacondy, neboť nám takto umožňuje snadné spravování programů v našich projektech bez rizika konfliktů mezi různými verzemi a podobných neduhů, kterých bychom se mohli dočkat při instalaci přímo do operačního systému. Jednotlivá prostředí jsou plně nezávislá a lze se jich kdykoliv zbavit, což je neocenitelné pokud máte například najednou rozdělaných více projektů na jednom počítači.

Pokud máte aktivované prostředí `statistika`, lze teď R jednoduše spustit přímo v příkazové řádce pomocí příkazu `R`. Stejně tak lze spustit i RStudio (pomocí `rstudio`)  a potažmo další software, který byste mohli potřebovat. Celého prostředí se všemi balíčky se pak snadno můžete zbavit pomocí příkazu `conda env remove -n statistika` (nezapomeňte se z něj nejprve odhlásit pomocí `deactivate statistika`). Pokud se chcete zbavit i stažených balíčků a cache, můžete tak potom učinit příkazem `conda clean --all`. Zatím si však prostředí nechte. V tutoriálu jej budeme ještě potřebovat.

Vraťme se teď ale zpět k Jupyteru. Pokud do našeho prostředí `statistika` ještě doinstalujeme dva balíčky (`conda install r-irkernel jupyter`), pak budeme mít v našem prostředí nově k dispozici příkaz `jupyter-notebook`, který spouští R na pozadí jako server a nám přímo v okně webového prohlížeče otevře náhled aktuálního adresáře, což může vypadat nějak takto:

![jupyter_gui.png](jupyter_gui.png  "jupyter_gui.png")

Rozhraní lze používat v podstatě stejně jako kterýkoliv jiný správce souborů. Po kliknutí na tlačítko *New* vpravo nahoře můžeme vytvářet adresáře a textové soubory, ale hlavně lze též vytvořit tzv. notebooky (jak v jazyce R, tak i Python), což jsou interaktivní textové soubory, které vypadají nějak takto:

![notebook_example.png](notebook_example.png  "notebook_example.png")

Sem již můžeme do tzv. buněk psát jednotlivé příkazy a přímo sledovat výstup z programu. Pro vykonání příkazů v buňce slouží kombinace kláves <kbd>shift</kbd> + <kbd>Enter</kbd>.  Jak s notebookem pracovat a jeho rozšířené funkce si však detailněji představíme až v [dalším tutoriálu](../02/).