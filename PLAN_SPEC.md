# Especificação do plano — v2 (03/09/2026)

Substitui a v1 (12 pilares, 183 semanas, 1.451h). Base desta revisão: **roadmaps.sh** (AI Engineer, Machine Learning, MLOps, Prompt Engineering, AI Agents) + relatório de vagas reais de 2026 (RESEARCH_2026.md).

## Totais

| Métrica | Valor |
|---|---|
| Pilares | 17 |
| Semanas | 247 (8h/semana padrão) |
| Horas totais | 1.945h |
| Já concluídas (CS50x 100h + CS50P 45h) | 145h |
| Restantes | 1.800h |
| Marcos de empregabilidade | 11 |
| Formações Coursera integrais | 6 (632h) |

## Mudanças vs v1 (baseadas nos roadmaps.sh)

| Gap identificado nos roadmaps | Ação no plano | Horas |
|---|---|---|
| Prompt Engineering como disciplina própria (CoT, ToT, ReAct, prompt tuning, debiasing) | Novo pilar 7a | 68h |
| MCP (Model Context Protocol) — host/client/server | Novo pilar 7a | 20h |
| Multimodal (visão, imagem, áudio) — ausente no v1 | Novo pilar 7b | 20h |
| Modelos open-source / self-hosted (Ollama, GGUF, quantização) | Novo pilar 7b | 16h |
| Vector DBs além de pgvector (Chroma, FAISS, Qdrant) | Novo pilar 7b | 14h |
| Reranking e comparação de embeddings | Novo pilar 7b | 12h |
| Explainable AI (SHAP/LIME) — ponte direta com MCDM | Novo pilar 7c | 30h |
| RL básico (roadmap ML lista; v1 não tinha) | Novo pilar 7c | 14h |
| Não-supervisionado aprofundado (clustering, PCA, anomalia) | Novo pilar 7c | 12h |
| DSA aplicado a ML (top-k, batching, streaming) | Pilar 13 (já criado) | 40h |
| Concorrência Python (GIL, asyncio, worker pool) | Pilar 13 | 24h |
| System design de inferência (routing, batching, fallback) | Pilar 13 | 28h |
| Orquestração de dados (Airflow) — roadmap MLOps | Expansão do pilar 10 | 16h |
| Kafka / streaming de eventos de inferência | Expansão do pilar 10 | 14h |
| Kubernetes para ML (HPA, GPU scheduling) | Expansão do pilar 10 | 20h |
| IaC (Terraform) — roadmap MLOps | Expansão do pilar 10 | 12h |
| Prometheus/Grafana (SLI/SLO de inferência) | Expansão do pilar 10 | 12h |
| Edge AI / ONNX (opcional) | Expansão do pilar 10 | 6h |

## Regras vigentes (inalteradas)

1. Coursera é eixo certificável; toda entrada é formação integral — nunca curso avulso, nunca módulo pulado.
2. FIAP Nano Courses (gratuitos) são preferidos para introdução a tópicos quando existem; CS50 é o eixo Harvard; Coursera é o eixo de formações.
3. Prática só em plataformas reconhecidas: Kaggle, Hugging Face, PyTorch tutorials, FSDL, roadmap.sh, LeetCode/HackerRank, AWS Skill Builder, docs oficiais, projeto próprio público.
4. Livro é só complemento rotulado.
5. Python autônomo antes de aprofundar ML; backend de produção cedo.
6. Frontend, inglês, posicionamento e projeto confidencial ficam fora do tracker.
7. Projeto-fio = `decision-intelligence-ai`, dados públicos/sintéticos.
8. Cada marco exige prova fechada sem IA + defesa oral.
9. Marco diz "prova mínima para candidatar-se a X" — depende de artefato, não só certificado.
10. Certificação cloud (AWS MLA) é opcional e só após prática real; versão MLA-C02, não MLA-C01.

## Política de corte

Se o ritmo cair, cortar **formações inteiras** (nunca fracionar) nesta ordem:

1. **Nunca cortar:** Pilar 2 (Python autônomo), Pilar 4 (Matemática), Pilar 8 (LLM/RAG), Pilar 13 (DSA/engenharia de sistemas).
2. Encurtar Pilar 12 (Cloud/AWS) para núcleo sem certificação.
3. Adiar Pilar 6 avançado (Deep Learning) para depois do primeiro emprego em IA.
4. Último recurso: mover Pilar 10 (MLOps) para trilha pós-contratação, mas isso quebra o requisito "MLOps" das vagas — exige reabrir esta especificação antes de fazer.
5. Os pilares 7a/7b/7c são expansion packs: se o prazo apertar, 7c (XAI/RL) é o primeiro a ser adiado inteiro.

## Estrutura de 17 pilares

| # | Pilar | Foco | Horas (aprox.) |
|---|---|---|---|
| 1 | Base de computação já concluída | CS50x + CS50P | 145 (pré-marcadas) |
| 2 | Python autônomo + ferramentas | Python 3 Programming + prática sem IA + Git/SQL/testes | ~160 |
| 3 | Containers, CI/CD e API de inferência | Docker, Actions, FastAPI serving | ~60 |
| 4 | Matemática para ML | Mathematics for ML (álgebra, cálculo, prob/estatística) | 94 |
| 5 | ML clássico | Machine Learning Specialization + prática Kaggle | ~150 |
| 6 | Deep Learning | Deep Learning Specialization + PyTorch tutorial + backprop manual | ~170 |
| 7 | NLP e Transformers | Hugging Face, fine-tuning, tokenização | ~80 |
| 7a | Prompt/context engineering e MCP | prompting sistemático, sampling, caching, MCP server próprio | 68 |
| 7b | Multimodal, open-source e vector DBs | visão/áudio, Ollama/GGUF, Chroma/FAISS/Qdrant, rerankers | 68 |
| 7c | XAI, RL e não-supervisionado | SHAP/LIME, ponte MCDM↔XAI, DQN, clustering | 62 |
| 8 | LLM Apps | Generative AI Engineering with LLMs + RAG/agentes/evals | ~150 |
| 9 | Data engineering e reprodutibilidade | versionamento de dados, pipelines, qualidade | ~60 |
| 10 | MLOps | MLOps Duke + MLflow + Airflow + Kafka + K8s + Terraform + Prometheus | ~240 |
| 11 | Capstone em produção | decision-intelligence-ai completo (RAG + evals + deploy) | ~150 |
| 12 | Cloud AWS (opcional certificação MLA) | AWS Skill Builder + prática | ~100 |
| 13 | DSA e engenharia de sistemas para IA | algoritmos aplicados a ML, concorrência, system design de inferência | 100 |

Verificação: a soma exata está em `data/plan_meta.json` (`formationHours`, `totalHours`). Total exato: **1.945h em 247 semanas**.

## Referências de roadmap

- https://roadmap.sh/ai-engineer — espinha dorsal dos pilares 7–12
- https://roadmap.sh/machine-learning — matemática, ML clássico, DL, XAI, RL
- https://roadmap.sh/mlops — Airflow, Kafka, K8s, Terraform, Prometheus, edge
- https://roadmap.sh/prompt-engineering — pilar 7a
- https://roadmap.sh/ai-agents — MCP, tool use, agentes no pilar 8
- https://roadmap.sh/system-design — pilar 13
