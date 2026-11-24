# SPAZIO/NEWS. Voyager 1 a un giorno-luce (NASA, 17/11/2026). Immagini NASA (pubblico dominio).
LINES = [
    (1, "In questi giorni una sonda della NASA ha fatto una cosa mai successa prima.", "In questi giorni | una sonda della NASA | ha fatto una cosa | MAI SUCCESSA prima.", 0),
    (2, "Voyager uno è arrivata a un giorno luce dalla Terra.", "Voyager 1 è arrivata | a un GIORNO LUCE | dalla Terra.", 0),
    (2, "Significa che un messaggio, alla velocità della luce, impiega ventiquattro ore per raggiungerla.", "Significa che un messaggio, | alla velocità della luce, | impiega 24 ORE | per raggiungerla.", 0),
    (3, "Circa ventisei miliardi di chilometri.", "Circa 26 MILIARDI | di chilometri.", 0),
    (3, "Nessun oggetto costruito dall'uomo è mai andato così lontano.", "Nessun oggetto | costruito dall'uomo | è mai andato così lontano.", 0),
    (4, "Per festeggiare, a New York l'Empire State Building si è illuminato d'oro.", "Per festeggiare, | a New York l'Empire State Building | si è illuminato d'ORO.", 0),
    (5, "Oro, come il disco che Voyager porta a bordo dal millenovecentosettantasette.", "Oro, come il disco | che Voyager porta a bordo | dal 1977.", 0),
    (5, "Dentro ci sono saluti in cinquantacinque lingue, musica e i suoni della Terra.", "Dentro ci sono saluti | in 55 lingue, | musica | e i suoni della Terra.", 0),
    (6, "Un messaggio per chiunque, un giorno, dovesse trovarla.", "Un messaggio per chiunque, | un giorno, | dovesse TROVARLA.", 0),
    (7, "Nei prossimi anni le sue batterie si spegneranno.", "Nei prossimi anni | le sue batterie | si spegneranno.", 0),
    (8, "Ma lei continuerà a viaggiare in silenzio, per sempre...", "Ma lei continuerà | a viaggiare in silenzio, | per sempre...", 0),
]
HEAD = {
    1: [("MAI SUCCESSO", 140, "g"), ("prima d'ora", 80, "w")],
    2: [("1 GIORNO LUCE", 128, "g"), ("dalla Terra", 80, "w")],
    3: [("26 MILIARDI", 140, "g"), ("di chilometri", 80, "w")],
    4: [("ILLUMINATO", 130, "w"), ("D'ORO", 170, "g")],
    5: [("IL DISCO D'ORO", 120, "g"), ("dal 1977", 80, "w")],
    6: [("UN MESSAGGIO", 128, "w"), ("per gli ALIENI?", 90, "g")],
    7: [("BATTERIE", 140, "r"), ("quasi finite", 80, "w")],
    8: [("MAI SUCCESSO", 140, "g"), ("prima d'ora", 80, "w")],
}
SCENE_IMG = {1: (1, .5, .5, 1.0, 1.08), 2: (3, .5, .5), 3: (1, .85, .75, 1.3, 1.45), 4: (6, .5, .5), 5: (1, .3, .5, 1.2, 1.35),
             6: (5, .5, .5), 7: (3, .2, .8, 1.25, 1.4), 8: (1, .5, .5, 1.08, 1.0)}
SONG = "output008.mp3"
TAIL = 0.25
