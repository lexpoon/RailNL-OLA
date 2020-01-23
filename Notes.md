Notes

- max 7 trajecten
- tijdsframe: 2 uur
- alle verbindingen bereden

voorbeeld output:
trein, lijnvoering
trein_1, "[Beverwijk, Castricum, Alkmaar, Hoorn, Zaandam]"

requirements:
- check in alle connecties of een station maar 1 keer voorkomt, dan is het een eindpunt
- een traject kan niet twee keer dezelfde connectie pakken, met booleans
- alle stations moeten bereikt zijn.
- alle verbindingen moeten bereden zijn.
<<<<<<< Updated upstream
=======


Algoritmes:

- Random:
- Greedy:
- Greedy + Random: Gebaseerd op twee variabelen in de score functie: Aantal connecties + Tijd, Random: score van de mogelijkheden zijn gelijk
- Breadth First: Bij ons geen voorkeur hoe diep er in de boom gekeken wordt, aantal nodes in route kan varieren en is afhankelijk van het aantal minuten en nog mogelijke routes die nog niet bereden zijn. Daarbij word er bij breadth first, in ons geval, veel gebruik gemaakt van onnodige rekenkracht/geheugen doordat het elke route gaat onthouden.
- Depth First: Alle mogelijke routes worden afgegaan zonder daarbij elke mogelijkheid in je archief/stack op te slaan. Het kost daardoor minder geheugen terwijl elke       
                mogelijkheid wordt bepaald.
    - Optimaal prunen:
        - Early constraint checking: Gebaseerd op de tijd, mag niet meer dan x aantal duren, afhankelijk van map
        - Archief: Houden bij welke routes gereden worden zodat je niet meerdere keren een dezelfde route in hetzelfde traject kan rijden
        - Branch and Bound: Niet van toepassing: omdat wij geen ideale bestemming hebben en dus wel dieper dan het korst gevonden pas, diepte maakt voor ons niet uit. Een omweg is per definitie niet slechter.
        - Dijkstra, A*: Dijkstra: Niet van toepassing: Zoekt naar het korste pad, geen toegevoegde waarde ivm formule en score,
        - Domein specifiek prunen: Niet van toepassing: niet vooruitkijken
    - Niet-optimaal prunen
        - Beam Search: Niet van toepassing: Is bedoeld voor breadth first
        - Greedy lookahead: 1. Als na x aantal stappen de score niet bijdraagt, abort mission
        - Heuristieken: Eerste station van routes is degene met minst aantal connecties,
- Iterative Deepening:
- Hillclimber:
    - Restart Hill Climber
    - Constrain Relaxation
    - Steepest Ascent Hill Climber
- Simulated Annealing:
>>>>>>> Stashed changes
