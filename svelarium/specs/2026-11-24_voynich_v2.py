# Nuovo formato: ~25 s, scene ogni ~3 s, nessun saluto finale, loop (l'ultima frase porta alla prima).
# Immagini REALI: pagine del manoscritto Voynich (Beinecke Library, Yale, MS 408, pubblico dominio).
LINES = [
    (1, "Questo libro non lo sa leggere nessuno.", "Questo libro | non lo sa leggere NESSUNO.", 0),
    (2, "Ha seicento anni: la pergamena risale ai primi del Quattrocento.", "Ha 600 anni: | la pergamena risale | ai primi del Quattrocento.", 0),
    (3, "È scritto in un alfabeto che non esiste da nessun'altra parte.", "È scritto in un alfabeto | che non esiste | da nessun'altra parte.", 0),
    (4, "Dentro ci sono piante sconosciute,", "Dentro ci sono piante sconosciute,", 0),
    (5, "mappe di stelle,", "mappe di stelle,", 0),
    (6, "e donne immerse in strane vasche.", "e donne immerse in strane vasche.", 0),
    (7, "I migliori crittografi della guerra ci hanno provato. Anche i computer moderni.",
     "I migliori crittografi della guerra | ci hanno provato. | Anche i computer moderni.", 0),
    (8, "Niente.", "NIENTE.", 0),
    (9, "E dopo seicento anni...", "E dopo 600 anni...", 0),
]
HEAD = {
    1: [("NESSUNO", 150, "w"), ("SA LEGGERLO", 120, "g")],
    2: [("600 ANNI", 160, "g"), ("primi del Quattrocento", 60, "w")],
    3: [("UN ALFABETO", 120, "w"), ("CHE NON ESISTE", 108, "g")],
    4: [("PIANTE", 150, "g"), ("sconosciute", 70, "w")],
    5: [("MAPPE", 150, "c"), ("di stelle", 70, "w")],
    6: [("STRANE VASCHE", 116, "g"), ("e donne immerse", 66, "w")],
    7: [("MAI DECIFRATO", 120, "r"), ("crittografi e computer", 60, "w")],
    8: [("NIENTE.", 170, "r")],
    9: [("NESSUNO", 150, "w"), ("SA LEGGERLO", 120, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .4, .3, 1.5, 1.7), 4: (4, .5, .5), 5: (5, .5, .5, 1.0, 1.1),
             6: (6, .5, .5), 7: (7, .5, .5), 8: (8, .5, .5), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
