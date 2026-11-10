#!/usr/bin/env python3
"""Génère 07_configurations_institutionnelles.sql à partir de configurations_tableau.json
(tableau « Configurations institutionnelles de l'action collective », M. Zacklad, version 4)."""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(ICI, "configurations_tableau.json")))
q = lambda s: "null" if s is None else "'" + s.replace("'", "''") + "'"

# Feuilles du tableau -> (slug, libellé, parent)
FEUILLES = {
 "Conjugales": ("configuration-conjugale", "Configuration conjugale", "configuration-domestique"),
 "Familiales": ("configuration-familiale", "Configuration familiale", "configuration-domestique"),
 "Amitiés intimes": ("amitie-intime", "Amitié intime", "configuration-elective"),
 "Foules et rassemblements": ("foules-et-rassemblements", "Foules et rassemblements", "configuration-de-sociabilite"),
 "Amicales et réticulaires": ("configuration-amicale-reticulaire", "Configuration amicale et réticulaire", "configuration-de-sociabilite"),
 "Groupales": ("configuration-groupale", "Configuration groupale", "configuration-de-sociabilite"),
 "Communautaires informelles": ("configuration-communautaire-informelle", "Configuration communautaire informelle", "configuration-de-sociabilite"),
 "Communautaires formelles": ("configuration-communautaire-formelle", "Configuration communautaire formelle", "configuration-de-sociabilite"),
 "Publiques": ("configuration-publique", "Configuration publique", "configuration-administrative-gestionnaire"),
 "De l'économie sociale": ("configuration-economie-sociale", "Configuration de l'économie sociale", "configuration-administrative-gestionnaire"),
 "Entrepreneuriales": ("configuration-entrepreneuriale", "Configuration entrepreneuriale", "configuration-administrative-gestionnaire"),
 "Citoyennes": ("configuration-citoyenne", "Configuration citoyenne", "configuration-civique"),
 "Juridico-administratives": ("configuration-juridico-administrative", "Configuration juridico-administrative", "configuration-civique"),
 "Participatives": ("configuration-participative", "Configuration participative", "configuration-civique"),
 "Client-fournisseur": ("configuration-client-fournisseur", "Configuration client-fournisseur", "configuration-marchande-contractuelle"),
 "Usager-prestataire": ("configuration-usager-prestataire", "Configuration usager-prestataire", "configuration-marchande-contractuelle"),
 "Religieuses": ("configuration-religieuse", "Configuration religieuse", "configuration-cultuelle-culturelle"),
 "Culturelles": ("configuration-culturelle", "Configuration culturelle", "configuration-cultuelle-culturelle"),
}
# Concepts de regroupement : slug, libellé, résumé, parent, relation
GROUPES = [
 ("configuration-institutionnelle", "Configuration institutionnelle", "Mode d'inscription des selfs dans l'action collective, décrit en types idéaux selon la valeur dominante, la nature du lien constituant les selfs, l'environnement et la coordination, les artefacts générés et la temporalité dominante. Trois grandes familles : primaires, secondaires et tertiaires.", None, None),
 ("configuration-primaire", "Configuration institutionnelle primaire", "Se caractérise par l'inscription des selfs dans leur continuité biographique et leur reproduction biologique. Le self y est engagé en totalité, dans sa singularité irréductible. Elle se répartit en configurations domestiques (conjugales, familiales) et électives (amitiés intimes).", "configuration-institutionnelle", "sous_type_de"),
 ("configuration-domestique", "Configuration domestique", "Configuration primaire, conjugale ou familiale.", "configuration-primaire", "sous_type_de"),
 ("configuration-elective", "Configuration élective", "Configuration primaire des amitiés intimes.", "configuration-primaire", "sous_type_de"),
 ("configuration-secondaire", "Configuration institutionnelle secondaire", "Se caractérise par l'appartenance du self à un collectif institué visant des finalités spécifiques. Elle se déploie sur deux versants : de sociabilité, et administratif et gestionnaire.", "configuration-institutionnelle", "sous_type_de"),
 ("configuration-de-sociabilite", "Configuration de sociabilité", "Versant de sociabilité des configurations secondaires : foules et rassemblements, amicales et réticulaires, groupales, communautaires informelles, communautaires formelles.", "configuration-secondaire", "face_de"),
 ("configuration-administrative-gestionnaire", "Configuration administrative et gestionnaire", "Versant administratif et gestionnaire des configurations secondaires : publiques, de l'économie sociale, entrepreneuriales.", "configuration-secondaire", "face_de"),
 ("configuration-tertiaire", "Configuration institutionnelle tertiaire", "Se caractérise par l'inscription des selfs dans un ordre symbolique relevant du droit, du sacré ou de l'œuvre d'art. Sous-familles : civiques et marchandes-contractuelles, fondées sur l'autorité du droit ; cultuelles-culturelles, qui relèvent de l'autorité du sacré (religieuses) ou de l'œuvre d'art (culturelles).", "configuration-institutionnelle", "sous_type_de"),
 ("configuration-civique", "Configuration civique", "Configuration tertiaire fondée sur l'autorité du droit : citoyenne, juridico-administrative, participative.", "configuration-tertiaire", "sous_type_de"),
 ("configuration-marchande-contractuelle", "Configuration marchande-contractuelle", "Configuration tertiaire fondée sur l'autorité du droit : client-fournisseur, usager-prestataire.", "configuration-tertiaire", "sous_type_de"),
 ("configuration-cultuelle-culturelle", "Configuration cultuelle-culturelle", "Configuration tertiaire qui relève de l'autorité du sacré (religieuse) ou de l'œuvre d'art (culturelle).", "configuration-tertiaire", "sous_type_de"),
 ("ordre-symbolique", "Ordre symbolique", "Ordre dans lequel les configurations tertiaires inscrivent les selfs ; il relève de l'autorité du droit, du sacré ou de l'œuvre d'art.", None, None),
 ("autorite-du-droit", "Autorité du droit", "Fonde les configurations civiques et marchandes-contractuelles.", "ordre-symbolique", "composante_de"),
 ("autorite-du-sacre", "Autorité du sacré", "Fonde les configurations religieuses.", "ordre-symbolique", "composante_de"),
 ("autorite-de-l-oeuvre-d-art", "Autorité de l'œuvre d'art", "Fonde les configurations culturelles (artistiques).", "ordre-symbolique", "composante_de"),
]
ATTR = [("exemples", "exemples"), ("valeur", "Valeur dominante"), ("lien", "Nature du lien constituant les selfs"),
        ("environnement", "Environnement et coordination"), ("artefacts", "Artefacts générés"), ("temporalite", "Temporalité dominante")]

concepts, rels, attrs = [], [], []
ordre = 0
for slug, lib, res, par, typ in GROUPES:
    ordre += 1; concepts.append((slug, lib, res, ordre))
    if par: rels.append((slug, typ, par, None))
for ligne in T["lignes"]:
    if "nom" not in ligne: continue
    slug, lib, par = FEUILLES[ligne["nom"]]
    ordre += 1; concepts.append((slug, lib, ligne["Nature du lien constituant les selfs"] + ".", ordre))
    rels.append((slug, "sous_type_de", par, None))
    for i, (cle, col) in enumerate(ATTR):
        attrs.append((slug, cle, ligne[col], i))

rels += [
 ("ordre-symbolique", "caracterise", "configuration-tertiaire", None),
 ("configuration-civique", "releve_de", "autorite-du-droit", None),
 ("configuration-marchande-contractuelle", "releve_de", "autorite-du-droit", None),
 ("configuration-religieuse", "releve_de", "autorite-du-sacre", None),
 ("configuration-culturelle", "releve_de", "autorite-de-l-oeuvre-d-art", None),
 ("configuration-communautaire-informelle", "oppose_a", "configuration-communautaire-formelle", None),
 ("self", "intervient_dans", "configuration-institutionnelle", "les configurations se distinguent par la nature du lien qui constitue les selfs"),
 ("configuration-institutionnelle", "intervient_dans", "organisation", "l'organisation explicite et stabilise les configurations institutionnelles qui légitiment l'agencement"),
 ("configuration-publique", "distingue_de", "configuration-juridico-administrative", "relations internes à l'administration (secondaire) et assujettissement des administrés au droit (tertiaire)"),
 ("configuration-entrepreneuriale", "distingue_de", "configuration-marchande-contractuelle", "collectif institué (secondaire) et relation contractuelle fondée sur le droit (tertiaire)"),
]

o = ["-- Généré par generer_configurations.py : configurations institutionnelles (tableau v4 de M. Zacklad, 10 novembre 2026). Statut provisoire.",
     "insert into famille (slug, libelle, description, ordre) values ('configuration', 'Configurations institutionnelles', 'Types idéaux des configurations institutionnelles de l''action collective', 18) on conflict (slug) do update set libelle = excluded.libelle, description = excluded.description, ordre = excluded.ordre;",
     "with c(slug, libelle, resume, ordre) as (values"]
o.append(",\n".join(f" ({q(s)}, {q(l)}, {q(r)}, {n})" for s, l, r, n in concepts))
o.append(") insert into concept (slug, libelle, famille_slug, resume, statut, ordre) select slug, libelle, 'configuration', resume, 'provisoire', ordre from c on conflict (slug) do update set libelle = excluded.libelle, famille_slug = excluded.famille_slug, resume = excluded.resume, ordre = excluded.ordre;")
o.append("with r(s, t, c, com, o) as (values")
o.append(",\n".join(f" ({q(s)}, {q(t)}, {q(c)}, {q(m)}, {i})" for i, (s, t, c, m) in enumerate(rels)))
o.append(") insert into relation (source_id, cible_id, type_slug, commentaire, ordre) select a.id, b.id, r.t, r.com, r.o from r join concept a on a.slug = r.s join concept b on b.slug = r.c where not exists (select 1 from relation x where x.source_id = a.id and x.cible_id = b.id and x.type_slug = r.t);")
o.append("with v(s, a, x, o) as (values")
o.append(",\n".join(f" ({q(s)}, {q(a)}, {q(x)}, {i})" for s, a, x, i in attrs))
o.append(") insert into concept_attribut (concept_id, attribut, valeur, ordre) select c.id, v.a, v.x, v.o from v join concept c on c.slug = v.s on conflict (concept_id, attribut) do update set valeur = excluded.valeur, ordre = excluded.ordre;")
open(os.path.join(ICI, "07_configurations_institutionnelles.sql"), "w").write("\n".join(o) + "\n")
print(len(concepts), "concepts,", len(rels), "relations,", len(attrs), "attributs")
