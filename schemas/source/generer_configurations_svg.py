#!/usr/bin/env python3
"""Schéma de la typologie des configurations institutionnelles -> schemas/configurations.svg"""
import os
from xml.sax.saxutils import escape as E

ICI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ICI, "..", "configurations.svg")
FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, GRIS = "#1f2430", "#55606e"

def t(x, y, lignes, taille=15, poids=400, coul=INK, anc="middle", lh=1.3, style=""):
    if isinstance(lignes, str): lignes = [lignes]
    return "".join(f'<text x="{x}" y="{y + i * taille * lh:.1f}" font-size="{taille}" font-weight="{poids}" fill="{coul}" text-anchor="{anc}"{style}>{E(l)}</text>' for i, l in enumerate(lignes))

def ct(cx, cy, lignes, taille=15, poids=400, coul=INK, lh=1.3, style=""):
    if isinstance(lignes, str): lignes = [lignes]
    y0 = cy - (len(lignes) - 1) * taille * lh / 2 + taille * 0.35
    return t(cx, y0, lignes, taille, poids, coul, "middle", lh, style)

def r(x, y, w, h, fond, trait, rx=12, ep=1.5, tirets=None):
    d = f' stroke-dasharray="{tirets}"' if tirets else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fond}" stroke="{trait}" stroke-width="{ep}"{d}/>'

PILL_H, PILL_G, SUB_HEAD = 44, 10, 58

def sous_famille(x, y, w, titre, feuilles, fond, trait, h_total):
    s = r(x, y, w, h_total, "#ffffff", trait, 12, 1.5)
    s += ct(x + w / 2, y + SUB_HEAD / 2 + 2, titre, 16, 700, trait)
    yy = y + SUB_HEAD
    for f in feuilles:
        s += r(x + 12, yy, w - 24, PILL_H, fond, "none", 22, 0) + ct(x + w / 2, yy + PILL_H / 2, f, 14.5)
        yy += PILL_H + PILL_G
    return s

def hauteur(n): return SUB_HEAD + n * (PILL_H + PILL_G) + 6

COLS = [
 dict(x=40, w=420, titre="Configurations primaires", fond="#f6dcdc", trait="#b0413e", clair="#fbeeee",
      def_=["Inscription des selfs dans leur continuité", "biographique et leur reproduction biologique ;", "le self est engagé en totalité, dans sa singularité"],
      sous=[(["Domestiques"], ["Conjugales", "Familiales"]), (["Électives"], ["Amitiés intimes"])]),
 dict(x=490, w=540, titre="Configurations secondaires", fond="#dcebc9", trait="#4f7a28", clair="#f0f6e8",
      def_=["Appartenance du self à un collectif institué", "visant des finalités spécifiques"],
      sous=[(["De sociabilité"], ["Foules et rassemblements", "Amicales et réticulaires", "Groupales", "Communautaires"]),
            (["Administratives", "et gestionnaires"], ["De l’économie sociale", "Entrepreneuriales", "Publiques"])]),
 dict(x=1060, w=600, titre="Configurations tertiaires", fond="#d6e5f6", trait="#2e5f92", clair="#edf3fb",
      poids=[1.3, 1.15, 0.9, 0.9],
      def_=["Inscription des selfs dans un ordre symbolique", "relevant du droit, du sacré ou de l’œuvre d’art"],
      sous=[(["Civiques"], ["Politiques", "Étatique et administrative", "Citoyenne et participative"]),
            (["Marchandes-", "contractuelles"], ["Client-fournisseur", "Usager-prestataire"]),
            (["Religieuses"], ["Religieuses"]),
            (["Artistiques"], ["Artistiques"])]),
]
# feuilles sur deux lignes
DEUX = {"Juridico-": ["Juridico-administratives"], "Culturelles-": ["Culturelles-artistiques"]}

W, Y0 = 1700, 96
H_SUB = hauteur(4) + 16
COL_TOP, HEAD_H = Y0 + 34, 128
COL_H = HEAD_H + H_SUB + 28
b = t(40, 58, "Configurations institutionnelles de l’action collective", 28, 700, anc="start")
b += t(40, 88, "Typologie en types idéaux", 17, 400, GRIS, anc="start")
b += r(40, COL_TOP - 30, 1620, 26, "#efece6", "none", 8, 0) + ct(850, COL_TOP - 17, "Configuration institutionnelle : mode d’inscription des selfs dans l’action collective", 14, 600, GRIS)

positions = {}
for c in COLS:
    x, w = c["x"], c["w"]
    b += r(x, COL_TOP, w, COL_H, c["clair"], c["trait"], 16, 2)
    b += ct(x + w / 2, COL_TOP + 30, c["titre"], 21, 700, c["trait"])
    b += ct(x + w / 2, COL_TOP + 62 + (len(c["def_"]) - 1) * 9, c["def_"], 13.5, 400, GRIS, 1.35)
    n = len(c["sous"]); g = 12
    poids = c.get("poids", [1] * n); unite = (w - 24 - g * (n - 1)) / sum(poids)
    sx = x + 12
    for i, (titre, feuilles) in enumerate(c["sous"]):
        sw = unite * poids[i]; sy = COL_TOP + HEAD_H
        if i: sx = positions[(c["titre"], i - 1)][0] + positions[(c["titre"], i - 1)][1] + g
        fe = []
        for f in feuilles:
            if f == "Juridico-": fe.append("Juridico-administratives")
            elif f == "Culturelles-": fe.append("Culturelles-artistiques")
            elif f == "artistiques": continue
            else: fe.append(f)
        s = r(sx, sy, sw, H_SUB, "#ffffff", c["trait"], 12, 1.3)
        s += ct(sx + sw / 2, sy + SUB_HEAD / 2 + 1, titre, 15.5, 700, c["trait"], 1.2)
        yy = sy + SUB_HEAD
        for f in fe:
            lignes = [f]
            if len(f) * 7.3 > sw - 28:
                coupe = f.find("-") + 1 if "-" in f else f.rfind(" ", 0, len(f) // 2 + 4)
                lignes = [f[:coupe].strip(), f[coupe:].strip()]
            hh = PILL_H if len(lignes) == 1 else PILL_H + 16
            fond = {"Religieuses": "#f6ead0", "Artistiques": "#f5dde8"}.get(f, c["fond"])
            s += r(sx + 10, yy, sw - 20, hh, fond, "none", 20, 0) + ct(sx + sw / 2, yy + hh / 2, lignes, 14, 400, INK, 1.2)
            yy += hh + PILL_G
        b += s
        positions[(c["titre"], i)] = (sx, sw)

# autorités sous les tertiaires
ya = COL_TOP + COL_H + 34
tert = COLS[2]
(cx0, cw0), (cx1, cw1), (cx2, cw2), (cx3, cw3) = (positions[(tert["titre"], i)] for i in range(4))
AUT = "#5b4a8c"
def autorite(x, w, lignes, coul=AUT, fond="#ece8f6"):
    return r(x, ya, w, 56, fond, coul, 28, 1.5) + ct(x + w / 2, ya + 28, lignes, 14, 700, coul)
def fleche(x, AUT=AUT):
    y1, y2 = ya - 4, COL_TOP + COL_H + 4
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 + 8}" stroke="{AUT}" stroke-width="2"/>'
            f'<polygon points="{x - 6},{y2 + 10} {x + 6},{y2 + 10} {x},{y2}" fill="{AUT}"/>')
b += autorite(cx0, cx1 + cw1 - cx0, "Autorité du droit") + fleche(cx0 + cw0 / 2) + fleche(cx1 + cw1 / 2)
b += autorite(cx2, cw2, ["Autorité", "du sacré"], "#8a5d0c", "#f6ead0") + fleche(cx2 + cw2 / 2, "#8a5d0c")
b += autorite(cx3, cw3, ["Autorité de", "l’œuvre d’art"], "#a33a6b", "#f5dde8") + fleche(cx3 + cw3 / 2, "#a33a6b")
b += t(tert["x"] + tert["w"] / 2, ya + 84, "Ordre symbolique", 15, 600, AUT, style=' font-style="italic"')
b += t(40, ya + 84, "D’après M. Zacklad, typologie des configurations institutionnelles (version 9)", 13, 400, GRIS, anc="start")

H = ya + 104
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">'
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>{b}</svg>')
open(OUT, "w").write(svg)
print(OUT, W, H)
