
LINES = [
    (1, "Il cemento romano dura più del nostro.", "Il cemento romano | dura più del nostro.", 0),
    (1, "E solo da poco sappiamo perché.", "E solo da poco | sappiamo perché.", 0),
    (2, "La cupola del Pantheon è la più grande del mondo in calcestruzzo non armato.",
     "La cupola del Pantheon | è la più grande del mondo | in calcestruzzo non armato.", 0),
    (3, "Ed è in piedi da quasi duemila anni.", "Ed è in piedi | da quasi 2.000 anni.", 0),
    (4, "Il segreto? Piccoli grumi bianchi di calce, che per secoli abbiamo scambiato per errori.",
     "Il segreto? | Piccoli grumi bianchi di calce, | che per secoli | abbiamo scambiato per errori.", 0),
    (5, "Nel duemilaventitré, i ricercatori del MIT hanno scoperto che sono una riserva nascosta.",
     "Nel 2023, | i ricercatori del MIT | hanno scoperto | che sono una riserva nascosta.", 0),
    (6, "Quando si apre una crepa ed entra l'acqua, la calce si scioglie, e la richiude.",
     "Quando si apre una crepa | ed entra l'acqua, | la calce si scioglie | e la richiude.", 0),
    (7, "Il cemento romano si ripara da solo.", "Il cemento romano | SI RIPARA DA SOLO.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.",
     "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("IL CEMENTO ROMANO", 92, "w"), ("DURA PIÙ DEL NOSTRO", 92, "g")],
    2: [("PANTHEON", 150, "g"), ("la cupola più grande del mondo", 54, "w")],
    3: [("~2.000 ANNI", 140, "g"), ("e ancora in piedi", 64, "w")],
    4: [("IL SEGRETO?", 130, "w"), ("questi grumi bianchi", 64, "g")],
    5: [("MIT · 2023", 130, "c"), ("una riserva nascosta", 64, "w")],
    6: [("CREPA + ACQUA", 110, "c"), ("= la calce la richiude", 64, "w")],
    7: [("SI RIPARA", 140, "g"), ("DA SOLO", 140, "w")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {
    1: (1, 0.5, 0.5, 1.15, 1.0),
    2: (1, 0.35, 0.05, 1.35, 1.6),
    3: (1, 0.5, 0.95, 1.5, 1.3),
    4: (2, 0.5, 0.5, 1.0, 1.15),
    5: (2, 0.55, 0.55, 1.4, 1.75),
    6: (3, 0.5, 0.5, 1.0, 1.15),
    7: (3, 0.75, 0.45, 1.5, 1.9),
    8: (1, 0.5, 0.5, 1.0, 1.1),
}
