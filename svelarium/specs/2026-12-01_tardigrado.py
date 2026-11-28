# SCIENZA (natura/spazio). Immagini: ricostruzioni generate con IA.
LINES = [
    (1, "Questo animale è sopravvissuto nello spazio aperto.", "Questo animale | è sopravvissuto | nello SPAZIO aperto.", 0),
    (1, "Senza tuta.", "Senza TUTA.", 0),
    (2, "È il tardigrado, lungo meno di un millimetro.", "È il TARDIGRADO, | lungo meno | di un millimetro.", 0),
    (3, "Vive nel muschio, nei laghi, perfino sotto il ghiaccio.", "Vive nel muschio, | nei laghi, | perfino sotto il ghiaccio.", 0),
    (4, "Nel duemilasette, gli scienziati lo spedirono in orbita, fuori da una capsula.", "Nel 2007, | gli scienziati | lo spedirono in ORBITA, | fuori da una capsula.", 0),
    (5, "Per dieci giorni restò nel vuoto, al gelo, tra i raggi cosmici.", "Per dieci giorni | restò nel VUOTO, | al gelo, | tra i raggi cosmici.", 0),
    (6, "Quando tornò sulla Terra, si risvegliò.", "Quando tornò sulla Terra, | si RISVEGLIÒ.", 0),
    (6, "E fece perfino dei figli.", "E fece perfino | dei figli.", 0),
    (7, "Il suo segreto?", "Il suo SEGRETO?", 0),
    (7, "Si secca quasi del tutto e si chiude in una pallina.", "Si secca | quasi del tutto | e si chiude | in una pallina.", 0),
    (8, "Così può restare in pausa per anni.", "Così può restare | in pausa | per ANNI.", 0),
    (9, "Basta una goccia d'acqua, e torna a camminare.", "Basta una goccia d'acqua, | e torna | a camminare.", 0),
    (10, "Per questo è uno degli animali più resistenti del pianeta...", "Per questo è | uno degli animali | più RESISTENTI | del pianeta...", 0),
]
HEAD = {
    1: [("NELLO SPAZIO", 124, "w"), ("senza tuta", 100, "g")],
    2: [("IL TARDIGRADO", 120, "g"), ("meno di 1 mm", 90, "w")],
    3: [("OVUNQUE", 160, "w"), ("anche sotto il ghiaccio", 66, "c")],
    4: [("2007", 190, "g"), ("in orbita", 100, "w")],
    5: [("10 GIORNI", 150, "w"), ("nel vuoto", 100, "c")],
    6: [("VIVO", 190, "g"), ("e fece dei figli", 86, "w")],
    7: [("IL SEGRETO", 140, "w"), ("si secca", 100, "g")],
    8: [("IN PAUSA", 160, "c"), ("per anni", 100, "w")],
    9: [("UNA GOCCIA", 140, "c"), ("e si risveglia", 90, "w")],
    10: [("NELLO SPAZIO", 124, "w"), ("senza tuta", 100, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (7, .5, .5), 8: (7, .5, .5, 1.3, 1.15), 9: (8, .5, .5), 10: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
