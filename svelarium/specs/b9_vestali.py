# STORIA. Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "Nell'antica Roma, sei donne custodivano un fuoco che non doveva spegnersi mai.", "Nell'antica Roma, | sei donne custodivano un fuoco | che non doveva spegnersi MAI.", 0),
    (2, "Erano le Vestali, sacerdotesse della dea Vesta.", "Erano le VESTALI, | sacerdotesse della dea Vesta.", 0),
    (3, "Venivano scelte da bambine, tra i sei e i dieci anni.", "Venivano scelte da bambine, | tra i 6 e i 10 anni.", 0),
    (4, "Servivano per trent'anni, e dovevano restare caste.", "Servivano per 30 ANNI, | e dovevano restare caste.", 0),
    (5, "In cambio avevano privilegi che nessun'altra donna romana aveva.", "In cambio avevano privilegi | che nessun'altra donna romana | aveva.", 0),
    (6, "Potevano fare testamento, e avevano posti d'onore ai giochi.", "Potevano fare testamento, | e avevano posti d'onore | ai giochi.", 0),
    (7, "Ma se il fuoco si spegneva, venivano frustate.", "Ma se il fuoco si spegneva, | venivano FRUSTATE.", 0),
    (7, "Se invece infrangevano il voto, la pena era terribile.", "Se invece infrangevano il voto, | la pena era TERRIBILE.", 0),
    (8, "Venivano sepolte vive, in una stanza sotto terra, con un po' di pane e una lampada.", "Venivano SEPOLTE VIVE, | in una stanza sotto terra, | con un po' di pane | e una lampada.", 0),
    (9, "Perché il sangue di una Vestale non poteva essere versato.", "Perché il sangue di una Vestale | non poteva essere versato.", 0),
    (10, "E nel tempio, intanto, il fuoco continuava a bruciare...", "E nel tempio, intanto, | il fuoco continuava a bruciare...", 0),
]
HEAD = {
    1: [("IL FUOCO", 160, "w"), ("che non si spegneva", 76, "g")],
    2: [("LE VESTALI", 150, "g"), ("sacerdotesse di Vesta", 66, "w")],
    3: [("SCELTE", 160, "w"), ("da bambine", 90, "g")],
    4: [("30 ANNI", 170, "g"), ("di servizio", 80, "w")],
    5: [("PRIVILEGI", 150, "g"), ("unici a Roma", 80, "w")],
    6: [("POSTI D'ONORE", 120, "g"), ("e un testamento", 76, "w")],
    7: [("LA PUNIZIONE", 130, "r"), ("era terribile", 80, "w")],
    8: [("SEPOLTE VIVE", 136, "r"), ("sotto terra", 80, "w")],
    9: [("IL SANGUE", 150, "w"), ("non si versava", 80, "r")],
    10: [("IL FUOCO", 160, "w"), ("che non si spegneva", 76, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .4), 3: (3, .5, .3), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .4), 7: (1, .5, .6, 1.2, 1.35), 8: (7, .5, .5), 9: (8, .3, .5), 10: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
