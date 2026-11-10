-- Généré par generer_configurations.py : configurations institutionnelles (tableau v4 de M. Zacklad, 10 novembre 2026). Statut provisoire.
insert into famille (slug, libelle, description, ordre) values ('configuration', 'Configurations institutionnelles', 'Types idéaux des configurations institutionnelles de l''action collective', 18) on conflict (slug) do update set libelle = excluded.libelle, description = excluded.description, ordre = excluded.ordre;
with c(slug, libelle, resume, ordre) as (values
 ('configuration-institutionnelle', 'Configuration institutionnelle', 'Mode d''inscription des selfs dans l''action collective, décrit en types idéaux selon la valeur dominante, la nature du lien constituant les selfs, l''environnement et la coordination, les artefacts générés et la temporalité dominante. Trois grandes familles : primaires, secondaires et tertiaires.', 1),
 ('configuration-primaire', 'Configuration institutionnelle primaire', 'Se caractérise par l''inscription des selfs dans leur continuité biographique et leur reproduction biologique. Le self y est engagé en totalité, dans sa singularité irréductible. Elle se répartit en configurations domestiques (conjugales, familiales) et électives (amitiés intimes).', 2),
 ('configuration-domestique', 'Configuration domestique', 'Configuration primaire, conjugale ou familiale.', 3),
 ('configuration-elective', 'Configuration élective', 'Configuration primaire des amitiés intimes.', 4),
 ('configuration-secondaire', 'Configuration institutionnelle secondaire', 'Se caractérise par l''appartenance du self à un collectif institué visant des finalités spécifiques. Elle se déploie sur deux versants : de sociabilité, et administratif et gestionnaire.', 5),
 ('configuration-de-sociabilite', 'Configuration de sociabilité', 'Versant de sociabilité des configurations secondaires : foules et rassemblements, amicales et réticulaires, groupales, communautaires informelles, communautaires formelles.', 6),
 ('configuration-administrative-gestionnaire', 'Configuration administrative et gestionnaire', 'Versant administratif et gestionnaire des configurations secondaires : publiques, de l''économie sociale, entrepreneuriales.', 7),
 ('configuration-tertiaire', 'Configuration institutionnelle tertiaire', 'Se caractérise par l''inscription des selfs dans un ordre symbolique relevant du droit, du sacré ou de l''œuvre d''art. Sous-familles : civiques et marchandes-contractuelles, fondées sur l''autorité du droit ; cultuelles-culturelles, qui relèvent de l''autorité du sacré (religieuses) ou de l''œuvre d''art (culturelles).', 8),
 ('configuration-civique', 'Configuration civique', 'Configuration tertiaire fondée sur l''autorité du droit : citoyenne, juridico-administrative, participative.', 9),
 ('configuration-marchande-contractuelle', 'Configuration marchande-contractuelle', 'Configuration tertiaire fondée sur l''autorité du droit : client-fournisseur, usager-prestataire.', 10),
 ('configuration-cultuelle-culturelle', 'Configuration cultuelle-culturelle', 'Configuration tertiaire qui relève de l''autorité du sacré (religieuse) ou de l''œuvre d''art (culturelle).', 11),
 ('ordre-symbolique', 'Ordre symbolique', 'Ordre dans lequel les configurations tertiaires inscrivent les selfs ; il relève de l''autorité du droit, du sacré ou de l''œuvre d''art.', 12),
 ('autorite-du-droit', 'Autorité du droit', 'Fonde les configurations civiques et marchandes-contractuelles.', 13),
 ('autorite-du-sacre', 'Autorité du sacré', 'Fonde les configurations religieuses.', 14),
 ('autorite-de-l-oeuvre-d-art', 'Autorité de l''œuvre d''art', 'Fonde les configurations culturelles (artistiques).', 15),
 ('configuration-conjugale', 'Configuration conjugale', 'Alliance élective qui institue les partenaires comme couple ; chacun se constitue comme conjoint par et pour l''autre.', 16),
 ('configuration-familiale', 'Configuration familiale', 'Filiation et parenté qui inscrivent le sujet dans une lignée ; les selfs deviennent fils/fille, parent, frère/sœur avant tout choix personnel.', 17),
 ('amitie-intime', 'Amitié intime', 'Élection réciproque et durable ; les selfs se reconnaissent mutuellement dans leur singularité, hors des rôles institués.', 18),
 ('foules-et-rassemblements', 'Foules et rassemblements', 'Coprésence sans lien préalable ; les selfs individuels s''effacent temporairement dans un « nous » situationnel indifférencié.', 19),
 ('configuration-amicale-reticulaire', 'Configuration amicale et réticulaire', 'Liens électifs faibles à moyens ; les selfs se déploient en nœuds multi-facettés d''un réseau de connaissances.', 20),
 ('configuration-groupale', 'Configuration groupale', 'Appartenance à un petit collectif structuré ; chaque self endosse un rôle contributif dans une équipe qui l''attend et le complète.', 21),
 ('configuration-communautaire-informelle', 'Configuration communautaire informelle', 'Participation à une pratique partagée ; les selfs se transforment en praticiens légitimes selon une trajectoire du périphérique au central.', 22),
 ('configuration-communautaire-formelle', 'Configuration communautaire formelle', 'Admission qui fait accéder au statut de membre à part entière ; les selfs se distinguent des non-membres par une identité collective portée par le statut.', 23),
 ('configuration-publique', 'Configuration publique', 'Statut de la fonction publique ; les selfs entrent dans un corps et un grade qui les identifient comme agents, fonctionnaires, cadres A/B/C.', 24),
 ('configuration-economie-sociale', 'Configuration de l''économie sociale', 'Adhésion à un projet et gouvernance partagée ; les selfs prennent qualité de membres, sociétaires ou administrateurs engagés.', 25),
 ('configuration-entrepreneuriale', 'Configuration entrepreneuriale', 'Contrat de travail ou d''association ; les selfs deviennent salariés, associés, cadres ou dirigeants selon une identité professionnelle instituée.', 26),
 ('configuration-citoyenne', 'Configuration citoyenne', 'Citoyenneté ; les selfs sont institués comme membres du corps politique et porteurs d''une identité nationale ou supranationale.', 27),
 ('configuration-juridico-administrative', 'Configuration juridico-administrative', 'Assujettissement au droit ; les selfs deviennent administrés, sujets de droits et d''obligations face à la puissance publique.', 28),
 ('configuration-participative', 'Configuration participative', 'Participation à la décision publique ; les selfs deviennent citoyens actifs, délibérants, contributifs.', 29),
 ('configuration-client-fournisseur', 'Configuration client-fournisseur', 'Contrat marchand qui constitue les selfs comme acheteur et vendeur ; identités transitoires liées à la transaction.', 30),
 ('configuration-usager-prestataire', 'Configuration usager-prestataire', 'Rôle d''usager institué hors régime marchand ; les selfs sont institués destinataires d''une prestation dont ils attendent un service dû.', 31),
 ('configuration-religieuse', 'Configuration religieuse', 'Foi ou pratique adressée à une transcendance ; les selfs deviennent fidèles, croyants, pratiquants, disciples et portent une identité spirituelle.', 32),
 ('configuration-culturelle', 'Configuration culturelle', 'Rapport à l''œuvre ou à la figure ; les selfs deviennent lecteurs, spectateurs, fans, avec des identités de récepteurs plus ou moins durables.', 33)
) insert into concept (slug, libelle, famille_slug, resume, statut, ordre) select slug, libelle, 'configuration', resume, 'provisoire', ordre from c on conflict (slug) do update set libelle = excluded.libelle, famille_slug = excluded.famille_slug, resume = excluded.resume, ordre = excluded.ordre;
with r(s, t, c, com, o) as (values
 ('configuration-primaire', 'sous_type_de', 'configuration-institutionnelle', null, 0),
 ('configuration-domestique', 'sous_type_de', 'configuration-primaire', null, 1),
 ('configuration-elective', 'sous_type_de', 'configuration-primaire', null, 2),
 ('configuration-secondaire', 'sous_type_de', 'configuration-institutionnelle', null, 3),
 ('configuration-de-sociabilite', 'face_de', 'configuration-secondaire', null, 4),
 ('configuration-administrative-gestionnaire', 'face_de', 'configuration-secondaire', null, 5),
 ('configuration-tertiaire', 'sous_type_de', 'configuration-institutionnelle', null, 6),
 ('configuration-civique', 'sous_type_de', 'configuration-tertiaire', null, 7),
 ('configuration-marchande-contractuelle', 'sous_type_de', 'configuration-tertiaire', null, 8),
 ('configuration-cultuelle-culturelle', 'sous_type_de', 'configuration-tertiaire', null, 9),
 ('autorite-du-droit', 'composante_de', 'ordre-symbolique', null, 10),
 ('autorite-du-sacre', 'composante_de', 'ordre-symbolique', null, 11),
 ('autorite-de-l-oeuvre-d-art', 'composante_de', 'ordre-symbolique', null, 12),
 ('configuration-conjugale', 'sous_type_de', 'configuration-domestique', null, 13),
 ('configuration-familiale', 'sous_type_de', 'configuration-domestique', null, 14),
 ('amitie-intime', 'sous_type_de', 'configuration-elective', null, 15),
 ('foules-et-rassemblements', 'sous_type_de', 'configuration-de-sociabilite', null, 16),
 ('configuration-amicale-reticulaire', 'sous_type_de', 'configuration-de-sociabilite', null, 17),
 ('configuration-groupale', 'sous_type_de', 'configuration-de-sociabilite', null, 18),
 ('configuration-communautaire-informelle', 'sous_type_de', 'configuration-de-sociabilite', null, 19),
 ('configuration-communautaire-formelle', 'sous_type_de', 'configuration-de-sociabilite', null, 20),
 ('configuration-publique', 'sous_type_de', 'configuration-administrative-gestionnaire', null, 21),
 ('configuration-economie-sociale', 'sous_type_de', 'configuration-administrative-gestionnaire', null, 22),
 ('configuration-entrepreneuriale', 'sous_type_de', 'configuration-administrative-gestionnaire', null, 23),
 ('configuration-citoyenne', 'sous_type_de', 'configuration-civique', null, 24),
 ('configuration-juridico-administrative', 'sous_type_de', 'configuration-civique', null, 25),
 ('configuration-participative', 'sous_type_de', 'configuration-civique', null, 26),
 ('configuration-client-fournisseur', 'sous_type_de', 'configuration-marchande-contractuelle', null, 27),
 ('configuration-usager-prestataire', 'sous_type_de', 'configuration-marchande-contractuelle', null, 28),
 ('configuration-religieuse', 'sous_type_de', 'configuration-cultuelle-culturelle', null, 29),
 ('configuration-culturelle', 'sous_type_de', 'configuration-cultuelle-culturelle', null, 30),
 ('ordre-symbolique', 'caracterise', 'configuration-tertiaire', null, 31),
 ('configuration-civique', 'releve_de', 'autorite-du-droit', null, 32),
 ('configuration-marchande-contractuelle', 'releve_de', 'autorite-du-droit', null, 33),
 ('configuration-religieuse', 'releve_de', 'autorite-du-sacre', null, 34),
 ('configuration-culturelle', 'releve_de', 'autorite-de-l-oeuvre-d-art', null, 35),
 ('configuration-communautaire-informelle', 'oppose_a', 'configuration-communautaire-formelle', null, 36),
 ('self', 'intervient_dans', 'configuration-institutionnelle', 'les configurations se distinguent par la nature du lien qui constitue les selfs', 37),
 ('configuration-institutionnelle', 'intervient_dans', 'organisation', 'l''organisation explicite et stabilise les configurations institutionnelles qui légitiment l''agencement', 38),
 ('configuration-publique', 'distingue_de', 'configuration-juridico-administrative', 'relations internes à l''administration (secondaire) et assujettissement des administrés au droit (tertiaire)', 39),
 ('configuration-entrepreneuriale', 'distingue_de', 'configuration-marchande-contractuelle', 'collectif institué (secondaire) et relation contractuelle fondée sur le droit (tertiaire)', 40)
) insert into relation (source_id, cible_id, type_slug, commentaire, ordre) select a.id, b.id, r.t, r.com, r.o from r join concept a on a.slug = r.s join concept b on b.slug = r.c where not exists (select 1 from relation x where x.source_id = a.id and x.cible_id = b.id and x.type_slug = r.t);
with v(s, a, x, o) as (values
 ('configuration-conjugale', 'exemples', 'Mariage, PACS, concubinage, union libre', 0),
 ('configuration-conjugale', 'valeur', 'Réciprocité affective, intimité partagée', 1),
 ('configuration-conjugale', 'lien', 'Alliance élective qui institue les partenaires comme couple ; chacun se constitue comme conjoint par et pour l''autre', 2),
 ('configuration-conjugale', 'environnement', 'Foyer, espace domestique ; coordination par négociation quotidienne, routines et division des tâches', 3),
 ('configuration-conjugale', 'artefacts', 'Constitutifs : alliance, contrat de mariage ou PACS, foyer commun
Générés incorporés : gestes de tendresse, routines domestiques partagées, langue et code privés du couple
Générés autonomes : patrimoine commun, photos et récits, correspondances', 4),
 ('configuration-conjugale', 'temporalite', 'Biographique, durée de l''union', 5),
 ('configuration-familiale', 'exemples', 'Famille nucléaire, élargie, recomposée ; fratries, ascendants, descendants', 0),
 ('configuration-familiale', 'valeur', 'Care, transmission, filiation', 1),
 ('configuration-familiale', 'lien', 'Filiation et parenté qui inscrivent le sujet dans une lignée ; les selfs deviennent fils/fille, parent, frère/sœur avant tout choix personnel', 2),
 ('configuration-familiale', 'environnement', 'Foyer d''origine et réseau parental ; coordination par autorité générationnelle, obligations tacites, événements familiaux', 3),
 ('configuration-familiale', 'artefacts', 'Constitutifs : livret de famille, maison familiale, repas rituels
Générés incorporés : gestes de care, manières de table, tours de main transmis
Générés autonomes : patrimoine et héritage, arbre généalogique, albums de famille', 4),
 ('configuration-familiale', 'temporalite', 'Multigénérationnelle, vie entière', 5),
 ('amitie-intime', 'exemples', 'Amis proches d''une vie, confidents, compagnons de route', 0),
 ('amitie-intime', 'valeur', 'Confiance inconditionnelle, reconnaissance mutuelle', 1),
 ('amitie-intime', 'lien', 'Élection réciproque et durable ; les selfs se reconnaissent mutuellement dans leur singularité, hors des rôles institués', 2),
 ('amitie-intime', 'environnement', 'Espaces partagés variables (domicile, cafés, voyages) ; coordination par disponibilité mutuelle, rythmes personnels', 3),
 ('amitie-intime', 'artefacts', 'Constitutifs : rituels d''amitié, disponibilité mutuelle, occasions de retrouvailles
Générés incorporés : gestes de la confidence, façons d''être ensemble, complicités gestuelles
Générés autonomes : correspondances, cadeaux et souvenirs partagés, photos communes', 4),
 ('amitie-intime', 'temporalite', 'Biographique, durable sans obligation de continuité', 5),
 ('foules-et-rassemblements', 'exemples', 'Manifestations, publics d''événements, foules de circulation, attroupements, mobilisations éphémères', 0),
 ('foules-et-rassemblements', 'valeur', 'Attention partagée, effervescence collective', 1),
 ('foules-et-rassemblements', 'lien', 'Coprésence sans lien préalable ; les selfs individuels s''effacent temporairement dans un « nous » situationnel indifférencié', 2),
 ('foules-et-rassemblements', 'environnement', 'Espace public, lieu d''événement ; coordination par foyer attentionnel commun, contagion émotionnelle, dispositifs d''encadrement', 3),
 ('foules-et-rassemblements', 'artefacts', 'Constitutifs : lieu d''événement, signalétique, dispositifs d''encadrement
Générés incorporés : gestes collectifs (applaudir, scander, marcher en cortège), postures partagées
Générés autonomes : banderoles et pancartes, captations vidéo, hashtags, images d''archive', 4),
 ('foules-et-rassemblements', 'temporalite', 'Brève, indexée sur la situation', 5),
 ('configuration-amicale-reticulaire', 'exemples', 'Cercles d''amis, camaraderies, carnets d''adresses, réseaux personnels, réseaux socio-numériques', 0),
 ('configuration-amicale-reticulaire', 'valeur', 'Sociabilité affinitaire, entretien du lien', 1),
 ('configuration-amicale-reticulaire', 'lien', 'Liens électifs faibles à moyens ; les selfs se déploient en nœuds multi-facettés d''un réseau de connaissances', 2),
 ('configuration-amicale-reticulaire', 'environnement', 'Sociabilités multi-situées, plateformes numériques ; coordination par entretien du lien, intermédiations, recommandations', 3),
 ('configuration-amicale-reticulaire', 'artefacts', 'Constitutifs : plateformes, moyens de communication, occasions de sociabilité
Générés incorporés : arts de l''entretien du lien, savoir-faire de recommandation, gestes d''attention
Générés autonomes : carnets d''adresses, profils numériques, correspondances archivées', 4),
 ('configuration-amicale-reticulaire', 'temporalite', 'Intermittente, ponctuelle, latente', 5),
 ('configuration-groupale', 'exemples', 'Équipes de travail, ateliers, groupes de pairs, collectifs de projet', 0),
 ('configuration-groupale', 'valeur', 'Coopération, action conjointe', 1),
 ('configuration-groupale', 'lien', 'Appartenance à un petit collectif structuré ; chaque self endosse un rôle contributif dans une équipe qui l''attend et le complète', 2),
 ('configuration-groupale', 'environnement', 'Lieu de travail commun ou espace de projet ; coordination par répartition des rôles, réunions, ajustement mutuel', 3),
 ('configuration-groupale', 'artefacts', 'Constitutifs : règles du jeu, plannings, outils partagés
Générés incorporés : savoir-faire coopératifs, ajustements mutuels, gestes coordonnés
Générés autonomes : livrables communs (documents, prototypes, produits), comptes rendus', 4),
 ('configuration-groupale', 'temporalite', 'Durée du projet ou de l''activité commune', 5),
 ('configuration-communautaire-informelle', 'exemples', 'Communautés de pratique, collectifs émergents, scènes culturelles', 0),
 ('configuration-communautaire-informelle', 'valeur', 'Apprentissage situé, reconnaissance par les pairs', 1),
 ('configuration-communautaire-informelle', 'lien', 'Participation à une pratique partagée ; les selfs se transforment en praticiens légitimes selon une trajectoire du périphérique au central', 2),
 ('configuration-communautaire-informelle', 'environnement', 'Espaces de la pratique (physiques ou numériques) ; coordination par imitation, mentorat informel, circulation du répertoire', 3),
 ('configuration-communautaire-informelle', 'artefacts', 'Constitutifs : espaces d''échange, répertoire partagé, mentorat informel
Générés incorporés : tours de main, savoir-faire du métier, gestes techniques transmis, énoncés du jargon en situation
Générés autonomes : traces de travail, forums et fils de discussion, artefacts emblématiques', 4),
 ('configuration-communautaire-informelle', 'temporalite', 'Durée de la pratique partagée, trajectoire de participation', 5),
 ('configuration-communautaire-formelle', 'exemples', 'Clubs, ordres, confréries, sociétés savantes, loges', 0),
 ('configuration-communautaire-formelle', 'valeur', 'Reconnaissance entre pairs, appartenance instituée', 1),
 ('configuration-communautaire-formelle', 'lien', 'Admission qui fait accéder au statut de membre à part entière ; les selfs se distinguent des non-membres par une identité collective portée par le statut', 2),
 ('configuration-communautaire-formelle', 'environnement', 'Locaux propres, événements réservés ; coordination par règlement, conseil, cotisations, procédure d''admission', 3),
 ('configuration-communautaire-formelle', 'artefacts', 'Constitutifs : statuts et règlement intérieur, locaux, cotisations
Générés incorporés : gestes rituels d''appartenance, port des insignes, manières distinctives
Générés autonomes : insignes et blasons, annuaires, registres, archives', 4),
 ('configuration-communautaire-formelle', 'temporalite', 'Durée de la qualité de membre, renouvelable', 5),
 ('configuration-publique', 'exemples', 'Administrations d''État, collectivités, opérateurs publics ; relations internes', 0),
 ('configuration-publique', 'valeur', 'Service public, continuité et neutralité', 1),
 ('configuration-publique', 'lien', 'Statut de la fonction publique ; les selfs entrent dans un corps et un grade qui les identifient comme agents, fonctionnaires, cadres A/B/C', 2),
 ('configuration-publique', 'environnement', 'Ministères, collectivités, opérateurs ; coordination par hiérarchie administrative, tutelle, procédures, statut', 3),
 ('configuration-publique', 'artefacts', 'Constitutifs : statut de la fonction publique, hiérarchie administrative, circulaires
Générés incorporés : gestes de l''expertise administrative, routines procédurales, formulations réglementaires
Générés autonomes : actes administratifs, dossiers instruits, rapports et notes', 4),
 ('configuration-publique', 'temporalite', 'Carrière statutaire, longue durée', 5),
 ('configuration-economie-sociale', 'exemples', 'Associations loi 1901, coopératives, mutuelles, fondations, structures ESS', 0),
 ('configuration-economie-sociale', 'valeur', 'Projet collectif, gouvernance démocratique', 1),
 ('configuration-economie-sociale', 'lien', 'Adhésion à un projet et gouvernance partagée ; les selfs prennent qualité de membres, sociétaires ou administrateurs engagés', 2),
 ('configuration-economie-sociale', 'environnement', 'Locaux associatifs ou coopératifs ; coordination par assemblée générale, projet associatif, engagement bénévole ou salarié', 3),
 ('configuration-economie-sociale', 'artefacts', 'Constitutifs : statuts, projet associatif, assemblées générales
Générés incorporés : gestes d''engagement, savoir-faire bénévoles, prises de parole en AG
Générés autonomes : services rendus, procès-verbaux d''AG, bilans d''activité', 4),
 ('configuration-economie-sociale', 'temporalite', 'Durée de l''engagement, mandats renouvelables', 5),
 ('configuration-entrepreneuriale', 'exemples', 'Entreprises, sociétés, relation salariale, partenariats productifs', 0),
 ('configuration-entrepreneuriale', 'valeur', 'Production de valeur économique, performance', 1),
 ('configuration-entrepreneuriale', 'lien', 'Contrat de travail ou d''association ; les selfs deviennent salariés, associés, cadres ou dirigeants selon une identité professionnelle instituée', 2),
 ('configuration-entrepreneuriale', 'environnement', 'Lieu de travail, marché ; coordination par hiérarchie, processus, division du travail, indicateurs de performance', 3),
 ('configuration-entrepreneuriale', 'artefacts', 'Constitutifs : contrat de travail, organigramme, outils de gestion
Générés incorporés : compétences professionnelles, gestes de métier, routines de travail
Générés autonomes : produits et prestations, comptabilité et bilans, marque et propriété intellectuelle', 4),
 ('configuration-entrepreneuriale', 'temporalite', 'Durée du contrat ou de l''association', 5),
 ('configuration-citoyenne', 'exemples', 'Droits et devoirs civiques, participation électorale, appartenance nationale', 0),
 ('configuration-citoyenne', 'valeur', 'Souveraineté populaire, égalité civique', 1),
 ('configuration-citoyenne', 'lien', 'Citoyenneté ; les selfs sont institués comme membres du corps politique et porteurs d''une identité nationale ou supranationale', 2),
 ('configuration-citoyenne', 'environnement', 'Nation, collectivité, espace public ; coordination par droit constitutionnel, élections, débat public', 3),
 ('configuration-citoyenne', 'artefacts', 'Constitutifs : Constitution, droit électoral, débat public
Générés incorporés : gestes du vote, participation aux débats, prises de position publiques
Générés autonomes : cartes d''identité et passeports, bulletins de vote et résultats, décisions politiques', 4),
 ('configuration-citoyenne', 'temporalite', 'Permanente (vie durant), scandée par les scrutins', 5),
 ('configuration-juridico-administrative', 'exemples', 'Impôt, régulation sectorielle, police administrative, obligations déclaratives', 0),
 ('configuration-juridico-administrative', 'valeur', 'Ordre public, intérêt général, redistribution', 1),
 ('configuration-juridico-administrative', 'lien', 'Assujettissement au droit ; les selfs deviennent administrés, sujets de droits et d''obligations face à la puissance publique', 2),
 ('configuration-juridico-administrative', 'environnement', 'Espaces réglementés, guichets administratifs, portails numériques ; coordination par loi, règlement, contrôle', 3),
 ('configuration-juridico-administrative', 'artefacts', 'Constitutifs : codes et règlements, administrations de contrôle
Générés incorporés : gestes de conformité, remplissage de formulaires, routines déclaratives
Générés autonomes : avis d''imposition, notifications administratives, sanctions et amendes, jurisprudence', 4),
 ('configuration-juridico-administrative', 'temporalite', 'Récurrente selon calendrier légal', 5),
 ('configuration-participative', 'exemples', 'Conseils citoyens, budgets participatifs, conventions citoyennes, référendums locaux', 0),
 ('configuration-participative', 'valeur', 'Délibération, coproduction de la décision publique', 1),
 ('configuration-participative', 'lien', 'Participation à la décision publique ; les selfs deviennent citoyens actifs, délibérants, contributifs', 2),
 ('configuration-participative', 'environnement', 'Espaces de délibération dédiés, plateformes participatives ; coordination par méthodologie de délibération, animation, restitution', 3),
 ('configuration-participative', 'artefacts', 'Constitutifs : dispositifs de délibération, méthodologies de participation, plateformes
Générés incorporés : gestes délibératifs, prises de parole argumentées, animation de groupes
Générés autonomes : comptes rendus délibératifs, rapports de synthèse, décisions restituées', 4),
 ('configuration-participative', 'temporalite', 'Durée du dispositif participatif', 5),
 ('configuration-client-fournisseur', 'exemples', 'Relations B2C, B2B, achats de biens et services, relations commerciales récurrentes', 0),
 ('configuration-client-fournisseur', 'valeur', 'Équivalence marchande, satisfaction du client', 1),
 ('configuration-client-fournisseur', 'lien', 'Contrat marchand qui constitue les selfs comme acheteur et vendeur ; identités transitoires liées à la transaction', 2),
 ('configuration-client-fournisseur', 'environnement', 'Marché, points de vente, plateformes de commerce ; coordination par prix, contrat, catalogue, prescription', 3),
 ('configuration-client-fournisseur', 'artefacts', 'Constitutifs : contrats commerciaux, catalogues et CGV, dispositifs de prescription
Générés incorporés : gestes de choix et d''essayage, manipulations d''achat, gestes de consommation courante
Générés autonomes : biens de consommation, factures, avis et notations, monnaie échangée', 4),
 ('configuration-client-fournisseur', 'temporalite', 'Ponctuelle ou récurrente, indexée sur la transaction', 5),
 ('configuration-usager-prestataire', 'exemples', 'Patient/hôpital, étudiant/université, bénéficiaire/structure médico-sociale, usager/service public local', 0),
 ('configuration-usager-prestataire', 'valeur', 'Qualité de service, droits du destinataire', 1),
 ('configuration-usager-prestataire', 'lien', 'Rôle d''usager institué hors régime marchand ; les selfs sont institués destinataires d''une prestation dont ils attendent un service dû', 2),
 ('configuration-usager-prestataire', 'environnement', 'Établissement prestataire, dispositif de service ; coordination par convention de service, dossier d''usager, référentiel qualité', 3),
 ('configuration-usager-prestataire', 'artefacts', 'Constitutifs : convention de service, dossier d''usager, référentiel qualité
Générés incorporés : gestes de recours au service, manipulation du dossier, prises de rendez-vous, formulation de demandes
Générés autonomes : dossiers constitués, prestations effectuées, enquêtes de satisfaction', 4),
 ('configuration-usager-prestataire', 'temporalite', 'Indexée sur la prestation ou le suivi', 5),
 ('configuration-religieuse', 'exemples', 'Église, temple, sangha, tradition spirituelle instituée ou diffuse', 0),
 ('configuration-religieuse', 'valeur', 'Salut, transcendance, communion', 1),
 ('configuration-religieuse', 'lien', 'Foi ou pratique adressée à une transcendance ; les selfs deviennent fidèles, croyants, pratiquants, disciples et portent une identité spirituelle', 2),
 ('configuration-religieuse', 'environnement', 'Lieu de culte, communauté des fidèles ; coordination par liturgie, autorité doctrinale, transmission des textes', 3),
 ('configuration-religieuse', 'artefacts', 'Constitutifs : textes sacrés, lieux de culte, clergé, calendrier liturgique
Générés incorporés : gestes rituels (prière, signe de croix, prosternation), disciplines corporelles, chants
Générés autonomes : rites accomplis, offrandes, ex-voto, patrimoine sacré construit', 4),
 ('configuration-religieuse', 'temporalite', 'Vie durant, scandée par le calendrier liturgique', 5),
 ('configuration-culturelle', 'exemples', 'Lectorat, spectateurs, auditeurs, cinéphiles, mélomanes, amateurs, fandoms', 0),
 ('configuration-culturelle', 'valeur', 'Émotion, admiration, transport', 1),
 ('configuration-culturelle', 'lien', 'Rapport à l''œuvre ou à la figure ; les selfs deviennent lecteurs, spectateurs, fans, avec des identités de récepteurs plus ou moins durables', 2),
 ('configuration-culturelle', 'environnement', 'Institutions culturelles (musée, salle, édition), plateformes, espaces de fandom ; coordination par programmation, critique, communauté d''amateurs', 3),
 ('configuration-culturelle', 'artefacts', 'Constitutifs : institutions culturelles, programmation, critique
Générés incorporés : gestes de la réception (lire, écouter, regarder), émotions rituellement partagées, applaudissements, silences d''écoute
Générés autonomes : productions dérivées de fans, collections, billets et catalogues conservés', 4),
 ('configuration-culturelle', 'temporalite', 'Ponctuelle (réception) ou biographique (passion durable)', 5)
) insert into concept_attribut (concept_id, attribut, valeur, ordre) select c.id, v.a, v.x, v.o from v join concept c on c.slug = v.s on conflict (concept_id, attribut) do update set valeur = excluded.valeur, ordre = excluded.ordre;
