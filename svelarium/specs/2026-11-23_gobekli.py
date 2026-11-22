
LINES = [
    (1, "Questo tempio ha quasi dodicimila anni.", "Questo tempio | ha quasi 12.000 anni.", 0),
    (1, "È più antico di Stonehenge di oltre seimila anni. E delle piramidi di settemila.", "È più antico di Stonehenge | di oltre 6.000 anni. | E delle piramidi di 7.000.", 0),
    (2, "Si chiama Göbekli Tepe, in Turchia.", "Si chiama GÖBEKLI TEPE, | in Turchia.", 0),
    (3, "Pilastri di pietra alti più di cinque metri, pesanti tonnellate, scolpiti con volpi, cinghiali, serpenti e avvoltoi.",
     "Pilastri di pietra | alti più di 5 metri, | pesanti tonnellate, | scolpiti con volpi, cinghiali, | serpenti e avvoltoi.", 0),
    (4, "Il mistero? Chi l'ha costruito non conosceva l'agricoltura. Né la scrittura. Né la ruota.",
     "Il mistero? | Chi l'ha costruito | non conosceva l'agricoltura. | Né la scrittura. | Né la ruota.", 0),
    (4, "Erano cacciatori-raccoglitori dell'età della pietra.", "Erano cacciatori-raccoglitori | dell'età della pietra.", 0),
    (5, "Abbiamo sempre pensato che prima nascessero i villaggi, e poi i templi.", "Abbiamo sempre pensato | che prima nascessero i villaggi, | e poi i templi.", 0),
    (5, "Göbekli Tepe potrebbe dirci il contrario.", "Göbekli Tepe | potrebbe dirci il contrario.", 0),
    (6, "E gran parte del sito è ancora sotto terra.", "E gran parte del sito | è ancora sotto terra.", 0),
    (7, "Tu cosa pensi che ci sia sepolto? Scrivilo nei commenti.", "Tu cosa pensi che ci sia sepolto? | Scrivilo nei commenti.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("12.000 ANNI", 150, "g"), ("più antico delle piramidi", 62, "w")],
    2: [("GÖBEKLI TEPE", 124, "g"), ("Turchia", 70, "w")],
    3: [("SCOLPITI", 130, "w"), ("volpi · cinghiali · serpenti", 56, "g")],
    4: [("IL MISTERO?", 130, "w"), ("niente agricoltura né scrittura", 54, "g")],
    5: [("PRIMA IL TEMPIO,", 96, "g"), ("POI IL VILLAGGIO?", 96, "w")],
    6: [("ANCORA", 130, "w"), ("SOTTO TERRA", 130, "g")],
    7: [("TU COSA", 130, "w"), ("NE PENSI?", 130, "g")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (6, .5, .5), 7: (2, .5, .7, 1.3, 1.1), 8: (1, .5, .5, 1.0, 1.1)}
SONG = "output008.mp3"
