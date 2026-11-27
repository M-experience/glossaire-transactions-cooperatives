-- 27 novembre 2026 : « Les trois modes de coordination dans la STC » (M. Zacklad).
-- Remplace les dimensions de la coordination (épistémique, relationnelle, spatio-temporelle).

-- 1. Familles
insert into famille (slug, libelle, description, ordre) values
 ('mode-coordination', 'Modes de coordination', 'Trois modes de coordination, chacun avec une dominante ontologique : le milieu, les selfs, les artefacts médiateurs', 15),
 ('forme-coordination', 'Formes de coordination', 'Trois formes par mode, qui ne s''excluent pas : une même situation les combine en proportions variables', 16),
 ('gradient-autorite', 'Gradient d''autorité', 'Variable transversale aux formes de coordination relationnelle : distribution de l''autorité entre les rôles', 17),
 ('dispositif-conversationnel', 'Dispositif conversationnel', 'Dispositif qui cadre les conversations, en position de tiers médiateur ; une composante par mode de coordination', 18)
on conflict (slug) do update set libelle = excluded.libelle, description = excluded.description, ordre = excluded.ordre;
update famille set ordre = 19 where slug = 'dispositif';
update famille set ordre = 20 where slug = 'configuration';

-- 2. Les anciennes dimensions deviennent les modes (même fiche, nouveau nom)
update concept set slug = 'coordination-par-l-acces' where slug = 'coordination-spatio-temporelle';
update concept set slug = 'coordination-interpretative' where slug = 'coordination-epistemique';

-- 3. Relations obsolètes
delete from relation r using concept a
 where r.source_id = a.id and a.slug in ('coordination-par-l-acces', 'coordination-relationnelle', 'coordination-interpretative');
delete from relation r using concept a, concept b
 where r.source_id = a.id and r.cible_id = b.id and b.slug = 'coordination' and r.type_slug = 'sous_type_de'
   and a.slug in ('synchrone-en-presence', 'synchrone-a-distance', 'asynchrone');

-- 4. Concepts
with c(slug, libelle, famille, resume, ordre) as (values
 ('coordination', 'Coordination', 'pole-praxeologique', 'Règle les conditions dans lesquelles les partenaires conduisent ensemble leurs conversations : qui accède à qui et à quoi, qui occupe quelle position, comment chacun lit la situation et les artefacts en jeu. Trois modes : par l''accès spatio-temporel, relationnelle, interprétative.', 75),
 ('coordination-par-l-acces', 'Coordination par l''accès spatio-temporel', 'mode-coordination', 'Distribue les conversations dans l''espace et dans le temps, selon l''accès des participants les uns aux autres et aux artefacts. Dominante : le milieu (territorialisation). Critère des formes : le partage du lieu et du temps.', 80),
 ('coordination-relationnelle', 'Coordination relationnelle', 'mode-coordination', 'Accorde les partenaires sur leurs positions et leurs rôles réciproques (prise de rôle au sens de Mead, attentes mutuelles, qui fait quoi et pour qui). Dominante : les selfs (subjectivation). Critère des formes : qui peut tenir le rôle.', 81),
 ('coordination-interpretative', 'Coordination interprétative', 'mode-coordination', 'Accorde les partenaires sur la lecture de la situation et des artefacts médiateurs qui orientent la réalisation de l''œuvre : procédures (ex ante) et résultats intermédiaires (en cours de réalisation). Dominante : les artefacts médiateurs. Ses formes suivent les trois registres de la sémiose cognitive.', 82),
 ('synchrone-en-presence', 'Synchrone en présence', 'forme-coordination', 'Les partenaires partagent le même lieu et le même temps, en face à face ou en réunion. Les artefacts y sont pour l''essentiel incorporés et la ritualisation tient lieu de documentarisation.', 83),
 ('synchrone-a-distance', 'Synchrone à distance', 'forme-coordination', 'Les partenaires partagent le même temps sans partager le lieu : téléphone, visiophonie, direct.', 84),
 ('asynchrone', 'Asynchrone', 'forme-coordination', 'L''échange est différé par des artefacts sur supports pérennes (textes, documents, messages, archives), qui permettent la distribution spatio-temporelle des contributions.', 85),
 ('coordination-interpersonnelle', 'Coordination interpersonnelle', 'forme-coordination', 'Le rôle s''ajuste à la personne singulière de l''autre, irremplaçable, qui tient lieu d''autrui significatif ; l''affect domine. Exemples : couple, amitiés intimes, parent et enfant, collègues proches.', 86),
 ('coordination-affiliative', 'Coordination affiliative', 'forme-coordination', 'Le rôle découle de la place occupée dans un collectif : seul un membre reconnu peut le tenir, les occupants sont remplaçables. Comprend le rang accordé par les membres, fondé sur l''estime sociale (Honneth). Exemples : équipe, groupe de pairs, association, communauté de pratique.', 87),
 ('coordination-positionnelle', 'Coordination positionnelle', 'forme-coordination', 'Le rôle est une position préétablie, découpée par un tiers en vertu de l''autorité du droit, du sacré ou de l''œuvre ; les occupants sont interchangeables et n''ont pas besoin de se connaître. Exemples : client et fournisseur, usager et agent, fidèle et officiant, public et artiste.', 88),
 ('conscience-mutuelle', 'Conscience mutuelle', 'forme-coordination', 'Les partenaires lisent ensemble la situation par les signaux, les regards, le rythme et la perception de l''état de l''action (awareness de la tradition CSCW). Registre de la raison sensible.', 89),
 ('typification', 'Typification', 'forme-coordination', 'Les partenaires partagent des types, des genres et des scripts (routines, check-lists, livrables attendus) et savent « ce qui se fait » à chaque étape. Registre de la raison pratique.', 90),
 ('conceptualisation', 'Conceptualisation', 'forme-coordination', 'Les partenaires s''accordent sur des modèles, des méthodes, des spécifications et des catégories, mais aussi sur des récits et des cadres d''interprétation. Registre de la raison conceptuelle.', 91),
 ('gradient-autorite', 'Gradient d''autorité', 'gradient-autorite', 'Variable transversale aux trois formes de coordination relationnelle : distribution de l''autorité entre les rôles (qui peut prescrire, décider ou trancher). Trois repères : hiérarchie, hétérarchie, parité. L''autorité y est un axe qui traverse les formes, et non une forme parmi d''autres (à la différence de Fiske).', 92),
 ('hierarchie', 'Hiérarchie', 'gradient-autorite', 'Asymétrie d''autorité stable et attachée aux rôles, comme pour le supérieur en vertu du contrat ou l''officiant.', 93),
 ('heterarchie', 'Hétérarchie', 'gradient-autorite', 'Autorité distribuée, qui passe d''un partenaire à l''autre selon la situation et les compétences, comme dans une équipe projet ou une séance de design collaboratif.', 94),
 ('parite', 'Parité', 'gradient-autorite', 'Aucun partenaire n''a d''autorité sur les autres ; les décisions se prennent par accord, comme dans un groupe d''amis ou un collectif autogéré.', 95),
 ('dispositif-conversationnel', 'Dispositif conversationnel', 'dispositif-conversationnel', 'Coordination stabilisée qui encadre les conversations à venir, en position de tiers médiateur : qui peut se joindre, quand et par quel canal, qui tient quel rôle, ce qui doit être lu et comment. Trois composantes : dispositif d''accès, relationnel, interprétatif.', 96),
 ('dispositif-acces', 'Dispositif d''accès', 'dispositif-conversationnel', 'Équipe la coordination par l''accès spatio-temporel : lieux et salles, agendas et plannings, outils de visiophonie, messageries, plateformes et espaces documentaires.', 97),
 ('dispositif-relationnel', 'Dispositif relationnel', 'dispositif-conversationnel', 'Équipe la coordination relationnelle : organigrammes et fiches de poste, contrats, statuts et délégations, mais aussi rôles tournants et règles d''appartenance d''un collectif.', 98),
 ('dispositif-interpretatif', 'Dispositif interprétatif', 'dispositif-conversationnel', 'Équipe la coordination interprétative : procédures, référentiels, spécifications, tableaux de bord, maquettes et prototypes, qui orientent la lecture commune de la situation et de l''œuvre.', 99),
 ('communication-coordinatrice', 'Communication coordinatrice', 'notion', 'Gestes de coordination dans les conversations : proposer un rendez-vous, donner la parole, répartir une tâche, rappeler une procédure, signaler l''état d''un travail.', 23),
 ('communication-cooperante', 'Communication coopérante', 'notion', 'Communication qui oriente les contributions vers la production de valeur, à côté de la communication coordinatrice et de la communication organisante.', 24),
 ('communication-organisante', 'Communication organisante', 'notion', 'Communication qui explicite et stabilise les configurations institutionnelles, à côté de la communication coopérante et de la communication coordinatrice.', 25)
)
insert into concept (slug, libelle, famille_slug, resume, statut, ordre)
select slug, libelle, famille, resume, 'stabilisé', ordre from c
on conflict (slug) do update set libelle = excluded.libelle, famille_slug = excluded.famille_slug, resume = excluded.resume, statut = excluded.statut, ordre = excluded.ordre;

delete from famille where slug = 'dimension-coordination' and not exists (select 1 from concept where famille_slug = 'dimension-coordination');

-- 5. Relations
with r(s, t, c, com, o) as (values
 ('coordination-par-l-acces', 'sous_type_de', 'coordination', null, 1),
 ('coordination-relationnelle', 'sous_type_de', 'coordination', null, 2),
 ('coordination-interpretative', 'sous_type_de', 'coordination', null, 3),
 ('synchrone-en-presence', 'sous_type_de', 'coordination-par-l-acces', null, 1),
 ('synchrone-a-distance', 'sous_type_de', 'coordination-par-l-acces', null, 2),
 ('asynchrone', 'sous_type_de', 'coordination-par-l-acces', null, 3),
 ('coordination-interpersonnelle', 'sous_type_de', 'coordination-relationnelle', null, 1),
 ('coordination-affiliative', 'sous_type_de', 'coordination-relationnelle', null, 2),
 ('coordination-positionnelle', 'sous_type_de', 'coordination-relationnelle', null, 3),
 ('conscience-mutuelle', 'sous_type_de', 'coordination-interpretative', null, 1),
 ('typification', 'sous_type_de', 'coordination-interpretative', null, 2),
 ('conceptualisation', 'sous_type_de', 'coordination-interpretative', null, 3),
 ('coordination-par-l-acces', 'correspond_a', 'milieu', 'dominante ontologique, sans exclusivité', 1),
 ('coordination-par-l-acces', 'correspond_a', 'territorialisation', 'les dispositifs qui l''équipent relèvent de la territorialisation', 2),
 ('coordination-par-l-acces', 'mobilise', 'dispositif-info-com', null, 3),
 ('coordination-relationnelle', 'correspond_a', 'self', 'dominante ontologique, sans exclusivité', 1),
 ('coordination-relationnelle', 'correspond_a', 'subjectivation', null, 2),
 ('coordination-interpretative', 'correspond_a', 'artefact-mediateur', 'dominante ontologique ; les artefacts coordonnent parce qu''ils sont interprétés', 1),
 ('conscience-mutuelle', 'correspond_a', 'raison-sensible', null, 1),
 ('typification', 'correspond_a', 'raison-pratique', null, 1),
 ('conceptualisation', 'correspond_a', 'raison-conceptuelle', null, 1),
 ('coordination-interpersonnelle', 'correspond_a', 'configuration-primaire', 'affinité, sans identité', 1),
 ('coordination-affiliative', 'correspond_a', 'configuration-secondaire', 'affinité, sans identité', 1),
 ('coordination-positionnelle', 'correspond_a', 'configuration-tertiaire', 'affinité, sans identité', 1),
 ('coordination-positionnelle', 'releve_de', 'ordre-symbolique', 'position découpée par un tiers en vertu de l''autorité du droit, du sacré ou de l''œuvre', 2),
 ('hierarchie', 'pole_de', 'gradient-autorite', null, 1),
 ('heterarchie', 'pole_de', 'gradient-autorite', 'repère intermédiaire', 2),
 ('parite', 'pole_de', 'gradient-autorite', null, 3),
 ('hierarchie', 'oppose_a', 'parite', null, 1),
 ('gradient-autorite', 'caracterise', 'coordination-relationnelle', 'variable transversale qui croise les trois formes relationnelles', 1),
 ('dispositif-conversationnel', 'face_de', 'coordination', 'la coordination qui cadre les conversations (approche dispositive)', 1),
 ('communication-coordinatrice', 'face_de', 'coordination', 'les gestes de coordination dans les conversations', 2),
 ('dispositif-acces', 'composante_de', 'dispositif-conversationnel', null, 1),
 ('dispositif-relationnel', 'composante_de', 'dispositif-conversationnel', null, 2),
 ('dispositif-interpretatif', 'composante_de', 'dispositif-conversationnel', null, 3),
 ('coordination-par-l-acces', 'mobilise', 'dispositif-acces', 'fonction de cadrage', 4),
 ('coordination-relationnelle', 'mobilise', 'dispositif-relationnel', 'fonction de cadrage', 3),
 ('coordination-interpretative', 'mobilise', 'dispositif-interpretatif', 'fonction de cadrage', 2),
 ('dispositif-acces', 'mobilise', 'dispositif-info-com', null, 1),
 ('communication-coordinatrice', 'sous_type_de', 'communication', null, 1),
 ('communication-cooperante', 'sous_type_de', 'communication', null, 2),
 ('communication-organisante', 'sous_type_de', 'communication', null, 3),
 ('communication-cooperante', 'correspond_a', 'cooperation', null, 1),
 ('communication-organisante', 'correspond_a', 'organisation', null, 1),
 ('coordination', 'distingue_de', 'cooperation', 'la coopération oriente les contributions vers la production de valeur', 1),
 ('coordination', 'distingue_de', 'organisation', 'l''organisation explicite et stabilise les configurations institutionnelles qui légitiment l''agencement ; la légitimité d''une procédure relève de l''organisation', 2)
)
insert into relation (source_id, cible_id, type_slug, commentaire, ordre)
select a.id, b.id, r.t, r.com, r.o from r join concept a on a.slug = r.s join concept b on b.slug = r.c
where not exists (select 1 from relation x where x.source_id = a.id and x.cible_id = b.id and x.type_slug = r.t);
