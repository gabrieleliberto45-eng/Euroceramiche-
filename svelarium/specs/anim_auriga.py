# STORIA ANIMATA (immagini IA animate: serve l'etichetta "Contenuti alterati").
LINES = [
    (1, "L'atleta più pagato della storia non è un calciatore. È un auriga romano.", "L'atleta più PAGATO della storia | non è un calciatore. | È un AURIGA ROMANO.", 0),
    (2, "Si chiamava Gaio Appuleio Diocle, e correva con le quadrighe al Circo Massimo.", "Si chiamava Gaio Appuleio DIOCLE, | e correva con le quadrighe | al Circo Massimo.", 0),
    (2, "Lì dentro potevano stare oltre centocinquantamila persone.", "Lì dentro potevano stare | oltre 150.000 PERSONE.", 0),
    (3, "C'erano quattro squadre: Verdi, Azzurri, Rossi e Bianchi. E i tifosi si odiavano.", "C'erano 4 squadre: | Verdi, Azzurri, Rossi e Bianchi. | E i tifosi si ODIAVANO.", 0),
    (4, "Le corse erano violentissime.", "Le corse erano | VIOLENTISSIME.", 0),
    (5, "I carri si schiantavano a ogni curva.", "I carri si schiantavano | a ogni CURVA.", 0),
    (6, "Diocle corse per ventiquattro anni e vinse quasi millecinquecento gare.", "Diocle corse per 24 anni | e vinse quasi 1.500 GARE.", 0),
    (7, "In tutto guadagnò trentacinque milioni di sesterzi.", "In tutto guadagnò | 35 MILIONI di sesterzi.", 0),
    (7, "Secondo alcuni studiosi, oggi varrebbero miliardi.", "Secondo alcuni studiosi, | oggi varrebbero MILIARDI.", 0),
    (8, "E tutto questo, quasi duemila anni fa...", "E tutto questo, | quasi 2.000 anni fa...", 0),
]
HEAD = {
    1: [("L'ATLETA", 150, "w"), ("più pagato della storia", 70, "g")],
    2: [("CIRCO MASSIMO", 124, "g"), ("150.000 spettatori", 76, "w")],
    3: [("4 SQUADRE", 150, "w"), ("tifosi rivali", 86, "g")],
    4: [("VIOLENTISSIME", 124, "r"), ("le corse dei carri", 76, "w")],
    5: [("SCHIANTI", 160, "r"), ("a ogni curva", 86, "w")],
    6: [("1.500 VITTORIE", 124, "g"), ("in 24 anni", 86, "w")],
    7: [("35 MILIONI", 150, "g"), ("di sesterzi", 90, "w")],
    8: [("L'ATLETA", 150, "w"), ("più pagato della storia", 70, "g")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5), 6: (6, .5, .5), 7: (7, .5, .5), 8: (1, .5, .5)}
SONG = "output005.mp3"
TAIL = 0.25
