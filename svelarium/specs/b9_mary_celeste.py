# MISTERI. Immagini: Rijksmuseum (pubblico dominio).
LINES = [
    (1, "Nel milleottocentosettantadue, una nave fu trovata alla deriva in mezzo all'Atlantico.", "Nel 1872, | una nave fu trovata alla deriva | in mezzo all'ATLANTICO.", 0),
    (2, "Si chiamava Mary Celeste. Alcune vele erano ancora spiegate.", "Si chiamava MARY CELESTE. | Alcune vele | erano ancora spiegate.", 0),
    (3, "A bordo c'era cibo per sei mesi, e acqua in abbondanza.", "A bordo c'era cibo | per 6 MESI, | e acqua in abbondanza.", 0),
    (4, "Gli oggetti dell'equipaggio erano tutti al loro posto.", "Gli oggetti dell'equipaggio | erano tutti al loro posto.", 0),
    (5, "Ma delle dieci persone a bordo, non c'era più nessuno.", "Ma delle 10 persone a bordo, | non c'era più NESSUNO.", 0),
    (6, "Mancava solo una scialuppa di salvataggio.", "Mancava solo | una SCIALUPPA di salvataggio.", 0),
    (6, "Nessuno di loro fu mai ritrovato.", "Nessuno di loro | fu MAI RITROVATO.", 0),
    (7, "Ammutinamento? Pirati? Una tempesta?", "Ammutinamento? | Pirati? | Una tempesta?", 0),
    (8, "Oggi l'ipotesi più seguita è che il carico di alcol abbia fatto temere un'esplosione.", "Oggi l'ipotesi più seguita | è che il carico di ALCOL | abbia fatto temere | un'esplosione.", 0),
    (9, "E che tutti siano saliti sulla scialuppa, per non tornare mai più...", "E che tutti | siano saliti sulla scialuppa, | per non tornare MAI PIÙ...", 0),
]
HEAD = {
    1: [("NAVE FANTASMA", 128, "w"), ("1872", 150, "g")],
    2: [("MARY CELESTE", 130, "g"), ("vele ancora alzate", 72, "w")],
    3: [("CIBO", 170, "w"), ("per 6 mesi", 90, "g")],
    4: [("TUTTO", 170, "w"), ("al suo posto", 90, "g")],
    5: [("10 PERSONE", 150, "w"), ("SPARITE", 160, "r")],
    6: [("UNA SCIALUPPA", 124, "g"), ("mai ritrovata", 80, "w")],
    7: [("COSA È SUCCESSO?", 108, "w")],
    8: [("L'IPOTESI", 150, "g"), ("il carico di alcol", 76, "w")],
    9: [("NAVE FANTASMA", 128, "w"), ("1872", 150, "g")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .45), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (7, .45, .5), 8: (8, .25, .5), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
