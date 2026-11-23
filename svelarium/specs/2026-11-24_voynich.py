LINES = [
    (1, "Questo libro ha seicento anni, e nessuno al mondo riesce a leggerlo.", "Questo libro ha 600 anni, | e nessuno al mondo | riesce a LEGGERLO.", 0),
    (2, "Si chiama manoscritto Voynich, dal nome del libraio che lo comprò nel millenovecentododici.",
     "Si chiama manoscritto VOYNICH, | dal nome del libraio | che lo comprò nel 1912.", 0),
    (3, "La pergamena è stata datata al radiocarbonio: tra il millequattrocentoquattro e il millequattrocentotrentotto.",
     "La pergamena è stata datata | al radiocarbonio: | tra il 1404 e il 1438.", 0),
    (4, "Dentro ci sono piante che non esistono, mappe di stelle, e strane figure femminili immerse in vasche.",
     "Dentro ci sono piante | che non esistono, | mappe di stelle, | e strane figure immerse in vasche.", 0),
    (5, "La scrittura è unica: un alfabeto mai visto altrove.", "La scrittura è unica: | un alfabeto mai visto altrove.", 0),
    (6, "Crittografi della Seconda guerra mondiale ci hanno provato. Anche i computer moderni.",
     "Crittografi della Seconda guerra mondiale | ci hanno provato. | Anche i computer moderni.", 0),
    (6, "Nessuno è riuscito a decifrarlo.", "Nessuno è riuscito | a DECIFRARLO.", 0),
    (7, "Forse è un codice segreto. O una lingua perduta. O un'elaborata burla.",
     "Forse è un codice segreto. | O una lingua perduta. | O un'elaborata burla.", 0),
    (7, "Tu cosa ne pensi? Scrivilo nei commenti.", "Tu cosa ne pensi? | Scrivilo nei commenti.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("600 ANNI", 160, "g"), ("e nessuno sa leggerlo", 64, "w")],
    2: [("IL VOYNICH", 140, "g"), ("comprato nel 1912", 66, "w")],
    3: [("1404 - 1438", 140, "c"), ("datato al radiocarbonio", 62, "w")],
    4: [("PIANTE CHE", 120, "w"), ("NON ESISTONO", 120, "g")],
    5: [("UN ALFABETO UNICO", 100, "g"), ("mai visto altrove", 66, "w")],
    6: [("MAI DECIFRATO", 120, "r"), ("neanche dai computer", 64, "w")],
    7: [("TU COSA", 130, "w"), ("NE PENSI?", 130, "g")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5), 6: (6, .5, .5),
             7: (1, .5, .55, 1.3, 1.55), 8: (4, .5, .5, 1.1, 1.0)}
SONG = "output005.mp3"
