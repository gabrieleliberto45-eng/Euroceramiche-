# ENIGMA (loop, risposta mai detta). Risposta: i sopravvissuti non si seppelliscono. Immagini NASA (pubblico dominio).
LINES = [
    (1, "Solo una persona su dieci risolve questo enigma.", "Solo una persona su dieci | risolve questo ENIGMA.", 0),
    (2, "Un aereo cade esattamente sul confine tra Italia e Francia.", "Un aereo cade | esattamente sul CONFINE | tra Italia e Francia.", 0),
    (3, "Le autorità devono decidere in quale paese seppellire i sopravvissuti.", "Le autorità devono decidere | in quale paese seppellire | i SOPRAVVISSUTI.", 0),
    (4, "Dove li seppelliscono? Hai tre secondi.", "Dove li seppelliscono? | Hai tre secondi.", 0),
    (5, "Tre.", "", 0),
    (6, "Due.", "", 0),
    (7, "Uno.", "", 0),
    (8, "Scrivi la risposta nei commenti.", "Scrivi la risposta | nei commenti.", 0),
    (9, "La risposta è...", "La risposta è...", 0),
]
HEAD = {
    1: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
    2: [("SUL CONFINE", 140, "w"), ("Italia - Francia", 90, "g")],
    3: [("DOVE", 170, "w"), ("li seppelliscono?", 86, "g")],
    4: [("ITALIA O FRANCIA?", 104, "g"), ("hai 3 secondi", 70, "w")],
    5: [("3", 420, "g")],
    6: [("2", 420, "g")],
    7: [("1", 420, "r")],
    8: [("SCRIVILO", 150, "g"), ("nei commenti", 76, "w")],
    9: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
}
SCENE_IMG = {1: (1, .4, .5, 1.0, 1.08), 2: (3, .5, .5), 3: (4, .5, .5), 4: (2, .5, .5),
             5: (1, .3, .5, 1.4, 1.5), 6: (1, .5, .5, 1.4, 1.5), 7: (1, .7, .5, 1.4, 1.5),
             8: (5, .5, .5, 1.1, 1.25), 9: (1, .4, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
