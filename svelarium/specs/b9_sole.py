# SCIENZA. Immagini NASA/SDO (pubblico dominio).
LINES = [
    (1, "Il Sole che vedi in cielo non è quello di adesso.", "Il Sole che vedi in cielo | NON È quello di adesso.", 0),
    (2, "La sua luce impiega circa otto minuti e venti secondi per arrivare fino a noi.", "La sua luce impiega | circa 8 MINUTI e 20 secondi | per arrivare fino a noi.", 0),
    (2, "Quindi lo vedi com'era otto minuti fa.", "Quindi lo vedi | com'era 8 minuti fa.", 0),
    (3, "Se il Sole si spegnesse all'improvviso, per otto minuti non ce ne accorgeremmo.", "Se il Sole si spegnesse | all'improvviso, | per 8 minuti | NON CE NE ACCORGEREMMO.", 0),
    (4, "Continuerebbe a splendere, e la Terra a girargli intorno.", "Continuerebbe a splendere, | e la Terra | a girargli intorno.", 0),
    (5, "Con le stelle è ancora più estremo.", "Con le stelle | è ancora più estremo.", 0),
    (5, "La luce di alcune è partita migliaia di anni fa.", "La luce di alcune | è partita MIGLIAIA di anni fa.", 0),
    (6, "Qualcuna potrebbe essersi già spenta, e noi la vediamo ancora.", "Qualcuna potrebbe | essersi già spenta, | e noi la vediamo ANCORA.", 0),
    (7, "Guardare il cielo è guardare nel passato.", "Guardare il cielo | è guardare nel PASSATO.", 0),
    (8, "Perfino adesso...", "Perfino adesso...", 0),
]
HEAD = {
    1: [("IL SOLE CHE VEDI", 116, "w"), ("è nel PASSATO", 110, "g")],
    2: [("8 MINUTI", 170, "g"), ("di ritardo", 80, "w")],
    3: [("SE SI SPEGNESSE", 120, "r"), ("non lo sapresti", 80, "w")],
    4: [("PER 8 MINUTI", 140, "g"), ("tutto normale", 80, "w")],
    5: [("LE STELLE", 150, "w"), ("luce antica", 90, "g")],
    6: [("GIÀ SPENTE?", 140, "r"), ("le vedi ancora", 80, "w")],
    7: [("GUARDI", 150, "w"), ("IL PASSATO", 140, "g")],
    8: [("IL SOLE CHE VEDI", 116, "w"), ("è nel PASSATO", 110, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (4, .5, .5), 4: (3, .5, .5), 5: (5, .5, .5),
             6: (6, .7, .5), 7: (2, .4, .6, 1.2, 1.35), 8: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
