-- Schéma du glossaire STC (migration schema_glossaire, appliquée le 2026-11-08)

create table public.famille (
  slug text primary key,
  libelle text not null,
  description text,
  ordre int not null default 0
);

create table public.concept (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  libelle text not null,
  famille_slug text not null references public.famille(slug) on update cascade,
  resume text,
  statut text not null default 'provisoire' check (statut in ('stabilisé','provisoire','en discussion','écarté')),
  ordre int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index on public.concept (famille_slug);

create table public.type_relation (
  slug text primary key,
  libelle text not null,
  libelle_inverse text not null,
  symetrique boolean not null default false,
  description text
);

create table public.relation (
  id uuid primary key default gen_random_uuid(),
  source_id uuid not null references public.concept(id) on delete cascade,
  cible_id uuid not null references public.concept(id) on delete cascade,
  type_slug text not null references public.type_relation(slug) on update cascade,
  commentaire text,
  ordre int not null default 0,
  unique (source_id, cible_id, type_slug),
  check (source_id <> cible_id)
);
create index on public.relation (source_id);
create index on public.relation (cible_id);

create table public.auteur (slug text primary key, nom text not null, description text);

create table public.reference (
  id uuid primary key default gen_random_uuid(),
  cle text not null unique,
  citation text not null,
  annee int,
  zotero_key text,
  url text,
  type text not null default 'publication' check (type in ('publication','support','note'))
);

create table public.concept_auteur (
  concept_id uuid not null references public.concept(id) on delete cascade,
  auteur_slug text not null references public.auteur(slug) on update cascade,
  nature text not null default 'inspiration',
  commentaire text,
  primary key (concept_id, auteur_slug, nature)
);

create table public.concept_reference (
  concept_id uuid not null references public.concept(id) on delete cascade,
  reference_id uuid not null references public.reference(id) on delete cascade,
  role text not null default 'source',
  localisation text,
  primary key (concept_id, reference_id, role)
);

create table public.definition (
  id uuid primary key default gen_random_uuid(),
  concept_id uuid not null references public.concept(id) on delete cascade,
  texte text not null,
  version int not null default 1,
  date_version date not null default current_date,
  reference_id uuid references public.reference(id),
  est_courante boolean not null default true,
  note text,
  unique (concept_id, version)
);

create table public.terme_ecarte (
  id uuid primary key default gen_random_uuid(),
  concept_id uuid references public.concept(id) on delete cascade,
  terme text not null,
  raison text,
  date_ecart date
);

create or replace function public.touch_updated_at() returns trigger
language plpgsql set search_path = '' as $$
begin new.updated_at = now(); return new; end; $$;
create trigger concept_touch before update on public.concept
for each row execute function public.touch_updated_at();

-- Lecture publique ; écriture réservée (service role, futurs comptes éditeurs)
do $$
declare t text;
begin
  foreach t in array array['famille','concept','type_relation','relation','auteur','reference','concept_auteur','concept_reference','definition','terme_ecarte']
  loop
    execute format('alter table public.%I enable row level security', t);
    execute format('create policy "lecture publique" on public.%I for select to anon, authenticated using (true)', t);
    execute format('grant select on public.%I to anon, authenticated', t);
  end loop;
end $$;

create view public.v_relation with (security_invoker = on) as
select r.id, r.type_slug, tr.libelle, tr.libelle_inverse, tr.symetrique, r.commentaire, r.ordre,
       s.slug as source_slug, s.libelle as source_libelle, s.famille_slug as source_famille,
       c.slug as cible_slug, c.libelle as cible_libelle, c.famille_slug as cible_famille
from public.relation r
join public.type_relation tr on tr.slug = r.type_slug
join public.concept s on s.id = r.source_id
join public.concept c on c.id = r.cible_id;
grant select on public.v_relation to anon, authenticated;
