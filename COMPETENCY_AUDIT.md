# Auditoria de competências — Pedro Henrique Gouveia de Souza

Data de referência: 03/09/2026.
Fontes: currículo (`Downloads/curriculo_pedro_gouveia_atualizado.md`), LinkedIn (`G:/Meu Drive/Pedro - Projetos/2 Carreira e Curriculos/linkedin_text.txt`), 58 repositórios GitHub (`evidence/project_inventory.json`), histórico CDSID/UFPE, declaração explícita do usuário.

## Contexto do perfil

- **Formação:** Engenharia de Produção UFPE (2021–2025); técnico em Mecânica IFPE; créditos de mestrado em PO trancados ago/2026; CS50x e CS50P concluídos.
- **Experiência:** 4+ anos no CDSID/UFPE (fev/2022–jul/2026) construindo sistemas de apoio multicritério à decisão; 2 softwares registrados no INPI (SADPF BR512025000931-3, FITradeoff-CB-HE 512025006292-3); resultados publicados na Springer LNBIP e apresentados no INFORMS 2024 e 27th MCDM 2024.
- **PJ própria desde jul/2026:** backend sob contrato (Python 3.12, FastAPI, SQLAlchemy 2 async, Pydantic, Alembic, PostgreSQL, JWT, Pytest).

## Impacto do uso de IA

O usuário declarou explicitamente que **todos os projetos Python foram construídos com auxílio de IA**. Isso muda a classificação defensável em duas direções:

- **Não muda:** exposição, capacidade de entregar, familiaridade com ferramentas, qualidade de especificação e revisão.
- **Muda:** fluência autônoma não é comprovada apenas pelo código existente. A classificação abaixo assume esse cenário.

A política de autonomia do plano (prova fechada sem IA por marco) existe exatamente para converter "entreguei com IA" em "sei fazer sem IA".

## Matriz de competências

| Competência | Nível defensável | Evidências | Risco de entrevista | Lacuna para Eng. de IA |
|---|---|---|---|---|
| **Modelagem matemática, PO, otimização** | Forte | SADPF, FITradeoff-CB-HE, Springe LNBIP, INFORMS, MCDM, notebooks `cdsid-colab-notebooks`, solver lp_solve, NSGA-II, Monte Carlo | Baixo — é a base real mais forte do perfil | Aplicar em contexto de IA (regularização, perda, validação) |
| **Sistemas de decisão multicritério (MCDM)** | Forte | 22 repos org `sad-mcdm` (AHP, BWM, ELECTRE, MACBETH, PROMETHEE, TOPSIS, VIKOR, SMARTS, Monte Carlo) em Python/R/JS/C++/Julia/Java | Baixo | Diferencial para "decision intelligence" em vagas aplicadas |
| **Legado desktop/web (Delphi/Object Pascal, IntraWeb, VBA)** | Forte | ~15 repos `cdsid-*` em Pascal | Médio — é habilidade rara, mas não reutilizável em IA | Nenhuma para IA; perecível |
| **SQL e bancos relacionais** | Forte | MySQL, PostgreSQL, modelagem conceitual/lógica/física, migração de esquema legado | Baixo | Otimização para data pipelines e feature stores |
| **Backend Python (FastAPI, Flask, SQLAlchemy, Pydantic)** | Em desenvolvimento — entregue **com IA** | `spear-elicitation-simulator` (pytest), `cdsid-surrogate-*`-python (Flask), trabalho PJ atual declarado | **Alto** — perguntas de implementação independente vão expor fluência real | Prova fechada sem IA (Pilar 2 do plano) |
| **Testes (pytest, integração contra banco real)** | Em desenvolvimento — com IA | `spear-elicitation-simulator`, suíte declarada no trabalho atual | Médio | Testes de modelos/evals exigem paradigma probabilístico novo |
| **Git/GitHub, PR, CODEOWNERS, SBOM** | Forte | 27 repos organizados, `THIRD-PARTY.md`, Git LFS | Baixo | CI/CD para ML (Pilar 3) |
| **Comunicação técnico-científica** | Forte | Springer, INFORMS, MCDM, SBPO | Baixo — diferencial real | Comunicar resultados de evals/observabilidade |
| **Cloud (AWS/Azure/GCP)** | Não comprovada | Nenhuma evidência | **Alto se alegado** — não inventar | Prática + AWS MLA (Pilar 12, opcional) |
| **ML clássico aplicado** | Não comprovada | Nenhum repo de ML supervisionado | **Alto se alegado** | Pilar 5 (ML Specialization + Kaggle) |
| **Deep Learning / PyTorch** | Não comprovada | — | **Alto se alegado** | Pilar 6 |
| **NLP / Transformers / LLM apps** | Não comprovada | — | **Alto se alegado** | Pilares 7–8 |
| **MLOps (serving, monitoramento, drift)** | Não comprovada | — | **Alto se alegado** | Pilar 10 |
| **Docker / Kubernetes** | Não comprovada | — | **Alto se alegado** | Pilar 3 (Docker/CI) |

## Leitura honesta

O perfil é **engenheiro de decisão com base matemática forte e backend em construção**, não engenheiro de IA. A transição tem um ativo raro: quem já construiu motores de Monte Carlo, NSGA-II e sistemas de decisão tem a base matemática e a disciplina de engenharia que faltam à maioria dos candidatos de IA. O que falta é:

1. **Prova de autonomia em Python sem IA** (Pilar 2 — primeira barreira).
2. **ML clássico aplicado com métricas e validação** (Pilar 5).
3. **Deep learning com PyTorch e implementação manual** (Pilar 6).
4. **LLM apps com evals e observabilidade** (Pilares 7–8).
5. **MLOps de ponta a ponta** (Pilar 10).

## O que não alegar em entrevista

- Docker, CI/CD, AWS, Kubernetes, Terraform, Kafka, Redis, ML, PyTorch, transformers, RAG, agentes — **nenhuma dessas skills entra no currículo antes do marco correspondente do plano** (consistente com a regra herdada "só alegar o que sustenta em 15 minutos de entrevista").
- O trabalho atual (PJ) continua sem nomear cliente, produto ou domínio (veto do cliente, documentado em `G:/Meu Drive/Pedro - Projetos/2 Carreira e Curriculos/Perfil_Plataformas_Ago2026.md`).
