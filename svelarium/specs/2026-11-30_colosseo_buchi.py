# STORIA. Immagini: Rijksmuseum, MKG Hamburg (pubblico dominio).
LINES = [
    (1, "Hai mai notato che il Colosseo è pieno di buchi?", "Hai mai notato | che il Colosseo | è pieno di BUCHI?", 0),
    (2, "Non sono stati i proiettili, e nemmeno le guerre.", "Non sono stati i proiettili, | e nemmeno le guerre.", 0),
    (3, "I blocchi di travertino erano tenuti insieme da perni di ferro e bronzo.", "I blocchi di travertino | erano tenuti insieme | da perni di FERRO e BRONZO.", 0),
    (4, "Nel Medioevo il metallo valeva moltissimo.", "Nel Medioevo | il metallo valeva moltissimo.", 0),
    (4, "Così la gente scavava nella pietra per strapparli via, uno dopo l'altro.", "Così la gente scavava nella pietra | per strapparli via, | uno dopo l'altro.", 0),
    (5, "Ogni buco che vedi è un perno rubato.", "Ogni buco che vedi | è un PERNO RUBATO.", 0),
    (6, "Dopo il terremoto del milletrecentoquarantanove, anche le pietre crollate furono portate via.", "Dopo il terremoto del 1349, | anche le pietre crollate | furono portate via.", 0),
    (6, "Finirono in chiese e palazzi di Roma.", "Finirono in chiese | e palazzi di Roma.", 0),
    (7, "Per secoli, il Colosseo è stato una cava.", "Per secoli, | il Colosseo è stato | una CAVA.", 0),
    (8, "E quei buchi sono ancora lì, a raccontarlo...", "E quei buchi sono ancora lì, | a raccontarlo...", 0),
]
HEAD = {
    1: [("PIENO DI BUCHI", 124, "w"), ("perché?", 120, "g")],
    2: [("NON SONO", 150, "w"), ("proiettili", 100, "r")],
    3: [("FERRO E BRONZO", 116, "g"), ("dentro la pietra", 80, "w")],
    4: [("IL MEDIOEVO", 140, "w"), ("il metallo valeva oro", 66, "g")],
    5: [("OGNI BUCO", 150, "w"), ("un perno rubato", 86, "r")],
    6: [("1349", 190, "g"), ("il terremoto", 90, "w")],
    7: [("UNA CAVA", 160, "g"), ("per secoli", 90, "w")],
    8: [("PIENO DI BUCHI", 124, "w"), ("perché?", 120, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (1, .3, .6, 1.4, 1.6), 4: (3, .5, .5), 5: (2, .7, .5, 1.3, 1.5),
             6: (4, .5, .5), 7: (5, .5, .15, 1.15, 1.3), 8: (1, .5, .5, 1.08, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
