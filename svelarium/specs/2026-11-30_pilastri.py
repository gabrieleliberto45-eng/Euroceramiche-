# SPAZIO. Immagini NASA, ESA/Hubble, JPL-Caltech (pubblico dominio).
LINES = [
    (1, "Questa è una delle foto più famose dell'universo.", "Questa è una delle foto | più FAMOSE dell'universo.", 0),
    (2, "Si chiamano i Pilastri della Creazione, e li ha fotografati Hubble nel millenovecentonovantacinque.", "Si chiamano i PILASTRI DELLA CREAZIONE, | e li ha fotografati Hubble | nel 1995.", 0),
    (3, "Sono colonne di gas e polvere nella Nebulosa Aquila.", "Sono colonne di gas e polvere | nella Nebulosa Aquila.", 0),
    (3, "La più alta è lunga circa quattro anni luce.", "La più alta è lunga | circa 4 ANNI LUCE.", 0),
    (4, "Dentro, nascono nuove stelle.", "Dentro, | nascono NUOVE STELLE.", 0),
    (5, "Ma sono lontani circa seimilacinquecento anni luce.", "Ma sono lontani | circa 6.500 anni luce.", 0),
    (5, "Quindi li vediamo com'erano prima che nascessero le piramidi.", "Quindi li vediamo com'erano | prima che nascessero | le PIRAMIDI.", 0),
    (6, "Nel duemilaventidue, il telescopio James Webb li ha fotografati di nuovo.", "Nel 2022, | il telescopio James Webb | li ha fotografati di nuovo.", 0),
    (7, "E chissà come sono, oggi...", "E chissà come sono, | oggi...", 0),
]
HEAD = {
    1: [("LA FOTO", 160, "w"), ("più famosa dell'universo", 64, "c")],
    2: [("PILASTRI", 160, "c"), ("della Creazione", 90, "w")],
    3: [("4 ANNI LUCE", 140, "g"), ("di altezza", 90, "w")],
    4: [("NUOVE STELLE", 128, "c"), ("nascono qui", 90, "w")],
    5: [("6.500 ANNI", 150, "g"), ("prima delle piramidi", 70, "w")],
    6: [("JAMES WEBB", 140, "c"), ("2022", 120, "w")],
    7: [("LA FOTO", 160, "w"), ("più famosa dell'universo", 64, "c")],
}
SCENE_IMG = {1: (1, .4, .6, 1.0, 1.08), 2: (1, .3, .55, 1.2, 1.35), 3: (3, .5, .5), 4: (1, .5, .4, 1.4, 1.6), 5: (2, .5, .5),
             6: (3, .6, .4, 1.2, 1.35), 7: (1, .4, .6, 1.08, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
