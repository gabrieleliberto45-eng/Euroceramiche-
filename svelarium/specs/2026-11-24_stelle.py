LINES = [
    (1, "Sei letteralmente fatto di stelle.", "Sei letteralmente | fatto di STELLE.", 0),
    (2, "Appena dopo il Big Bang, l'universo conteneva quasi solo idrogeno ed elio.", "Appena dopo il Big Bang, | l'universo conteneva | quasi solo idrogeno ed elio.", 0),
    (3, "Ma il carbonio delle tue cellule, l'ossigeno che respiri, il calcio delle tue ossa: sono stati creati dentro le stelle.",
     "Ma il carbonio delle tue cellule, | l'ossigeno che respiri, | il calcio delle tue ossa: | sono stati creati dentro le stelle.", 0),
    (4, "Per miliardi di anni, le stelle hanno fuso atomi leggeri in atomi più pesanti, come enormi fornaci.",
     "Per miliardi di anni, | le stelle hanno fuso atomi leggeri | in atomi più pesanti, | come enormi fornaci.", 0),
    (5, "Quando una stella grande muore, esplode in una supernova, e sparge questi elementi nello spazio.",
     "Quando una stella grande muore, | esplode in una SUPERNOVA, | e sparge questi elementi | nello spazio.", 0),
    (6, "Da quella polvere sono nati nuovi pianeti. Compresa la Terra. E poi, la vita.",
     "Da quella polvere | sono nati nuovi pianeti. | Compresa la Terra. | E poi, la vita.", 0),
    (7, "Anche il ferro nel tuo sangue viene da stelle morte miliardi di anni fa.",
     "Anche il ferro nel tuo sangue | viene da stelle morte | miliardi di anni fa.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("FATTO DI STELLE", 116, "g"), ("letteralmente", 70, "w")],
    2: [("IL BIG BANG", 136, "c"), ("solo idrogeno ed elio", 64, "w")],
    3: [("CARBONIO · OSSIGENO", 88, "w"), ("creati nelle stelle", 66, "g")],
    4: [("FORNACI COSMICHE", 104, "g"), ("per miliardi di anni", 64, "w")],
    5: [("SUPERNOVA", 150, "r"), ("la stella esplode", 68, "w")],
    6: [("NASCE LA TERRA", 116, "c"), ("dalla polvere di stelle", 62, "w")],
    7: [("IL FERRO NEL SANGUE", 94, "r"), ("viene da stelle morte", 64, "w")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5), 6: (6, .5, .5),
             7: (3, .55, .45, 1.3, 1.55), 8: (1, .5, .5, 1.1, 1.0)}
SONG = "output008.mp3"
