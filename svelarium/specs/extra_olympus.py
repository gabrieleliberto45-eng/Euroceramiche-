# Immagini: NASA/JPL (Viking, MRO HiRISE) e NASA (STS-66) - pubblico dominio.
LINES = [
    (1, "Questo è il vulcano più alto del Sistema Solare.", "Questo è il vulcano più alto | del SISTEMA SOLARE.", 0),
    (2, "Si chiama Olympus Mons, ed è su Marte.", "Si chiama Olympus Mons, | ed è su MARTE.", 0),
    (3, "È alto circa ventidue chilometri.", "È alto circa 22 chilometri.", 0),
    (4, "Il monte Everest ne misura meno di nove.", "Il monte Everest | ne misura meno di 9.", 0),
    (5, "La sua base è larga circa seicento chilometri, più o meno come da Milano a Napoli.",
     "La sua base è larga circa 600 km, | più o meno | come da Milano a Napoli.", 0),
    (6, "E se fossi in cima, non vedresti la base: è oltre l'orizzonte.", "E se fossi in cima, | non vedresti la base: | è oltre l'orizzonte.", 0),
    (7, "E la cosa più incredibile è che...", "E la cosa più incredibile | è che...", 0),
]
HEAD = {
    1: [("IL VULCANO", 140, "w"), ("PIÙ ALTO", 150, "r")],
    2: [("OLYMPUS MONS", 124, "g"), ("su Marte", 76, "w")],
    3: [("22 KM", 190, "r"), ("di altezza", 70, "w")],
    4: [("EVEREST", 150, "c"), ("meno di 9 km", 72, "w")],
    5: [("600 KM", 180, "g"), ("da Milano a Napoli", 66, "w")],
    6: [("OLTRE", 160, "w"), ("L'ORIZZONTE", 130, "g")],
    7: [("IL VULCANO", 140, "w"), ("PIÙ ALTO", 150, "r")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.1), 2: (2, .5, .5, 1.6, 1.8), 3: (3, .5, .5), 4: (4, .5, .5), 5: (1, .5, .5, 1.0, 1.2),
             6: (6, .5, .5), 7: (1, .5, .5, 1.1, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
