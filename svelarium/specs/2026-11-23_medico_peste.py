LINES = [
    (1, "Questa maschera è il simbolo della peste nera.", "Questa maschera | è il simbolo della PESTE NERA.", 0),
    (1, "Ma c'è un problema: durante la peste nera non esisteva.", "Ma c'è un problema: | durante la peste nera | NON ESISTEVA.", 0),
    (2, "La grande epidemia è del milletrecentoquarantotto.", "La grande epidemia | è del 1348.", 0),
    (3, "Il costume col becco compare quasi tre secoli dopo, nel Seicento, e viene attribuito a un medico francese, Charles de Lorme.",
     "Il costume col becco | compare quasi tre secoli dopo, | nel Seicento, | attribuito a un medico francese, | Charles de Lorme.", 0),
    (4, "Il becco era lungo e pieno di erbe profumate: menta, rose, chiodi di garofano, canfora.",
     "Il becco era lungo | e pieno di erbe profumate: | menta, rose, | chiodi di garofano, canfora.", 0),
    (5, "Perché? Si credeva che la malattia si diffondesse con l'aria cattiva, i cosiddetti miasmi.",
     "Perché? | Si credeva che la malattia | si diffondesse con l'aria cattiva, | i cosiddetti MIASMI.", 0),
    (6, "Il cappotto era di tela cerata, e il medico usava un bastone per visitare i malati senza toccarli.",
     "Il cappotto era di tela cerata, | e il medico usava un bastone | per visitare i malati | senza toccarli.", 0),
    (7, "Funzionava? Contro la peste, quasi per niente.", "Funzionava? | Contro la peste, | quasi per niente.", 0),
    (7, "Il vero colpevole erano le pulci.", "Il vero colpevole | erano le pulci.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("IL SIMBOLO", 130, "w"), ("della peste nera", 70, "g")],
    2: [("ANNO 1348", 140, "r"), ("la grande epidemia", 66, "w")],
    3: [("300 ANNI DOPO", 120, "g"), ("nel Seicento", 70, "w")],
    4: [("UN BECCO DI ERBE", 104, "w"), ("menta · rose · canfora", 60, "g")],
    5: [("L'ARIA CATTIVA", 116, "c"), ("la teoria dei miasmi", 64, "w")],
    6: [("SENZA TOCCARE", 116, "w"), ("solo con il bastone", 64, "g")],
    7: [("FUNZIONAVA?", 140, "r"), ("quasi per niente", 70, "w")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5), 6: (6, .5, .5),
             7: (1, .5, .45, 1.35, 1.6), 8: (1, .5, .5, 1.1, 1.0)}
SONG = "output012.mp3"
