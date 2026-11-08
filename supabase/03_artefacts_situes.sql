-- Migration artefacts_situes (2026-11-08) : artefacts positionnés sur les gradients
create table public.artefact_exemple (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  libelle text not null,
  commentaire text,
  reference_id uuid references public.reference(id),
  ordre int not null default 0
);
create table public.positionnement (
  exemple_id uuid not null references public.artefact_exemple(id) on delete cascade,
  gradient_id uuid not null references public.concept(id) on delete cascade,
  position numeric(3,2) not null check (position between 0 and 1), -- 0 = premier pôle, 1 = second pôle
  libelle text not null,
  commentaire text,
  primary key (exemple_id, gradient_id)
);
alter table public.artefact_exemple enable row level security;
alter table public.positionnement enable row level security;
create policy "lecture publique" on public.artefact_exemple for select to anon, authenticated using (true);
create policy "lecture publique" on public.positionnement for select to anon, authenticated using (true);
grant select on public.artefact_exemple, public.positionnement to anon, authenticated;
-- Données : 8 artefacts du diaporama (exercice 2), 7 termes écartés, 2 relations « caractérise » vers l'artefact médiateur
