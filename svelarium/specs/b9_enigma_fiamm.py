# ENIGMA (loop, risposta mai detta). Risposta: il fiammifero (va acceso per primo). Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "Solo una persona su dieci risolve questo enigma.", "Solo una persona su dieci | risolve questo ENIGMA.", 0),
    (2, "Entri in una stanza buia. Hai un solo fiammifero.", "Entri in una stanza BUIA. | Hai un solo FIAMMIFERO.", 0),
    (3, "Nella stanza ci sono una candela, una lampada a olio e un camino.", "Nella stanza ci sono | una candela, | una lampada a olio | e un camino.", 0),
    (4, "Cosa accendi per primo? Hai tre secondi.", "Cosa accendi PER PRIMO? | Hai tre secondi.", 0),
    (5, "Tre.", "", 0),
    (6, "Due.", "", 0),
    (7, "Uno.", "", 0),
    (8, "Scrivi la risposta nei commenti.", "Scrivi la risposta | nei commenti.", 0),
    (9, "La risposta è...", "La risposta è...", 0),
]
HEAD = {
    1: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
    2: [('STANZA BUIA', 140, 'w'), ('1 solo fiammifero', 76, 'g')],
    3: [('CANDELA', 130, 'g'), ('LAMPADA', 130, 'g'), ('CAMINO', 130, 'g')],
    4: [('COSA ACCENDI', 120, 'w'), ('PER PRIMO?', 140, 'g')],
    5: [("3", 420, "g")],
    6: [("2", 420, "g")],
    7: [("1", 420, "r")],
    8: [("SCRIVILO", 150, "g"), ("nei commenti", 76, "w")],
    9: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (4, .5, .5), 4: (3, .5, .4),
             5: (1, .3, .5, 1.4, 1.5), 6: (1, .5, .5, 1.4, 1.5), 7: (1, .7, .5, 1.4, 1.5),
             8: (5, .5, .5, 1.1, 1.25), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
