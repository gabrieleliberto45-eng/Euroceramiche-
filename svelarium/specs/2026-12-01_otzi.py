# STORIA (preistoria, Alpi). Immagini: ricostruzioni generate con IA.
LINES = [
    (1, "Nel millenovecentonovantuno, due escursionisti trovano un corpo nel ghiaccio delle Alpi.", "Nel 1991, | due escursionisti | trovano un corpo | nel GHIACCIO delle Alpi.", 0),
    (1, "Pensano a un alpinista morto da poco.", "Pensano a un alpinista | morto da poco.", 0),
    (2, "Invece quell'uomo aveva più di cinquemila anni.", "Invece quell'uomo | aveva più di | 5.000 ANNI.", 0),
    (3, "Oggi lo chiamiamo Ötzi.", "Oggi lo chiamiamo | ÖTZI.", 0),
    (4, "Aveva con sé un'ascia di rame, un arco e delle frecce.", "Aveva con sé | un'ascia di RAME, | un arco | e delle frecce.", 0),
    (5, "Sulla pelle, sessantuno tatuaggi.", "Sulla pelle, | 61 TATUAGGI.", 0),
    (5, "Nello stomaco, il suo ultimo pasto: carne di stambecco.", "Nello stomaco, | il suo ultimo pasto: | carne di stambecco.", 0),
    (6, "Ma dieci anni dopo, una radiografia mostrò qualcosa di incredibile.", "Ma dieci anni dopo, | una radiografia | mostrò qualcosa | di INCREDIBILE.", 0),
    (7, "Una punta di freccia, conficcata nella spalla sinistra.", "Una PUNTA DI FRECCIA, | conficcata | nella spalla sinistra.", 0),
    (8, "Quindi non era morto di freddo.", "Quindi non era morto | di freddo.", 0),
    (8, "Era stato ucciso.", "Era stato | UCCISO.", 0),
    (9, "Chi lo abbia colpito, e perché, resta un mistero da cinquemila anni...", "Chi lo abbia colpito, | e perché, | resta un mistero | da 5.000 anni...", 0),
]
HEAD = {
    1: [("NEL GHIACCIO", 124, "w"), ("delle Alpi", 100, "c")],
    2: [("5.000 ANNI", 150, "g"), ("prima di noi", 90, "w")],
    3: [("ÖTZI", 200, "w"), ("l'uomo venuto dal ghiaccio", 60, "c")],
    4: [("ASCIA DI RAME", 120, "g"), ("arco e frecce", 90, "w")],
    5: [("61 TATUAGGI", 140, "w"), ("sulla pelle", 90, "g")],
    6: [("10 ANNI DOPO", 130, "w"), ("una radiografia", 90, "g")],
    7: [("UNA FRECCIA", 140, "r"), ("nella spalla", 90, "w")],
    8: [("UCCISO", 180, "r"), ("non dal freddo", 90, "w")],
    9: [("NEL GHIACCIO", 124, "w"), ("delle Alpi", 100, "c")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .45), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (7, .5, .5), 8: (8, .5, .5), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
