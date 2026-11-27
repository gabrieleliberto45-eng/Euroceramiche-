# MISTERO. Immagini: ricostruzioni generate con IA.
LINES = [
    (1, "Nel millecinquecentonovanta, un uomo torna dalla sua colonia in America.", "Nel 1590, | un uomo torna | dalla sua colonia in America.", 0),
    (1, "E non trova più nessuno.", "E non trova | più NESSUNO.", 0),
    (2, "Tre anni prima aveva lasciato lì più di cento coloni, tra cui sua nipote, appena nata.", "Tre anni prima | aveva lasciato lì | più di 100 coloni, | tra cui sua nipote, | appena nata.", 0),
    (3, "Era la colonia di Roanoke, uno dei primi villaggi inglesi in America.", "Era la colonia di ROANOKE, | uno dei primi villaggi | inglesi in America.", 0),
    (4, "Le case erano state smontate.", "Le case | erano state smontate.", 0),
    (4, "Nessun segno di battaglia.", "Nessun segno | di battaglia.", 0),
    (5, "Su un palo c'era incisa una sola parola: Croatoan.", "Su un palo | c'era incisa | una sola parola: | CROATOAN.", 0),
    (6, "Era il nome di un'isola vicina, e di una tribù amica.", "Era il nome | di un'isola vicina, | e di una tribù amica.", 0),
    (7, "Una tempesta impedì all'uomo di andare a controllare.", "Una TEMPESTA | impedì all'uomo | di andare a controllare.", 0),
    (7, "Non tornò mai più.", "Non tornò | MAI PIÙ.", 0),
    (8, "E dei coloni non si seppe più nulla.", "E dei coloni | non si seppe | più nulla.", 0),
    (9, "Ancora oggi gli archeologi cercano tracce di quelle persone...", "Ancora oggi | gli archeologi cercano | tracce di quelle persone...", 0),
]
HEAD = {
    1: [("SPARITI", 170, "w"), ("115 persone", 100, "g")],
    2: [("1587", 190, "g"), ("più di 100 coloni", 80, "w")],
    3: [("ROANOKE", 160, "w"), ("America", 90, "g")],
    4: [("NESSUNA", 150, "w"), ("battaglia", 110, "r")],
    5: [("CROATOAN", 150, "g"), ("una sola parola", 80, "w")],
    6: [("UN'ISOLA", 150, "w"), ("e una tribù amica", 80, "g")],
    7: [("LA TEMPESTA", 130, "w"), ("non tornò mai più", 80, "r")],
    8: [("SPARITI", 170, "w"), ("nel nulla", 100, "r")],
    9: [("ANCORA OGGI", 130, "w"), ("si cercano tracce", 80, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .4),
             6: (6, .5, .5), 7: (7, .5, .5), 8: (1, .4, .6, 1.25, 1.1), 9: (8, .5, .5)}
SONG = "output005.mp3"
TAIL = 0.25
