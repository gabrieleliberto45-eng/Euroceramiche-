# ENIGMA (loop, risposta mai detta). Risposta: i leoni, perché dopo tre anni senza mangiare sono morti.
LINES = [
    (1, "Solo una persona su dieci risolve questo enigma.", "Solo una persona su dieci | risolve questo ENIGMA.", 0),
    (2, "Sei chiuso in un castello, e devi scegliere una porta.", "Sei chiuso in un castello, | e devi scegliere una porta.", 0),
    (3, "Nella prima stanza c'è un incendio che non si spegne mai.", "Nella prima stanza | c'è un incendio | che non si spegne mai.", 0),
    (4, "Nella seconda, dieci assassini armati ti aspettano.", "Nella seconda, | dieci assassini armati | ti aspettano.", 0),
    (5, "Nella terza, leoni che non mangiano da tre anni.", "Nella terza, | leoni che non mangiano | da tre anni.", 0),
    (6, "Quale porta scegli? Hai tre secondi.", "Quale porta scegli? | Hai tre secondi.", 0),
    (7, "Tre.", "", 0),
    (8, "Due.", "", 0),
    (9, "Uno.", "", 0),
    (10, "Scrivi la risposta nei commenti.", "Scrivi la risposta | nei commenti.", 0),
    (11, "La risposta è...", "La risposta è...", 0),
]
HEAD = {
    1: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
    2: [("SCEGLI", 150, "w"), ("UNA PORTA", 130, "g")],
    3: [("PORTA 1", 150, "r"), ("un incendio eterno", 66, "w")],
    4: [("PORTA 2", 150, "r"), ("10 assassini armati", 66, "w")],
    5: [("PORTA 3", 150, "r"), ("leoni a digiuno da 3 anni", 60, "w")],
    6: [("QUALE SCEGLI?", 120, "g"), ("hai 3 secondi", 70, "w")],
    7: [("3", 420, "g")],
    8: [("2", 420, "g")],
    9: [("1", 420, "r")],
    10: [("SCRIVILO", 150, "g"), ("nei commenti", 76, "w")],
    11: [("SOLO 1 SU 10", 140, "g"), ("risolve questo enigma", 64, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (1, .5, .6, 1.1, 1.3), 3: (2, .5, .5), 4: (3, .5, .5), 5: (4, .5, .5),
             6: (5, .5, .5), 7: (1, .2, .6, 1.4, 1.5), 8: (1, .5, .6, 1.4, 1.5), 9: (1, .8, .6, 1.4, 1.5),
             10: (5, .6, .4, 1.2, 1.3), 11: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
