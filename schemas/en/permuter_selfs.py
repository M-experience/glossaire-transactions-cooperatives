#!/usr/bin/env python3
"""Slide 12: puts the project owner / beneficiary self on the left and the entrepreneur / performer self
on the right (boxes swapped with their drawings, descriptions rewritten).
Usage: permuter_selfs.py ORIGINAL.webp OUT.webp"""
import sys
from PIL import Image, ImageDraw
from traduire_illustrations import bloc, INK

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
G = (320, 446, 582, 637)      # left box (entrepreneur in the original)
D = (1288, 446, 1560, 640)    # right box (project owner in the original)
g, d = im.crop(G), im.crop(D)
im.paste(d.resize((G[2] - G[0], G[3] - G[1]), Image.LANCZOS), G[:2])
im.paste(g.resize((D[2] - D[0], D[3] - D[1]), Image.LANCZOS), D[:2])
# mirror the drawings (below the titles) so that the two selves face each other
for x0, y0, x1, y1 in (G, D):
    zone = (x0 + 4, 512, x1 - 4, y1 - 4)
    im.paste(im.crop(zone).transpose(Image.FLIP_LEFT_RIGHT), zone[:2])
bloc(im, (326, 637, 522, 706), ["Exprime un besoin, apporte", "des ressources, évalue,", "réutilise, bénéficie."], "serif", 19, INK, "l")
bloc(im, (1308, 637, 1545, 706), ["Porte une intention,", "mobilise des ressources,", "agit, produit."], "serif", 19)
im.convert("RGB").save(out, quality=90)
