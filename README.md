# Glossaire de la Sémiotique des Transactions Coopératives

Glossaire relationnel des concepts de la STC (Manuel Zacklad, Cnam, Dicen-IDF).

- Site : https://transactions-cooperatives.zacklad.org
- Données : base Supabase `glossaire-stc` (lecture publique, écriture réservée)
- Front : page unique `index.html`, sans build, hébergée par GitHub Pages

## Structure des données

- `famille` : familles de concepts (facettes, gradients, moments du parcours, etc.)
- `concept` : libellé, famille, résumé provisoire, statut (stabilisé, provisoire, en discussion, écarté)
- `type_relation` et `relation` : relations typées et orientées entre concepts
- `definition` : définitions versionnées
- `auteur`, `concept_auteur` : auteurs et traditions mobilisés
- `reference`, `concept_reference` : références bibliographiques
- `terme_ecarte` : termes écartés et raisons

## Mise à jour

Les contenus se modifient dans Supabase : le site se met à jour sans redéploiement.
Le code du site se modifie ici : chaque `git push` sur `main` republie le site.

## Langues

Le site est disponible en français (référence), en anglais, espagnol, allemand, portugais et italien (traductions de travail).
- Choix de langue : boutons FR / EN / ES / DE / PT / IT, mémorisé dans le navigateur ; lien partageable avec `?lang=en`, `es`, `de`, `pt` ou `it`.
- Contenus traduits : table `traduction` (table, clé, champ, langue, texte, statut « travail » ou « relue »).
- Terminologie : voir `TERMINOLOGIE.md` ; sources des traductions dans `supabase/traductions_en.py` et `traductions_es.py`.
- Ajouter une langue : un bloc dans `I18N` (index.html) et des lignes dans `traduction` ; tout texte non traduit s'affiche en français.
