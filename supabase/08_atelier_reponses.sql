-- Atelier STC : dépôt des réponses des étudiants et lecture par l'enseignant.
-- Les étudiants n'ont aucun accès direct à la table : ils déposent par la fonction
-- atelier_deposer. L'enseignant lit par atelier_lire, protégée par un code secret
-- dont seul le hachage est stocké (table atelier_secret, valeur posée hors dépôt).

create table if not exists public.atelier_reponse (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  classe text not null check (char_length(classe) between 1 and 40),
  eleve text not null check (char_length(eleve) between 1 and 80),
  cle text not null check (char_length(cle) between 8 and 64),
  payload jsonb not null check (pg_column_size(payload) < 60000)
);
create index if not exists atelier_reponse_classe_idx on public.atelier_reponse (classe, cle, created_at desc);
alter table public.atelier_reponse enable row level security;

create table if not exists public.atelier_secret (
  id int primary key default 1 check (id = 1),
  code_hash text not null
);
alter table public.atelier_secret enable row level security;

-- Dépôt : une ligne par envoi ; l'enseignant voit le dernier envoi de chaque étudiant.
create or replace function public.atelier_deposer(p_classe text, p_eleve text, p_cle text, p_payload jsonb)
returns timestamptz
language plpgsql security definer set search_path = public, extensions as $$
declare t timestamptz;
begin
  if (select count(*) from public.atelier_reponse
      where cle = p_cle and created_at > now() - interval '1 hour') >= 30 then
    raise exception 'trop_d_envois';
  end if;
  insert into public.atelier_reponse (classe, eleve, cle, payload)
  values (trim(p_classe), trim(p_eleve), p_cle, p_payload)
  returning created_at into t;
  return t;
end $$;

-- Lecture enseignant : dernier envoi par étudiant, pour une classe ou toutes.
create or replace function public.atelier_lire(p_code text, p_classe text default null)
returns table (classe text, eleve text, cle text, created_at timestamptz, payload jsonb, envois bigint)
language plpgsql security definer set search_path = public, extensions as $$
begin
  if not exists (select 1 from public.atelier_secret s where s.code_hash = crypt(p_code, s.code_hash)) then
    raise exception 'code_invalide';
  end if;
  return query
    select distinct on (r.cle) r.classe, r.eleve, r.cle, r.created_at, r.payload,
           count(*) over (partition by r.cle) as envois
    from public.atelier_reponse r
    where p_classe is null or p_classe = '' or r.classe = trim(p_classe)
    order by r.cle, r.created_at desc;
end $$;

revoke all on function public.atelier_deposer(text, text, text, jsonb) from public;
revoke all on function public.atelier_lire(text, text) from public;
grant execute on function public.atelier_deposer(text, text, text, jsonb) to anon, authenticated;
grant execute on function public.atelier_lire(text, text) to anon, authenticated;

-- Poser ou changer le code enseignant (à exécuter à part, jamais dans le dépôt) :
-- insert into public.atelier_secret (id, code_hash) values (1, extensions.crypt('CODE', extensions.gen_salt('bf')))
--   on conflict (id) do update set code_hash = excluded.code_hash;
