# ENIGMA (loop, risposta mai detta). Risposta: 9 (tutte tranne nove scappano: ne restano nove). Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "Solo una persona su dieci risolve questo enigma.", "Solo una persona su dieci | risolve questo ENIGMA.", 0),
    (2, "Un contadino ha diciassette pecore.", "Un contadino | ha 17 PECORE.", 0),
    (3, "Una notte, tutte tranne nove scappano.", "Una notte, | tutte TRANNE NOVE | scappano.", 0),
    (4, "Quante pecore restano al contadino? Hai tre secondi.", "Quante pecore | restano al contadino? | Hai tre secondi.", 0),
    (5, "Tre.", "", 0),
    (6, "Due.", "", 0),
    (7, "Uno.", "", 0),
    (8, "Scrivi la risposta nei commenti.", "Scrivi la risposta | nei commenti.", 0),
    (9, "La risposta è...", "La risposta è...", 0),
]
HEAD = {
    1: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
    2: [('17 PECORE', 150, 'g'), ('un contadino', 80, 'w')],
    3: [('UNA NOTTE', 140, 'w'), ('tutte tranne 9 scappano', 62, 'r')],
    4: [('QUANTE NE RESTANO?', 100, 'g'), ('hai 3 secondi', 70, 'w')],
    5: [("3", 420, "g")],
    6: [("2", 420, "g")],
    7: [("1", 420, "r")],
    8: [("SCRIVILO", 150, "g"), ("nei commenti", 76, "w")],
    9: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5),
             5: (1, .3, .5, 1.4, 1.5), 6: (1, .5, .5, 1.4, 1.5), 7: (1, .7, .5, 1.4, 1.5),
             8: (5, .5, .5, 1.1, 1.25), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
