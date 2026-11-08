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
