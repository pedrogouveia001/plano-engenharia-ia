# Plano de Estudos Backend/Fullstack v3 Full — especificação

**Data:** 14/08/2026 (revisões Produção + Certificados Integrais)  
**Arquivo:** `Plano_Estudos_Backend.html` — **18 pilares · 324 semanas · 2.527h · 13 marcos**  
**Já concluído no tracker:** **145h** (CS50x + CS50P pré-marcados) → restam **~2.382h**  
**Chave localStorage:** `sad_backend_v3_full_tracker_state`  
**Geradores:** `job_hunter/build_backend_plan_v2_weeks.py` → `data/backend_weeks.json` → `build_backend_plan_html.py`  
**Backup imediato anterior:** `_arquivados_trackers/backend_historico/Plano_Estudos_Backend_BACKUP_pre_v3_full_20260807.html`

## Objetivo

Formar um profissional **fullstack/backend certificável de elite**, cobrindo **do básico ao avançado**, sem buracos na escada — sem violar as regras fixas (Coursera/certificável, plataformas de mercado, zero CESAR-AI, zero CiApp, zero posicionamento, Python antes de OS, frontend depois do backend).

## Família CS50 (Pilar 1)

| Curso | h | Estado |
|---|---|---|
| **CS50x** | 100 | **Já concluído** — tarefas `completed: true` |
| **CS50P** | 45 | **Já concluído** — tarefas `completed: true` |
| **CS50SQL** | 30 | **Em andamento (~50% em 20/08/2026)** — ponte antes do Postgres avançado |
| **CS50W** | 50 | A fazer — ponte antes do Meta Back-End / FastAPI |
| **CS50 Cybersecurity** | 20 | A fazer — ponte antes do PortSwigger |
| **CS50 AI** | — | **Fora** (overlap CESAR School) |

## Escada básico → avançado (por domínio)

| Domínio | Básico | Intermediário | Avançado / cert |
|---|---|---|---|
| CS / programação | CS50x → CS50P | Michigan Python 3 **integral (5 cursos)** | Packt ×4 → **PCPP1** |
| Rede / OS / Git | Google Networking, Codio Linux, IBM Linux | Git Google + Learn Git Branching | GitHub Foundations + Linux Server |
| SQL / DB | CS50SQL | Boulder design + Michigan Postgres | Tuning + LeetCode/DataLemur/StrataScratch + HR Advanced |
| Web / API | CS50W | Meta Back-End PC **integral (9 cursos)** + FastAPI | Projeto-fio E-Commerce |
| Testes | Minnesota **integral (4 cursos)** + Playwright/pytest | Testcontainers/contrato/migration | Suite do projeto-fio |
| DSA | (CS50x) | UCSD **integral (6 cursos)** | Stanford **integral (4 cursos)** + NeetCode 150 + Blind 75 |
| Cache/NoSQL | Mongo intro | Redis University + Mongo path | Caching proxy |
| Mensageria | RabbitMQ tutorials | Kafka specialization | Outbox no projeto-fio |
| Containers | KodeKloud Docker beginner | IBM Containers | KodeKloud K8s + Compose/K8s no projeto |
| Cloud | AWS SA PC **integral (4 cursos, inclui Essentials)** | **SAA-C03** + deploy |
| DevOps/Obs | CI/CD fundamentals | Terraform prep + SRE + OTel | Pipeline no projeto-fio |
| Segurança | CS50 Cyber | IBM AppSec | **PortSwigger** + TryHackMe + hardening |
| Arquitetura | Alberta **integral (4 cursos)** | System Design Primer | Decomposição + ADRs |
| Distribuidos | — | UIUC Cloud Computing **integral (6 cursos)** | Performance + k6 |
| Frontend | freeCodeCamp | Meta Front-End PC **integral (9 cursos)** | Next + a11y + front do projeto-fio |
| Capstone | — | — | Produto em produção + ADRs |

## 17 pilares

| # | Pilar | h | sem |
|---|---|---|---|
| 1 | Fundamentos Harvard CS50 | 245 | 31 |
| **2** | **Containers, CI/CD e Deploy — essencial de mercado** | **54** | **7** |
| 3 | Python Avançado e Certificação PCPP1 | 229 | 29 |
| 4 | Internet, Linux e Git | 103 | 13 |
| 5 | PostgreSQL Avançado e Modelagem | 147 | 19 |
| 6 | APIs, Autenticação e Frameworks Backend | 268 | 34 |
| 7 | Testes, TDD e Qualidade | 130 | 17 |
| 8 | Estruturas de Dados, Algoritmos e Entrevista | 280 | 35 |
| 9 | Caching, NoSQL e Busca | 68 | 9 |
| 10 | Mensageria e Arquitetura Event-Driven | 68 | 9 |
| 11 | Containers e Kubernetes | 84 | 11 |
| 12 | Cloud AWS e Deploy | 76 | 10 |
| 13 | CI/CD, Infra como Código e Observabilidade | 98 | 13 |
| 14 | Segurança de Aplicações | 80 | 10 |
| 15 | Arquitetura de Software e System Design | 100 | 13 |
| 16 | Escala, Performance e Sistemas Distribuídos | 162 | 21 |
| 17 | Frontend Profissional e Fullstack | 277 | 35 |
| 18 | Capstone Fullstack | 58 | 8 |
| | **Total** | **2.527** | **324** |

## Revisão de 20/08/2026 — Pilar 2 adiantado

**Problema.** Docker, CI/CD e cloud aparecem em quase toda vaga de backend pleno do funil, e estavam
nos pilares 10, 11 e 12 — centenas de semanas à frente. Consequência prática: esses termos ficavam
fora do currículo e do LinkedIn por não se sustentarem em entrevista, e isso derrubava candidaturas.

**Mudança.** Criado o **Pilar 2 — Containers, CI/CD e Deploy** (54h · 7 semanas), logo após a
família CS50. Cobre o mínimo defensável em entrevista, com entregável público a cada etapa:

| Item | h | Entregável |
|---|---|---|
| Docker for Absolute Beginners (KodeKloud) | 10 | — |
| Conteinerizar projeto próprio | 8 | `Dockerfile` multi-stage + `compose.yaml` com PostgreSQL |
| CI/CD com GitHub Actions | 10 | — |
| Pipeline no repositório próprio | 6 | Actions rodando `pytest` + `ruff`, badge no README |
| Deploy em plataforma gerenciada | 8 | URL viva no README |
| AWS Cloud Practitioner Essentials | 12 | Vocabulário de nuvem para entrevista |

**Veículo:** [`spear-elicitation-simulator`](https://github.com/pedrogouveia001/spear-elicitation-simulator) —
repositório público em Python, já com suíte pytest. Estudo e prova de portfólio no mesmo artefato.

**O que não mudou.** Os pilares 11 (Containers/K8s, 84h), 12 (Cloud AWS + SAA-C03, 76h) e 13
(CI/IaC/Observabilidade, 98h) permanecem para o domínio real. O P2 não substitui nenhum deles —
tira do caminho o que trava entrevista hoje. `Docker for Absolute Beginners` foi movido do antigo
P10 para o P2 para não contar duas vezes.

**Marco novo:** *"Backend Pleno — gaps de mercado fechados"*. A partir dele, `Docker` e `CI/CD`
podem entrar no currículo e no LinkedIn (ver §4, grupo 2, de `../2 Carreira e Curriculos/LinkedIn_Overhaul_Ago2026_TEXTOS.md`).

## Certificações (eixo)

**Pagas (~US$415 + Linux opcional):** PCPP1 · AWS SAA-C03 · Terraform Associate (opcional) · LFCS (opcional, após LFS207).  
**Harvard/edX (gratuitas com certificado):** CS50x (feito) · CS50P · CS50SQL · CS50W · CS50 Cyber.  
**Coursera PCs / specs (todos integrais para certificado):** Michigan Python (5 cursos) · Meta Back-End (9) · Meta Front-End (9) · AWS SA (4) · UCSD DSA (6) · Stanford Algorithms (4) · Alberta Architecture (4) · UIUC Cloud (6) · Minnesota Testing (4) · Packt (Python/FastAPI/Next) · etc.  
**Skill / labs:** HackerRank ×3 · GitHub Foundations · freeCodeCamp ×3 · Redis University · PortSwigger · KodeKloud · TryHackMe · Frontend Mentor · LeetCode.

## Calendário (8h/sem default)

| Ritmo | Restante (~2.383h) | Conclusão aprox. |
|---|---|---|
| 8h/sem | ~298 sem úteis | **~1º semestre/2032** |
| Faseado 10→6 (CESAR)→11 | depende das pausas | **~2031** |
| 12h/sem | ~199 sem | **~meados/2030** |

**Política de corte:** não fracionar uma especialização/Professional Certificate. Se precisar reduzir prazo, mova uma formação inteira para uma trilha posterior e não declare o certificado correspondente.  
**Nunca cortar:** P1 CS50 (exceto o já feito), P2 Python/PCPP1, P4 Postgres, P13 Segurança.

## Regras que continuam valendo

1. Curso certificável; Coursera + Harvard CS50 como eixos de base.  
2. Prática só em plataforma de mercado (allowlist).  
3. Livro só complemento rotulado.  
4. Python (CS50P/avançado) antes de aprofundar OS — CS50x já cobre intro de tudo e está concluído.  
5. Frontend no P16 (depois do backend).  
6. Zero CiApp / zero posicionamento / zero inglês no tracker.  
7. Zero overlap CESAR: sem CS50 AI, sem LLM/RAG/agentes/PM no autoestudo.  
8. Projeto-fio = E-Commerce API.\n9. Especialização ou Professional Certificate marcado no tracker = **todos os cursos, avaliações e capstone obrigatórios**; não há módulos “pulados”.

## Revisão de produção (14/08/2026)

A revisão preserva o escopo amplo e inclui critérios verificáveis de engenharia de produção:

- **P3:** Linux Foundation LFS207 e LFCS opcional após laboratório de servidor.
- **P4:** laboratório em PostgreSQL real com migrations, `EXPLAIN ANALYZE`, locks, pool, backup e restore; SQLite não substitui este critério.
- **P6:** Testcontainers com PostgreSQL, testes de contrato OpenAPI e de migration na E-Commerce API.
- **P8–P9:** Redis para Python e fundamentos oficiais do Kafka pela Confluent; aplicar cache, Streams, idempotência, retry e DLQ no projeto-fio.
- **P12:** Google SRE Fundamentals; SLI/SLO, alertas, OpenTelemetry, runbook e postmortem simulado.
- **P14–P15:** C4, ADRs, falhas controladas e recuperação documentada.
- **P17:** entrega exige PostgreSQL real, fila, CI, observabilidade, SLO, carga, backup/restore e rollback, além da documentação de arquitetura.
## Revisão de certificados integrais (14/08/2026)

O tracker agora usa a carga completa da formação sempre que o objetivo é o certificado final, sem compensar sobreposição com CS50 por módulos pulados:

- Michigan Python: 5 cursos / 118h; Meta Back-End: 9 cursos / ~192h; Meta Front-End: 9 cursos / ~168h.
- UCSD DSA: 6 cursos / 182h; Stanford Algorithms: 4 cursos / 57h; Minnesota Testing: 4 cursos / 95h.
- PostgreSQL Michigan: 4 cursos / 57h; AWS Solutions Architect: 4 cursos / 62h (inclui Cloud Technical Essentials); Alberta: 4 cursos / 52h; UIUC Cloud: 6 cursos / 122h.
- Removidas apenas duas repetições internas: Introduction to Software Testing e AWS Cloud Technical Essentials, pois já são o curso 1 das respectivas formações completas.

## Revisão de trajetória de carreira e conformidade R01–R21 (14/08/2026)

Sequência de carreira confirmada (fora do tracker, mas condiciona o calendário): **CESAR School (Eng. de Software com IA) → consolidação de experiência backend/healthtech em produção (12–24 meses) → mestrado profissional em Ciência da Computação, CIn/UFPE, com tema extraído do trabalho real (confiabilidade, testes, arquitetura, segurança ou interoperabilidade)**. Nenhuma segunda graduação nessa sequência.

Auditoria completa contra a checklist R01–R21 em `Analise_Requisitos_Plano_Estudos_Backend.md` §4. Veredito: todos os Obrigatórios em PASS; dois Fortes estavam parciais e são fechados por esta revisão:

- **R17 (convivência com CESAR) — calendário oficial passa a ser o faseado, não o 8h/sem constante:** 10h/sem até a matrícula → **6h/sem durante a especialização** (~set/2026–meados/2027) → 10–11h/sem depois. O 8h/sem plano era otimista demais dentro da CESAR e conservador demais fora dela; o faseado é o que de fato vai rodar. Estimativa de conclusão não muda de faixa (~2031/2032), mas passa a ser a assumida por padrão.
- **R18 (linha de corte) — ordem explícita se o ritmo cair, nunca tocando P1 CS50 restante, P2 Python/PCPP1, P4 Postgres, P13 Segurança:**
  1. Encurtar P15 (Distribuídos) ao núcleo UIUC + performance, sem k6 avançado.
  2. Reduzir P9/P10 (Mensageria/Containers) ao essencial de produção, sem Kafka Streams aprofundado.
  3. Adiar P16 Frontend para depois do P17 Capstone — não cortar, só reordenar.
  4. Último recurso: não fechar UIUC Cloud integral. Isso quebra a regra 8 (formação sempre integral) e exige reabrir esta especificação antes de fazer — não é corte silencioso.

**P17 Capstone como base de pré-projeto de mestrado:** a mesma E-Commerce API do projeto-fio deve, na entrega final, documentar de forma auditável (ADRs, testes, métricas) pelo menos dois destes eixos — confiabilidade (P6), segurança (P13), arquitetura (P14) ou interoperabilidade (P5) — servindo de ponto de partida real para um pré-projeto de mestrado profissional no CIn. Isso não adiciona horas: é enquadramento do que o P17 já exige (SLO, backup/restore, rollback, documentação de arquitetura).

## Regeneração

```text
cd job_hunter
python build_backend_plan_v2_weeks.py
python build_backend_plan_html.py
```

Backup obrigatório. Não editar HTML à mão.  
Se CS50P também já estiver certificado, marque as tarefas no tracker (não precisa regenerar).
