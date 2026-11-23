# Immagini: John Thomson 1871 (Wellcome Collection, CC BY 4.0) + NASA (pubblico dominio).
LINES = [
    (1, "Si dice che la Grande Muraglia si veda dallo spazio.", "Si dice che la Grande Muraglia | si veda dallo SPAZIO.", 0),
    (2, "È lunga più di ventimila chilometri.", "È lunga più di 20.000 chilometri.", 0),
    (3, "Ma è larga solo pochi metri.", "Ma è larga | solo pochi metri.", 0),
    (4, "Dalla Stazione Spaziale, a quattrocento chilometri d'altezza, è come cercare un capello a tre chilometri di distanza.",
     "Dalla Stazione Spaziale, | a 400 km d'altezza, | è come cercare un capello | a 3 km di distanza.", 0),
    (5, "Nel duemilatre il primo astronauta cinese, Yang Liwei, lo confermò: non l'aveva vista.",
     "Nel 2003 il primo astronauta cinese, | Yang Liwei, lo confermò: | NON l'aveva vista.", 0),
    (6, "Con un teleobiettivo, o con il radar, sì.", "Con un teleobiettivo, | o con il radar, sì.", 0),
    (7, "Ma a occhio nudo, no.", "Ma a occhio nudo... NO.", 0),
    (8, "Eppure, ancora oggi...", "Eppure, ancora oggi...", 0),
]
HEAD = {
    1: [("SI VEDE", 150, "w"), ("DALLO SPAZIO?", 116, "g")],
    2: [("20.000 KM", 150, "g"), ("di lunghezza", 70, "w")],
    3: [("POCHI METRI", 136, "r"), ("di larghezza", 70, "w")],
    4: [("COME UN CAPELLO", 108, "w"), ("visto da 3 km", 72, "g")],
    5: [("YANG LIWEI", 140, "g"), ("primo astronauta cinese", 60, "w")],
    6: [("CON IL RADAR", 124, "c"), ("sì", 90, "w")],
    7: [("A OCCHIO NUDO", 116, "w"), ("NO", 160, "r")],
    8: [("SI VEDE", 150, "w"), ("DALLO SPAZIO?", 116, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.1), 2: (4, .3, .5, 1.0, 1.15), 3: (4, .45, .5, 1.2, 1.4), 4: (6, .5, .5), 5: (8, .5, .5),
             6: (7, .5, .5), 7: (6, .5, .5, 1.3, 1.5), 8: (1, .5, .5, 1.1, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
