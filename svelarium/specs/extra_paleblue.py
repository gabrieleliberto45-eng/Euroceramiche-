# Immagini: NASA/JPL (pubblico dominio). Loop: finisce "Su quel puntino azzurro..." -> riparte "Quel puntino azzurro sei tu."
LINES = [
    (1, "Quel puntino azzurro sei tu.", "Quel puntino azzurro | sei TU.", 0),
    (2, "Nel millenovecentonovanta, la sonda Voyager uno era a sei miliardi di chilometri da casa.",
     "Nel 1990, la sonda Voyager 1 | era a 6 miliardi di chilometri | da casa.", 0),
    (3, "Carl Sagan chiese di girare la fotocamera, un'ultima volta, verso la Terra.", "Carl Sagan chiese di girare la fotocamera, | un'ultima volta, | verso la Terra.", 0),
    (4, "Ecco cosa vide.", "Ecco cosa vide.", 0),
    (5, "Ogni persona che hai mai conosciuto, ogni guerra, ogni storia d'amore, ogni re e ogni contadino:",
     "Ogni persona che hai mai conosciuto, | ogni guerra, ogni storia d'amore, | ogni re e ogni contadino:", 0),
    (6, "sono esistiti tutti lì, su un granello di polvere sospeso in un raggio di sole.",
     "sono esistiti tutti lì, | su un granello di polvere | sospeso in un raggio di sole.", 0),
    (7, "Su quel puntino azzurro...", "Su quel puntino azzurro...", 0),
]
HEAD = {
    1: [("QUESTO PUNTINO", 116, "w"), ("SEI TU", 150, "c")],
    2: [("VOYAGER 1", 150, "g"), ("6 miliardi di km da casa", 60, "w")],
    3: [("GIRATI", 150, "w"), ("un'ultima volta", 70, "g")],
    4: [("ECCO", 150, "c"), ("cosa vide", 76, "w")],
    5: [("TUTTI", 160, "w"), ("quelli che hai conosciuto", 60, "g")],
    6: [("UN GRANELLO", 130, "g"), ("di polvere nel sole", 66, "w")],
    7: [("QUESTO PUNTINO", 116, "w"), ("SEI TU", 150, "c")],
}
SCENE_IMG = {1: (1, .5, .45, 1.0, 1.1), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5, 1.0, 1.25),
             5: (5, .5, .5), 6: (6, .5, .5, 1.0, 1.15), 7: (1, .5, .45, 1.1, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
