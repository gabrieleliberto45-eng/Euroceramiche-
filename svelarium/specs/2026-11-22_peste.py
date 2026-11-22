
LINES = [
    (1, "Ottobre milletrecentoquarantasette. Dodici navi entrano nel porto di Messina.", "Ottobre 1347. | Dodici navi | entrano nel porto di Messina.", 0),
    (2, "A bordo, quasi tutti i marinai sono morti. O stanno morendo.", "A bordo, | quasi tutti i marinai sono morti. | O stanno morendo.", 0),
    (3, "È l'inizio della peste nera.", "È l'inizio della PESTE NERA.", 0),
    (3, "In pochi anni ucciderà almeno un europeo su tre.", "In pochi anni ucciderà | almeno un europeo su tre.", 0),
    (4, "Il colpevole era un batterio, portato dalle pulci dei ratti.", "Il colpevole era un batterio, | portato dalle pulci dei ratti.", 0),
    (4, "Ma nessuno lo sapeva.", "Ma nessuno lo sapeva.", 0),
    (5, "Così, nel 1377, Ragusa, l'attuale Dubrovnik, prova una cosa nuova:", "Così, nel 1377, | Ragusa, l'attuale Dubrovnik, | prova una cosa nuova:", 0),
    (5, "chi arriva dal mare deve aspettare trenta giorni prima di entrare in città.", "chi arriva dal mare | deve aspettare 30 giorni | prima di entrare in città.", 0),
    (6, "Poi i giorni diventano quaranta.", "Poi i giorni diventano 40.", 0),
    (6, "Ed è da lì che nasce una parola che conosci benissimo:", "Ed è da lì che nasce una parola | che conosci benissimo:", 0),
    (7, "quarantena.", "QUARANTENA.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("OTTOBRE 1347", 120, "w"), ("12 navi arrivano a Messina", 62, "g")],
    2: [("A BORDO", 130, "w"), ("quasi tutti morti", 70, "r")],
    3: [("LA PESTE NERA", 120, "r"), ("1 europeo su 3", 76, "w")],
    4: [("IL COLPEVOLE?", 120, "w"), ("le pulci dei ratti", 70, "g")],
    5: [("RAGUSA · 1377", 116, "g"), ("30 giorni di attesa", 70, "w")],
    6: [("DA 30 A 40", 150, "g"), ("giorni di attesa", 70, "w")],
    7: [("QUARANTENA", 150, "r"), ("è nata così", 70, "w")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5, 1.0, 1.12), 7: (6, .75, .2, 1.4, 1.7), 8: (1, .5, .5, 1.12, 1.0)}
SONG = "output012.mp3"
