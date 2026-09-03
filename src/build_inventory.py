# -*- coding: utf-8 -*-
"""Gera evidence/project_inventory.json com metadados seguros dos repositorios.

Escopo: repos proprios de pedrogouveia001 + repos da org sad-mcdm.
Exclui: code50, me50 (perfis de cursos CS50) e forks.
Somente metadados: nada de codigo, conteudo de arquivos ou segredos.

Fonte: `gh repo list <owner> --limit 100 --json ...` (inclui privados que
o token pode ver). Fallback: `gh api`.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "evidence" / "project_inventory.json"
EXCLUDE_OWNERS = {"code50", "me50"}
# O próprio repo do plano não é projeto de competência; apareceu após o create
EXCLUDE_REPOS = {"plano-engenharia-ia"}

GH_REPO_FIELDS = "name,owner,isPrivate,isArchived,isFork,primaryLanguage,description,diskUsage,updatedAt,createdAt,pushedAt,defaultBranchRef,homepageUrl,url"


def run(cmd: list[str]) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=300)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])}... falhou: {result.stderr.strip()[:300]}")
    return result.stdout.strip()


def list_repos(owner: str, org: bool) -> list[dict]:
    target = owner
    raw = run(["gh", "repo", "list", target, "--limit", "200", "--json", GH_REPO_FIELDS])
    if not raw:
        return []
    return json.loads(raw)


def clean(repo: dict) -> dict:
    owner = (repo.get("owner") or {}).get("login", "?")
    lang = (repo.get("primaryLanguage") or {}).get("name")
    branch = (repo.get("defaultBranchRef") or {}).get("name")
    return {
        "owner": owner,
        "name": repo.get("name"),
        "private": bool(repo.get("isPrivate")),
        "archived": bool(repo.get("isArchived")),
        "fork": bool(repo.get("isFork")),
        "language": lang,
        "description": repo.get("description"),
        "size": repo.get("diskUsage"),
        "updated_at": repo.get("updatedAt"),
        "created_at": repo.get("createdAt"),
        "pushed_at": repo.get("pushedAt"),
        "default_branch": branch,
        "homepage": repo.get("homepageUrl"),
        "html_url": repo.get("url"),
    }


def main() -> int:
    inventory: list[dict] = []
    for owner, org in (("pedrogouveia001", False), ("sad-mcdm", True)):
        try:
            inventory.extend(clean(r) for r in list_repos(owner, org))
        except RuntimeError as exc:
            print(f"AVISO: {exc}", file=sys.stderr)
            return 1

    # code50/me50 aparecem em contexto de cursos CS50; forks e o próprio
    # repositório do plano descartados
    inventory = [r for r in inventory
                 if r["owner"] not in EXCLUDE_OWNERS
                 and r["name"] not in EXCLUDE_REPOS
                 and not r["fork"]]

    # Deduplicar por (owner, name)
    seen: set[tuple[str, str]] = set()
    unique: list[dict] = []
    for r in inventory:
        key = (r["owner"], r["name"])
        if key not in seen:
            seen.add(key)
            unique.append(r)
    unique.sort(key=lambda x: (x["owner"], x["name"]))

    public = [r for r in unique if not r["private"]]
    private = [r for r in unique if r["private"]]

    langs: dict[str, int] = {}
    for r in unique:
        key = r["language"] or "sem linguagem"
        langs[key] = langs.get(key, 0) + 1
    langs_sorted = dict(sorted(langs.items(), key=lambda x: -x[1]))

    out = {
        "generatedAt": "2026-09-03T18:00:00-03:00",
        "scope": (
            "repos proprios de pedrogouveia001 + org sad-mcdm via gh repo list; "
            "exclui code50/me50 e forks"
        ),
        "totals": {
            "all": len(unique),
            "public": len(public),
            "private": len(private),
            "personalOwned": len([r for r in unique if r["owner"] == "pedrogouveia001"]),
            "orgSadMcdm": len([r for r in unique if r["owner"] == "sad-mcdm"]),
        },
        "languages": langs_sorted,
        # Lista detalhada apenas dos PUBLICOS; privados ficam como contagem
        "publicRepos": public,
        "privateCount": len(private),
        "privacyNote": (
            "Somente metadados da API. Repositorios privados nao sao listados "
            "individualmente (nem nome, nem descricao, nem link)."
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    t = out["totals"]
    print(f"Inventario: {t['all']} repos ({t['public']} publicos, {t['private']} privados) -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
