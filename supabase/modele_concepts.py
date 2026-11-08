# Modélisation des concepts du diaporama « Communication et conversation dans la STC »
# Les résumés sont des notes provisoires tirées du diaporama, pas des définitions.

FAMILLES = [
    ("notion", "Notions fondamentales", "Concepts de base de la définition de la communication", 1),
    ("type-geste", "Types de gestes", "Niveau 1 : gestes élémentaires", 2),
    ("artefact", "Artefacts médiateurs", "Types d'artefacts médiateurs selon le parcours", 3),
    ("gradient", "Gradients de l'artefact", "Quatre gradients indépendants pour situer un artefact médiateur", 4),
    ("pole-gradient", "Pôles des gradients", "Pôles opposés de chaque gradient", 5),
    ("forme-conversation", "Formes de conversation", "Formes de conversation selon ce qu'elles visent", 6),
    ("facette", "Facettes de la signification", "Les quatre sémioses transactionnelles", 7),
    ("dimension-performative", "Dimensions performatives", "Ce que la transaction transforme", 8),
    ("raison-cognitive", "Raisons cognitives", "Modalités de la sémiose cognitive", 9),
    ("moment-parcours", "Moments du parcours narratif", "Parcours transactionnel transposé de Greimas", 10),
    ("phase-acte", "Phases de l'acte (Mead)", "Phases de l'acte chez Mead (1938)", 11),
    ("role", "Rôles transactionnels", "Rôles répartis autour du parcours", 12),
    ("pole-praxeologique", "Pôles praxéologiques", "Modalités de l'agir ensemble autour de la conversation", 13),
    ("regime-cooperation", "Régimes de coopération", "Rapport des participants à la valeur produite", 14),
    ("mode-coordination", "Modes de coordination", "Accès spatio-temporel des participants", 15),
    ("dimension-coordination", "Dimensions de la coordination", "Coordination lue selon la facette performative", 16),
    ("dispositif", "Types de dispositifs", "Dispositifs d'information et de communication", 17),
]

# slug, libellé, famille, résumé, statut
CONCEPTS = [
    # Notions
    ("communication", "Communication", "notion", "Former, éprouver et reprendre des artefacts médiateurs par des gestes, au sein d'une conversation. Elle constitue la coopération, la coordination et l'organisation.", "stabilisé"),
    ("communication-axiogene", "Communication axiogène", "notion", "Communication qui engendre de la valeur ; vue par les artefacts, au sens de la mise en commun deweyenne.", "provisoire"),
    ("geste", "Geste", "notion", "Plus petit élément de la communication, matériel ou sémiosique ; il prend sens dans l'instant et en différé.", "stabilisé"),
    ("artefact-mediateur", "Artefact médiateur", "notion", "Partie de l'environnement à laquelle un geste intentionnel donne forme afin de produire un effet sur les sens et d'entrer dans un processus sémiotique.", "stabilisé"),
    ("conversation", "Conversation", "notion", "Séquence de gestes interprétés les uns par les autres, verbaux ou non, synchrones ou asynchrones ; matérielle avant d'être verbale (Mead).", "stabilisé"),
    ("interaction", "Interaction", "notion", "Met en rapport des termes qui restent inchangés (Dewey et Bentley).", "stabilisé"),
    ("transaction", "Transaction", "notion", "Transforme les termes dans la relation (Dewey et Bentley).", "stabilisé"),
    ("intensite-transactionnelle", "Intensité transactionnelle", "notion", "Degré de transformation effective des termes d'une conversation ; varie dans chaque forme de conversation. Critères de variation à préciser.", "en discussion"),
    ("intensite-emotionnelle", "Intensité émotionnelle", "notion", "À distinguer de l'intensité transactionnelle : un rituel peut être intense émotionnellement et faiblement transactionnel.", "provisoire"),
    ("signification", "Signification", "notion", "Niveau 2 : les gestes prennent sens selon le contexte des gestes précédents et selon quatre facettes.", "stabilisé"),
    ("semiose-transactionnelle", "Sémiose transactionnelle", "notion", "Interprétation d'une transaction selon quatre facettes interdépendantes, de même rang.", "stabilisé"),
    ("situation-transactionnelle", "Situation transactionnelle", "notion", "Un problème, un besoin, une opportunité, inscrits dans un contexte institutionnel, culturel, technique.", "provisoire"),
    ("situation-problematique", "Situation problématique", "notion", "Au sens de Dewey, point de départ du parcours narratif.", "stabilisé"),
    ("self", "Self", "notion", "Participant individuel ou collectif transformé par la subjectivation.", "stabilisé"),
    ("oeuvre", "Œuvre", "notion", "Artefact porteur de valeur, produit de la création.", "stabilisé"),
    ("milieu", "Milieu", "notion", "Environnement approprié par la territorialisation.", "stabilisé"),
    ("milieu-constituant", "Milieu-constituant", "notion", "Le milieu n'est pas un décor : transformé par la transaction, il contribue à la constituer.", "provisoire"),
    ("consommatoire", "Consommatoire", "notion", "Les deux faces de la performance : accomplissement côté réalisateur, réception, usage et appropriation côté bénéficiaire.", "stabilisé"),
    ("rituel", "Rituel", "notion", "Processus qui réactualise ce qui est symbolique.", "provisoire"),
    ("ritualisation", "Ritualisation", "notion", "Pendant de la documentarisation dans la communication orale, en l'absence de support pérenne.", "provisoire"),
    ("documentarisation", "Documentarisation", "notion", "Stabilisation des artefacts sur support pérenne.", "provisoire"),
    ("dispositif-info-com", "Dispositif d'information et de communication", "notion", "Artefacts et milieux qui équipent la conversation ; relèvent de la territorialisation.", "stabilisé"),
    ("metacommunication", "Métacommunication", "notion", "Gestes portant sur l'agencement lui-même (demander, décider, promettre, nommer), au sens de Bateson.", "provisoire"),
    # Gestes
    ("geste-materiel", "Geste matériel", "type-geste", "Transforme des objets, des corps, le milieu : déplacer, assembler, installer.", "stabilisé"),
    ("geste-semiosique", "Geste sémiosique", "type-geste", "Produit des formes codifiées : parler, écrire, schématiser, signer. Il n'est pas immatériel.", "stabilisé"),
    ("geste-de-reception", "Geste de réception", "type-geste", "Geste par lequel un artefact est perçu et éprouvé (relire un document, par exemple).", "provisoire"),
    # Artefacts du parcours
    ("artefact-virtualisant", "Artefact virtualisant", "artefact", "Scelle l'engagement : un devis, un cahier des charges.", "stabilisé"),
    ("artefact-capacitant", "Artefact capacitant", "artefact", "Équipe la compétence : un outil, une méthode. Pôle du gradient de finalité.", "stabilisé"),
    ("artefact-porteur-de-valeur", "Artefact porteur de valeur", "artefact", "L'œuvre, qui circule du réalisateur au bénéficiaire. Pôle du gradient de finalité.", "stabilisé"),
    ("artefact-evaluatif", "Artefact évaluatif", "artefact", "Soutient le bilan : une grille, une facture, un retour.", "stabilisé"),
    # Gradients
    ("gradient-de-finalite", "Gradient de finalité", "gradient", "Capacitant ↔ porteur de valeur.", "stabilisé"),
    ("gradient-de-symbolicite", "Gradient de symbolicité", "gradient", "Profane ↔ symbolique.", "stabilisé"),
    ("gradient-d-incarnation", "Gradient d'incarnation", "gradient", "Incorporé ↔ autonome : de la voix, qui disparaît, au document, qui circule.", "stabilisé"),
    ("gradient-de-materialite", "Gradient de matérialité", "gradient", "Matérielle ↔ sémiosique : une efficace causale, ou par une forme codifiée.", "stabilisé"),
    ("dynamique-de-la-valeur", "Dynamique de la valeur", "gradient", "Regroupe les gradients de finalité et de symbolicité.", "stabilisé"),
    ("mode-d-existence-de-l-artefact", "Mode d'existence de l'artefact", "gradient", "Regroupe les gradients d'incarnation et de matérialité, qui font le lien direct avec les gestes.", "stabilisé"),
    # Pôles
    ("profane", "Profane", "pole-gradient", "Au sens de Durkheim, par opposition à ce qui est rechargé par le rituel.", "stabilisé"),
    ("symbolique", "Symbolique", "pole-gradient", "Ce que le rituel réactualise.", "stabilisé"),
    ("incorpore", "Incorporé", "pole-gradient", "Geste et artefact coïncident : la voix, la posture.", "stabilisé"),
    ("autonome", "Autonome", "pole-gradient", "Geste et artefact se séparent : le document, l'objet fabriqué, qui persistent et circulent.", "stabilisé"),
    ("materielle", "Matérielle", "pole-gradient", "Efficace causale.", "stabilisé"),
    ("semiosique", "Sémiosique", "pole-gradient", "Efficace par une forme codifiée.", "stabilisé"),
    # Formes de conversation
    ("conversation-ordinaire", "Conversation ordinaire", "forme-conversation", "Reproduction des pratiques : les pratiques établies sont reconduites.", "stabilisé"),
    ("conversation-rituelle", "Conversation rituelle", "forme-conversation", "Ressourcement : les participants et le self collectif sont réaffirmés.", "stabilisé"),
    ("conversation-inventive", "Conversation inventive", "forme-conversation", "Réinvention : l'œuvre, les selfs et le milieu sont réinventés. Écho à Simondon.", "stabilisé"),
    ("inventive-effervescente", "Conversation inventive effervescente", "forme-conversation", "Sous-type envisagé : création chaude, ponctuelle.", "en discussion"),
    ("inventive-elaborative", "Conversation inventive élaborative", "forme-conversation", "Sous-type envisagé : création soutenue, travaillée.", "en discussion"),
    # Facettes
    ("semiose-praxeologique", "Sémiose praxéologique", "facette", "Comment la transaction se conduit-elle ? Agencement collectif des contributions : conversation, coopération, coordination, organisation.", "stabilisé"),
    ("semiose-narrative", "Sémiose narrative", "facette", "Où le geste se situe-t-il dans le parcours ? Engagement, compétence, performance, bilan.", "stabilisé"),
    ("semiose-cognitive", "Sémiose cognitive", "facette", "Comment le geste ou l'artefact est-il compris ? Sensible, pratique, conceptuelle.", "stabilisé"),
    ("semiose-performative", "Sémiose performative", "facette", "Que produit la transaction, que transforme-t-elle ? Création, subjectivation, territorialisation.", "stabilisé"),
    # Dimensions performatives
    ("creation", "Création", "dimension-performative", "Les artefacts médiateurs ressources deviennent une œuvre.", "stabilisé"),
    ("subjectivation", "Subjectivation", "dimension-performative", "Les actants vivants deviennent des selfs transformés.", "stabilisé"),
    ("territorialisation", "Territorialisation", "dimension-performative", "L'environnement devient un milieu approprié.", "stabilisé"),
    # Raisons
    ("raison-sensible", "Raison sensible", "raison-cognitive", "Sens en situation ou qualitatif : signal, singulier, éprouvé ici et maintenant.", "stabilisé"),
    ("raison-pratique", "Raison pratique", "raison-cognitive", "Signification typifiée ou référentielle : type, genre, ce que l'on sait faire avec.", "stabilisé"),
    ("raison-conceptuelle", "Raison conceptuelle", "raison-cognitive", "Signification théorique ou hypothétique : concept, catégorie ; inclut récits et idéologies.", "stabilisé"),
    # Parcours
    ("parcours-narratif", "Parcours narratif", "moment-parcours", "Aussi appelé parcours transactionnel : séquence orientée vers l'œuvre, de la situation problématique au bilan ; c'est une boucle.", "stabilisé"),
    ("engagement", "Engagement", "moment-parcours", "Commanditaire et entrepreneur s'engagent : demande et offre.", "stabilisé"),
    ("competence", "Compétence", "moment-parcours", "Relève de l'entrepreneur : confère un pouvoir-faire.", "stabilisé"),
    ("performance", "Performance", "moment-parcours", "Deux faces : réalisation et réception.", "stabilisé"),
    ("realisation", "Réalisation (accomplissement)", "moment-parcours", "Face de la performance côté réalisateur : « ça y est ».", "stabilisé"),
    ("reception", "Réception (usage et appropriation)", "moment-parcours", "Face de la performance côté bénéficiaire : faire sienne l'œuvre, l'intégrer, la détourner ou la prolonger.", "stabilisé"),
    ("bilan", "Bilan", "moment-parcours", "Clôt le parcours et peut en relancer un autre ; comprend évaluation et rétribution.", "stabilisé"),
    ("evaluation", "Évaluation", "moment-parcours", "Jugement du résultat ; accomplir n'est pas évaluer.", "stabilisé"),
    ("retribution", "Rétribution", "moment-parcours", "Paiement, remerciement, reconnaissance.", "stabilisé"),
    # Phases Mead
    ("phase-impulsion", "Impulsion", "phase-acte", "Première phase de l'acte chez Mead.", "stabilisé"),
    ("phase-perception", "Perception", "phase-acte", "Deuxième phase de l'acte chez Mead.", "stabilisé"),
    ("phase-manipulation", "Manipulation", "phase-acte", "Troisième phase de l'acte chez Mead.", "stabilisé"),
    ("phase-consommation", "Consommation", "phase-acte", "Quatrième phase de l'acte chez Mead.", "stabilisé"),
    # Rôles
    ("commanditaire", "Commanditaire", "role", "Exprime une demande ; intervient à l'engagement et au bilan.", "stabilisé"),
    ("entrepreneur", "Entrepreneur", "role", "Fait une offre ; intervient à l'engagement et à la compétence.", "stabilisé"),
    ("realisateur", "Réalisateur", "role", "Accomplit l'œuvre lors de la performance.", "stabilisé"),
    ("beneficiaire", "Bénéficiaire", "role", "Reçoit et s'approprie l'œuvre ; intervient à la performance et au bilan.", "stabilisé"),
    # Pôles praxéologiques
    ("cooperation", "Coopération", "pole-praxeologique", "Production de valeur (œuvre, self, milieu) selon un régime contributif, concurrentiel ou antagoniste ; englobe le conflit.", "stabilisé"),
    ("coordination", "Coordination", "pole-praxeologique", "Les participants se coordonnent selon leur accès les uns aux autres et aux artefacts, dans l'espace et le temps.", "stabilisé"),
    ("organisation", "Organisation", "pole-praxeologique", "Stabilise les configurations institutionnelles : rôles et parcours stabilisés.", "stabilisé"),
    # Régimes
    ("regime-contributif", "Régime contributif", "regime-cooperation", "Converger : contribuer à une œuvre commune et se reconnaître mutuellement.", "stabilisé"),
    ("regime-concurrentiel", "Régime concurrentiel", "regime-cooperation", "Rivaliser : viser une même valeur rare selon des règles partagées.", "stabilisé"),
    ("regime-antagoniste", "Régime antagoniste", "regime-cooperation", "S'opposer tout en continuant d'interagir à travers des artefacts communs.", "stabilisé"),
    # Modes de coordination
    ("synchrone-en-presence", "Synchrone en présence", "mode-coordination", "Face à face, réunion, conférence ; espace et mobilier font partie du dispositif.", "stabilisé"),
    ("synchrone-a-distance", "Synchrone à distance", "mode-coordination", "Téléphonie, visiophonie, messagerie instantanée, coédition.", "stabilisé"),
    ("asynchrone", "Asynchrone", "mode-coordination", "Par traces et documents consignés.", "stabilisé"),
    # Dimensions de la coordination
    ("coordination-epistemique", "Coordination épistémique", "dimension-coordination", "Coordination lue du point de vue de la création.", "provisoire"),
    ("coordination-relationnelle", "Coordination relationnelle", "dimension-coordination", "Coordination lue du point de vue de la subjectivation.", "provisoire"),
    ("coordination-spatio-temporelle", "Coordination spatio-temporelle", "dimension-coordination", "Coordination lue du point de vue de la territorialisation et des dispositifs.", "provisoire"),
    # Dispositifs
    ("communication-orale-interactive", "Communication orale interactive", "dispositif", "Production verbale et gestuelle plus ou moins ritualisée.", "stabilisé"),
    ("diffusion-unidirectionnelle", "Diffusion à distance unidirectionnelle", "dispositif", "Contenus audio et vidéo non interactifs, sans support pérenne ; logique de flux.", "stabilisé"),
    ("dispositif-informationnel", "Dispositif informationnel", "dispositif", "Textes sur support pérenne : rapports, monographies, journaux, affiches.", "stabilisé"),
    ("info-communicationnel-numerique", "Dispositif info-communicationnel numérique", "dispositif", "Contenus dialogiques et fragmentaires : documents pour l'action.", "stabilisé"),
    ("transmediation", "Transmédiation", "dispositif", "Événements ritualisés et contenus documentarisés produits de façon coordonnée.", "stabilisé"),
]

TYPES_RELATION = [
    ("pole_de", "est un pôle de", "a pour pôle", False),
    ("oppose_a", "s'oppose à", "s'oppose à", True),
    ("sous_type_de", "est un type de", "a pour type", False),
    ("composante_de", "est une composante de", "comprend", False),
    ("precede", "précède", "suit", False),
    ("peut_relancer", "peut relancer", "peut être relancé par", False),
    ("produit", "produit", "est produit par", False),
    ("correspond_a", "correspond à", "correspond à", True),
    ("mobilise", "mobilise", "est mobilisé par", False),
    ("intervient_dans", "intervient dans", "fait intervenir", False),
    ("releve_de", "relève de", "englobe", False),
    ("distingue_de", "est à distinguer de", "est à distinguer de", True),
    ("equivaut_a", "équivaut à", "équivaut à", True),
    ("regroupe", "regroupe", "appartient à", False),
    ("caracterise", "caractérise", "est caractérisé par", False),
    ("actualise", "réactualise", "est réactualisé par", False),
    ("constitue", "constitue", "est constitué par", False),
    ("transpose", "transpose", "est transposé par", False),
    ("face_de", "est une face de", "a pour face", False),
]

R = []
def rel(s, t, c, typ, com=None):
    pass

def add(src, typ, *cibles, com=None):
    for c in cibles:
        R.append((src, typ, c, com))

# Gestes et artefacts
add("geste-materiel", "sous_type_de", "geste")
add("geste-semiosique", "sous_type_de", "geste")
add("geste-de-reception", "sous_type_de", "geste")
add("geste-materiel", "oppose_a", "geste-semiosique", com="On parle de dominante : aucun geste n'est purement matériel ou sémiosique.")
add("geste", "face_de", "communication", com="Vue par les gestes : l'activité dans son déroulement.")
add("artefact-mediateur", "face_de", "communication", com="Vue par les artefacts : ce que l'activité produit, fait circuler et stabilise.")
add("geste", "produit", "artefact-mediateur", com="Le geste donne forme à l'artefact ou le reprend.")
add("communication", "mobilise", "geste", "artefact-mediateur", "conversation")
add("communication-axiogene", "correspond_a", "communication", com="Vue par les artefacts de la communication.")
add("communication", "constitue", "cooperation", "coordination", "organisation")
add("geste", "caracterise", "signification", com="Niveau 1 vers niveau 2 : les gestes prennent sens.")
add("conversation", "composante_de", "communication")
add("interaction", "oppose_a", "transaction")
add("transaction", "caracterise", "conversation", com="Toute conversation est transactionnelle, plus ou moins.")
add("intensite-transactionnelle", "caracterise", "conversation")
add("intensite-transactionnelle", "distingue_de", "intensite-emotionnelle")
add("situation-transactionnelle", "precede", "transaction")
add("situation-problematique", "precede", "engagement")

# Artefacts et gradients
for a in ["artefact-virtualisant", "artefact-capacitant", "artefact-porteur-de-valeur", "artefact-evaluatif"]:
    add(a, "sous_type_de", "artefact-mediateur")
add("oeuvre", "equivaut_a", "artefact-porteur-de-valeur")
add("artefact-capacitant", "pole_de", "gradient-de-finalite")
add("artefact-porteur-de-valeur", "pole_de", "gradient-de-finalite")
add("artefact-capacitant", "oppose_a", "artefact-porteur-de-valeur")
add("profane", "pole_de", "gradient-de-symbolicite")
add("symbolique", "pole_de", "gradient-de-symbolicite")
add("profane", "oppose_a", "symbolique")
add("incorpore", "pole_de", "gradient-d-incarnation")
add("autonome", "pole_de", "gradient-d-incarnation")
add("incorpore", "oppose_a", "autonome")
add("materielle", "pole_de", "gradient-de-materialite")
add("semiosique", "pole_de", "gradient-de-materialite")
add("materielle", "oppose_a", "semiosique")
add("materielle", "correspond_a", "geste-materiel", com="La matérialité reprend les termes des gestes.")
add("semiosique", "correspond_a", "geste-semiosique", com="La matérialité reprend les termes des gestes.")
for g in ["gradient-de-finalite", "gradient-de-symbolicite", "gradient-d-incarnation", "gradient-de-materialite"]:
    add(g, "caracterise", "artefact-mediateur")
add("dynamique-de-la-valeur", "regroupe", "gradient-de-finalite", "gradient-de-symbolicite")
add("mode-d-existence-de-l-artefact", "regroupe", "gradient-d-incarnation", "gradient-de-materialite")
add("gradient-d-incarnation", "distingue_de", "gradient-de-materialite", com="Mode d'existence de l'artefact vs mode d'inscription du sens.")
add("rituel", "actualise", "symbolique")
add("ritualisation", "correspond_a", "documentarisation", com="La ritualisation est le pendant de la documentarisation en l'absence de support pérenne.")

# Formes de conversation
for f in ["conversation-ordinaire", "conversation-rituelle", "conversation-inventive"]:
    add(f, "sous_type_de", "conversation")
add("inventive-effervescente", "sous_type_de", "conversation-inventive")
add("inventive-elaborative", "sous_type_de", "conversation-inventive")
add("conversation-rituelle", "mobilise", "rituel")

# Facettes
for f in ["semiose-praxeologique", "semiose-narrative", "semiose-cognitive", "semiose-performative"]:
    add(f, "pole_de", "semiose-transactionnelle")
add("semiose-transactionnelle", "caracterise", "signification")
for d in ["creation", "subjectivation", "territorialisation"]:
    add(d, "composante_de", "semiose-performative")
for r in ["raison-sensible", "raison-pratique", "raison-conceptuelle"]:
    add(r, "composante_de", "semiose-cognitive")
for m in ["engagement", "competence", "performance", "bilan"]:
    add(m, "composante_de", "parcours-narratif")
add("parcours-narratif", "releve_de", "semiose-narrative")
for p in ["conversation", "cooperation", "coordination", "organisation"]:
    add(p, "composante_de", "semiose-praxeologique")
add("conversation", "constitue", "cooperation", "coordination", "organisation", com="La conversation est au centre de l'action collective ; relations réciproques.")
add("metacommunication", "releve_de", "semiose-praxeologique")

# Performative
add("creation", "produit", "oeuvre")
add("subjectivation", "produit", "self")
add("territorialisation", "produit", "milieu")
add("milieu-constituant", "sous_type_de", "milieu")
add("dispositif-info-com", "releve_de", "territorialisation")

# Parcours
add("engagement", "precede", "competence")
add("competence", "precede", "performance")
add("performance", "precede", "bilan")
add("bilan", "peut_relancer", "engagement", com="Le parcours est une boucle.")
add("realisation", "face_de", "performance")
add("reception", "face_de", "performance")
add("realisation", "precede", "reception")
add("evaluation", "composante_de", "bilan")
add("retribution", "composante_de", "bilan")
add("evaluation", "precede", "retribution")
add("consommatoire", "correspond_a", "performance")
add("realisation", "composante_de", "consommatoire")
add("reception", "composante_de", "consommatoire")
add("phase-impulsion", "precede", "phase-perception")
add("phase-perception", "precede", "phase-manipulation")
add("phase-manipulation", "precede", "phase-consommation")
add("phase-impulsion", "correspond_a", "engagement")
add("phase-perception", "correspond_a", "competence")
add("phase-manipulation", "correspond_a", "performance")
add("phase-consommation", "correspond_a", "bilan", com="Correspondance de la diapositive 29 ; la consommation devient aussi la performance (consommatoire).")
add("parcours-narratif", "transpose", "phase-impulsion", com="Transposition des phases de l'acte de Mead et du schéma narratif de Greimas.")

# Rôles
add("commanditaire", "intervient_dans", "engagement", "bilan")
add("entrepreneur", "intervient_dans", "engagement", "competence")
add("realisateur", "intervient_dans", "performance")
add("beneficiaire", "intervient_dans", "performance", "bilan")
add("engagement", "mobilise", "artefact-virtualisant")
add("competence", "mobilise", "artefact-capacitant")
add("performance", "mobilise", "artefact-porteur-de-valeur")
add("bilan", "mobilise", "artefact-evaluatif")

# Praxéologique
for r in ["regime-contributif", "regime-concurrentiel", "regime-antagoniste"]:
    add(r, "sous_type_de", "cooperation")
for m in ["synchrone-en-presence", "synchrone-a-distance", "asynchrone"]:
    add(m, "sous_type_de", "coordination")
add("coordination-epistemique", "sous_type_de", "coordination")
add("coordination-relationnelle", "sous_type_de", "coordination")
add("coordination-spatio-temporelle", "sous_type_de", "coordination")
add("coordination-epistemique", "correspond_a", "creation")
add("coordination-relationnelle", "correspond_a", "subjectivation")
add("coordination-spatio-temporelle", "correspond_a", "territorialisation")
add("coordination-spatio-temporelle", "mobilise", "dispositif-info-com")
for d in ["communication-orale-interactive", "diffusion-unidirectionnelle", "dispositif-informationnel", "info-communicationnel-numerique", "transmediation"]:
    add(d, "sous_type_de", "dispositif-info-com")
add("communication-orale-interactive", "mobilise", "ritualisation")
add("dispositif-informationnel", "mobilise", "documentarisation")
add("communication-orale-interactive", "correspond_a", "synchrone-en-presence")
add("diffusion-unidirectionnelle", "correspond_a", "synchrone-a-distance")
add("dispositif-informationnel", "correspond_a", "asynchrone")

AUTEURS = [
    ("mead", "George Herbert Mead", "Sémiotique interactionniste ; conversation de gestes ; phases de l'acte"),
    ("greimas", "Algirdas Julien Greimas", "Sémiotique narrative ; schéma narratif canonique"),
    ("peirce", "Charles Sanders Peirce", "Sémiotique triadique"),
    ("morris", "Charles W. Morris", "Syntaxe, sémantique, pragmatique (1938) ; Signification and Significance (1964)"),
    ("dewey-bentley", "John Dewey et Arthur F. Bentley", "Distinction interaction / transaction (1949)"),
    ("dewey", "John Dewey", "Situation problématique ; mise en commun"),
    ("durkheim", "Émile Durkheim", "Profane et sacré ; rituel"),
    ("simondon", "Gilbert Simondon", "Invention"),
    ("taylor", "James R. Taylor", "Dualité conversation / texte"),
    ("bateson", "Gregory Bateson", "Métacommunication"),
]

CONCEPT_AUTEUR = [
    ("conversation", "mead", "inspiration", "La conversation est matérielle avant d'être verbale."),
    ("semiose-praxeologique", "mead", "inspiration", None),
    ("semiose-narrative", "greimas", "inspiration", None),
    ("semiose-cognitive", "peirce", "inspiration", None),
    ("semiose-cognitive", "morris", "inspiration", "Peirce enrichi par Morris (1938)."),
    ("parcours-narratif", "greimas", "transposition", "Schéma narratif transposé à la transaction."),
    ("parcours-narratif", "mead", "transposition", "Phases de l'acte (1938)."),
    ("phase-impulsion", "mead", "emprunt", None),
    ("phase-perception", "mead", "emprunt", None),
    ("phase-manipulation", "mead", "emprunt", None),
    ("phase-consommation", "mead", "emprunt", None),
    ("interaction", "dewey-bentley", "emprunt", None),
    ("transaction", "dewey-bentley", "emprunt", None),
    ("situation-problematique", "dewey", "emprunt", None),
    ("communication-axiogene", "dewey", "inspiration", "Communication comme mise en commun."),
    ("profane", "durkheim", "emprunt", None),
    ("conversation-inventive", "simondon", "inspiration", "Le terme fait écho à Simondon."),
    ("artefact-mediateur", "taylor", "inspiration", "Dualité conversation / texte généralisée en conversation / artefact."),
    ("metacommunication", "bateson", "emprunt", None),
    ("regime-antagoniste", "greimas", "inspiration", "Figure de l'anti-sujet."),
]

REFERENCES = [
    ("brassac-zacklad-2013", "Brassac, C. et Zacklad, M. (2013). Pragmatisme et activités : des interactions aux transactions. Activités, 10(1).", 2013, "publication"),
    ("zacklad-2015", "Zacklad, M. (2015). Régimes de coopération dans les comportements collectifs médiatisés. L'Harmattan.", 2015, "publication"),
    ("zacklad-2016", "Zacklad, M. (2016). Diversité des ontologies de la communication et de l'action collective. RFSIC, 9.", 2016, "publication"),
    ("zacklad-2020", "Zacklad, M. (2020). Changements de régimes de conversation dans la transition numérique. ATIC, 1(1), 7-40.", 2020, "publication"),
    ("zacklad-2023", "Zacklad, M. (2023). La sémio-pragmatique est-elle soluble dans la sémiotique du dispositif ? ATIC, 7(2), 25-65.", 2023, "publication"),
    ("mead-1938", "Mead, G. H. (1938). The Philosophy of the Act. University of Chicago Press.", 1938, "publication"),
    ("morris-1964", "Morris, C. W. (1964). Signification and Significance. MIT Press.", 1964, "publication"),
    ("greimas-courtes-1979", "Greimas, A. J. et Courtés, J. (1979). Sémiotique. Dictionnaire raisonné de la théorie du langage. Hachette.", 1979, "publication"),
    ("dewey-bentley-1949", "Dewey, J. et Bentley, A. F. (1949). Knowing and the Known. Beacon Press.", 1949, "publication"),
    ("diaporama-communication-conversation", "Zacklad, M. (2026). Communiquer, c'est faire des gestes qui prennent sens dans l'instant et en différé. Diaporama de cours, Master Information-Communication, Cnam.", 2026, "support"),
]

CONCEPT_REFERENCE = [
    ("interaction", "dewey-bentley-1949", "source"),
    ("transaction", "dewey-bentley-1949", "source"),
    ("conversation", "brassac-zacklad-2013", "source"),
    ("conversation", "zacklad-2020", "source"),
    ("intensite-transactionnelle", "zacklad-2020", "source"),
    ("parcours-narratif", "mead-1938", "source"),
    ("parcours-narratif", "greimas-courtes-1979", "source"),
]
