# plano-engenharia-ia

Plano de transição de Backend/PO para **Engenharia de IA aplicada** — Pedro Henrique Gouveia de Souza.

Site público: <https://pedrogouveia001.github.io/plano-engenharia-ia/>

## O que é

- **Diagnóstico honesto** do perfil (58 repos GitHub, currículo, LinkedIn), classificando competências como forte / em desenvolvimento / não comprovada.
- **Plano de 12 pilares, 183 semanas, 1.451h** (145h já concluídas em CS50x+CS50P), com 6 marcos de empregabilidade.
- **6 formações Coursera integrais** (Python 3 Programming, Mathematics for ML, Machine Learning, Deep Learning, Generative AI Engineering with LLMs, MLOps Duke) — nunca curso avulso, nunca módulo pulado.
- **Política de autonomia:** cada marco exige uma prova fechada **sem IA** + defesa oral.
- **Projeto-fio público:** `decision-intelligence-ai`, com dados públicos/sintéticos apenas.

## Arquivos

| Caminho | O que é |
|---|---|
| `src/build_plan.py` | Gera `data/ai_weeks.json` e `data/plan_meta.json` |
| `src/build_html.py` | Gera `index.html` autocontido (tracker semanal com filtros, progresso, localStorage) |
| `src/build_inventory.py` | Gera `evidence/project_inventory.json` (metadados de 58 repos via `gh repo list`) |
| `tests/test_plan.py` | Invariantes de horas, IDs, HTTPS, cap de 8h, formações completas |
| `evidence/PLAN_SPEC.md` | Regras, mudanças vs plano anterior, política de corte |
| `evidence/COMPETENCY_AUDIT.md` | Matriz de competências com evidências |
| `evidence/SOURCES.md` | Fontes citadas e data de acesso |
| `evidence/project_inventory.json` | Inventário de repos (público detalhado; privados agregados) |

## Como gerar

```bash
python src/build_plan.py      # -> data/ai_weeks.json, data/plan_meta.json
python src/build_html.py      # -> index.html
python src/build_inventory.py # -> evidence/project_inventory.json (requer gh autenticado)
```

## Como testar

```bash
python -m unittest discover -s tests -v
```

## Publicar (GitHub Pages)

O workflow `.github/workflows/pages.yml` builda, testa e faz deploy do `index.html` para o GitHub Pages no push em `main`.

## Privacidade

- Nada de telefone, e-mail, CNPJ ou detalhes do cliente sob NDA no site.
- Repos privados aparecem apenas como contagem agregada, sem nome ou link.
