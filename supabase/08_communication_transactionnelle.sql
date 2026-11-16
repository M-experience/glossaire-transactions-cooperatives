-- 16 novembre 2026 : entrée « Communication transactionnelle » (notions fondamentales), équivalente à la communication axiogène,
-- et définition de la communication axiogène ou transactionnelle propre à la STC (texte de M. Zacklad), posée sur les deux concepts.
insert into concept (slug, libelle, famille_slug, resume, statut, ordre)
values ('communication-transactionnelle', 'Communication transactionnelle', 'notion',
 'Autre nom de la communication axiogène, propre à la STC : former, éprouver et reprendre des artefacts médiateurs par des gestes, au sein d''une conversation.', 'stabilisé', 1)
on conflict (slug) do nothing;
insert into relation (source_id, cible_id, type_slug, commentaire, ordre)
select a.id, b.id, 'equivaut_a', null, 0 from concept a, concept b
where a.slug='communication-transactionnelle' and b.slug='communication-axiogene'
 and not exists (select 1 from relation x where x.source_id=a.id and x.cible_id=b.id and x.type_slug='equivaut_a');
insert into definition (concept_id, texte, version, est_courante, note)
select c.id, 'Communiquer, c''est former, éprouver et reprendre des artefacts médiateurs par des gestes, au sein d''une conversation. Former, c''est produire ou transformer un artefact par un geste ; éprouver, c''est le percevoir et en faire usage ; reprendre, c''est le mobiliser à nouveau, parfois bien plus tard et dans une autre situation.',
 1, true, 'Définition de la communication axiogène ou transactionnelle propre à la STC.'
from concept c where c.slug in ('communication-transactionnelle','communication-axiogene')
 and not exists (select 1 from definition d where d.concept_id=c.id);
