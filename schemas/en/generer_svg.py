#!/usr/bin/env python3
"""English SVG versions of the STC schemas (international reference)."""
import os, sys
from xml.sax.saxutils import escape as _E
def E(s): return _E(T(s))

OUT = sys.argv[1]
LANG = sys.argv[2] if len(sys.argv) > 2 else "en"
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traductions_schemas import TR
_TR = TR.get(LANG, {})
def T(s): return _TR.get(s, s)
FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK = "#1f2430"; GREY = "#55606e"; LINE = "#8a8f98"

def svg(w, h, body, bg="#ffffff"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker>'
            f'<marker id="ad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')

def rect(x, y, w, h, fill="#fff", stroke=LINE, rx=10, sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def text(x, y, lines, size=15, weight=400, fill=INK, anchor="middle", lh=1.3, style=""):
    """lines: list of str or list of (str, bold) segments."""
    out = []
    for i, ln in enumerate(lines):
        yy = y + i * size * lh
        if isinstance(ln, str):
            ln = [(ln, weight >= 600)]
        spans = "".join(f'<tspan font-weight="{700 if b else weight if weight<600 else 400}">{E(s)}</tspan>' for s, b in ln)
        out.append(f'<text xml:space="preserve" x="{x}" y="{yy:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{style}>{spans}</text>')
    return "".join(out)

def ctext(cx, cy, lines, size=15, weight=400, fill=INK, lh=1.3, style=""):
    n = len(lines); y0 = cy - (n - 1) * size * lh / 2 + size * 0.35
    return text(cx, y0, lines, size, weight, fill, "middle", lh, style)

def line(pts, marker="a", end=True, start=False, color=LINE, sw=2, dash=None):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    m = (f' marker-end="url(#{marker})"' if end else "") + (f' marker-start="url(#{marker})"' if start else "")
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{m}{da}/>'

def hexa(cx, cy, w, h, fill, stroke=INK):
    k = h / 2
    pts = [(cx - w/2, cy), (cx - w/2 + k, cy - h/2), (cx + w/2 - k, cy - h/2), (cx + w/2, cy), (cx + w/2 - k, cy + h/2), (cx - w/2 + k, cy + h/2)]
    return f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'

S = {}

# ---- slide04 : levels of meaning
b = text(40, 46, ["The same gesture takes on its meaning in the conversational situation"], 22, 700, anchor="start")
b += rect(40, 90, 460, 370, "#fff", "#c9c7bd", 12, 2)
b += text(68, 132, ["Level 1 - Elementary gestures"], 19, 700, anchor="start")
b += rect(68, 160, 404, 110, "#fff", "#c9c7bd", 12, 2)
b += text(96, 204, ["Material gestures"], 19, 700, anchor="start") + text(96, 238, ["transforming objects and milieu"], 16, fill=GREY, anchor="start")
b += rect(68, 318, 404, 110, "#fff", "#c9c7bd", 12, 2)
b += text(96, 362, ["Semiosic gestures"], 19, 700, anchor="start") + text(96, 396, ["producing codified forms"], 16, fill=GREY, anchor="start")
b += text(570, 262, ["interpretation"], 15, fill=GREY) + line([(504, 275), (636, 275)])
b += rect(640, 90, 660, 370, "#e5eef9", "#2f7bd6", 12, 2.5)
b += text(668, 132, ["Level 2 - Conversational meaning"], 19, 700, anchor="start")
b += text(668, 176, ["Meaning interpreted according to:"], 18, anchor="start")
b += text(668, 220, ["• the context: the preceding gestures", "• the four facets of meaning:"], 16, anchor="start", lh=2.6)
b += text(696, 296, ["praxeological · narrative", "cognitive · performative"], 16, anchor="start", lh=1.9)
b += text(668, 408, ["This is the level of communication"], 19, 700, anchor="start")
b += text(40, 520, ["Example: handing over a tool can offer help, request an intervention or pass on a responsibility.",
                    "Example: “yes” can accept, confirm, acquiesce, be ironic or give in."], 16, anchor="start", lh=2.3)
S["slide04"] = svg(1340, 580, b)

# ---- slide05 : transactional semioses
def facet(x, y, w, h, fill, name, items):
    return rect(x, y, w, h, fill, INK, 0, 1.2) + ctext(x + w/2, y + h/2, items(name), 20, lh=1.4)
b = rect(578, 314, 342, 202, "#ee6e68", INK, 0, 1.2)
b += ctext(749, 415, [[("Transactional", True)], [("semioses", True)], "(facets of the meaning", "of transactions)"], 20, lh=1.35)
b += rect(543, 16, 410, 162, "#dddafa", INK, 0, 1.2) + ctext(748, 97, [[("Performative ", False), ("(creation,", True)], [("subjectivation,", True)], [("territorialization)", True)]], 20, lh=1.4)
b += rect(30, 320, 404, 190, "#efecb6", INK, 0, 1.2) + ctext(232, 415, ["Praxeological", [("(", False), ("conversation", True), (", ", False), ("cooperation,", True)], [("coordination, organization", True), (")", False)]], 20, lh=1.4)
b += rect(1110, 324, 374, 178, "#b9edca", INK, 0, 1.2) + ctext(1297, 413, [[("Narrative (", False), ("commitment,", True)], [("competence, performance,", True)], [("review", True), (")", False)]], 20, lh=1.4)
b += rect(543, 651, 410, 127, "#f5c6c6", INK, 0, 1.2) + ctext(748, 714, [[("Cognitive ", False), ("(sensible, practical,", True)], [("conceptual)", True)]], 20, lh=1.4)
b += line([(749, 314), (749, 180)], "ad", color=INK, sw=1.5) + line([(578, 414), (436, 414)], "ad", color=INK, sw=1.5)
b += line([(920, 414), (1108, 413)], "ad", color=INK, sw=1.5) + line([(749, 516), (749, 649)], "ad", color=INK, sw=1.5)
b += ctext(328, 211, ["Mead’s interactionist", "semiotics"], 17)
b += ctext(1238, 211, ["Greimas’s narrative", "semiotics "], 17)
b += ctext(1176, 681, ["Peirce’s triadic semiotics", "enriched by Morris"], 17)
S["slide05"] = svg(1500, 800, b)

# ---- slide08 : gesture and substrate
b = rect(10, 8, 1580, 562, "#fff", "none", 18, 0)
b += text(62, 78, ["The gesture is always ephemeral; the artifact lasts according to the nature of its substrate"], 27, 700, anchor="start")
b += rect(64, 116, 584, 160, "#e8f0fa", "#2f6fbf", 14, 3)
b += text(94, 168, ["The gesture"], 28, 700, anchor="start") + text(94, 212, ["Always ephemeral, it gives form to a", "substrate, here and now."], 22, anchor="start", lh=1.5)
b += text(798, 166, ["gives form or takes up"], 19, fill=GREY) + text(798, 202, ["⇄"], 30, fill=GREY) + text(798, 245, ["is perceived and appropriated"], 19, fill=GREY)
b += rect(950, 116, 584, 160, "#fdf1ec", "#e06a3f", 14, 3)
b += text(980, 168, ["The mediating artifact"], 28, 700, anchor="start") + text(980, 212, ["The substrate formed by the gesture: ephemeral", "or persistent according to its nature."], 22, anchor="start", lh=1.5)
b += rect(64, 308, 722, 222, "#f5f7fb", "none", 10, 0) + '<rect x="64" y="308" width="7" height="222" rx="3" fill="#2f6fbf"/>'
b += text(98, 356, ["Ephemeral substrate"], 26, 700, anchor="start")
b += text(98, 398, ["Air for the voice, the body for facial expression."], 22, fill=GREY, anchor="start")
b += text(98, 440, ["The artifact lasts only as long as the gesture and", "merges with it in experience."], 22, anchor="start", lh=1.45)
b += rect(814, 308, 722, 222, "#fdf7f3", "none", 10, 0) + '<rect x="814" y="308" width="7" height="222" rx="3" fill="#e06a3f"/>'
b += text(848, 356, ["Persistent substrate"], 26, 700, anchor="start")
b += text(848, 398, ["Paper or the digital file, but also the cake or the", "meal."], 22, fill=GREY, anchor="start", lh=1.45)
b += text(848, 472, ["The artifact keeps its form beyond the instant: it can", "circulate and be taken up again."], 22, anchor="start", lh=1.45)
S["slide08"] = svg(1600, 578, b, "#efece3")

# ---- slide09 : four gradients
BLUE = "#2e5f92"; RED = "#c8102e"
def card(x, y, title, poles, col, desc):
    return (rect(x, y, 776, 212, "#fff", "#e6e2d8", 14, 1.5) + text(x + 34, y + 54, [title], 29, 700, anchor="start")
            + text(x + 34, y + 102, [poles], 24, 700, fill=col, anchor="start") + text(x + 34, y + 146, desc, 23, anchor="start", lh=1.5))
b = card(10, 14, "Finality", "enabling ↔ value-bearing", BLUE, ["The work is the value-bearing artifact."])
b += card(812, 14, "Symbolicity", "profane ↔ symbolic", BLUE, ["From the profane, in Durkheim’s sense, to what", "ritual reactualizes."])
b += card(10, 250, "Persistence", "ephemeral ↔ persistent", RED, ["Depends on the substrate: the voice vanishes with", "the gesture, the document or the cake outlive it."])
b += card(812, 250, "Materiality", "material ↔ semiosic", RED, ["Acts through force, or through the interpretation", "of a sign."])
b += text(10, 524, [[("In blue", True), (", value dynamics. ", False), ("In red", True), (", the artifact’s mode of existence, directly linked to gestures.", False)]], 24, anchor="start")
b = b.replace('<tspan font-weight="700">In blue</tspan>', f'<tspan font-weight="700" fill="{BLUE}">In blue</tspan>').replace('<tspan font-weight="700">In red</tspan>', f'<tspan font-weight="700" fill="{RED}">In red</tspan>')
S["slide09"] = svg(1600, 545, b, "#faf8f3")

# ---- slide19 : creation, subjectivation, territorialization
b = ""
cols = [(170, "ARTIFACT", "#a9cdf1", ["Mediating", "artifacts", "(resources)"], "Creation", "#4f97e8", ["Work (value-", "bearing", "artifact)"]),
        (542, "SELF", "#efcfcf", ["Living actants", "(individual or", "collective)"], "Subjectivation", "#dc9b98", ["Self (individual", "or collective)"]),
        (946, "ENVIRONMENT", "#d4eab9", ["Environment (and", "instrumental", "mediating artifacts)"], "Territorialization", "#9ccf62", ["Appropriated", "milieu"])]
for cx, head, c1, t1, verb, c2, t2 in cols:
    b += text(cx, 46, [head], 34)
    b += rect(cx - 133, 86, 266, 156, c1, INK, 26, 1.5) + ctext(cx, 164, t1, 23)
    b += line([(cx, 246), (cx, 296)], end=False, color=INK, sw=5, dash="1 11").replace('stroke-width="5"', 'stroke-width="5" stroke-linecap="round"')
    vw = len(T(verb)) * 17 + 20
    b += f'<rect x="{cx - vw/2}" y="300" width="{vw}" height="58" fill="#fff"/>' + ctext(cx, 329, [verb], 32, 700)
    b += line([(cx, 368), (cx, 410)], end=False, color=INK, sw=5, dash="1 11").replace('stroke-width="5"', 'stroke-width="5" stroke-linecap="round"')
    b += f'<polygon points="{cx-16},{412} {cx+16},{412} {cx},{456}" fill="{INK}"/>'
    b += rect(cx - 133, 460, 266, 150, c2, INK, 26, 1.5) + ctext(cx, 535, t2, 23, 700)
S["slide19"] = svg(1140, 640, b, "#f2f2f2")

# ---- slide23 : cognitive semiosis
b = rect(445, 79, 385, 84, "#e8e8e8", INK, 16, 1.2) + ctext(637, 121, ["Cognitive semiosis"], 21, 700)
b += line([(637, 163), (637, 220)], end=False, color="#333", sw=1.5)
b += line([(222, 222), (1061, 222)], end=False, color="#333", sw=1.5)
br = [(222, "#eddcdc", "Sensible semiosis", "or reason", "#eddcdc", ["Situated sense", "(or qualitative)"], "Signal / Singular"),
      (637, "#d3e8bd", "Practical semiosis", "or reason", "#d5e75d", ["Typified meaning", "(or referential)"], "Type / Genre"),
      (1061, "#f6d898", "Conceptual semiosis", "or reason", "#f1c644", ["Theoretical meaning", "(or hypothetical)"], "Concept / Category")]
for cx, c1, l1, l2, c2, t2, t3 in br:
    b += line([(cx, 222), (cx, 278)], "ad", color="#333", sw=1.5)
    b += rect(cx - 160, 280, 320, 148, c1, INK, 26, 1.2) + ctext(cx, 354, [l1, l2], 21)
    b += line([(cx, 428), (cx, 490)], "ad", color="#333", sw=1.5)
    b += rect(cx - 180, 492, 360, 96, c2, INK, 16, 1.2) + ctext(cx, 540, t2, 20, 700)
    b += line([(cx, 588), (cx, 648)], "ad", color="#333", sw=1.2, dash="5 4")
    b += f'<rect x="{cx-152}" y="651" width="304" height="104" fill="#f2ef7c" stroke="#e2e0c0"/>' + ctext(cx, 703, [t3], 27, 700)
S["slide23"] = svg(1300, 830, b)

# ---- slide30 : narrative trajectory
b = hexa(138, 52, 226, 54, "#df3473", "#c02060") + ctext(138, 52, ["Problematic", "situation"], 15)
def node(x, y, w, h, fill, lab, dash=None):
    return rect(x, y, w, h, fill, INK, 9, 1, dash) + ctext(x + w/2, y + h/2, [lab], 15)
b += node(318, 25, 142, 52, "#a9cdf1", "Commitment") + node(556, 25, 142, 52, "#6aa8e6", "Competence")
b += node(556, 190, 142, 52, "#f1c644", "Performance") + node(318, 190, 142, 52, "#d1eab9", "Review")
b += node(230, 291, 142, 52, "#d1eab9", "Evaluation", "5 3") + node(400, 291, 142, 52, "#d1eab9", "Retribution", "5 3")
b += line([(252, 51), (314, 51)], sw=2.2) + line([(460, 51), (552, 51)], sw=2.2) + line([(627, 77), (627, 186)], sw=2.2)
b += line([(556, 216), (464, 216)], sw=2.2) + line([(389, 190), (389, 81)], sw=2.2, dash="7 5")
b += line([(389, 242), (303, 289)], sw=2.2) + line([(389, 242), (470, 289)], sw=2.2)
S["slide30"] = svg(740, 370, b)

# ---- slide31 : reception belongs to performance
b = text(40, 56, ["Reception belongs to performance, on the beneficiary’s side"], 23, 700, anchor="start")
b += rect(40, 92, 688, 50, "#ececea", "#c9c7bd", 12, 1.5) + ctext(384, 117, ["Vision, commitment, realization"], 18)
b += rect(742, 92, 560, 50, "#ececea", "#c9c7bd", 12, 1.5) + ctext(1022, 117, ["Reception, evaluation, retribution"], 18)
b += rect(42, 178, 212, 246, "#fff", "#c9c7bd", 12, 2) + ctext(148, 300, ["Commitment"], 20, 700)
b += rect(283, 178, 212, 246, "#fff", "#c9c7bd", 12, 2) + ctext(389, 300, ["Competence"], 20, 700)
b += rect(523, 178, 424, 246, "#fff", "#c9c7bd", 12, 2) + text(735, 214, ["Performance"], 20, 700)
for x, a, r in [(537, "Realization", "(performer)"), (742, "Reception", "(beneficiary)")]:
    b += rect(x, 233, 192, 170, "#e5eef9", "#2f7bd6", 12, 2.5) + text(x + 96, 276, [a], 20, 700) + text(x + 96, 318, ["consummatory", r], 18, lh=1.75)
b += rect(976, 178, 326, 246, "#fff", "#c9c7bd", 12, 2) + text(1139, 214, ["Review"], 20, 700)
b += rect(990, 230, 298, 82, "#fff", "#c9c7bd", 12, 2) + ctext(1139, 271, ["Evaluation"], 20, 700)
b += rect(990, 325, 298, 82, "#fff", "#c9c7bd", 12, 2) + ctext(1139, 366, ["Retribution"], 20, 700)
for x1, x2 in [(256, 280), (497, 520), (949, 973)]:
    b += line([(x1, 300), (x2, 300)], color="#c9c7bd")
b += text(185, 480, ["Emphasis: the consummatory, experienced by the performer in accomplishment", "and by the beneficiary in reception, as use and appropriation."], 18, anchor="start", lh=1.75)
b += line([(1139, 424), (1139, 558), (148, 558), (148, 428)], color="#c9c7bd")
b += text(644, 594, ["evaluation can launch a new trajectory"], 18, fill=GREY)
S["slide31"] = svg(1340, 620, b)

# ---- slide32 : actantial roles
b = f'<ellipse cx="397" cy="49" rx="113" ry="34" fill="#df3473"/>' + ctext(397, 49, ["Problematic", "situation"], 14)
for cx, cy, lab in [(133, 160, "Project owner"), (667, 162, "Entrepreneur"), (133, 447, "Beneficiary"), (669, 455, "Performer")]:
    b += hexa(cx, cy, 220, 76, "#e6e6e6", "#999") + ctext(cx, cy, [lab], 15, 700)
for x, y, w, h, fill, lab in [(319, 129, 168, 60, "#d5e75d", "Commitment"), (605, 262, 130, 80, "#6aa8e6", "Competence"),
                              (62, 274, 141, 76, "#f1c644", "Review"), (313, 415, 167, 64, "#e05638", "Performance")]:
    b += rect(x, y, w, h, fill, INK, 10, 1) + ctext(x + w/2, y + h/2, [lab], 15, 700)
b += line([(243, 159), (315, 159)], sw=1, color="#333") + line([(563, 162), (491, 159)], sw=1, color="#333")
b += line([(133, 198), (133, 270)], sw=1, color="#333") + line([(669, 200), (669, 258)], sw=1, color="#333")
b += line([(133, 409), (133, 354)], sw=1, color="#333") + line([(669, 417), (669, 346)], sw=1, color="#333")
b += line([(243, 447), (309, 447)], sw=1, color="#333") + line([(559, 446), (484, 446)], sw=1, color="#333")
S["slide32"] = svg(800, 500, b)

# ---- slide33 : mediating artifacts in the trajectory
ROLE = "#efcfcf"; LAB = "#fbf36b"; PUR = "#3b3fa3"
b = ""
for x, y, lines_ in [(182, 76, [[("Project owner", True)], "(demand)"]), (835, 76, [[("Entrepreneur", True)], "(offer)"]),
                     (182, 416, [[("Beneficiary", True)], "(receiving, having", "the experience,", "consuming)"]),
                     (835, 416, [[("Performer", True)], "(giving, doing,", "exchanging)"])]:
    b += rect(x, y, 205, 120 if y < 200 else 132, ROLE, "#555", 0, 1.2) + ctext(x + 102, y + (60 if y < 200 else 66), lines_, 18, lh=1.6)
for x, y, fill, l2 in [(487, 76, "#6aa8e6", "virtualizing"), (835 - 0, 246, "#b4d394", "enabling"), (182, 246, "#f7d796", "evaluative"), (487, 416, "#df856e", "value-bearing")]:
    b += rect(x, y, 230 if x == 487 else 205, 120, fill, INK, 24, 1.2) + ctext(x + (115 if x == 487 else 102), y + 60, (["MEDIATOR_LINE1", l2] if LANG in ("es", "pt", "it") else [l2, "mediating artifact"]), 18, lh=1.6)
G = "#8a8a8a"
b += line([(387, 106), (487, 106)], end=False, color=G, sw=4) + line([(717, 106), (830, 106)], color=G, sw=3)
b += line([(487, 140), (392, 140)], color=G, sw=3) + line([(835, 140), (717, 140)], end=False, color=G, sw=4)
b += line([(912, 196), (912, 246)], end=False, color=G, sw=4) + line([(958, 246), (958, 201)], color=G, sw=3)
b += line([(912, 366), (912, 411)], color=G, sw=3) + line([(958, 416), (958, 366)], end=False, color=G, sw=4)
b += line([(257, 246), (257, 201)], color=G, sw=3) + line([(292, 196), (292, 246)], end=False, color=G, sw=4)
b += line([(257, 366), (257, 416)], end=False, color=G, sw=4) + line([(292, 366), (292, 411)], color=G, sw=3)
b += line([(487, 452), (392, 452)], color=G, sw=3) + line([(387, 486), (487, 486)], end=False, color=G, sw=4)
b += line([(717, 452), (835, 452)], end=False, color=G, sw=4) + line([(717, 486), (830, 486)], color=G, sw=3)
b = b.replace('marker-end="url(#a)"', 'marker-end="url(#h)"')
it = ' font-style="italic"'
b += f'<rect x="474" y="8" width="250" height="40" fill="{LAB}"/>' + ctext(599, 28, ["Commitment"], 26, 700, PUR, style=it)
b += f'<rect x="1040" y="288" width="216" height="38" fill="{LAB}"/>' + ctext(1148, 307, ["Competence"], 26, 700, PUR, style=it)
b += f'<rect x="486" y="552" width="250" height="40" fill="{LAB}"/>' + ctext(611, 572, ["Performance"], 26, 700, PUR, style=it)
b += f'<rect x="0" y="260" width="180" height="96" fill="{LAB}"/>' + ctext(90, 280, ["Review"], 26, 700, PUR, style=it) + ctext(90, 326, ["Evaluation &", "retribution"], 18, 700, PUR, lh=1.6, style=it)
S["slide33"] = svg(1260, 600, b).replace("</defs>", '<marker id="h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1,1 L9,5 L1,9 z" fill="#fff" stroke="#8a8a8a" stroke-width="1.6"/></marker></defs>')

# ---- slide39 : four transactional semioses (praxeology)
SER = " font-family=\"Georgia, 'Times New Roman', serif\""
def big(x, y, w, h, fill, stroke, title, desc, ts):
    return (rect(x, y, w, h, fill, stroke, 22, 4) + text(x + w/2, y + 80, [title], ts, 700, style=SER)
            + text(x + w/2, y + 150, desc, 36, style=SER, lh=1.5))
b = big(440, 40, 1120, 224, "#eee7f5", "#6b4f9c", "Organization", ["makes explicit and stabilizes the institutional", "configurations that legitimize the arrangement"], 56)
b += rect(580, 430, 840, 200, "#fce4e7", "#c8102e", 22, 5) + text(1000, 525, ["Conversation"], 64, 700, style=SER) + text(1000, 600, ["material and semiosic gestures"], 38, style=SER)
b += big(20, 800, 880, 320, "#e4f0e8", "#2e7d55", "Cooperation", ["value production (work, self, milieu)", "under a contributive, competitive", "or antagonistic regime"], 60)
b += big(1100, 800, 880, 320, "#e4ebf5", "#2e5a8a", "Coordination", ["spatio-socio-temporal distribution", "of conversations,", "synchronous or asynchronous"], 60)
L = dict(color=LINE, sw=4, start=True)
b += line([(1000, 270), (1000, 424)], **L) + line([(434, 152), (200, 152), (200, 794)], **L) + line([(1566, 152), (1800, 152), (1800, 794)], **L)
b += line([(574, 530), (460, 530), (460, 794)], **L) + line([(1426, 530), (1540, 530), (1540, 794)], **L)
b += line([(460, 1126), (460, 1170), (1540, 1170), (1540, 1126)], **L)
S["slide39"] = svg(2000, 1190, b)

for k, v in S.items():
    open(os.path.join(OUT, k + ".svg"), "w").write(v)
print(len(S), "files")
