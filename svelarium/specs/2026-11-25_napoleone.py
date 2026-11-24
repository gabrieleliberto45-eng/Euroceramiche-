# Immagini: Rijksmuseum (PD), Badisches Landesmuseum (CC0), Deutsche Fotothek (PD). Loop: "Ancora oggi..." -> "Napoleone era basso."
LINES = [
    (1, "Napoleone era basso. Lo sanno tutti. Ed è falso.", "Napoleone era basso. | Lo sanno tutti. | Ed è FALSO.", 0),
    (2, "Era alto circa un metro e sessantanove: nella media, anzi un po' sopra, per un francese del suo tempo.",
     "Era alto circa 1,69 m: | nella media, anzi un po' sopra, | per un francese del suo tempo.", 0),
    (3, "Il mito nasce da un errore di misura.", "Il mito nasce | da un errore di misura.", 0),
    (3, "Nei documenti era alto cinque piedi e due pollici: ma erano pollici francesi, più lunghi di quelli inglesi.",
     "Nei documenti: 5 piedi e 2 pollici. | Ma erano pollici FRANCESI, | più lunghi di quelli inglesi.", 0),
    (4, "Poi arrivò la propaganda: i vignettisti inglesi lo disegnavano piccolo e rabbioso.",
     "Poi arrivò la propaganda: | i vignettisti inglesi | lo disegnavano piccolo e rabbioso.", 0),
    (5, "I suoi soldati lo chiamavano il piccolo caporale, ma per affetto.", "I suoi soldati lo chiamavano | il piccolo caporale, | ma per affetto.", 0),
    (6, "E intorno a lui c'era sempre la Guardia Imperiale, scelta tra uomini molto alti.",
     "E intorno a lui c'era sempre | la Guardia Imperiale, | scelta tra uomini molto alti.", 0),
    (7, "Ancora oggi, quella propaganda funziona...", "Ancora oggi, | quella propaganda funziona...", 0),
]
HEAD = {
    1: [("NAPOLEONE", 150, "g"), ("ERA BASSO?", 130, "w")],
    2: [("1,69 METRI", 150, "g"), ("nella media", 72, "w")],
    3: [("IL TRUCCO", 150, "w"), ("dei pollici francesi", 64, "g")],
    4: [("PROPAGANDA", 140, "r"), ("inglese", 76, "w")],
    5: [("PICCOLO CAPORALE", 104, "g"), ("un soprannome affettuoso", 58, "w")],
    6: [("LA GUARDIA", 140, "w"), ("tutti altissimi", 72, "g")],
    7: [("NAPOLEONE", 150, "g"), ("ERA BASSO?", 130, "w")],
}
SCENE_IMG = {1: (1, .5, .0, 1.0, 1.06), 2: (2, .5, .35), 3: (3, .5, .3, 1.0, 1.1), 4: (4, .5, .15, 1.2, 1.35), 5: (5, .5, .4, 1.3, 1.5),
             6: (6, .5, .5), 7: (1, .5, .0, 1.06, 1.0)}
SONG = "output012.mp3"
TAIL = 0.25

HEAD_Y = {1: 1060, 7: 1060}  # titolo in basso: in alto c'è il volto
