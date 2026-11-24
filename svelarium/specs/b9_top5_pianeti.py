# TOP 5. Immagini NASA/JPL (pubblico dominio).
LINES = [
    (1, "Cinque record del Sistema Solare che sembrano impossibili. Resta fino al numero uno.", "5 record del SISTEMA SOLARE | che sembrano impossibili. | Resta fino al numero 1.", 0),
    (2, "Numero cinque: Saturno. È così leggero che, in una vasca abbastanza grande, galleggerebbe.", "Numero 5: SATURNO. | È così leggero che, | in una vasca abbastanza grande, | GALLEGGEREBBE.", 0),
    (3, "Numero quattro: Nettuno. I suoi venti superano i duemila chilometri all'ora.", "Numero 4: NETTUNO. | I suoi venti superano | i 2.000 km all'ora.", 0),
    (4, "Numero tre: Giove. La sua Grande Macchia Rossa è una tempesta più grande della Terra.", "Numero 3: GIOVE. | La sua Grande Macchia Rossa | è una tempesta | più grande della Terra.", 0),
    (5, "Numero due: Urano. Ruota sdraiato su un fianco, come una palla che rotola.", "Numero 2: URANO. | Ruota sdraiato su un fianco, | come una palla che rotola.", 0),
    (6, "Numero uno: Venere. Lì un giorno dura più di un anno, e il Sole sorge a ovest.", "Numero 1: VENERE. | Lì un giorno | dura più di un ANNO, | e il Sole sorge a OVEST.", 0),
    (7, "E questi sono solo cinque...", "E questi sono solo cinque...", 0),
]
HEAD = {
    1: [("5 RECORD", 160, "w"), ("IMPOSSIBILI", 136, "g")],
    2: [("#5", 230, "g"), ("Saturno galleggia", 76, "w")],
    3: [("#4", 230, "g"), ("venti a 2.000 km/h", 72, "w")],
    4: [("#3", 230, "g"), ("tempesta gigante", 76, "w")],
    5: [("#2", 230, "g"), ("il pianeta sdraiato", 72, "w")],
    6: [("#1", 230, "r"), ("giorno più lungo dell'anno", 60, "w")],
    7: [("5 RECORD", 160, "w"), ("IMPOSSIBILI", 136, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.1), 2: (1, .62, .5), 3: (2, .5, .5), 4: (3, .5, .5), 5: (4, .5, .5),
             6: (5, .5, .5), 7: (1, .5, .5, 1.1, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
