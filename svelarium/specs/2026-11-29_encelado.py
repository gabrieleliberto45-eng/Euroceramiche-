# SPAZIO. Immagini NASA/JPL-Caltech/Space Science Institute (pubblico dominio); scena 3: illustrazione NASA.
LINES = [
    (1, "Su questa luna di Saturno ci sono fontane d'acqua alte centinaia di chilometri.", "Su questa luna di SATURNO | ci sono fontane d'acqua | alte CENTINAIA di km.", 0),
    (2, "Si chiama Encelado, ed è larga quanto la distanza tra Roma e Milano.", "Si chiama ENCELADO, | ed è larga quanto | la distanza tra Roma e Milano.", 0),
    (2, "È coperta di ghiaccio, ed è uno degli oggetti più bianchi del Sistema Solare.", "È coperta di ghiaccio, | ed è uno degli oggetti | più BIANCHI del Sistema Solare.", 0),
    (3, "Nel duemilacinque, la sonda Cassini ha scoperto dei getti che escono dal polo sud.", "Nel 2005, | la sonda Cassini ha scoperto | dei getti | che escono dal POLO SUD.", 0),
    (4, "Sono geyser di acqua e ghiaccio, sparati nello spazio.", "Sono GEYSER | di acqua e ghiaccio, | sparati nello spazio.", 0),
    (5, "Vuol dire che sotto la crosta c'è un oceano d'acqua liquida.", "Vuol dire che sotto la crosta | c'è un OCEANO | d'acqua liquida.", 0),
    (6, "Cassini ci è passata attraverso, e ha trovato sale e molecole organiche.", "Cassini ci è passata attraverso, | e ha trovato SALE | e MOLECOLE ORGANICHE.", 0),
    (6, "Acqua, energia e chimica: gli ingredienti della vita.", "Acqua, energia e chimica: | gli ingredienti della VITA.", 0),
    (7, "Per questo è uno dei posti migliori dove cercarla.", "Per questo | è uno dei posti migliori | dove cercarla.", 0),
    (8, "E intanto, a più di un miliardo di chilometri da qui...", "E intanto, | a più di un miliardo di km | da qui...", 0),
]
HEAD = {
    1: [("FONTANE", 160, "c"), ("nello spazio", 90, "w")],
    2: [("ENCELADO", 160, "w"), ("luna di Saturno", 80, "c")],
    3: [("CASSINI", 160, "g"), ("la scoperta del 2005", 70, "w")],
    4: [("GEYSER", 170, "c"), ("di acqua e ghiaccio", 76, "w")],
    5: [("UN OCEANO", 150, "c"), ("sotto il ghiaccio", 80, "w")],
    6: [("SALE", 160, "w"), ("e molecole organiche", 70, "g")],
    7: [("VITA?", 190, "g"), ("il posto giusto per cercarla", 56, "w")],
    8: [("FONTANE", 160, "c"), ("nello spazio", 90, "w")],
}
SCENE_IMG = {1: (1, .55, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (4, .5, .3), 4: (5, .55, .5), 5: (6, .5, .6), 6: (3, .5, .6),
             7: (2, .4, .5, 1.2, 1.35), 8: (1, .55, .5, 1.08, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
