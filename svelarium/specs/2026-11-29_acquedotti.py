# STORIA. Immagini: Rijksmuseum, Ajuntament de Girona, MKG Hamburg (pubblico dominio).
LINES = [
    (1, "La Fontana di Trevi è alimentata da un acquedotto di duemila anni fa.", "La Fontana di Trevi | è alimentata da un acquedotto | di 2.000 ANNI fa.", 0),
    (2, "Si chiama Acqua Vergine, e la costruì Agrippa nel diciannove avanti Cristo.", "Si chiama ACQUA VERGINE, | e la costruì Agrippa | nel 19 a.C.", 0),
    (3, "Roma arrivò ad avere undici acquedotti.", "Roma arrivò ad avere | 11 ACQUEDOTTI.", 0),
    (3, "Portavano in città centinaia di milioni di litri d'acqua al giorno.", "Portavano in città | CENTINAIA DI MILIONI | di litri al giorno.", 0),
    (4, "Senza pompe e senza motori: solo con la gravità.", "Senza pompe | e senza motori: | solo con la GRAVITÀ.", 0),
    (5, "Il segreto era una pendenza minuscola, a volte pochi centimetri ogni cento metri.", "Il segreto | era una pendenza minuscola, | a volte POCHI CENTIMETRI | ogni 100 metri.", 0),
    (6, "Quasi tutti i percorsi erano sotto terra.", "Quasi tutti i percorsi | erano SOTTO TERRA.", 0),
    (6, "Gli archi che vedi servivano solo ad attraversare le valli.", "Gli archi che vedi | servivano solo | ad attraversare le valli.", 0),
    (7, "E oggi, quando lanci una moneta nella fontana...", "E oggi, | quando lanci una moneta | nella fontana...", 0),
]
HEAD = {
    1: [("2.000 ANNI", 160, "g"), ("e funziona ancora", 80, "w")],
    2: [("ACQUA VERGINE", 124, "g"), ("19 a.C.", 100, "w")],
    3: [("11 ACQUEDOTTI", 124, "w"), ("per una sola città", 76, "g")],
    4: [("ZERO POMPE", 140, "r"), ("solo gravità", 86, "w")],
    5: [("IL SEGRETO", 150, "g"), ("una pendenza minuscola", 64, "w")],
    6: [("SOTTO TERRA", 140, "w"), ("gli archi? solo nelle valli", 60, "g")],
    7: [("2.000 ANNI", 160, "g"), ("e funziona ancora", 80, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .4, .5), 4: (4, .5, .5), 5: (5, .4, .5),
             6: (6, .3, .5), 7: (1, .5, .5, 1.08, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
