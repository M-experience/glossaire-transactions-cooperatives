#!/usr/bin/env python3
"""English versions of the four STC illustrations: French text is covered and replaced in place.
Usage: traduire_illustrations.py SRC_DIR OUT_DIR   (reads slideNN.webp, writes slideNN.webp)"""
import sys, os
from statistics import median
from PIL import Image, ImageDraw, ImageFont

F = {
 "serif": "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
 "serifb": "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
 "serifi": "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
 "sans": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
 "sansm": "/usr/share/fonts/opentype/inter/Inter-Medium.otf",
 "sansb": "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
}
BOLD = {"serif": "serifb", "serifi": "serifb", "sans": "sansb", "sansm": "sansb", "serifb": "serifb", "sansb": "sansb"}
INK = (29, 29, 29)

def fond(im, box, pad=3):
    """Dominant colour inside the box (text pixels are a minority)."""
    from collections import Counter
    x0, y0, x1, y1 = box; px = im.load(); c = Counter()
    for x in range(x0 + 2, x1 - 2, 2):
        for y in range(y0 + 2, y1 - 2, 2):
            r, g, b = px[x, y][:3]; c[(r // 6, g // 6, b // 6)] += 1
    k = c.most_common(1)[0][0]
    pts = [px[x, y][:3] for x in range(x0 + 2, x1 - 2, 2) for y in range(y0 + 2, y1 - 2, 2)
           if tuple(v // 6 for v in px[x, y][:3]) == k]
    return tuple(int(median(p[i] for p in pts)) for i in range(3))

def segments(ligne):
    out, b = [], False
    for i, part in enumerate(ligne.split("*")):
        if part: out.append((part, b))
        b = not b
    return out

def rendre_ligne(ligne, police, taille, couleur):
    segs = segments(ligne)
    fonts = [ImageFont.truetype(F[BOLD[police]] if b else F[police], taille) for _, b in segs]
    larg = sum(int(f.getlength(s)) + 1 for (s, _), f in zip(segs, fonts))
    asc, desc = fonts[0].getmetrics()
    calque = Image.new("RGBA", (max(1, larg), asc + desc), (0, 0, 0, 0)); d = ImageDraw.Draw(calque); x = 0
    for (s, _), f in zip(segs, fonts):
        d.text((x, 0), s, font=f, fill=couleur); x += f.getlength(s)
    return calque

PLUME = 2
def bloc(im, box, lignes, police="serif", taille=20, couleur=INK, align="c", lh=1.18, bg=None, valign="c", zone=None):
    from PIL import ImageFilter
    masque = Image.new("L", im.size, 0); dm = ImageDraw.Draw(masque); p = PLUME
    if zone:
        cx, cy, rx, ry, yh = zone
        dm.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255); dm.rectangle((0, 0, im.size[0], yh), fill=0)
    else:
        dm.rectangle((box[0] - p, box[1] - p, box[2] + p, box[3] + p), fill=255)
    if PLUME: masque = masque.filter(ImageFilter.GaussianBlur(PLUME))
    im.paste(Image.new("RGBA", im.size, (bg or fond(im, box)) + (255,)), (0, 0), masque)
    x0, y0, x1, y1 = box[0] + 4, box[1] + 2, box[2] - 4, box[3] - 2; w, h = x1 - x0, y1 - y0
    if isinstance(lignes, str): lignes = [lignes]
    s = min(taille, int(h / (len(lignes) * lh)) + 1)
    while True:
        cals = [rendre_ligne(l, police, s, couleur) for l in lignes]
        echelle = min(1, min(w / c.width for c in cals))
        if echelle >= 0.86 or s <= 9: break
        s -= 1
    cals = [c.resize((max(1, int(c.width * min(1, w / c.width))), c.height), Image.LANCZOS) for c in cals]
    pas = s * lh; total = pas * (len(cals) - 1) + cals[0].height
    y = y0 + ((h - total) / 2 if valign == "c" else 0)
    for c in cals:
        x = x0 + ((w - c.width) / 2 if align == "c" else 0)
        im.alpha_composite(c, (int(x), int(y))); y += pas

T = {}
# ---------------- slide12 : overview of the STC
T["slide12"] = [
 ((360, 4, 1240, 58), ["*The Semiotics of Cooperative Transactions (STC)*"], "serif", 44),
 ((233, 88, 402, 164), ["*Resource*", "*identity &*", "*competences*"], "serif", 23),
 ((540, 72, 1170, 108), ["*Subjectivation: transformation of the human milieu*"], "serif", 30),
 ((562, 112, 1198, 158), ["Health (physical balance), Culture (ability to learn from one’s experiences),", "Sociality (ability to develop a living community)"], "serif", 18),
 ((1348, 90, 1548, 166), ["*Transformed*", "*identity &*", "*competences*"], "serif", 23),
 ((480, 280, 1262, 315), ["*Transformation of lived experience within collective arrangements*"], "serif", 28),
 ((488, 316, 1258, 366), ["Transformation of selves or agents: perception/attention, knowledge/own body,", "relations/collective"], "serif", 19),
 ((30, 350, 226, 416), ["*Transactional*", "*context*"], "serif", 28, (90, 90, 90), "l"),
 ((32, 420, 226, 498), ["Institutional,", "cultural, technical,", "environmental…"], "serifi", 21, (90, 90, 90), "l"),
 ((106, 528, 282, 590), ["*Transactional*", "*situation*"], "serif", 26, (210, 40, 40), "l"),
 ((110, 591, 282, 664), ["Problem,", "need,", "opportunity…"], "serifi", 21, (210, 40, 40), "l"),
 ((640, 400, 1160, 437), ["*Course of the cooperative transaction*"], "serif", 29),
 ((585, 439, 1272, 462), ["Commitment  →  Competence  →  Performance (creation, subjectivation, territorialization)  →  Review"], "serif", 16),
 ((333, 452, 563, 512), ["*Project owner /*", "*beneficiary self*"], "serif", 26),
 ((845, 470, 1015, 502), ["*Creation:*"], "serif", 28),
 ((775, 502, 1085, 550), ["*value-bearing and enabling*", "*mediating artifacts*"], "serif", 21),
 ((1298, 452, 1548, 512), ["*Entrepreneur /*", "*performer self*"], "serif", 26),
 ((326, 637, 522, 706), ["Expresses a need, brings", "resources, evaluates,", "reuses, benefits."], "serif", 19, INK, "l"),
 ((735, 660, 1095, 706), ["Documents, objects, tools, spaces, gestures,", "inscriptions, digital environments…"], "serif", 19),
 ((1308, 637, 1545, 706), ["Carries an intention,", "mobilizes resources,", "acts, produces."], "serif", 19),
 ((595, 738, 1205, 773), ["*Transformations of artifacts in the environment*"], "serif", 30),
 ((585, 775, 1220, 821), ["Transformation of works or everyday goods (product or service):", "content/function, expression/techniques, rhetoric/uses"], "serif", 19),
 ((233, 856, 402, 928), ["*Resource*", "*heritage &*", "*capital*"], "serif", 23),
 ((462, 843, 1335, 881), ["*Territorialization: transformation of the technical milieu and ecosystems*"], "serif", 30),
 ((640, 882, 1130, 926), ["Material milieus (land, machines, networks…) and immaterial", "(linguistic, symbolic, legal, financial…)"], "serif", 18),
 ((1393, 856, 1548, 928), ["*Transformed*", "*heritage &*", "*capital*"], "serif", 23),
 ((14, 1004, 196, 1036), ["*STC according to M. Zacklad*"], "serif", 21, INK, "l"),
]
# ---------------- slide14 : three forms of conversation
def self_box(box, extra): return (box, ["*Self*"] + extra, "sansm", 20)
T["slide14"] = [
 ((26, 20, 422, 59), ["1. Ordinary conversation"], "sansm", 30, INK, "l"),
 ((28, 60, 422, 87), ["low transactional intensity"], "sans", 21, INK, "l"),
 ((28, 108, 348, 248), ["Situated exchanges that", "enable the coordination", "of everyday activities", "and the reproduction", "of existing practices."], "serif", 22, INK, "l"),
 ((683, 12, 1207, 71), ["*Environment / milieu*", "(relatively stable material and social context)"], "sansm", 21),
 ((798, 101, 1052, 175), ["*Mediating artifacts*", "(money, packaging, receipt,", "counter, basket, etc.)"], "sansm", 18),
 self_box((448, 230, 714, 294), ["(Project owner / Beneficiary)"]),
 ((793, 226, 1057, 294), ["*Work*", "(exchanged object: product, service)"], "sansm", 20),
 self_box((1163, 230, 1437, 294), ["(Entrepreneur / Performer)"]),
 ((26, 344, 412, 381), ["2. Ritual conversation"], "sansm", 30, INK, "l"),
 ((28, 382, 412, 409), ["moderate transactional intensity"], "sans", 21, INK, "l"),
 ((28, 430, 348, 598), ["More formalized exchanges,", "structured by rules, roles", "and shared dispositifs,", "which enable the", "maintenance and", "reinforcement of a", "common framework."], "serif", 22, INK, "l"),
 ((660, 336, 1207, 397), ["*Environment / milieu*", "(shared framework: rules, material dispositif, play space)"], "sansm", 21),
 ((773, 426, 1074, 505), ["*Mediating artifacts*", "(rules, board, cards, pawns,", "timer, etc.)"], "sansm", 18),
 self_box((423, 560, 697, 642), ["(Project owner / Beneficiary", "*- player*)"]),
 ((778, 572, 1072, 632), ["*Work*", "(game session, shared experience)"], "sansm", 20),
 self_box((1176, 566, 1457, 644), ["(Entrepreneur / Performer", "*- player*)"]),
 ((26, 690, 372, 726), ["3. Inventive conversation"], "sansm", 30, INK, "l"),
 ((28, 727, 372, 781), ["high transactional intensity", "reinvention"], "sans", 21, INK, "l"),
 ((28, 798, 348, 1018), ["Exchanges oriented toward", "transformation, in which", "agents, artifacts and milieu", "interact dynamically: they", "transform one another to", "produce new practices,", "new artifacts and a", "renewed milieu."], "serif", 22, INK, "l"),
 ((670, 681, 1247, 742), ["*Environment / milieu*", "(evolving context: resources, places, constraints, audiences, uses)"], "sansm", 21),
 ((803, 795, 1067, 874), ["*Mediating artifacts*", "(creation tools, sketches, mock-ups,", "software, images, data, etc.)"], "sansm", 18),
 self_box((403, 935, 697, 1014), ["(Project owner / Beneficiary", "*- initiator, user, audience*)"]),
 ((788, 933, 1059, 1010), ["*Work*", "(new object, image, prototype,", "solution, idea)"], "sansm", 19),
 self_box((1183, 935, 1462, 1014), ["(Entrepreneur / Performer", "*- designer, creator*)"]),
]
# ---------------- slide17 : transactional semioses
T["slide17"] = [
 ((503, 16, 1097, 69), ["*Performative semiosis*"], "serif", 40),
 ((528, 69, 1082, 121), ["*(creation, subjectivation,*", "*territorialization)*"], "serif", 26),
 ((828, 148, 1092, 282), ["Production of meaning,", "creation of new meanings,", "constitution of subjects", "and of territories", "of action."], "serif", 21, INK, "l"),
 ((92, 116, 403, 181), ["Inspired by the pragmatism", "of *Mead* (1934)"], "serif", 24),
 ((108, 184, 397, 214), ["Interactionist semiotics"], "serif", 20),
 ((1202, 116, 1513, 212), ["Inspired by the narrative", "semiotics of *Greimas*", "(Greimas & Courtés, 1993)"], "serif", 24),
 ((18, 313, 542, 422), ["*Praxeological semiosis*", "*(conversation, cooperation,*", "*coordination, organization)*"], "serif", 34),
 ((283, 448, 542, 587), ["Meaning arising from practices,", "interactions and collective", "activities: cooperation,", "coordination, organization", "of situations."], "serif", 20, INK, "l"),
 ((1058, 313, 1587, 424), ["*Narrative semiosis*", "*(commitment, competence,*", "*performance, review)*"], "serif", 34),
 ((1353, 453, 1582, 592), ["Emplotment of actions", "and experiences: roles,", "trials, competences,", "commitments and reviews."], "serif", 20, INK, "l"),
 ((684, 447, 916, 570), ["*Transactional*", "*semioses*", "(facets of the meaning", "of transactions)"], "serif", 27, INK, "c", (800, 487, 176, 106, 446)),
 ((899, 305, 1044, 392), ["Closely", "interdependent", "modes of", "interpretation"], "serif", 17, INK, "l"),
 ((503, 670, 1100, 757), ["*Cognitive semiosis*", "*(sensible, practical, conceptual)*"], "serif", 36),
 ((810, 783, 1097, 942), ["Construction of categories,", "organization of knowledge,", "production and interpretation", "of representations, relying", "on artifacts (especially", "symbolic ones)."], "serif", 20, INK, "l"),
 ((62, 773, 384, 874), ["Inspired by the pragmatism", "of *Peirce* (1931),", "enriched by *Morris*"], "serif", 25),
 ((118, 879, 332, 910), ["Triadic semiotics"], "serif", 20),
 ((1203, 646, 1580, 714), ["*Semiotics of information*", "*and data*"], "serif", 22),
 ((1333, 733, 1582, 842), ["Relies more particularly", "on *cognitive semiosis*:", "categorization and", "organization of knowledge."], "serif", 18, INK, "l"),
 ((1333, 863, 1584, 970), ["Situated and distributed", "cognition, largely", "embedded in artifacts,", "especially symbolic ones."], "serif", 18, INK, "l"),
 ((16, 1006, 640, 1048), ["*Transactional semioses according to M. Zacklad*"], "serif", 29, INK, "l"),
]
# ---------------- slide20 : the three dimensions
T["slide20"] = [
 ((360, 4, 1275, 51), ["*The three dimensions of cooperative transactions*"], "serif", 42),
 ((680, 50, 925, 80), ["(according to M. Zacklad)"], "serif", 24),
 ((30, 94, 370, 128), ["*Before: distinguished elements*"], "serif", 26),
 ((92, 139, 474, 173), ["*Individual or collective agents*"], "serif", 27),
 ((150, 173, 395, 203), ["(I / self / me, we)"], "serif", 22),
 ((338, 230, 523, 335), ["Persons, groups,", "organizations", "involved in", "transactions."], "serif", 20, INK, "l"),
 ((605, 139, 1000, 173), ["*Resource mediating artifacts*"], "serif", 27),
 ((630, 173, 975, 199), ["Artifacts available for action"], "serif", 21),
 ((866, 230, 1050, 332), ["Documents, tools,", "instruments, media,", "digital spaces,", "etc."], "serif", 20, INK, "l"),
 ((1140, 139, 1515, 173), ["*Environment artifacts*"], "serif", 27),
 ((1140, 173, 1515, 199), ["Physical, social and symbolic milieu"], "serif", 21),
 ((1423, 238, 1582, 342), ["Spaces, places,", "infrastructures,", "rules, documents,", "organizations, etc."], "serif", 19, INK, "l"),
 ((730, 448, 872, 487), ["*Creation*"], "serif", 31),
 ((1225, 448, 1480, 487), ["*Territorialization*"], "serif", 31),
 ((30, 512, 442, 546), ["*After: an integrated transaction*"], "serif", 26),
 ((718, 536, 882, 572), ["*Work*"], "serif", 29),
 ((655, 572, 945, 603), ["*(value-bearing artifact)*"], "serif", 23),
 ((42, 669, 282, 698), ["*(individual and collective)*"], "serif", 20),
 ((44, 708, 262, 787), ["Identities, competences,", "roles, commitment,", "collectives."], "serif", 20),
 ((1316, 623, 1536, 659), ["*Constituent milieu*"], "serif", 27),
 ((1282, 661, 1584, 792), ["Set of material and symbolic", "artifacts (places, instruments,", "documents, dispositifs,", "digital spaces,", "rules, etc.)."], "serif", 20),
 ((600, 848, 1000, 908), ["Documents, services, dispositifs, solutions,", "knowledge, etc."], "serif", 20),
 ((720, 960, 878, 1004), ["*Creation*"], "serif", 34),
 ((1198, 960, 1475, 1004), ["*Territorialization*"], "serif", 34),
]

def principal():
  global PLUME
  SRC, OUT = sys.argv[1], sys.argv[2]
  os.makedirs(OUT, exist_ok=True)
  for nom, blocs in T.items():
      PLUME = 7 if nom == "slide20" else 2
      im = Image.open(os.path.join(SRC, nom + ".webp")).convert("RGBA")
      for b in blocs:
          box, lignes, police, taille = b[:4]
          couleur = b[4] if len(b) > 4 else INK
          align = b[5] if len(b) > 5 else "c"
          bloc(im, box, lignes, police, taille, couleur, align, zone=b[6] if len(b) > 6 else None)
      im.convert("RGB").save(os.path.join(OUT, nom + ".webp"), quality=88)
      print(nom)

if __name__ == "__main__":
    principal()
