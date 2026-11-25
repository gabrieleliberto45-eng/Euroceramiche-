# MISTERI. Immagini: Rijksmuseum, Albertina, Deutsche Fotothek (pubblico dominio); Wellcome Collection (CC BY 4.0).
LINES = [
    (1, "Sotto il mare vicino a Napoli c'è una città romana intera.", "Sotto il mare | vicino a Napoli | c'è una CITTÀ ROMANA intera.", 0),
    (2, "Si chiamava Baia, ed era la località di lusso dei Romani più ricchi.", "Si chiamava BAIA, | ed era la località di lusso | dei Romani più ricchi.", 0),
    (3, "Qui avevano le loro ville Giulio Cesare e Nerone.", "Qui avevano le loro ville | Giulio CESARE | e NERONE.", 0),
    (4, "Terme, mosaici, statue. Poi, lentamente, tutto è sprofondato.", "Terme, mosaici, statue. | Poi, lentamente, | tutto è SPROFONDATO.", 0),
    (5, "Colpa del bradisismo dei Campi Flegrei: il suolo sale e scende, come se respirasse.", "Colpa del BRADISISMO | dei Campi Flegrei: | il suolo sale e scende, | come se RESPIRASSE.", 0),
    (6, "Oggi strade e ville sono sott'acqua, a pochi metri di profondità.", "Oggi strade e ville | sono SOTT'ACQUA, | a pochi metri di profondità.", 0),
    (7, "Poco lontano, a Pozzuoli, c'è una prova incredibile.", "Poco lontano, a Pozzuoli, | c'è una prova incredibile.", 0),
    (7, "Le colonne di un antico mercato sono bucate da molluschi marini.", "Le colonne di un antico mercato | sono BUCATE | da molluschi marini.", 0),
    (8, "Significa che sono finite sott'acqua, e poi sono riemerse.", "Significa che sono finite sott'acqua, | e poi sono RIEMERSE.", 0),
    (9, "E il suolo, ancora oggi, continua a muoversi...", "E il suolo, ancora oggi, | continua a MUOVERSI...", 0),
]
HEAD = {
    1: [("UNA CITTÀ", 160, "w"), ("sotto il MARE", 110, "c")],
    2: [("BAIA", 190, "g"), ("la città dei ricchi", 76, "w")],
    3: [("CESARE", 160, "g"), ("e NERONE", 110, "w")],
    4: [("SPROFONDATA", 136, "r"), ("lentamente", 80, "w")],
    5: [("IL SUOLO", 160, "w"), ("RESPIRA", 150, "g")],
    6: [("SOTT'ACQUA", 150, "c"), ("a pochi metri", 80, "w")],
    7: [("LA PROVA", 160, "g"), ("colonne bucate", 80, "w")],
    8: [("SOTT'ACQUA", 150, "c"), ("e poi di nuovo fuori", 70, "w")],
    9: [("UNA CITTÀ", 160, "w"), ("sotto il MARE", 110, "c")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .3, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (7, .5, .45), 8: (8, .7, .5), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25
