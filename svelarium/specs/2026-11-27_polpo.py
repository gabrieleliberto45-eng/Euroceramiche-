# SCIENZA. Immagini: ricostruzioni generate con IA.
LINES = [
    (1, "Questo animale ha tre cuori.", "Questo animale | ha TRE CUORI.", 0),
    (1, "E il sangue blu.", "E il sangue BLU.", 0),
    (2, "È il polpo.", "È il POLPO.", 0),
    (3, "Due cuori pompano il sangue verso le branchie, il terzo verso il resto del corpo.", "Due cuori | pompano il sangue | verso le branchie, | il terzo | verso il resto del corpo.", 0),
    (4, "E quando nuota, il terzo cuore si ferma.", "E quando nuota, | il terzo cuore | SI FERMA.", 0),
    (5, "Per questo preferisce camminare sul fondo: nuotare lo stanca.", "Per questo | preferisce camminare | sul fondo: | nuotare lo stanca.", 0),
    (6, "Il sangue è blu perché trasporta l'ossigeno con il rame, non con il ferro.", "Il sangue è blu | perché trasporta l'ossigeno | con il RAME, | non con il ferro.", 0),
    (7, "Ma la cosa più strana sono i tentacoli.", "Ma la cosa più strana | sono i TENTACOLI.", 0),
    (8, "Due terzi dei suoi neuroni si trovano nelle braccia.", "Due terzi | dei suoi neuroni | si trovano | nelle BRACCIA.", 0),
    (9, "Ogni braccio può toccare e assaggiare quello che afferra.", "Ogni braccio | può toccare | e ASSAGGIARE | quello che afferra.", 0),
    (10, "Come se avesse nove cervelli che pensano insieme...", "Come se avesse | NOVE CERVELLI | che pensano insieme...", 0),
]
HEAD = {
    1: [("TRE CUORI", 150, "w"), ("e sangue BLU", 100, "c")],
    2: [("IL POLPO", 160, "g")],
    3: [("2 + 1", 190, "w"), ("cuori", 110, "r")],
    4: [("SI FERMA", 160, "r"), ("quando nuota", 90, "w")],
    5: [("CAMMINA", 160, "w"), ("nuotare lo stanca", 80, "g")],
    6: [("RAME", 190, "c"), ("non ferro", 100, "w")],
    7: [("I TENTACOLI", 130, "w")],
    8: [("2/3", 190, "g"), ("dei neuroni nelle braccia", 64, "w")],
    9: [("TOCCA E ASSAGGIA", 110, "w")],
    10: [("9 CERVELLI", 150, "g"), ("che pensano insieme", 76, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (2, .5, .5), 3: (1, .4, .5, 1.3, 1.15), 4: (3, .5, .5), 5: (4, .5, .5),
             6: (5, .5, .5), 7: (6, .5, .5), 8: (7, .5, .5), 9: (8, .5, .5), 10: (1, .5, .5, 1.15, 1.0)}
SONG = "output005.mp3"
TAIL = 0.25
