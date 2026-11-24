# TOP 5. Immagini: Deutsche Fotothek, Rijksmuseum, National Gallery of Denmark (SMK) - pubblico dominio.
LINES = [
    (1, "Usi ogni giorno cinque invenzioni romane. Resta fino al numero uno.", "Usi ogni giorno | 5 invenzioni ROMANE. | Resta fino al numero 1.", 0),
    (2, "Numero cinque: le strade lastricate. La via Appia ha più di duemila anni, e ci si cammina ancora.",
     "Numero 5: | le strade lastricate. | La via Appia ha più di 2.000 anni, | e ci si cammina ancora.", 0),
    (3, "Numero quattro: il giornale. Giulio Cesare faceva affiggere nel Foro le notizie del giorno.",
     "Numero 4: il giornale. | Giulio Cesare faceva affiggere nel Foro | le notizie del giorno.", 0),
    (4, "Numero tre: il cemento. Il Pantheon è in piedi da quasi duemila anni.", "Numero 3: il cemento. | Il Pantheon è in piedi | da quasi 2.000 anni.", 0),
    (5, "Numero due: il calendario. Lo riformò Giulio Cesare, con l'anno bisestile.", "Numero 2: il calendario. | Lo riformò Giulio Cesare, | con l'anno bisestile.", 0),
    (6, "Numero uno: i nomi dei mesi. Luglio viene da Giulio Cesare. Agosto, da Augusto.",
     "Numero 1: i nomi dei mesi. | LUGLIO viene da Giulio Cesare. | AGOSTO, da Augusto.", 0),
    (7, "E la prossima volta che guardi il calendario...", "E la prossima volta | che guardi il calendario...", 0),
]
HEAD = {
    1: [("5 INVENZIONI", 136, "w"), ("ROMANE", 160, "g")],
    2: [("#5", 230, "g"), ("le strade", 80, "w")],
    3: [("#4", 230, "g"), ("il giornale", 80, "w")],
    4: [("#3", 230, "g"), ("il cemento", 80, "w")],
    5: [("#2", 230, "g"), ("il calendario", 80, "w")],
    6: [("#1", 230, "r"), ("i nomi dei mesi", 76, "w")],
    7: [("5 INVENZIONI", 136, "w"), ("ROMANE", 160, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.1), 2: (2, .5, .55), 3: (1, .3, .5, 1.3, 1.45), 4: (3, .5, .55), 5: (5, .5, .4, 1.0, 1.15),
             6: (6, .5, .4), 7: (1, .5, .5, 1.1, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
