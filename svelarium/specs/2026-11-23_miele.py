LINES = [
    (1, "Esiste un cibo che non scade praticamente mai.", "Esiste un cibo | che non scade | praticamente MAI.", 0),
    (2, "Negli scavi delle tombe egizie, gli archeologi hanno trovato vasi di miele vecchi di migliaia di anni.",
     "Negli scavi delle tombe egizie, | gli archeologi hanno trovato | vasi di miele | vecchi di migliaia di anni.", 0),
    (2, "E, a quanto raccontano, era ancora commestibile.", "E, a quanto raccontano, | era ancora commestibile.", 0),
    (3, "Il segreto è la chimica.", "Il segreto è la chimica.", 0),
    (3, "Il miele contiene pochissima acqua e tantissimo zucchero: i batteri, lì dentro, si disidratano e muoiono.",
     "Il miele contiene pochissima acqua | e tantissimo zucchero: | i batteri, lì dentro, | si disidratano e muoiono.", 0),
    (4, "Inoltre è acido, più o meno come il succo d'arancia.", "Inoltre è acido, | più o meno come il succo d'arancia.", 0),
    (5, "Poi le api ci aggiungono un enzima che produce piccole quantità di acqua ossigenata.",
     "Poi le api ci aggiungono un enzima | che produce piccole quantità | di ACQUA OSSIGENATA.", 0),
    (6, "Se lo conservi chiuso bene, lontano dall'umidità, dura praticamente per sempre.",
     "Se lo conservi chiuso bene, | lontano dall'umidità, | dura praticamente per sempre.", 0),
    (7, "Se si cristallizza, non è andato a male: basta scaldarlo a bagnomaria.",
     "Se si cristallizza, | non è andato a male: | basta scaldarlo a bagnomaria.", 0),
    (8, "Seguimi su Svelarium: ogni giorno, un segreto svelato.", "Seguimi su SVELARIUM: | ogni giorno, | un segreto svelato.", 0),
]
HEAD = {
    1: [("NON SCADE MAI", 124, "g"), ("esiste davvero", 70, "w")],
    2: [("TOMBE EGIZIE", 130, "g"), ("miele vecchio di millenni", 60, "w")],
    3: [("IL SEGRETO?", 136, "w"), ("pochissima acqua", 70, "g")],
    4: [("ACIDO", 170, "g"), ("come il succo d'arancia", 62, "w")],
    5: [("ACQUA OSSIGENATA", 100, "c"), ("prodotta grazie alle api", 60, "w")],
    6: [("PER SEMPRE", 140, "g"), ("se è chiuso bene", 70, "w")],
    7: [("CRISTALLIZZATO?", 110, "w"), ("non è andato a male", 66, "g")],
    8: [("SVELARIUM", 150, "g"), ("ogni giorno un segreto svelato", 52, "w")],
}
SCENE_IMG = {1: (1, .5, .5), 2: (2, .5, .5), 3: (3, .5, .5), 4: (4, .5, .5), 5: (5, .5, .5),
             6: (2, .5, .7, 1.35, 1.6), 7: (6, .5, .5), 8: (1, .5, .5, 1.12, 1.0)}
SONG = "output005.mp3"
