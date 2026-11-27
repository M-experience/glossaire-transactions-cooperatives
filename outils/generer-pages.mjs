#!/usr/bin/env node
// Génère les pages statiques indexables du glossaire (une page par concept et par langue),
// l'index des concepts, sitemap.xml et robots.txt, à partir de la base Supabase.
// Usage : node outils/generer-pages.mjs   (depuis la racine du dépôt)
import fs from "node:fs";
import path from "node:path";

const RACINE = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const BASE = "https://transactions-cooperatives.zacklad.org";
const LANGUES = ["fr", "en", "es", "de", "pt", "it"];

// Clé publique, adresse et libellés d'interface : repris de index.html pour rester synchrones.
const index = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");
const URL_SB = index.match(/const SUPABASE_URL = "([^"]+)"/)[1];
const KEY = index.match(/const SUPABASE_KEY = "([^"]+)"/)[1];
const i18nSrc = index.slice(index.indexOf("const I18N = {") + "const I18N = ".length, index.indexOf("\n};", index.indexOf("const I18N = {")) + 2);
const I18N = new Function("return " + i18nSrc)();

const PLUS = {
  fr: { interactif: "Ouvrir dans le glossaire interactif (graphe, schémas)", tous: "Tous les concepts", famille: "Famille", liste_titre: "Liste des concepts", liste_intro: "Tous les concepts du glossaire, par famille. Chaque fiche présente le résumé, la définition lorsqu'elle est établie et les relations du concept." },
  en: { interactif: "Open in the interactive glossary (graph, diagrams)", tous: "All concepts", famille: "Family", liste_titre: "List of concepts", liste_intro: "All the concepts of the glossary, by family. Each entry gives the summary, the definition when established and the relations of the concept." },
  es: { interactif: "Abrir en el glosario interactivo (grafo, esquemas)", tous: "Todos los conceptos", famille: "Familia", liste_titre: "Lista de conceptos", liste_intro: "Todos los conceptos del glosario, por familia. Cada ficha presenta el resumen, la definición cuando está establecida y las relaciones del concepto." },
  de: { interactif: "Im interaktiven Glossar öffnen (Graph, Schemata)", tous: "Alle Begriffe", famille: "Familie", liste_titre: "Liste der Begriffe", liste_intro: "Alle Begriffe des Glossars, nach Familien. Jeder Eintrag enthält die Zusammenfassung, die Definition, sofern festgelegt, und die Relationen des Begriffs." },
  pt: { interactif: "Abrir no glossário interativo (grafo, esquemas)", tous: "Todos os conceitos", famille: "Família", liste_titre: "Lista de conceitos", liste_intro: "Todos os conceitos do glossário, por família. Cada ficha apresenta o resumo, a definição quando estabelecida e as relações do conceito." },
  it: { interactif: "Apri nel glossario interattivo (grafo, schemi)", tous: "Tutti i concetti", famille: "Famiglia", liste_titre: "Elenco dei concetti", liste_intro: "Tutti i concetti del glossario, per famiglia. Ogni scheda presenta il riassunto, la definizione quando stabilita e le relazioni del concetto." },
};

async function api(chemin) {
  const r = await fetch(`${URL_SB}/rest/v1/${chemin}`, { headers: { apikey: KEY } });
  if (!r.ok) throw new Error(`${chemin} : ${r.status}`);
  return r.json();
}

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const court = (s, n = 155) => { s = String(s ?? "").replace(/\s+/g, " ").trim(); return s.length <= n ? s : s.slice(0, s.lastIndexOf(" ", n - 1)) + "…"; };
const prefixe = l => (l === "fr" ? "" : `/${l}`);
const urlConcept = (l, slug) => `${BASE}${prefixe(l)}/concept/${slug}/`;
const urlListe = l => `${BASE}${prefixe(l)}/concepts/`;

const [familles, concepts, relations, ...trads] = await Promise.all([
  api("famille?select=slug,libelle,description,ordre&order=ordre"),
  api("concept?select=slug,libelle,famille_slug,resume,statut,ordre,updated_at,definition(texte,version,est_courante),concept_attribut(attribut,valeur,ordre)&order=ordre"),
  api("v_relation?select=*&order=ordre"),
  ...LANGUES.filter(l => l !== "fr").map(l => api(`traduction?select=table_nom,cle,champ,texte&langue=eq.${l}`)),
]);
const TRAD = { fr: {} };
LANGUES.filter(l => l !== "fr").forEach((l, i) => { TRAD[l] = Object.fromEntries(trads[i].map(r => [`${r.table_nom}|${r.cle}|${r.champ}`, r.texte])); });

function donnees(l) {
  const T = TRAD[l]; const tr = (tab, cle, champ, d) => T[`${tab}|${cle}|${champ}`] ?? d;
  const fam = Object.fromEntries(familles.map(f => [f.slug, { ...f, libelle: tr("famille", f.slug, "libelle", f.libelle) }]));
  const cs = concepts.map(c => ({ ...c, libelle: tr("concept", c.slug, "libelle", c.libelle), resume: tr("concept", c.slug, "resume", c.resume),
    attributs: (c.concept_attribut || []).sort((a, b) => a.ordre - b.ordre).map(a => ({ ...a, valeur: tr("concept_attribut", `${c.slug}|${a.attribut}`, "valeur", a.valeur) })) }));
  const rels = relations.map(r => ({ ...r, libelle: tr("type_relation", r.type_slug, "libelle", r.libelle), libelle_inverse: tr("type_relation", r.type_slug, "libelle_inverse", r.libelle_inverse) }));
  return { fam, cs, parSlug: Object.fromEntries(cs.map(c => [c.slug, c])), rels };
}
const t = (l, k) => (I18N[l] && I18N[l][k] !== undefined ? I18N[l][k] : I18N.fr[k] ?? k);

function alternates(chemin) {
  return LANGUES.map(l => `<link rel="alternate" hreflang="${l}" href="${chemin(l)}">`).join("\n") + `\n<link rel="alternate" hreflang="x-default" href="${chemin("fr")}">`;
}

const CSS = `body{margin:0;font-family:Inter,system-ui,sans-serif;color:#1d2330;background:#fafaf8;line-height:1.6}
a{color:#C4122C;text-decoration:none}a:hover{text-decoration:underline}
header{background:#fff;border-bottom:3px solid #C4122C;padding:14px 24px}
header .st{color:#C4122C;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}
header .ti{font-family:"Source Serif 4",Georgia,serif;font-size:1.5rem;font-weight:600;color:#1d2330}
main{max-width:860px;margin:0 auto;padding:24px}
h1,h2{font-family:"Source Serif 4",Georgia,serif;font-weight:600}h1{font-size:2rem;margin:.2em 0}
.fil{font-size:.88rem;color:#5b6372}.statut{display:inline-block;font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;padding:2px 8px;border-radius:10px;background:#e8f1ec;color:#2f6f4f}
.resume{border-left:4px solid #C4122C;background:#fff;padding:12px 16px;font-family:"Source Serif 4",Georgia,serif;font-size:1.08rem}
.def{background:#fff;border:1px solid #e3e5ea;border-radius:10px;padding:14px 18px}
dl{display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:6px 16px}dt{font-weight:600;color:#5b6372}dd{margin:0}
.rel h3{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:#5b6372;margin:14px 0 4px}.rel ul,.liste ul{margin:0;padding-left:18px}
.bouton{display:inline-block;margin:18px 0;padding:9px 16px;border:1px solid #C4122C;border-radius:8px}
footer{max-width:860px;margin:30px auto;padding:0 24px 30px;color:#5b6372;font-size:.85rem}
.langues a{margin-right:10px}`;

function gabarit(l, { titre, description, canonique, alt, jsonld, corps }) {
  return `<!DOCTYPE html>
<html lang="${l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(titre)}</title>
<meta name="description" content="${esc(description)}">
<link rel="canonical" href="${canonique}">
${alt}
<meta property="og:title" content="${esc(titre)}">
<meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${canonique}">
<meta property="og:type" content="article">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>${CSS}</style>
<script type="application/ld+json">${JSON.stringify(jsonld)}</script>
</head>
<body>
<header><a href="${BASE}/?lang=${l}"><div class="st">${esc(t(l, "sous_titre"))}</div><div class="ti">${esc(t(l, "titre"))}</div></a></header>
<main>
${corps}
</main>
<footer>${esc(t(l, "pied"))} · <a href="${urlListe(l)}">${esc(PLUS[l].tous)}</a></footer>
</body>
</html>
`;
}

const ensemble = l => ({ "@type": "DefinedTermSet", "@id": `${urlListe(l)}#glossaire`, name: t(l, "titre_long"), url: urlListe(l), inLanguage: l,
  author: { "@type": "Person", name: "Manuel Zacklad", affiliation: { "@type": "Organization", name: "Cnam, Dicen-IDF" } } });

function ecrire(rel, contenu) {
  const f = path.join(RACINE, rel); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, contenu);
}

// pages des concepts disparus ou renommés : on repart de zéro à chaque génération
for (const l of LANGUES) fs.rmSync(path.join(RACINE, prefixe(l).slice(1), "concept"), { recursive: true, force: true });

let n = 0;
const urls = [];
for (const l of LANGUES) {
  const { fam, cs, parSlug, rels } = donnees(l);
  const lien = slug => (parSlug[slug] ? `<a href="${urlConcept(l, slug)}">${esc(parSlug[slug].libelle)}</a>` : esc(slug));
  for (const c of cs) {
    const def = (c.definition || []).filter(d => d.est_courante).sort((a, b) => b.version - a.version)[0];
    const defTexte = def ? (l === "fr" ? def.texte : TRAD[l][`definition|${c.slug}|texte`] ?? def.texte) : null;
    const groupes = {};
    for (const r of rels) {
      if (r.source_slug === c.slug) (groupes[r.libelle] ??= []).push(r.cible_slug);
      else if (r.cible_slug === c.slug) (groupes[r.libelle_inverse || r.libelle] ??= []).push(r.source_slug);
    }
    const f = fam[c.famille_slug];
    let corps = `<p class="fil"><a href="${urlListe(l)}">${esc(t(l, "nav_concepts"))}</a> › ${esc(f?.libelle ?? "")}</p>
<h1>${esc(c.libelle)}</h1>
<span class="statut">${esc(t(l, c.statut))}</span>`;
    if (c.resume) corps += `\n<div class="resume"><p>${esc(c.resume)}</p></div>`;
    if (defTexte) corps += `\n<h2>${esc(t(l, "definition"))}</h2>\n<div class="def"><p>${esc(defTexte)}</p></div>`;
    const attrs = c.attributs.filter(a => a.attribut !== "lien");
    if (attrs.length) corps += `\n<h2>${esc(t(l, "caracteristiques"))}</h2>\n<dl>` + attrs.map(a => `<dt>${esc(t(l, "attr_" + a.attribut))}</dt><dd>${esc(a.valeur).replace(/\n/g, "<br>")}</dd>`).join("") + `</dl>`;
    const g = Object.entries(groupes);
    if (g.length) corps += `\n<h2>${esc(t(l, "relations"))}</h2>\n<div class="rel">` + g.map(([lab, sl]) => `<h3>${esc(lab)}</h3><ul>${[...new Set(sl)].map(s => `<li>${lien(s)}</li>`).join("")}</ul>`).join("") + `</div>`;
    corps += `\n<a class="bouton" href="${BASE}/?lang=${l}#/concept/${c.slug}">${esc(PLUS[l].interactif)}</a>`;
    corps += `\n<p class="langues">${LANGUES.filter(x => x !== l).map(x => `<a href="${urlConcept(x, c.slug)}" hreflang="${x}">${x.toUpperCase()}</a>`).join("")}</p>`;
    const description = court(defTexte || c.resume || c.libelle);
    const jsonld = { "@context": "https://schema.org", "@type": "DefinedTerm", "@id": urlConcept(l, c.slug), name: c.libelle, description: defTexte || c.resume || undefined,
      url: urlConcept(l, c.slug), inLanguage: l, termCode: c.slug, inDefinedTermSet: ensemble(l) };
    ecrire(`${prefixe(l).slice(1) ? prefixe(l).slice(1) + "/" : ""}concept/${c.slug}/index.html`,
      gabarit(l, { titre: `${c.libelle} · ${t(l, "titre")}`, description, canonique: urlConcept(l, c.slug), alt: alternates(x => urlConcept(x, c.slug)), jsonld, corps }));
    urls.push({ chemin: x => urlConcept(x, c.slug), lastmod: (c.updated_at || "").slice(0, 10), l });
    n++;
  }
  // Index des concepts, par famille
  let corps = `<h1>${esc(PLUS[l].liste_titre)}</h1>\n<p>${esc(PLUS[l].liste_intro)}</p>\n<p><a class="bouton" href="${BASE}/?lang=${l}">${esc(PLUS[l].interactif)}</a></p>\n<div class="liste">`;
  for (const f of familles) {
    const membres = cs.filter(c => c.famille_slug === f.slug);
    if (!membres.length) continue;
    corps += `<h2>${esc(fam[f.slug].libelle)}</h2><ul>${membres.map(c => `<li>${lien(c.slug)}${c.resume ? ` - ${esc(court(c.resume, 120))}` : ""}</li>`).join("")}</ul>`;
  }
  corps += `</div>`;
  const jsonld = { "@context": "https://schema.org", ...ensemble(l), hasDefinedTerm: cs.map(c => ({ "@type": "DefinedTerm", name: c.libelle, url: urlConcept(l, c.slug) })) };
  ecrire(`${prefixe(l).slice(1) ? prefixe(l).slice(1) + "/" : ""}concepts/index.html`,
    gabarit(l, { titre: `${PLUS[l].liste_titre} · ${t(l, "titre_long")}`, description: court(PLUS[l].liste_intro), canonique: urlListe(l), alt: alternates(urlListe), jsonld, corps }));
  urls.push({ chemin: urlListe, lastmod: "", l });
}

// Plan du site avec les versions linguistiques
// date stable (dernière modification de la base) pour éviter un commit quotidien sans changement réel
const auj = concepts.map(c => (c.updated_at || "").slice(0, 10)).sort().pop() || new Date().toISOString().slice(0, 10);
const entree = (loc, chemin, lastmod) => `<url><loc>${loc}</loc><lastmod>${lastmod || auj}</lastmod>${LANGUES.map(x => `<xhtml:link rel="alternate" hreflang="${x}" href="${chemin(x)}"/>`).join("")}</url>`;
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${entree(`${BASE}/`, x => `${BASE}/?lang=${x}`, auj).replace(/hreflang="fr" href="[^"]+"/, `hreflang="fr" href="${BASE}/"`)}
${urls.map(u => entree(u.chemin(u.l), u.chemin, u.lastmod)).join("\n")}
</urlset>
`;
ecrire("sitemap.xml", sitemap);
ecrire("robots.txt", `User-agent: *\nAllow: /\n\nSitemap: ${BASE}/sitemap.xml\n`);
console.log(`${n} pages de concepts, ${LANGUES.length} index, sitemap de ${urls.length + 1} adresses`);
