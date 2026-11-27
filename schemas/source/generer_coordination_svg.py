#!/usr/bin/env python3
"""Schéma des trois modes et neuf formes de coordination -> schemas/coordination.svg"""
import os
from xml.sax.saxutils import escape as E

ICI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ICI, "..", "coordination.svg")
FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, GRIS = "#1f2430", "#55606e"

def t(x, y, lignes, taille=15, poids=400, coul=INK, anc="middle", lh=1.3, extra=""):
    if isinstance(lignes, str): lignes = [lignes]
    return "".join(f'<text x="{x}" y="{y + i * taille * lh:.1f}" font-size="{taille}" font-weight="{poids}" fill="{coul}" text-anchor="{anc}"{extra}>{E(l)}</text>' for i, l in enumerate(lignes))

def ct(cx, cy, lignes, taille=15, poids=400, coul=INK, lh=1.3, extra=""):
    if isinstance(lignes, str): lignes = [lignes]
    return t(cx, cy - (len(lignes) - 1) * taille * lh / 2 + taille * 0.35, lignes, taille, poids, coul, "middle", lh, extra)

def r(x, y, w, h, fond, trait, rx=12, ep=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fond}" stroke="{trait}" stroke-width="{ep}"/>'

def fleche(x, y1, y2, coul):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 9}" stroke="{coul}" stroke-width="2"/>'
            f'<polygon points="{x - 6},{y2 - 10} {x + 6},{y2 - 10} {x},{y2}" fill="{coul}"/>')

MODES = [
 dict(titre=["Coordination par l’accès", "spatio-temporel"], dom="MILIEU · TERRITORIALISATION", crit="partage du lieu et du temps",
      trait="#4f7a28", fond="#dcebc9", clair="#f0f6e8",
      formes=[("Même lieu, même temps", "Synchrone en présence", "face-à-face, réunion"),
              ("Même temps, sans partage du lieu", "Synchrone à distance", "téléphone, visiophonie, direct"),
              ("Échange différé", "Asynchrone", "textes, documents, messages, archives")],
      disp="Dispositif d’accès", ex=["lieux et salles, agendas, visiophonie,", "messageries, plateformes, espaces documentaires"]),
 dict(titre=["Coordination", "relationnelle"], dom="SELFS · SUBJECTIVATION", crit="qui peut tenir le rôle",
      trait="#b0413e", fond="#f6dcdc", clair="#fbeeee",
      formes=[("Cette personne-ci", "Interpersonnelle", "couple, amis intimes, parent et enfant"),
              ("Un membre du collectif", "Affiliative", "équipe, association, leader reconnu"),
              ("Quiconque remplit les conditions", "Positionnelle", "client et fournisseur, usager et agent")],
      disp="Dispositif relationnel", ex=["organigrammes, fiches de poste, contrats,", "statuts, délégations, règles d’appartenance"]),
 dict(titre=["Coordination", "interprétative"], dom="ARTEFACTS MÉDIATEURS", crit="registre de la sémiose cognitive",
      trait="#2e5f92", fond="#d6e5f6", clair="#edf3fb",
      formes=[("Raison sensible", "Conscience mutuelle", "signaux, regards, rythme (awareness)"),
              ("Raison pratique", "Typification", "routines, check-lists, livrables"),
              ("Raison conceptuelle", "Conceptualisation", "modèles, spécifications, récits")],
      disp="Dispositif interprétatif", ex=["procédures, référentiels, spécifications,", "tableaux de bord, maquettes, prototypes"]),
]

W, X0, CW, G = 1700, 40, 510, 45
b = t(40, 56, "Les trois modes de coordination dans la STC", 28, 700, anc="start")
b += t(40, 86, "Trois modes, neuf formes, un dispositif conversationnel", 17, 400, GRIS, anc="start")
YB = 108
b += r(40, YB, 1620, 34, "#efece6", "none", 8, 0)
b += ct(850, YB + 17, "Coordination : règle l’accès, les rôles réciproques et la lecture partagée de la situation", 15, 600, GRIS)

YC, HEAD, CARD_H, CARD_G = YB + 56, 132, 92, 12
COL_H = HEAD + 3 * CARD_H + 2 * CARD_G + 84
for i, m in enumerate(MODES):
    x = X0 + i * (CW + G)
    b += r(x, YC, CW, COL_H, m["clair"], m["trait"], 16, 2)
    b += t(x + CW / 2, YC + 30, m["dom"], 12.5, 700, m["trait"], extra=' letter-spacing="1.5"')
    b += ct(x + CW / 2, YC + 66, m["titre"], 21, 700, m["trait"], 1.2)
    b += t(x + CW / 2, YC + 116, f"Critère des formes : {m['crit']}", 13.5, 400, GRIS)
    relationnel = i == 1
    cw = CW - 24
    for j, (sur, nom, ex) in enumerate(m["formes"]):
        cy = YC + HEAD + j * (CARD_H + CARD_G)
        b += r(x + 12, cy, cw, CARD_H, "#ffffff", m["fond"], 12, 2)
        b += t(x + 12 + cw / 2, cy + 24, sur, 12.5, 600, m["trait"], extra=' font-style="italic"')
        b += t(x + 12 + cw / 2, cy + 52, nom, 18, 700)
        b += t(x + 12 + cw / 2, cy + 76, ex, 13, 400, GRIS)
    if relationnel:
        gy = YC + HEAD + 3 * CARD_H + 2 * CARD_G + 14
        b += ('<defs><linearGradient id="aut" x1="0" y1="0" x2="1" y2="0">'
              '<stop offset="0" stop-color="#8a3330"/><stop offset="0.5" stop-color="#d79d9a"/><stop offset="1" stop-color="#f8e6e5"/></linearGradient></defs>')
        b += r(x + 12, gy, cw, 46, "url(#aut)", "#b0413e", 23, 1.2)
        b += t(x + 30, gy + 29, "hiérarchie", 13, 700, "#ffffff", anc="start")
        b += t(x + 12 + cw / 2, gy + 20, "Gradient d’autorité", 12.5, 700, "#5a1f1d")
        b += t(x + 12 + cw / 2, gy + 37, "hétérarchie", 12.5, 600, "#5a1f1d")
        b += t(x + cw - 6, gy + 29, "parité", 13, 700, "#8a3330", anc="end")

# Dispositif conversationnel
YD = YC + COL_H + 50
DISP = "#5b4a8c"
b += r(40, YD, 1620, 186, "#f4f2fa", DISP, 16, 2)
b += t(70, YD + 32, "Dispositif conversationnel", 19, 700, DISP, anc="start")
b += t(330, YD + 32, "coordination stabilisée qui cadre les conversations, en position de tiers médiateur", 14, 400, GRIS, anc="start")
for i, m in enumerate(MODES):
    x = X0 + i * (CW + G)
    b += fleche(x + CW / 2, YC + COL_H + 4, YD, DISP)
    b += t(x + CW / 2 + 10, YC + COL_H + 28, "cadrage", 12, 600, DISP, anc="start", extra=' font-style="italic"')
    b += r(x + 12, YD + 60, CW - 24, 108, "#ffffff", "#c9c1e3", 12, 1.5)
    b += t(x + CW / 2, YD + 92, m["disp"], 17, 700, DISP)
    b += t(x + CW / 2, YD + 120, m["ex"], 13, 400, GRIS, lh=1.4)

YF = YD + 186 + 34
b += t(40, YF, "Dans chaque mode, les formes ne s’excluent pas ; les trois modes se combinent dans toute situation de coordination.", 14, 400, INK, anc="start")
b += t(40, YF + 24, "D’après M. Zacklad, Les trois modes de coordination dans la STC (2026)", 13, 400, GRIS, anc="start")
H = YF + 44
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">'
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>{b}</svg>')
open(OUT, "w").write(svg)
print(OUT, W, H)
