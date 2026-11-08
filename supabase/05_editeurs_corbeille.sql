-- 2026-11-08 : migration editeurs_et_corbeille (appliquée)
-- - table editeur (emails autorisés) et fonction est_editeur()
-- - écriture (insert/update/delete) réservée aux éditeurs authentifiés sur toutes les tables du glossaire
-- - table corbeille + trigger archiver_concept : tout concept supprimé est archivé (jsonb) avec ses relations,
--   définitions, auteurs, références et termes écartés, pour restauration éventuelle
-- L'interface d'édition en ligne n'est pas activée : les modifications passent par Claude.

-- 2026-11-08 : migration illustrations (appliquée) : tables illustration et concept_illustration ;
-- 14 schémas du diaporama, fichiers dans /schemas (webp), rattachés aux concepts pertinents (principal = schéma de référence)
