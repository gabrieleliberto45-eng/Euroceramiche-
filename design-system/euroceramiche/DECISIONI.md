# Decisioni sul sistema di design (rispetto a MASTER.md)

MASTER.md è l'output grezzo della skill UI/UX Pro Max. Sul sito sono state applicate queste scelte:

- **Stile**: Minimalism & Swiss Style — adottato.
- **Colori**: fondo caldo (#faf7f3) e accento oro adottati, ma come oro si usa quello delle
  stelle del logo Euroceramiche (#a87b2d, #85601f per il testo piccolo) e il nero (#111) resta
  il colore principale, come nel sito originale.
- **Tipografia**: Cinzel / Josefin Sans **non** adottati (troppo distanti dall'identità del
  marchio). Si usa Hanken Grotesk con titoli che alternano peso sottile e grassetto, come
  nell'originale.
- **Motion**: stagger standard 300–450 ms adottato in CSS (senza GSAP), con prefers-reduced-motion.
- **Regole UX applicate**: carosello con frecce, pausa e stop su hover/focus; testo dell'hero su
  pannello pieno (contrasto); etichette visibili e validazione all'uscita dal campo; target touch
  ≥ 44 px; header fisso con scroll-padding.
