# Statistická analýza dat &ndash; R tutoriál

Toto je repozitář učebních materiálů ke cvičení ze [Statistické analýzy dat](https://student.vscht.cz/predmety/index.php?do=predmet&kod=N143042). Lekce jsou organizované do složek, které obsahují jak učební text, tak i zdrojový kód. 

V každé složce se nachází soubor `README.md`, který čtenáře danou lekcí provede a popřípadě odkáže na další zdroje. Většina lekcí je realizována pomocí interaktivních notebooků, které lze po stažení spustit a volně modifikovat v prostředí Jupyter (instalace a použití jsou diskutovány v lekcích [jedna](01) a [dva](02)).

Jakékoliv dotazy lze mimo běžné kanály též směrovat na [issue tracker](https://github.com/martin-sicho/r_tutorial/issues).

## Seznam lekcí

1. [Instalace a první spuštění R](./01)
2. [Jupyter Notebook &ndash; letem světem](./02)
3. [Základy programování v R](./03)
4. [Datové struktury](./04)
5. [Manipulace dat](./05)
6. [Popisná statistika](./06)
7. [Intervaly spolehlivosti](./07)
8. [Testování statistických hypotéz](./08)
9. [3D vizualizace](./09)
10. [Procvičování](./procvicovani)

## Rychlý návod k instalaci prostředí a spuštění notebooků

Stáhněte se distribuci balíčkovacího systému [Miniconda](https://conda.io/miniconda.html). Pomocí Anaconda Prompt si do hlavního prostředí nainstalujte git, pokud ho nemáte:

```bash
conda install -c conda-forge git
```

Po instalaci přejděte do adresáře, kde chcete mít repozitář s tutoriálem uložený, například na Windows by to mohlo být:

```bash
D:
cd moje_projekty\SAD
```

Potom použijte git pro získání obrazu repozitáře a přejděte do něj:

```bash
git clone https://github.com/lich-uct/r_tutorial.git
cd r_tutorial
```
Vytvořte si pracovní prostředí pomocí souboru `environment.yml`:

```bash
conda env create -n sadenv -f environment.yml
```

a aktivujte jej:

```bash
activate sadenv # syntaxe pro Windows
```

Nyní byste již měli být schopni si v libovolné složce spustit Jupyter Notebook server a vše by mělo fungovat:

```
jupyter-notebook
```
