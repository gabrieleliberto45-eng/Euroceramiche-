# Immagini: NASA/ESA/JPL (pubblico dominio; 'Oumuamua = illustrazione artistica NASA/ESO-M. Kornmesser via JPL PIA22357).
LINES = [
    (1, "Nel duemiladiciassette, qualcosa è arrivato da un'altra stella.", "Nel 2017, | qualcosa è arrivato | da un'altra STELLA.", 0),
    (2, "Gli astronomi lo chiamarono Oumuamua: in hawaiano, messaggero che arriva da lontano.",
     "Gli astronomi lo chiamarono 'Oumuamua: | in hawaiano, | messaggero che arriva da lontano.", 0),
    (3, "Era il primo oggetto interstellare mai osservato.", "Era il primo oggetto interstellare | mai osservato.", 0),
    (4, "Aveva una forma strana, forse molto allungata, e nessuna coda di gas.", "Aveva una forma strana, | forse molto allungata, | e nessuna coda di gas.", 0),
    (5, "Poi accelerò, allontanandosi dal Sole, come se qualcosa lo spingesse.", "Poi ACCELERÒ, | allontanandosi dal Sole, | come se qualcosa lo spingesse.", 0),
    (6, "Un astronomo di Harvard ipotizzò perfino una vela costruita da una civiltà aliena.",
     "Un astronomo di Harvard | ipotizzò perfino una vela | costruita da una civiltà ALIENA.", 0),
    (7, "Molti scienziati pensano invece a gas invisibili.", "Molti scienziati pensano invece | a gas invisibili.", 0),
    (7, "Ma nessuno lo sa con certezza.", "Ma nessuno lo sa | con certezza.", 0),
    (8, "E ormai è troppo lontano per scoprirlo...", "E ormai è troppo lontano | per scoprirlo...", 0),
]
HEAD = {
    1: [("DA UN'ALTRA", 130, "w"), ("STELLA", 160, "c")],
    2: [("'OUMUAMUA", 140, "g"), ("il messaggero", 72, "w")],
    3: [("IL PRIMO", 150, "w"), ("oggetto interstellare", 64, "g")],
    4: [("NESSUNA CODA", 120, "w"), ("forma strana", 70, "g")],
    5: [("HA ACCELERATO", 116, "r"), ("da solo", 76, "w")],
    6: [("UNA VELA", 150, "g"), ("ALIENA?", 140, "r")],
    7: [("NESSUNO", 150, "w"), ("lo sa con certezza", 66, "g")],
    8: [("DA UN'ALTRA", 130, "w"), ("STELLA", 160, "c")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.1), 2: (2, .1, .5, 1.0, 1.08), 3: (3, .5, .5), 4: (2, .1, .5, 1.25, 1.4), 5: (2, .25, .45, 1.0, 1.12),
             6: (5, .5, .5), 7: (6, .5, .5), 8: (1, .5, .5, 1.1, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
