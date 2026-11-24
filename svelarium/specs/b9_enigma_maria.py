# ENIGMA (loop, risposta mai detta). Risposta: Maria (è il padre di Maria: la quinta figlia è lei). Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "Solo una persona su dieci risolve questo enigma.", "Solo una persona su dieci | risolve questo ENIGMA.", 0),
    (2, "Il padre di Maria ha cinque figlie.", "Il padre di MARIA | ha 5 figlie.", 0),
    (3, "La prima si chiama Lala. La seconda Lele. La terza Lili.", "La prima si chiama LALA. | La seconda LELE. | La terza LILI.", 0),
    (4, "Poi c'è Lolo, la quarta.", "Poi c'è LOLO, | la quarta.", 0),
    (5, "Come si chiama la quinta figlia? Hai tre secondi.", "Come si chiama | la QUINTA figlia? | Hai tre secondi.", 0),
    (6, "Tre.", "", 0),
    (7, "Due.", "", 0),
    (8, "Uno.", "", 0),
    (9, "Scrivi la risposta nei commenti.", "Scrivi la risposta | nei commenti.", 0),
    (10, "La risposta è...", "La risposta è...", 0),
]
HEAD = {
    1: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
    2: [('IL PADRE DI MARIA', 100, 'w'), ('5 FIGLIE', 160, 'g')],
    3: [('LALA', 130, 'g'), ('LELE', 130, 'g'), ('LILI', 130, 'g')],
    4: [('LOLO', 150, 'g')],
    5: [('LA QUINTA?', 150, 'r'), ('hai 3 secondi', 70, 'w')],
    6: [("3", 420, "g")],
    7: [("2", 420, "g")],
    8: [("1", 420, "r")],
    9: [("SCRIVILO", 150, "g"), ("nei commenti", 76, "w")],
    10: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .4), 5: (5, .5, .4),
             6: (1, .3, .5, 1.4, 1.5), 7: (1, .5, .5, 1.4, 1.5), 8: (1, .7, .5, 1.4, 1.5),
             9: (5, .5, .5, 1.1, 1.25), 10: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
