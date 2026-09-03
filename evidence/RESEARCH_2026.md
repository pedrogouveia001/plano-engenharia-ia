# Trilha 2026 — Engenheiro de IA/ML aplicado

**Data de acesso e verificação:** 03/09/2026 (UTC−03).  
**Perfil considerado:** engenheiro de produção, backend em transição, forte em PO/MCDM e legado; lacuna principal em Python escrito sem IA.  
**Regra de seleção:** no Coursera, só entram **Specializations** ou **Professional Certificates completos**; curso avulso não é eixo.

## 1. O que os três cargos significam hoje

Os títulos se sobrepõem; a distinção útil é o **objeto de responsabilidade** e não a palavra no crachá.

| Papel | Responsabilidade predominante | Evidência em fontes/vagas atuais | Barra técnica realista |
|---|---|---|---|
| **AI Engineer / Applied AI Engineer** | Transformar modelos fundacionais e serviços de IA em produto: requisitos → arquitetura → RAG/agentes/tool use → avaliações → API/UX → segurança, custo, latência e operação. Treina ou ajusta modelos quando necessário, mas o produto é a unidade de entrega. | A definição da Microsoft combina software, programação, data science/engineering, modelos e integração por API.[1] A vaga Google de Applied AI pede backend, sistemas distribuídos, infraestrutura de ML, agent harness, reasoning, skills, APIs e framework de avaliação.[3] A vaga Apple exige Python, PyTorch/TensorFlow/scikit-learn, RAG, agentes, busca híbrida, FastAPI/Flask, MLOps, CI/CD, observabilidade, guardrails e inferência em tempo real.[4] | Engenharia de software forte; Python; APIs; SQL/dados; LLM/RAG/agentes; evals; observabilidade; segurança; cloud; capacidade de ligar métrica técnica a impacto de negócio. |
| **ML Engineer** | Construir, treinar, avaliar, servir, escalar e manter modelos e pipelines tradicionais **e** generativos. A unidade é o sistema de ML reprodutível e operável. | O guia oficial Google inclui grandes datasets, código reusável, arquitetura de modelo, data/ML pipelines, MLOps, métricas, governança, treino/re-treino, serving e monitoramento.[2] Em vaga real, a Amazon pede transformar código de pesquisa em produção, deployment end-to-end, automação de análise/dados/validação/serving, confiabilidade e escala.[16] Outra vaga MLE II enfatiza experimentos estatisticamente rigorosos, Big Data, protótipos e integração de modelos em produção distribuída.[17] | Tudo do ciclo de ML: estatística/experimentos, features/dados, scikit-learn/PyTorch, distributed systems, serving, CI/CD/CT, registry, drift, custo/latência, governança. |
| **Research Engineer** | Converter perguntas novas em hipóteses, experimentos e implementações de alto desempenho; construir infraestrutura/dados/evals que torna pesquisa de fronteira possível. A unidade é conhecimento/capacidade nova com evidência experimental. | A OpenAI pede programação forte, sistemas distribuídos e implementações de DL de alto desempenho.[5] No Codex, o papel atravessa RL, dados sintéticos, graders/evals, post-training, observabilidade, reprodutibilidade e lançamento de modelos.[6] A Anthropic pede Python/PyTorch, desenho e análise de experimentos, arquitetura/algoritmos/otimizadores e treino em larga escala; GPU/Kubernetes/OS/ETL/RL aparecem como diferenciais.[7] | Base matemática/estatística mais profunda; leitura e reprodução de papers; desenho experimental; PyTorch internals; profiling; GPU/distribuído; rigor de ablação e comunicação. MSc/PhD ajuda e às vezes é pedido, mas evidência de pesquisa/engenharia pode pesar mais conforme a vaga. |

### Síntese de requisitos compartilhados em 2026

1. **Python sem muletas**, testes, debugging, Git, estruturas de dados e design de software.
2. **Fundamentos de ML/estatística:** splits corretos, leakage, métricas por custo do erro, calibração, incerteza, experimentos e análise de falhas.
3. **Deep learning/transformers:** treino, fine-tuning/PEFT, embeddings, inferência e profiling — não apenas chamadas de API.
4. **Dados e sistemas:** SQL, pipelines, batch/streaming, Docker, APIs, filas, caching, concorrência e sistemas distribuídos.
5. **Produção/MLOps:** rastreio e versionamento, CI/CD/CT, serving, observabilidade, drift, rollback, segurança, privacidade e custos.
6. **GenAI aplicado:** RAG, busca híbrida/reranking, agentes/tool calling, evals offline/online, groundedness, prompt injection, guardrails e human-in-the-loop.
7. **Produto e comunicação:** transformar problema ambíguo em hipótese, baseline e SLO; explicar trade-offs e impacto a público técnico e não técnico.

**Direção recomendada para este perfil:** mirar primeiro **AI Engineer aplicado com rigor de ML Engineer**. O background backend + PO/MCDM é vantagem para produto, decisão e trade-offs; a lacuna bloqueadora é implementar/debugar Python e ML sem IA. Research Engineer deve ser uma bifurcação posterior, não o primeiro título-alvo.

## 2. Coursera — formações completas verificadas

As horas entre parênteses são as estimativas visíveis de cada curso na página em 03/09/2026; a duração é a estimativa publicada pela própria página. A soma das horas pode divergir ligeiramente da duração anunciada por arredondamento/ritmo do aluno.

| Ordem/uso | Formação completa e composição integral | Carga/duração oficial | Certificado final | Decisão |
|---|---|---|---|---|
| **1 — base obrigatória** | **Python 3 Programming Specialization — University of Michigan**: (1) Python Basics (27h); (2) Python Functions, Files, and Dictionaries (42h); (3) Data Collection and Processing with Python (21h); (4) Python Classes and Inheritance (20h); (5) Python Project: Software Engineering and Image Manipulation (8h).[8] | 5 cursos; **3 meses** publicados; soma ≈ **118h** (≈14,8 semanas a 8h/sem). | Certificado compartilhável da Specialization, emitido após completar a série paga.[8] | Obrigatória porque ataca diretamente a dependência de IA em Python. Não “testar para pular” sem passar o gate independente abaixo. |
| **2 — ML fundamental** | **Machine Learning Specialization — DeepLearning.AI/Stanford Online**: (1) Supervised Machine Learning: Regression and Classification (33h); (2) Advanced Learning Algorithms (34h); (3) Unsupervised Learning, Recommenders, Reinforcement Learning (28h).[9] | 3 cursos; **2 meses a 10h/sem**; soma ≈ **95h** (≈11,9 semanas a 8h/sem). | Certificado compartilhável da Specialization.[9] | Obrigatória; usar para construir intuição e baselines, não para colecionar notebooks guiados. |
| **3 — DL sólido** | **Deep Learning Specialization — DeepLearning.AI**: (1) Neural Networks and Deep Learning (25h); (2) Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization (24h); (3) Structuring Machine Learning Projects (7h); (4) Convolutional Neural Networks (36h); (5) Sequence Models (37h).[10] | 5 cursos; **3 meses a 10h/sem**; soma ≈ **129h** (≈16,1 semanas a 8h/sem). | Certificado compartilhável da Specialization.[10] | Obrigatória para a barra “grande ML/AI Engineer”; dá base para diagnosticar modelos, não só integrar APIs. |
| **4A — GenAI, opção preferida agnóstica de cloud** | **Generative AI Engineering with LLMs Specialization — IBM**: (1) Generative AI and LLMs: Architecture and Data Preparation (6h); (2) Gen AI Foundational Models for NLP & Language Understanding (10h); (3) Generative AI Language Modeling with Transformers (9h); (4) Generative AI Engineering and Fine-Tuning Transformers (8h); (5) Generative AI Advanced Fine-Tuning for LLMs (9h); (6) Fundamentals of AI Agents Using RAG and LangChain (9h); (7) Project: Generative AI Applications with RAG and LangChain (9h).[11] | 7 cursos; **12 semanas a 4h/sem** (FAQ diz 13–14 semanas a 4–5h); soma ≈ **60h** (≈7,5 semanas a 8h/sem). | Certificado compartilhável/“career certificate” da IBM ao concluir toda a Specialization.[11] | Preferida para LLM internals + PEFT/RLHF/DPO + RAG/agentes. Refazer o capstone fora do ambiente guiado. |
| **4B — alternativa Azure; não somar à 4A** | **Microsoft Generative AI Engineering Professional Certificate**: (1) Getting Started with Generative AI in Azure (12h na extração da página); (2) Core Generative Models and Techniques (21h); (3) Working with Large Language Models Using Azure (21h); (4) Multimodal and Cross-modal AI Integrations (20h); (5) MLOps and Responsible AI Practices (22h).[13] | 5 cursos; **3 meses a 8h/sem**; soma ≈ **96h**. A própria página avisa custos Azure estimados de **US$40–60 mínimos**, **US$75–125 típicos**, podendo exceder US$200.[13] | Professional Certificate compartilhável da Microsoft.[13] | Escolher no lugar de 4A se as vagas-alvo são Azure. É mais cloud/produto e menos detalhado em NLP/LLM. Não fazer ambos inicialmente. |
| **5 — produção/MLOps** | **MLOps \| Machine Learning Operations Specialization — Duke University**: (1) Python Essentials for MLOps (43h); (2) DevOps, DataOps, MLOps (45h); (3) MLOps Platforms: Amazon SageMaker and Azure ML (31h); (4) MLOps Tools: MLflow and Hugging Face (26h).[12] | 4 cursos; **6 meses a 5h/sem**; soma ≈ **145h** (≈18,1 semanas a 8h/sem). | Certificado compartilhável/“career certificate” da Duke ao completar a Specialization.[12] | Fazer por último. Há alguma revisão de Python, mas o valor incremental está em testes, pipelines, cloud, MLflow, HF, Docker/CI/CD. |

### O que não empilhar

- Não somar 4A e 4B na primeira passagem: RAG, LLMs, fine-tuning e aplicação se sobrepõem.
- O **IBM AI Engineering Professional Certificate** está ativo (13 cursos; 4 meses a 10h/sem; certificado IBM), mas inclui ML, Keras/TensorFlow, PyTorch e os mesmos 7 cursos da Specialization de LLMs.[15] É uma alternativa “all-in-one” às etapas 2–4, **não** um complemento; para este perfil, a sequência Stanford/DLAI + DLS + IBM LLM tem fundamentos mais coerentes.
- O **Microsoft AI & ML Engineering Professional Certificate** também está ativo (5 cursos; 6 meses a 7h/sem; 182h somadas), mas repete fundamentos, algoritmos e cloud/capstone.[14] Só o escolheria como substituto corporativo Azure para 2–3, não em adição.
- A antiga URL da Specialization “Machine Learning Engineering for Production (MLOps)” da DeepLearning.AI agora redireciona para um curso avulso; por isso ela não foi recomendada como eixo. A opção completa atual verificada é Duke.[12]

## 3. Sequência prática a 8h/semana

**Rota principal:** 1 → 2 → 3 → 4A → 5. São cerca de **547h de conteúdo estimado**, ou 68 semanas se fossem só cursos. Reservando cerca de 160h para reconstrução, projeto e entrevistas, planeje **~88–92 semanas (20–22 meses)** a 8h/sem. Não matricular tudo de uma vez.

| Fase | Semanas-alvo | Divisão semanal | Saída obrigatória antes de avançar |
|---|---:|---|---|
| Python independente | 1–15 | 5h formação + 3h projeto | pacote Python instalável, CLI/API, testes ≥80%, tipagem/lint, sem código gerado não explicado |
| ML clássico | 16–29 | 5h formação + 3h experimento | baseline + 3 modelos; split temporal/grupo correto; relatório de leakage, calibração, custo dos erros e reprodutibilidade |
| Deep learning | 30–48 | 5h formação + 3h PyTorch | loop de treino escrito à mão, ablação, curvas, seeds, checkpoint e comparação com baseline simples |
| LLM/RAG/agentes | 49–59 | 5h formação + 3h sistema | corpus versionado; retrieval/answer eval; citações; threat model; custo/latência; fallback |
| MLOps/produção | 60–82 | 4h formação + 4h produção | imagem Docker, CI, registry, endpoint, monitoramento, canary/rollback e runbook |
| Consolidação/entrevista | 83–92 | 2h revisão + 6h testes cegos/portfolio | demo pública, postmortem, desenho de sistema e defesa oral de 15 min por claim |

## 4. Projeto-fio verificável

### “DecisionOps”: decisão multicritério + ML + GenAI para operações

Problema: prever atraso/risco/custo em ordens ou fornecedores e recomendar uma carteira/priorização com restrições e preferências MCDM, explicando evidência e incerteza.

1. **v0 — Engenharia Python:** ingestão CSV/JSON, validação, regras MCDM (TOPSIS/PROMETHEE/AHP ou método de domínio), CLI e FastAPI. Testes unitários, property-based e golden files.
2. **v1 — ML clássico:** baseline heurístico + regressão/classificação/ranking; validação temporal; calibração; custo esperado; fairness/slices; model card.
3. **v2 — DL:** previsão temporal ou classificação de texto de incidentes; loop PyTorch, ablações e comparação honesta contra v1. Só manter DL se superar baseline em métrica de negócio.
4. **v3 — GenAI:** RAG sobre SOPs/contratos/incidentes; resposta com trechos citados; ferramenta que consulta o motor MCDM; conjunto de avaliação congelado; mede recall@k/nDCG, faithfulness factual por regra/humano, taxa de recusa, latência e custo.
5. **v4 — Produção:** Docker Compose; Postgres; MLflow; GitHub Actions; deploy em uma cloud; logs/traces; monitoramento de dados/modelo/prompt; canary, rollback e runbook.
6. **v5 — Research Engineer opcional:** reproduzir um paper relevante, formular hipótese, realizar ablações com intervalos de confiança e publicar relatório de resultado negativo/positivo.

### Evidência mínima no portfólio

- **GitHub público:** uma release tagueada por fase, issues/PRs, arquitetura, decisões (ADRs), licença, SBOM e CI verde.
- **Dados/modelo:** dataset card, model card, schema, checksums, seeds e comando único (`make reproduce`) que gera tabela de métricas a partir de ambiente limpo.
- **Mercado:** Kaggle para benchmark/dataset; Hugging Face Hub/Spaces para model card/demo; MLflow para experiments/registry; Docker + GitHub Actions; uma cloud (AWS SageMaker, Azure ML ou GCP Vertex AI) para endpoint e monitoramento.
- **Qualidade:** testes unitários/integrados/contrato/carga; relatório de segurança (PII, prompt injection, secrets, dependências); SLOs p95, disponibilidade, custo por 1.000 decisões e plano de rollback.
- **Comunicação:** demo de 5–8 min, relatório técnico curto, one-pager executivo e postmortem. Cada número do currículo deve apontar para artefato reproduzível.

## 5. Critérios de domínio **independente de IA**

Não declarar uma skill antes de passar os gates abaixo. Durante o gate: sem ChatGPT/Copilot/Claude; primeiro bloco sem internet, segundo bloco permite apenas documentação oficial. Registrar tela/terminal, commit e tempo.

| Gate | Teste observável | Aprovado quando… |
|---|---|---|
| Python | 90 min, editor vazio: ler CSV/JSON, validar, transformar, criar módulo + CLI/API e ≥5 testes; depois corrigir um bug injetado. | roda do zero; testes passam; explica complexidade, exceções, mutabilidade, tipos e trade-offs sem ler resposta pronta. |
| ML | 120 min em dataset inédito: EDA mínima, split correto, baseline, pipeline, métrica e análise de erro. | não há leakage; resultado reproduz; justifica métrica e threshold pelo custo do erro; identifica limitações. |
| DL | implementar em PyTorch Dataset/DataLoader, treino/validação, checkpoint e early stopping; diagnosticar overfit/underfit. | consegue explicar gradientes, loss, regularização, shapes, memória e por que cada curva mudou. |
| LLM/RAG | montar retriever + geração a partir de API/docs, com 20 casos de teste e ataque de prompt injection. | mede retrieval separado da resposta; cita fonte; implementa recusa/fallback; relata custo/latência e falhas, não apenas “parece bom”. |
| Produção | receber imagem/repo quebrado e restaurar CI/deploy/monitoramento em 2h. | endpoint saudável, teste de contrato/carga, trace de uma requisição, rollback demonstrado e segredo fora do repo. |
| Entrevista | **15 min por claim** do CV com follow-ups “por quê?”, “como mediu?”, “o que falhou?”, “qual alternativa?”. | sustenta detalhes, desenha componentes e reconhece incerteza. Se não sustenta 15 min, rebaixar a formulação do claim. |
| Transferência | repetir uma feature pequena em stack/dataset não vistos, sem copiar o projeto-fio. | resolve com docs oficiais, escreve testes e produz decisão técnica própria. |

**Política de IA durante o aprendizado:** IA é revisora/tutora depois da tentativa; nunca autora invisível. Para cada PR: (a) tentativa própria; (b) testes próprios; (c) marcar trechos sugeridos por IA; (d) reescrever ao menos uma solução crítica sem IA; (e) explicar diff em voz alta. O objetivo não é “não usar IA”, e sim preservar autoria, debugging e julgamento.

## 6. Resultado-alvo por cargo

- **Pronto para AI Engineer aplicado:** v0–v4, gates Python/ML/LLM/produção e system design de RAG/agentes com evals, segurança, custo e fallback.
- **Pronto para ML Engineer:** acima + forte v1/v2, pipelines de dados/treino, distributed/serving, drift, calibração e experimentação estatística.
- **Candidato plausível a Research Engineer:** acima + v5 reproduzido, leitura semanal de papers, ablações, profiling/GPU/distribuído e histórico público de experimentos. Cursos não substituem essa evidência.

## Sources

[1] https://learn.microsoft.com/en-us/training/career-paths/ai-engineer — Microsoft Learn: AI engineer
[2] https://cloud.google.com/learn/certification/machine-learning-engineer — Google Cloud: Professional ML Engineer
[3] https://www.google.com/about/careers/applications/jobs/results/99475216295436998-applied-ai-software-engineer — Google: Applied AI Software Engineer
[4] https://jobs.apple.com/en-us/details/200653602-1052/ai-ml-software-engineer-ses-gen-ai-solutions-is-t — Apple: AI/ML Software Engineer
[5] https://openai.com/careers/research-engineer-san-francisco — OpenAI: Research Engineer
[6] https://openai.com/careers/research-engineer-codex-san-francisco — OpenAI: Research Engineer, Codex
[7] https://www.anthropic.com/careers/jobs/4616971008 — Anthropic: Research Engineer/Scientist, Pre-training
[8] https://www.coursera.org/specializations/python-3-programming — Coursera: Python 3 Programming Specialization
[9] https://www.coursera.org/specializations/machine-learning-introduction — Coursera: Machine Learning Specialization
[10] https://www.coursera.org/specializations/deep-learning — Coursera: Deep Learning Specialization
[11] https://www.coursera.org/specializations/generative-ai-engineering-with-llms — Coursera: Generative AI Engineering with LLMs Specialization
[12] https://www.coursera.org/specializations/mlops-machine-learning-duke — Coursera: MLOps Specialization (Duke)
[13] https://www.coursera.org/professional-certificates/microsoft-generative-ai-engineering — Coursera: Microsoft Generative AI Engineering Professional Certificate
[14] https://www.coursera.org/professional-certificates/microsoft-ai-and-ml-engineering — Coursera: Microsoft AI & ML Engineering Professional Certificate
[15] https://www.coursera.org/professional-certificates/ai-engineer — Coursera: IBM AI Engineering Professional Certificate
[16] https://www.amazon.jobs/en/jobs/3158229/sr-machine-learning-engineer-aws-applied-ai-solution — Amazon: Senior Machine Learning Engineer, AWS Applied AI
[17] https://www.amazon.jobs/en/jobs/10418966/machine-learning-engineer-ii-eu-intech-exports-emerging-and-expansions — Amazon: Machine Learning Engineer II
