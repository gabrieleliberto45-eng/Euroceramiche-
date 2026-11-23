LINES = [
    (1, "Gli abitanti di Pompei non sapevano di vivere sotto un vulcano.", "Gli abitanti di Pompei | non sapevano | di vivere sotto un VULCANO.", 0),
    (2, "Per loro il Vesuvio era una montagna verde, coperta di vigne.", "Per loro il Vesuvio | era una montagna verde, | coperta di vigne.", 0),
    (2, "Da secoli non c'era una grande eruzione, e nessuno la ricordava.", "Da secoli | non c'era una grande eruzione, | e nessuno la ricordava.", 0),
    (3, "Nel sessantadue dopo Cristo, un forte terremoto danneggiò la città.", "Nel 62 dopo Cristo, | un forte terremoto | danneggiò la città.", 0),
    (3, "Ma nessuno lo collegò al vulcano, e Pompei fu ricostruita.", "Ma nessuno lo collegò al vulcano, | e Pompei fu ricostruita.", 0),
    (4, "Poi, nel settantanove, il Vesuvio esplose.", "Poi, nel 79, | il Vesuvio ESPLOSE.", 0),
    (4, "Una colonna di cenere e pietre salì per oltre trenta chilometri.", "Una colonna di cenere e pietre | salì per oltre 30 chilometri.", 0),
    (5, "Plinio il Giovane la vide dall'altra parte del golfo, a Miseno, e la descrisse come un enorme pino.",
     "Plinio il Giovane la vide | dall'altra parte del golfo, a Miseno, | e la descrisse | come un enorme pino.", 0),
    (6, "Suo zio, Plinio il Vecchio, partì con le navi per salvare la gente.", "Suo zio, Plinio il Vecchio, | partì con le navi | per salvare la gente.", 0),
    (6, "Non tornò mai.", "Non tornò mai.", 0),
    (7, "Oggi quel tipo di eruzione si chiama proprio così: pliniana.", "Oggi quel tipo di eruzione | si chiama proprio così: | PLINIANA.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("POMPEI", 160, "g"), ("non sapeva del vulcano", 64, "w")],
    2: [("UNA MONTAGNA VERDE", 96, "w"), ("coperta di vigne", 66, "g")],
    3: [("ANNO 62", 150, "g"), ("il terremoto", 70, "w")],
    4: [("ANNO 79", 150, "r"), ("il Vesuvio esplode", 66, "w")],
    5: [("COME UN PINO", 120, "w"), ("lo racconta Plinio", 64, "g")],
    6: [("NON TORNÒ MAI", 118, "r"), ("Plinio il Vecchio", 66, "w")],
    7: [("PLINIANA", 150, "g"), ("si chiama così", 70, "w")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .2, .5, 1.25, 1.35), 4: (4, .5, .5), 5: (5, .5, .5), 6: (6, .5, .5),
             7: (4, .5, .2, 1.4, 1.6), 8: (1, .5, .5, 1.1, 1.0)}
SONG = "output012.mp3"
