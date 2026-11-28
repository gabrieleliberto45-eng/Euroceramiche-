# MISTERO (ANIMATO). Immagini e clip: ricostruzioni generate con IA.
LINES = [
    (1, "Nel dicembre del millenovecento, un faro in Scozia smette di accendersi.", "Nel dicembre del 1900, | un faro in Scozia | smette di ACCENDERSI.", 0),
    (2, "Sulla piccola isola vivono tre guardiani.", "Sulla piccola isola | vivono TRE GUARDIANI.", 0),
    (3, "Quando arriva la nave dei rifornimenti, undici giorni dopo, nessuno va ad accoglierla.", "Quando arriva | la nave dei rifornimenti, | 11 giorni dopo, | NESSUNO va ad accoglierla.", 0),
    (4, "Il cancello è chiuso.", "Il cancello | è chiuso.", 0),
    (4, "La lampada è pulita e pronta.", "La lampada | è pulita e pronta.", 0),
    (5, "Ma i guardiani sono spariti.", "Ma i guardiani | sono SPARITI.", 0),
    (6, "Appesa all'ingresso c'è ancora una cerata: uno di loro è uscito senza giacca, in pieno inverno.", "Appesa all'ingresso | c'è ancora una cerata: | uno di loro è uscito | SENZA GIACCA, | in pieno inverno.", 0),
    (7, "Sul lato ovest, la tempesta aveva divelto ringhiere e spostato massi enormi.", "Sul lato ovest, | la TEMPESTA | aveva divelto ringhiere | e spostato massi enormi.", 0),
    (8, "Secondo l'ipotesi più probabile, un'onda gigantesca li trascinò in mare.", "Secondo l'ipotesi | più probabile, | un'ONDA GIGANTESCA | li trascinò in mare.", 0),
    (9, "Ma i loro corpi non furono mai ritrovati...", "Ma i loro corpi | non furono | MAI RITROVATI...", 0),
]
HEAD = {
    1: [("IL FARO", 180, "w"), ("dei 3 scomparsi", 96, "r")],
    2: [("3 GUARDIANI", 140, "w"), ("isole Flannan", 90, "g")],
    3: [("NESSUNO", 170, "r"), ("11 giorni dopo", 90, "w")],
    4: [("TUTTO IN ORDINE", 110, "w"), ("la lampada pronta", 80, "g")],
    5: [("SPARITI", 180, "r")],
    6: [("SENZA GIACCA", 130, "w"), ("in pieno inverno", 86, "c")],
    7: [("LA TEMPESTA", 130, "w"), ("massi spostati", 90, "g")],
    8: [("UN'ONDA", 170, "c"), ("gigantesca?", 100, "w")],
    9: [("IL FARO", 180, "w"), ("dei 3 scomparsi", 96, "r")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (7, .5, .5, 1.0, 1.1), 8: (7, .5, .5), 9: (1, .5, .5, 1.08, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
