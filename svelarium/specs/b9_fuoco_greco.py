# STORIA. Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "C'era un'arma che bruciava perfino sull'acqua.", "C'era un'arma | che bruciava | perfino SULL'ACQUA.", 0),
    (2, "La usavano i Bizantini, nel settimo secolo, per difendere Costantinopoli.", "La usavano i BIZANTINI, | nel VII secolo, | per difendere Costantinopoli.", 0),
    (3, "Dalle loro navi usciva un getto di fuoco liquido, spinto da un sifone.", "Dalle loro navi | usciva un getto di FUOCO LIQUIDO, | spinto da un sifone.", 0),
    (4, "Gettare acqua non serviva: le fiamme continuavano a bruciare.", "Gettare acqua non serviva: | le fiamme continuavano | a bruciare.", 0),
    (4, "Si diceva che solo sabbia, aceto o urina potessero spegnerlo.", "Si diceva che solo sabbia, | aceto o URINA | potessero spegnerlo.", 0),
    (5, "Grazie a quest'arma, la città resistette agli assedi arabi.", "Grazie a quest'arma, | la città resistette | agli assedi arabi.", 0),
    (6, "Ma la ricetta era un segreto di Stato.", "Ma la ricetta | era un SEGRETO DI STATO.", 0),
    (6, "La conoscevano solo pochissime famiglie.", "La conoscevano | solo pochissime famiglie.", 0),
    (7, "Con il tempo, andò perduta.", "Con il tempo, | andò PERDUTA.", 0),
    (8, "Ancora oggi nessuno sa con certezza come fosse fatto.", "Ancora oggi NESSUNO sa | con certezza | come fosse fatto.", 0),
    (9, "Petrolio? Calce viva? Zolfo? Il mistero resta...", "Petrolio? | Calce viva? | Zolfo? | Il mistero resta...", 0),
]
HEAD = {
    1: [("BRUCIAVA", 160, "r"), ("anche sull'ACQUA", 90, "w")],
    2: [("BISANZIO", 160, "g"), ("VII secolo", 80, "w")],
    3: [("FUOCO LIQUIDO", 124, "r"), ("sparato dalle navi", 76, "w")],
    4: [("L'ACQUA", 160, "w"), ("non lo spegneva", 80, "r")],
    5: [("COSTANTINOPOLI", 108, "g"), ("salvata", 90, "w")],
    6: [("SEGRETO", 160, "r"), ("di Stato", 90, "w")],
    7: [("PERDUTO", 170, "g"), ("per sempre", 80, "w")],
    8: [("COME ERA FATTO?", 112, "w"), ("nessuno lo sa", 80, "g")],
    9: [("BRUCIAVA", 160, "r"), ("anche sull'ACQUA", 90, "w")],
}
SCENE_IMG = {1: (1, .6, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (1, .75, .5, 1.2, 1.35), 4: (4, .5, .5), 5: (5, .45, .5),
             6: (6, .5, .5), 7: (7, .45, .5), 8: (8, .5, .5), 9: (1, .6, .5, 1.08, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
