# Immagini: NASA (satellite + ISS, PD) e ceramiche Nazca del Museum of World Culture, Svezia (CC0).
LINES = [
    (1, "Nel deserto del Perù ci sono disegni giganti che si vedono bene solo dall'alto.",
     "Nel deserto del Perù | ci sono disegni GIGANTI | che si vedono bene solo dall'alto.", 0),
    (2, "Li tracciò il popolo Nazca, più di millecinquecento anni fa.", "Li tracciò il popolo Nazca, | più di 1.500 anni fa.", 0),
    (3, "Un colibrì, una scimmia, un ragno, e centinaia di linee dritte lunghe chilometri.",
     "Un colibrì, una scimmia, un ragno, | e centinaia di linee dritte | lunghe chilometri.", 0),
    (4, "Ma da terra sembrano solo sentieri.", "Ma da terra | sembrano solo sentieri.", 0),
    (5, "Nel duemilaventiquattro, grazie all'intelligenza artificiale, ne sono state scoperte altre trecentotré.",
     "Nel 2024, | grazie all'intelligenza artificiale, | ne sono state scoperte altre 303.", 0),
    (6, "Calendari del cielo? Riti per chiamare l'acqua? Nessuno lo sa con certezza.",
     "Calendari del cielo? | Riti per chiamare l'acqua? | Nessuno lo sa con certezza.", 0),
    (6, "Tu cosa ne pensi? Scrivilo nei commenti.", "Tu cosa ne pensi? | Scrivilo nei commenti.", 0),
    (7, "E chi le ha disegnate, non le ha mai viste così...", "E chi le ha disegnate, | non le ha mai viste così...", 0),
]
HEAD = {
    1: [("VISIBILI", 150, "w"), ("SOLO DALL'ALTO", 116, "g")],
    2: [("IL POPOLO NAZCA", 112, "g"), ("oltre 1.500 anni fa", 66, "w")],
    3: [("LINEE", 160, "w"), ("lunghe chilometri", 70, "g")],
    4: [("DA TERRA", 150, "w"), ("solo sentieri", 72, "g")],
    5: [("+303", 210, "c"), ("scoperte con l'IA nel 2024", 58, "w")],
    6: [("PERCHÉ?", 170, "r"), ("nessuno lo sa", 72, "w")],
    7: [("VISIBILI", 150, "w"), ("SOLO DALL'ALTO", 116, "g")],
}
SCENE_IMG = {1: (1, .45, .4, 1.0, 1.1), 2: (2, .3, .5), 3: (1, .4, .35, 1.4, 1.6), 4: (5, .5, .6), 5: (3, .5, .5),
             6: (4, .5, .45), 7: (1, .45, .4, 1.1, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
