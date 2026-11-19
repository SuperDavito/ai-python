# Sterrenjager

Een 3D arcade space shooter in één HTML-bestand, gebouwd met [three.js](https://threejs.org/) (r147, geladen via jsDelivr).

## Spelen

Open `index.html` in een browser met WebGL-ondersteuning (internetverbinding nodig voor three.js en de fonts). Werkt met toetsenbord, muis en touch.

| Actie    | Toetsenbord          | Muis / touch                   |
|----------|----------------------|--------------------------------|
| Bewegen  | pijltjes of WASD     | slepen                         |
| Schieten | spatie               | ingedrukt houden (automatisch) |
| Pauze    | P of Esc             | pauzeknop rechtsboven          |
| Geluid   | M                    | geluidsknop rechtsboven        |

## Gameplay

- Vier soorten tegenstanders: verkenners (rood), jagers (goud, schieten terug), tanks (paars, veel HP, schieten drie kogels tegelijk) en asteroïden.
- Elke 350 punten ga je naar de volgende sector en wordt de vijand sneller en sterker.
- Elke vierde sector verschijnt een moederschip met drie aanvalspatronen.
- Power-ups: **R** snelvuur, **S** spreidschot, **B** schild, **+** extra leven.
- De highscore wordt in je browser bewaard.

## Techniek

- Procedurele 3D-modellen (geen externe assets), PBR-materialen met een omgevingsmap van de nevel.
- Post-processing: HDR-bloom, ACES-tonemapping, vignet en chromatische aberratie bij treffers.
- Shader-achtergrond met nevel en een geringde gasreus, 2.600 bewegende sterren.
- Explosies met deeltjes, brokstukken, schokgolven en lichtflitsen; schermschud (uit bij "beperkte beweging").
- Synthetische geluidseffecten via de Web Audio API.
- Past de renderresolutie automatisch aan als de framerate te laag wordt.
