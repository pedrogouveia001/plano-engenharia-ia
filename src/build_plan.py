"""Gera o plano semanal de transição para Engenharia de IA.

Fonte de verdade: IMPLEMENTATION_BRIEF.md. O gerador é determinístico e usa
somente a biblioteca padrão. O HTML consome os JSONs gerados.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REFERENCE_DATE = "2026-09-03"
DEFAULT_START_DATE = "2026-09-07"
DEFAULT_WEEKLY_HOURS = 8
STORAGE_KEY = "ai_engineering_transition_v1"
EXPECTED_TOTAL_HOURS = 1945


def activity(
    ident: str,
    title: str,
    provider: str,
    url: str,
    hours: int,
    description: str,
    acceptance: str,
    *,
    kind: str = "prática",
    completed: bool = False,
    formation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": ident, "title": title, "provider": provider, "url": url,
        "hours": hours, "description": description, "acceptance": acceptance,
        "kind": kind, "completed": completed, "formation": formation,
    }


def coursera(
    ident: str,
    title: str,
    provider: str,
    url: str,
    hours: int,
    course_count: int,
    topics: str,
) -> dict[str, Any]:
    formation = {
        "id": ident, "title": title, "provider": provider, "url": url,
        "hours": hours, "courseCount": course_count,
        "type": "Specialization", "complete": True,
    }
    return activity(
        ident, title, f"Coursera · {provider}", url, hours,
        f"Formação integral de {course_count} cursos ({hours}h), incluindo todas as avaliações e capstone obrigatórios. {topics}",
        f"Concluir os {course_count} cursos, avaliações e capstone; anexar certificado da formação integral e índice dos artefatos.",
        kind="formação integral", formation=formation,
    )


AUTONOMY = (
    "Prova fechada sem IA: primeira tentativa e depuração próprias, sem chat, "
    "Copilot ou geração; commit somente após concluir. Depois do commit, usar IA "
    "para revisão registrada. Defender por 20–30 min, reimplementar um núcleo e "
    "diagnosticar uma falha inédita."
)


PILLARS: list[dict[str, Any]] = [
    {
        "id": "ai-p01", "title": "Base de computação já concluída", "level": "base",
        "goal": "Registrar a base certificada sem confundi-la com fluência autônoma atual.",
        "activities": [
            activity(
                "ai-p01-cs50x", "CS50x — Introduction to Computer Science", "Harvard CS50",
                "https://cs50.harvard.edu/x/", 100,
                "Fundamentos de computação, C, algoritmos, memória, Python, SQL, web e projeto final.",
                "Certificado e projeto final verificáveis.", kind="formação concluída", completed=True,
            ),
            activity(
                "ai-p01-cs50p", "CS50P — Introduction to Programming with Python", "Harvard CS50",
                "https://cs50.harvard.edu/python/", 45,
                "Python, testes, arquivos, bibliotecas, orientação a objetos e projeto final.",
                "Certificado e projeto final verificáveis.", kind="formação concluída", completed=True,
            ),
        ],
    },
    {
        "id": "ai-p02", "title": "Python autônomo, testes, SQL e Git",
        "level": "base → intermediário",
        "goal": "Converter exposição assistida em fluência independente demonstrável.",
        "activities": [
            coursera(
                "ai-p02-michigan-python", "Python 3 Programming Specialization", "University of Michigan",
                "https://www.coursera.org/specializations/python-3-programming", 118, 5,
                "Python, coleções, APIs, orientação a objetos e projeto final.",
            ),
            activity(
                "ai-p02-python-katas", "Python sem assistência: 30 problemas graduais", "LeetCode + HackerRank",
                "https://www.hackerrank.com/domains/python", 24,
                "Resolver parsing, coleções, iteradores, OOP, erros e algoritmos sem geração de código.",
                "30 soluções autorais; ≥80% dos testes na primeira sessão e diário de erros.",
            ),
            activity(
                "ai-p02-debug-tests", "Debugging e testes em Python", "pytest + documentação oficial",
                "https://docs.pytest.org/en/stable/", 14,
                "Testes unitários, fixtures, mocks criteriosos, debugger, profiling e leitura de traceback.",
                "Corrigir 10 falhas sem IA e entregar suíte com cobertura de ramos críticos.",
            ),
            activity(
                "ai-p02-sql", "SQL aplicado e PostgreSQL", "PostgreSQL oficial + HackerRank",
                "https://www.postgresql.org/docs/current/tutorial-sql.html", 12,
                "JOIN, CTE, janela, transação, índice e EXPLAIN em PostgreSQL real.",
                "20 consultas e relatório de dois planos EXPLAIN ANALYZE.",
            ),
            activity(
                "ai-p02-git", "Git de trabalho: histórico, revisão e recuperação", "Git oficial",
                "https://git-scm.com/docs/gittutorial", 12,
                "Branch, rebase, conflito, bisect, reflog e revisão de diff.",
                "Repositório-lab com conflito resolvido, bisect e recuperação via reflog.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a estágio/júnior Python",
            "evidence": "CLI em Python, suíte pytest, consultas PostgreSQL e histórico Git auditável.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p03", "title": "Backend mínimo de produção para inferência",
        "level": "intermediário",
        "goal": "Colocar API, testes, container, CI/CD e deploy antes do aprofundamento em ML.",
        "activities": [
            activity(
                "ai-p03-api", "API de inferência com FastAPI", "FastAPI oficial",
                "https://fastapi.tiangolo.com/tutorial/", 20,
                "Contrato OpenAPI, validação, async quando justificado, erros, healthcheck e logging.",
                "API tipada com /health, /predict, tratamento de erro e OpenAPI versionado.",
            ),
            activity(
                "ai-p03-tests", "Testes de contrato e integração", "pytest + HTTPX",
                "https://fastapi.tiangolo.com/tutorial/testing/", 12,
                "Testes unitários, integração com PostgreSQL e contrato de API.",
                "Pipeline reproduzível com testes de sucesso, erro, schema e migration.",
            ),
            activity(
                "ai-p03-docker", "Docker e Compose reproduzíveis", "Docker oficial",
                "https://docs.docker.com/get-started/", 12,
                "Imagem mínima, usuário sem privilégio, healthcheck, volumes e Compose.",
                "Build limpo e aplicação + PostgreSQL sobem com um comando.",
            ),
            activity(
                "ai-p03-ci", "CI/CD básico", "GitHub Actions",
                "https://docs.github.com/en/actions", 10,
                "Lint, testes, build de imagem, cache e proteção de branch.",
                "Workflow público verde em push e pull request.",
            ),
            activity(
                "ai-p03-deploy", "Deploy do baseline", "AWS Skill Builder + docs oficiais",
                "https://skillbuilder.aws/", 10,
                "Deploy gerenciado, variáveis, logs, healthcheck e rollback simples.",
                "URL pública, runbook e rollback testado; nenhum dado privado.",
            ),
            activity(
                "ai-p03-closed", "Prova fechada de backend", "Projeto público próprio",
                "https://github.com/pedrogouveia001", 8, AUTONOMY,
                "Reconstruir endpoint, teste e Dockerfile; defender decisões e depurar falha surpresa.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a Backend Python com deploy",
            "evidence": "API pública conteinerizada, CI verde, banco real, contrato e rollback.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p04", "title": "Matemática, estatística e experimentação",
        "level": "base → intermediário",
        "goal": "Reativar a base quantitativa e ligá-la ao comportamento de modelos.",
        "activities": [
            coursera(
                "ai-p04-math", "Mathematics for Machine Learning and Data Science", "DeepLearning.AI",
                "https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science", 94, 3,
                "Álgebra linear, cálculo, probabilidade e estatística.",
            ),
            activity(
                "ai-p04-numpy", "Implementações numéricas com NumPy", "NumPy oficial",
                "https://numpy.org/learn/", 18,
                "Vetores, matrizes, gradientes, decomposições e estabilidade numérica.",
                "Notebook reproduzível implementando regressão e descida do gradiente.",
            ),
            activity(
                "ai-p04-experiments", "Estatística e experimentação", "Kaggle Learn",
                "https://www.kaggle.com/learn", 10,
                "Amostragem, intervalo, teste, poder, tamanho de efeito e múltiplas comparações.",
                "Plano e análise de experimento sintético com hipóteses pré-registradas.",
            ),
            activity(
                "ai-p04-closed", "Prova fechada quantitativa", "Projeto público próprio",
                "https://github.com/pedrogouveia001", 6, AUTONOMY,
                "Derivar gradiente, explicar viés/variância e diagnosticar experimento inválido.",
            ),
        ],
    },
    {
        "id": "ai-p05", "title": "Machine Learning clássico", "level": "intermediário",
        "goal": "Construir baselines confiáveis antes de deep learning e LLMs.",
        "activities": [
            coursera(
                "ai-p05-ml", "Machine Learning Specialization", "Stanford Online + DeepLearning.AI",
                "https://www.coursera.org/specializations/machine-learning-introduction", 95, 3,
                "Aprendizado supervisionado, não supervisionado, recomendação e boas práticas.",
            ),
            activity(
                "ai-p05-kaggle", "Pipeline tabular completo", "Kaggle",
                "https://www.kaggle.com/competitions", 28,
                "EDA, split, preprocessing, baseline, experimento e submissão reproduzível.",
                "Pipeline sem leakage, seeds fixas e relatório comparando ≥3 modelos.",
            ),
            activity(
                "ai-p05-validation", "Validação, leakage e métricas", "scikit-learn oficial",
                "https://scikit-learn.org/stable/model_selection.html", 15,
                "Cross-validation adequada, desbalanceamento, calibração e threshold.",
                "Teste automatizado contra leakage e justificativa de métrica/threshold.",
            ),
            activity(
                "ai-p05-responsible", "Tuning, interpretabilidade e fairness", "scikit-learn oficial",
                "https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html", 14,
                "Busca de hiperparâmetro, erro por fatia, importância e análise de equidade.",
                "Model card com limites, subgrupos, incerteza e decisão de não uso.",
            ),
            activity(
                "ai-p05-thread", "decision-intelligence-ai v1: baseline tabular", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 8,
                "Dados públicos/sintéticos, baseline e API; sem dados privados.",
                "Dataset documentado, baseline reproduzível, API e relatório de erro.",
            ),
            activity(
                "ai-p05-closed", "Prova fechada de ML clássico", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Reimplementar pipeline, explicar escolhas e corrigir leakage introduzido.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a estágio/júnior de ML",
            "evidence": "Baseline tabular público, validação sem leakage, model card e API.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p06", "title": "Deep Learning e treinamento",
        "level": "intermediário → avançado",
        "goal": "Entender e implementar treinamento, sem depender apenas de APIs de alto nível.",
        "activities": [
            coursera(
                "ai-p06-dl", "Deep Learning Specialization", "DeepLearning.AI",
                "https://www.coursera.org/specializations/deep-learning", 120, 5,
                "Redes neurais, otimização, projetos de ML, CNNs e modelos de sequência.",
            ),
            activity(
                "ai-p06-pytorch", "Fundamentos e training loop em PyTorch", "PyTorch official tutorials",
                "https://pytorch.org/tutorials/beginner/basics/intro.html", 16,
                "Tensores, Dataset/DataLoader, autograd, módulos, otimização e checkpoint.",
                "Training loop com validação, checkpoint, device e curva de aprendizado.",
            ),
            activity(
                "ai-p06-backprop", "Backpropagation do zero", "Projeto público próprio",
                "https://github.com/pedrogouveia001", 8,
                "Rede pequena em NumPy, gradiente analítico e gradient check.",
                "Erro relativo do gradient check <1e-5 e explicação linha a linha.",
            ),
            activity(
                "ai-p06-loop", "Diagnóstico de treinamento", "Full Stack Deep Learning",
                "https://fullstackdeeplearning.com/course/", 8,
                "Overfit de lote, baseline, curvas, ablação e depuração de dados/modelo.",
                "Checklist aplicado a três falhas deliberadas com causa comprovada.",
            ),
            activity(
                "ai-p06-tensorflow", "Leitura comparativa em TensorFlow", "TensorFlow oficial",
                "https://www.tensorflow.org/tutorials", 4,
                "Mapear tensores, autograd, módulo, treino e serving entre frameworks.",
                "Reproduzir uma rede pequena e documentar equivalências com PyTorch.",
            ),
            activity(
                "ai-p06-closed", "Prova fechada de deep learning", "Projeto público próprio",
                "https://github.com/pedrogouveia001", 4, AUTONOMY,
                "Implementar training loop e diagnosticar ausência de convergência.",
            ),
        ],
    },
    {
        "id": "ai-p07", "title": "NLP, transformers e fine-tuning eficiente",
        "level": "avançado",
        "goal": "Dominar o caminho do texto bruto à avaliação de um transformer adaptado.",
        "activities": [
            activity(
                "ai-p07-hf", "Trilha NLP/Transformers", "Hugging Face Learn",
                "https://huggingface.co/learn/nlp-course/", 20,
                "Tokenização, datasets, transformers, treinamento e compartilhamento de modelos.",
                "Completar capítulos e publicar model card + dataset card.",
            ),
            activity(
                "ai-p07-internals", "Transformer e tokenização por dentro", "PyTorch + Hugging Face",
                "https://pytorch.org/tutorials/beginner/transformer_tutorial.html", 12,
                "Attention, máscaras, posições, BPE e limites de contexto.",
                "Implementar attention pequena e explicar formas/tensores sem consulta.",
            ),
            activity(
                "ai-p07-peft", "Fine-tuning eficiente", "Hugging Face PEFT",
                "https://huggingface.co/docs/peft/", 16,
                "LoRA/PEFT, preparação de dados, treino, avaliação e custo.",
                "Comparar baseline e PEFT com métricas, memória, latência e custo.",
            ),
            activity(
                "ai-p07-eval", "Avaliação de NLP", "Hugging Face Evaluate",
                "https://huggingface.co/docs/evaluate/", 10,
                "Métricas, conjuntos de desafio, erro por fatia e análise qualitativa.",
                "Relatório de erro com ≥50 casos rotulados e limites explícitos.",
            ),
            activity(
                "ai-p07-thread", "decision-intelligence-ai v2: componente NLP", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 8,
                "Classificação ou extração em dados públicos/sintéticos.",
                "Endpoint, model card, avaliação e rastreabilidade do dataset.",
            ),
            activity(
                "ai-p07-closed", "Prova fechada de NLP", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Explicar attention, reimplementar pipeline e diagnosticar tokenização errada.",
            ),
        ],
    },
    {
        "id": "ai-p08", "title": "Aplicações com LLMs, RAG e agentes",
        "level": "avançado",
        "goal": "Construir sistemas auditáveis com recuperação, citações e ferramentas.",
        "activities": [
            coursera(
                "ai-p08-ibm", "Generative AI Engineering with LLMs", "IBM",
                "https://www.coursera.org/specializations/generative-ai-engineering-with-llms", 60, 7,
                "LLMs, transformers, fine-tuning, RAG e engenharia generativa.",
            ),
            activity(
                "ai-p08-api", "APIs/SDKs e structured output", "Documentação oficial dos provedores",
                "https://platform.openai.com/docs/guides/structured-outputs", 12,
                "Mensagens, streaming, schema, retry, idempotência e limites.",
                "Cliente tipado com schema validado, retry limitado e testes determinísticos.",
            ),
            activity(
                "ai-p08-retrieval", "Embeddings e busca híbrida", "Hugging Face + PostgreSQL/pgvector",
                "https://github.com/pgvector/pgvector", 16,
                "Chunking, metadados, dense+sparse, filtros e conjunto de avaliação.",
                "Recall@k medido em conjunto rotulado; índice reproduzível.",
            ),
            activity(
                "ai-p08-rag", "Reranking e RAG com citações", "Full Stack Deep Learning",
                "https://fullstackdeeplearning.com/llm-bootcamp/", 14,
                "Reranker, montagem de contexto, abstention, citação e cache.",
                "Respostas citam trechos recuperados; faithfulness e cobertura medidas.",
            ),
            activity(
                "ai-p08-agents", "Tool calling e agentes limitados", "roadmap.sh AI Engineer",
                "https://roadmap.sh/ai-engineer", 12,
                "Ferramentas tipadas, estado, limite de passos, autorização e falhas.",
                "Agente com ≥2 ferramentas, orçamento, timeout e trilha de auditoria.",
            ),
            activity(
                "ai-p08-thread", "decision-intelligence-ai v3: RAG citado", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 8,
                "RAG sobre fontes públicas, API e interface mínima de inspeção.",
                "Corpus público, citações verificáveis, eval set e relatório de custo.",
            ),
            activity(
                "ai-p08-closed", "Prova fechada de LLM apps", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Reimplementar retrieval, explicar falhas e corrigir citação inválida.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a AI Engineer aplicado júnior",
            "evidence": "RAG público com busca híbrida, citações, eval set, API e limites operacionais.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p09", "title": "Evals, observabilidade, segurança e eficiência",
        "level": "avançado",
        "goal": "Tratar qualidade, ataque, privacidade, custo e latência como requisitos de produto.",
        "activities": [
            activity(
                "ai-p09-deterministic", "Evals determinísticas", "Full Stack Deep Learning",
                "https://fullstackdeeplearning.com/course/", 12,
                "Schema, retrieval, regras, golden set, regressão e slices.",
                "Suite versionada roda em CI e bloqueia três regressões conhecidas.",
            ),
            activity(
                "ai-p09-judges", "Evals model-based e humanas", "Documentação oficial + projeto",
                "https://platform.openai.com/docs/guides/evals", 10,
                "Rubrica, juiz calibrado, concordância humana e análise de viés.",
                "Comparar juiz e dois avaliadores; relatar discordância e incerteza.",
            ),
            activity(
                "ai-p09-observability", "Observabilidade de LLM", "OpenTelemetry oficial",
                "https://opentelemetry.io/docs/", 10,
                "Traços, métricas de qualidade, tokens, latência, erro e alertas.",
                "Dashboard local + trace de uma requisição sem registrar dados sensíveis.",
            ),
            activity(
                "ai-p09-security", "Prompt injection e segurança", "OWASP GenAI",
                "https://genai.owasp.org/", 12,
                "Injeção direta/indireta, exfiltração, tool abuse, allowlist e isolamento.",
                "Threat model e 20 testes adversariais com controles e risco residual.",
            ),
            activity(
                "ai-p09-privacy", "Privacidade e governança", "NIST AI RMF",
                "https://www.nist.gov/itl/ai-risk-management-framework", 8,
                "Minimização, retenção, PII, licença, provenance e human-in-the-loop.",
                "Data flow, política de retenção e teste de redaction; só dados públicos/sintéticos.",
            ),
            activity(
                "ai-p09-efficiency", "Custo e latência", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6,
                "Caching, batching, modelos menores, timeout e orçamento.",
                "Benchmark p50/p95, custo por tarefa e decisão com trade-off explícito.",
            ),
            activity(
                "ai-p09-closed", "Red team e prova fechada", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Defender threat model, reproduzir ataque e implementar mitigação sob tempo.",
            ),
        ],
    },
    {
        "id": "ai-p10", "title": "Data engineering e reprodutibilidade",
        "level": "intermediário → avançado",
        "goal": "Tornar dados, features e experimentos repetíveis e auditáveis.",
        "activities": [
            activity(
                "ai-p10-contracts", "Contratos e validação de dados", "Pandera oficial",
                "https://pandera.readthedocs.io/", 10,
                "Schema, nulidade, faixa, categoria, drift de schema e quarantine.",
                "Contrato falha cedo para cinco corrupções deliberadas.",
            ),
            activity(
                "ai-p10-pipeline", "Pipeline de ingestão e preparo", "PostgreSQL + Python oficiais",
                "https://www.postgresql.org/docs/current/", 12,
                "Ingestão idempotente, incremental, lineage e partições.",
                "Duas execuções geram o mesmo estado e possuem auditoria por lote.",
            ),
            activity(
                "ai-p10-repro", "Ambiente e experimentos reproduzíveis", "Python + Docker oficiais",
                "https://docs.python.org/3/tutorial/venv.html", 8,
                "Dependências travadas, configuração, seeds e artefatos.",
                "Clone limpo reproduz métrica dentro de tolerância documentada.",
            ),
            activity(
                "ai-p10-versioning", "Versionamento de dados e modelos", "DVC oficial",
                "https://dvc.org/doc", 8,
                "Dataset, modelo, métricas e cache remoto simulado.",
                "Reproduzir duas versões e comparar dados/modelo/métrica.",
            ),
            activity(
                "ai-p10-features", "Feature pipeline", "scikit-learn oficial",
                "https://scikit-learn.org/stable/modules/compose.html", 8,
                "Transformações treináveis, consistência treino-serving e leakage.",
                "Mesmo input gera mesmas features offline/online; teste automatizado.",
            ),
            activity(
                "ai-p10-docs", "Testes e documentação de dados", "Great Expectations docs",
                "https://docs.greatexpectations.io/", 6,
                "Qualidade, freshness, volume, ownership e incidentes.",
                "Checks em CI e dataset card com origem/licença/limites.",
            ),
            activity(
                "ai-p10-closed", "Prova fechada de pipeline", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 4, AUTONOMY,
                "Depurar quebra de schema e reconstruir etapa idempotente.",
            ),
        ],
    },
    {
        "id": "ai-p11", "title": "MLOps, serving e monitoramento",
        "level": "avançado",
        "goal": "Operar o ciclo de vida de modelos com CI/CD, métricas, drift e rollback.",
        "activities": [
            coursera(
                "ai-p11-mlops", "MLOps | Machine Learning Operations", "Duke University",
                "https://www.coursera.org/specializations/mlops-machine-learning-duke", 145, 4,
                "DevOps, plataformas de ML, modelos em produção e MLOps aplicado.",
            ),
            activity(
                "ai-p11-orchestration", "Orquestração de pipelines (Airflow)", "Apache Airflow docs",
                "https://airflow.apache.org/docs/", 16,
                "DAGs, schedules, sensors, XCom, backfill, retries e alertas — orquestração de pipelines de dados/ML.",
                "DAG que roda ingestão + treino + eval em 3 etapas, com retry e alerta documentados.",
            ),
            activity(
                "ai-p11-streaming", "Kafka e streaming de dados", "Confluent + Kafka docs",
                "https://kafka.apache.org/documentation/", 14,
                "Topics, partitions, consumer groups, streaming de eventos de inferência, DLQ e exatamente-once.",
                "Consumer Kafka que processa eventos de inferência com idempotência; cenário de falha documentado.",
            ),
            activity(
                "ai-p11-k8s", "Kubernetes para ML", "Kubernetes docs + kubectl",
                "https://kubernetes.io/docs/home/", 20,
                "Pods, deployments, services, probes, HPA, GPU scheduling básico e rodando um modelo de inferência.",
                "Serviço de inferência no K8s local (kind/minikube) com HPA e rollout observado.",
            ),
            activity(
                "ai-p11-iac", "Infra como código (Terraform)", "Terraform docs",
                "https://developer.hashicorp.com/terraform/docs", 12,
                "Providers, state, variables, outputs, plan/apply, drift e módulos reutilizáveis.",
                "Infra do projeto-fio provisionada por Terraform; destruída e recriada reproduzindo o mesmo estado.",
            ),
            activity(
                "ai-p11-prometheus", "Monitoring: Prometheus e Grafana", "Prometheus + Grafana docs",
                "https://prometheus.io/docs/introduction/overview/", 12,
                "Métricas customizadas, alertas, dashboards, histogramas de latência e SLIs/SLOs de inferência.",
                "Dashboard Grafana do projeto-fio com 5 métricas (incluindo custo por 1k inferências).",
            ),
            activity(
                "ai-p11-edge", "Edge AI e servindo modelos em dispositivos (opcional)", "TFLite + ONNX Runtime",
                "https://onnxruntime.ai/", 6,
                "Quantização, ONNX export, TFLite/PyTorch Mobile e inferência em CPU — quando vale a pena.",
                "Modelo do projeto-fio exportado para ONNX e inferindo 2x mais rápido no CPU local.",
                kind="prática opcional",
            ),
            activity(
                "ai-p11-mlflow", "Tracking e registry", "MLflow oficial",
                "https://mlflow.org/docs/latest/", 10,
                "Experimentos, artefatos, lineage, registry e promoção.",
                "Experimento reproduzível e promoção baseada em gate de métrica.",
            ),
            activity(
                "ai-p11-monitor", "Serving, monitoramento e drift", "Full Stack Deep Learning",
                "https://fullstackdeeplearning.com/course/", 12,
                "Serving batch/online, canary, qualidade, data/concept drift e alerta.",
                "Canary local; alerta de drift e resposta documentada.",
            ),
            activity(
                "ai-p11-cicd", "CI/CD de modelo e rollback", "GitHub Actions + MLflow",
                "https://docs.github.com/en/actions", 9,
                "Teste de dados/modelo, avaliação, aprovação e rollback.",
                "Release bloqueia regressão e rollback restaura versão anterior.",
            ),
            activity(
                "ai-p11-closed", "Prova fechada de MLOps", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 8, AUTONOMY,
                "Diagnosticar drift, promover modelo e executar rollback sem assistência.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a ML Engineer júnior",
            "evidence": "Pipeline versionado, registry, serving, monitoramento, CI/CD e rollback demonstrados.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p12", "title": "AWS e capstone em produção", "level": "avançado",
        "goal": "Integrar ML, LLM, dados, operação e segurança em um sistema público defensável.",
        "activities": [
            activity(
                "ai-p12-aws", "Laboratórios AWS para ML", "AWS Skill Builder",
                "https://skillbuilder.aws/", 20,
                "IAM mínimo, S3, ECR, compute/serving, logs, rede e orçamento.",
                "Ambiente efêmero por IaC, least privilege, budget e teardown verificado.",
            ),
            activity(
                "ai-p12-cert", "Decisão de certificação AWS MLA", "AWS Certification",
                "https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/", 4,
                "Opcional e somente após os labs: avaliar prontidão e a versão vigente do exame; não fixar MLA-C01.",
                "Gap assessment contra o guia vigente; decisão go/no-go registrada.",
                kind="certificação opcional",
            ),
            activity(
                "ai-p12-capstone", "decision-intelligence-ai v4: capstone", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 40,
                "Baseline tabular, API, RAG citado, evals, MLflow, CI/CD e deploy com dados públicos/sintéticos.",
                "Demo pública, arquitetura, testes, eval set, model/system cards e rastreabilidade ponta a ponta.",
            ),
            activity(
                "ai-p12-slo", "Carga, SLO, custo e capacidade", "k6 + OpenTelemetry",
                "https://grafana.com/docs/k6/latest/", 12,
                "Teste de carga, p95, disponibilidade, orçamento de erro e custo por tarefa.",
                "SLO medido; limite de capacidade e plano de custo documentados.",
            ),
            activity(
                "ai-p12-sec", "Revisão de segurança e privacidade", "OWASP GenAI + NIST AI RMF",
                "https://genai.owasp.org/", 8,
                "Threat model final, segredos, dependências, retenção e abuso de ferramentas.",
                "Checklist, testes adversariais e riscos residuais publicados sem dados sensíveis.",
            ),
            activity(
                "ai-p12-runbook", "Runbook, incidentes e rollback", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6,
                "On-call simulado, backup/restore, degradação segura e postmortem.",
                "Game day executado; restauração e rollback cronometrados.",
            ),
            activity(
                "ai-p12-closed", "Banca fechada do capstone", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Defesa de 30 min, reimplementação de núcleo e diagnóstico de incidente surpresa.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima para candidatar-se a AI Engineer aplicado / ML Engineer",
            "evidence": "Capstone público operável com dados seguros, avaliação, observabilidade, segurança, custo e rollback.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p07a", "title": "Prompt engineering, context engineering e MCP",
        "level": "intermediário",
        "goal": "Dominar prompting sistemático, gestão de contexto e o protocolo MCP — requisitos explícitos dos roadmaps AI Engineer e AI Agents.",
        "activities": [
            activity(
                "ai-p07a-prompting", "Prompt engineering sistemático", "roadmap.sh Prompt Engineering",
                "https://roadmap.sh/prompt-engineering", 16,
                "Zero/few-shot, CoT, ToT, ReAct, self-consistency, step-back, prompt tuning, debiasing, ensembling, calibração de confiabilidade e melhoria de precisão.",
                "10 técnicas aplicadas ao projeto-fio com comparativo antes/depois documentado.",
            ),
            activity(
                "ai-p07a-sampling", "Parâmetros de sampling e output control", "Docs oficiais (OpenAI/Anthropic/Google)",
                "https://platform.openai.com/docs/guides/text-generation", 8,
                "Temperature, top-k, top-p, max tokens, stop sequences, repetition/frequency/presence penalty, streaming e comportamento determinístico.",
                "Benchmarks comparando configurações em tarefa do projeto-fio; documentar escolha com justificativa.",
            ),
            activity(
                "ai-p07a-structured", "Structured output e context engineering", "Docs OpenAI + Anthropic + Google",
                "https://docs.anthropic.com/en/docs/build-with-claude/context-windows", 12,
                "JSON/XML/CSV tipado, system/role/contextual prompting, gestão de contexto: janela, compressão, isolamento, caching, compaction e falhas de contexto.",
                "Schema estruturado com fallback em produção simulada; testes de regressão de prompt versionados.",
            ),
            activity(
                "ai-p07a-caching", "Prompt caching e otimização de tokens", "Anthropic + OpenAI docs",
                "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching", 6,
                "Cache de prompt, cobrança por token, escolha de modelo, batching de requisições e otimização de custo por 1k decisões.",
                "Benchmark antes/depois do caching com economia medida no projeto-fio.",
            ),
            activity(
                "ai-p07a-mcp", "Model Context Protocol (MCP)", "Hugging Face MCP Course",
                "https://huggingface.co/learn/mcp-course/unit0/introduction", 20,
                "MCP host, client e server; transporte, descoberta de ferramentas, permissões e segurança; integrar com o projeto-fio.",
                "Servidor MCP próprio publicado com 2 ferramentas do projeto-fio, cliente conectado e testes de permissão.",
            ),
            activity(
                "ai-p07a-closed", "Prova fechada de prompting/contexto", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Código autoral + relatório de 3 melhorias de prompt medindo qualidade e custo.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima de prompting/contexto/MCP",
            "evidence": "Biblioteca de prompts versionada, servidor MCP próprio, benchmarks de sampling/caching e defesa oral.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p07b", "title": "Multimodal, modelos open-source e vector DBs",
        "level": "avançado",
        "goal": "Estender para além de texto puro e rodar modelos abertos localmente — requisitos dos roadmaps AI Engineer e AI Agents.",
        "activities": [
            activity(
                "ai-p07b-multimodal", "Multimodal: visão, imagem e áudio", "Hugging Face + OpenAI/Anthropic/Google docs",
                "https://huggingface.co/learn/computer-vision-course/unit0/welcome", 20,
                "Vision API, image understanding, image generation, Whisper (speech-to-text), TTS, casos de uso de imagem/vídeo/áudio e limites.",
                "Pipeline multimodal no projeto-fio: 1 tarefa de visão + 1 de áudio, com avaliação e custo medidos.",
            ),
            activity(
                "ai-p07b-opensource", "Modelos open-source e self-hosted", "Hugging Face Hub + Ollama",
                "https://ollama.com/docs", 16,
                "Gemma, Qwen, Llama, Mistral; quantização (GGUF), escolha de modelo, inferência local com Ollama, custos zero vs API e trade-offs de qualidade.",
                "Modelo aberto rodando localmente no projeto-fio; comparativo de qualidade/latência/custo vs API.",
            ),
            activity(
                "ai-p07b-vector-db", "Vector databases além de pgvector", "Chroma, FAISS, Qdrant, Weaviate, LanceDB",
                "https://docs.trychroma.com/", 14,
                "Comparar 2 alternativas além de pgvector: índice HNSW, filtros metadados, persistência, throughput e custo de memória.",
                "Benchmark de recall/latência/memória em dataset do projeto-fio; ADR documentando escolha.",
            ),
            activity(
                "ai-p07b-embeddings", "Embedding models e reranking", "Sentence Transformers + Cohere docs",
                "https://www.sbert.net/", 12,
                "Sentence transformers, open-embeddings, Cohere/Gemini embedding, rerankers, matryoshka e distância/cosine.",
                "Matriz comparativa de 4 embeddings no eval set do projeto-fio com custo e latência.",
            ),
            activity(
                "ai-p07b-closed", "Prova fechada multimodal/open-source", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "ADR atualizado e defesa oral de 15 min.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima de multimodal e open-source",
            "evidence": "Pipeline multimodal no projeto, modelo aberto local rodando, benchmark de vector db e defesa.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p07c", "title": "Explainable AI, RL e aprendizado não-supervisionado",
        "level": "avançado",
        "goal": "Complementos do roadmap Machine Learning: interpretabilidade (SHAP/LIME — ponte direta com seu MCDM), RL básico e não-supervisionado aprofundado.",
        "activities": [
            activity(
                "ai-p07c-xai", "Explainable AI: SHAP e LIME", "SHAP docs + Interpretml",
                "https://shap.readthedocs.io/en/latest/", 20,
                "SHAP values, LIME, feature importance, dependência, interação, explicação global vs local e limites.",
                "Relatório de interpretabilidade em modelo do projeto-fio; explicar 5 decisões de um modelo tabular.",
            ),
            activity(
                "ai-p07c-xai-mcdm", "Ponte MCDM ↔ XAI", "Projeto público próprio (sad-mcdm)",
                "https://github.com/sad-mcdm/sad-mcdm-lib", 10,
                "Conectar pesos ROC/importância MCDM com SHAP; comparar explicações multicritério com explicações de ML.",
                "Notebook público integrando um método MCDM (ex. PROMETHEE) com SHAP em dataset público.",
            ),
            activity(
                "ai-p07c-unsup", "Não-supervisionado aprofundado", "scikit-learn oficial",
                "https://scikit-learn.org/stable/modules/clustering.html", 12,
                "Clustering (k-means, DBSCAN, hierárquico), PCA, t-SNE, autoencoders e detecção de anomalia.",
                "Duas análises exploratórias completas com escolha justificada de algoritmo.",
            ),
            activity(
                "ai-p07c-rl", "Reinforcement learning básico", "OpenAI Gymnasium + PyTorch",
                "https://gymnasium.farama.org/", 14,
                "Q-learning, DQN, policy gradient básico e actor-critic introdutório — nível roadmap ML, sem aprofundar em pesquisa.",
                "Agente DQN treinado em ambiente simples com curva de aprendizado documentada.",
            ),
            activity(
                "ai-p07c-closed", "Prova fechada de XAI/RL", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 6, AUTONOMY,
                "Notebook autoral e defesa oral de 15 min.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima de XAI e aprendizados avançados",
            "evidence": "Relatório SHAP, integração MCDM↔XAI, análise não-supervisionada e agente RL básico documentados.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p13", "title": "DSA e engenharia de sistemas para IA",
        "level": "intermediário → avançado",
        "goal": "Estruturas de dados, complexidade, concorrência e system design de inferência — base para PyTorch internals, batching/streaming e entrevista técnica de IA.",
        "activities": [
            activity(
                "ai-p13-dsa-core", "Estruturas de dados e algoritmos aplicados a ML", "LeetCode (trilha ML-adjacente) + NeetCode",
                "https://neetcode.io/practice", 40,
                "Arrays, hashmaps, heap, árvore, grafo, DP e complexidade — foco em problemas que aparecem em sistemas de ML (batching, top-k, janela deslizante, deduplicação).",
                "60 problemas resolvidos sem IA; 15 deles com notebook explicando a relação com um problema real de ML (ex.: top-k retrieval, sliding window em streaming).",
            ),
            activity(
                "ai-p13-concurrency", "Concorrência e paralelismo em Python", "Docs oficiais Python (asyncio, threading, multiprocessing)",
                "https://docs.python.org/3/library/asyncio.html", 24,
                "GIL, asyncio, thread pool, process pool, filas, lock/semáforo, race conditions — essencial para serving de modelos e pipelines de dados.",
                "Implementar um worker pool que processa batch de inferência com backpressure; benchmark e explicação de quando usar async vs threads vs processos.",
            ),
            activity(
                "ai-p13-system-design", "System design de sistemas de IA", "Roadmap.sh System Design + padrões de inferência",
                "https://roadmap.sh/system-design", 28,
                "Arquitetura de inferência online: roteamento, batching dinâmico, cache de embedding e resposta, fallback, rate limit, multi-modelo, multi-região e degradação.",
                "Desenho de arquitetura (diagrama + ADR) de um sistema de inferência em produção, publicado no projeto-fio e defendido por 20 min.",
            ),
            activity(
                "ai-p13-closed", "Prova fechada de DSA e system design", "Projeto público próprio",
                "https://github.com/pedrogouveia001/decision-intelligence-ai", 8, AUTONOMY,
                "Código autoral, análise de complexidade e defesa oral de 20 min.",
            ),
        ],
        "milestone": {
            "title": "Prova mínima de base de engenharia para entrevista de IA",
            "evidence": "60 problemas de algoritmos, worker pool implementado, desenho de arquitetura de inferência e defesa oral.",
            "closedProof": AUTONOMY,
        },
    },
    {
        "id": "ai-p14", "title": "Certificações oficiais de IA e cloud",
        "level": "avançado",
        "goal": "Credenciais reconhecidas de mercado (AWS, Google Cloud, NVIDIA) após prática real — certificado sem projeto não sustenta entrevista, então cada exame vem depois da prática correspondente.",
        "activities": [
            activity(
                "ai-p14-aws-aif", "AWS Certified AI Practitioner (AIF-C01)", "AWS Certification",
                "https://aws.amazon.com/certification/certified-ai-practitioner/", 20,
                "Exame foundational de IA/ML/GenAI na AWS (US$100, 65 questões, 90 min). Cobre fundamentos de IA/ML, GenAI, foundation models, responsible AI e segurança/governança. Vale como vocabulário e porta de entrada; não é o exame de engenharia.",
                "Simulados ≥85% consistente; exame agendado e aprovado.",
                kind="certificação",
            ),
            activity(
                "ai-p14-aws-mla", "AWS Certified Machine Learning Engineer – Associate (MLA-C02)", "AWS Certification",
                "https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/", 40,
                "Exame associate de ML engineering (US$150, ~65 questões). Valida ingestão/preparo de dados, desenvolvimento de modelos, deploy/orquestração, monitoramento e segurança — com GenAI e agentes na versão MLA-C02. Só tentar após o Pilar 10 (MLOps) e prática real em SageMaker/Bedrock.",
                "Simulados ≥85%; exame aprovado; badge no LinkedIn e GitHub.",
                kind="certificação",
            ),
            activity(
                "ai-p14-gcp-pmle", "Google Cloud Professional Machine Learning Engineer (PMLE)", "Google Cloud Certification",
                "https://cloud.google.com/learn/certification/machine-learning-engineer", 40,
                "Exame professional de ML Engineer (US$200, ~60 questões, 120 min). Valida arquitetura de soluções de IA/ML, dados, pipelines, serving, MLOps, monitoramento e responsible AI. Google recomenda 3+ anos de experiência — a prática do plano substitui parte disso, mas o exame é exigente.",
                "Simulados ≥80%; exame aprovado; badge no LinkedIn e GitHub.",
                kind="certificação",
            ),
            activity(
                "ai-p14-nvidia-aiio", "NVIDIA-Certified Associate AI Infrastructure and Operations (NCA-AIIO)", "NVIDIA Certification",
                "https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/", 16,
                "Exame associate de infraestrutura de IA (US$125, 50 questões, 60 min). Cobre GPU, accelerated computing, networking, data center e operação de workloads de IA. Diferencial raro para quem quer atuar perto de infraestrutura/inferência de modelos; opcional se o foco for aplicado.",
                "Simulados ≥80%; exame aprovado; badge no LinkedIn e GitHub.",
                kind="certificação",
            ),
        ],
        "milestone": {
            "title": "Prova mínima de credencial de IA reconhecida de mercado",
            "evidence": "Pelo menos AWS MLA-C02 ou Google PMLE aprovado; AIF-C01 e NCA-AIIO como complementos opcionais.",
            "closedProof": AUTONOMY,
        },
    },
]


def split_activity(item: dict[str, Any]) -> list[dict[str, Any]]:
    """Divide uma atividade em blocos estáveis de até 8h."""
    parts = math.ceil(item["hours"] / DEFAULT_WEEKLY_HOURS)
    remaining = item["hours"]
    result = []
    for part in range(1, parts + 1):
        hours = min(DEFAULT_WEEKLY_HOURS, remaining)
        result.append({
            "id": f"{item['id']}-s{part:02d}", "activityId": item["id"],
            "title": item["title"], "part": part, "parts": parts,
            "text": f"{item['title']} · etapa {part}/{parts}",
            "provider": item["provider"], "url": item["url"], "hours": hours,
            "description": item["description"], "acceptance": item["acceptance"],
            "kind": item["kind"], "completed": item["completed"],
            "formationId": item["formation"]["id"] if item["formation"] else None,
        })
        remaining -= hours
    return result


def pack_pillar(pillar: dict[str, Any], sequence_start: int) -> list[dict[str, Any]]:
    weeks: list[dict[str, Any]] = []
    tasks: list[dict[str, Any]] = []
    used = 0

    def flush() -> None:
        nonlocal tasks, used
        if not tasks:
            return
        sequence = sequence_start + len(weeks)
        weeks.append({
            "id": f"ai-w{sequence:03d}", "sequence": sequence,
            "pillarId": pillar["id"], "pillarTitle": pillar["title"],
            "level": pillar["level"], "title": tasks[0]["title"],
            "totalHours": used, "tasks": tasks,
        })
        tasks = []
        used = 0

    for item in pillar["activities"]:
        for segment in split_activity(item):
            remaining = segment["hours"]
            segment_piece = 1
            while remaining:
                space = DEFAULT_WEEKLY_HOURS - used
                if space == 0:
                    flush()
                    space = DEFAULT_WEEKLY_HOURS
                take = min(space, remaining)
                task = dict(segment)
                if take != segment["hours"]:
                    task["id"] = f"{segment['id']}-p{segment_piece}"
                task["hours"] = take
                tasks.append(task)
                used += take
                remaining -= take
                segment_piece += 1
                if used == DEFAULT_WEEKLY_HOURS:
                    flush()
    flush()
    if pillar.get("milestone"):
        weeks[-1]["milestone"] = pillar["milestone"]
    return weeks


def validate_source() -> None:
    activity_ids: set[str] = set()
    formation_ids: set[str] = set()
    for pillar in PILLARS:
        for item in pillar["activities"]:
            if item["id"] in activity_ids:
                raise ValueError(f"ID de atividade duplicado: {item['id']}")
            activity_ids.add(item["id"])
            if not re.fullmatch(r"ai-p\d{2}[a-z]?-[a-z0-9-]+", item["id"]):
                raise ValueError(f"ID inválido: {item['id']}")
            if not item["url"].startswith("https://"):
                raise ValueError(f"URL não HTTPS: {item['url']}")
            if "Coursera" in item["provider"]:
                formation = item["formation"]
                if not formation or not formation["complete"] or formation["courseCount"] < 2:
                    raise ValueError(f"Coursera avulso proibido: {item['title']}")
                if formation["id"] in formation_ids:
                    raise ValueError(f"Formação duplicada: {formation['id']}")
                formation_ids.add(formation["id"])


def build() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    validate_source()
    weeks: list[dict[str, Any]] = []
    pillar_summaries: list[dict[str, Any]] = []
    formations: list[dict[str, Any]] = []
    for pillar in PILLARS:
        pillar_weeks = pack_pillar(pillar, len(weeks) + 1)
        weeks.extend(pillar_weeks)
        hours = sum(item["hours"] for item in pillar["activities"])
        pillar_summaries.append({
            "id": pillar["id"], "title": pillar["title"], "level": pillar["level"],
            "goal": pillar["goal"], "hours": hours, "weeks": len(pillar_weeks),
            "milestone": pillar.get("milestone"),
        })
        formations.extend(item["formation"] for item in pillar["activities"] if item["formation"])

    all_tasks = [task for week in weeks for task in week["tasks"]]
    total_hours = sum(task["hours"] for task in all_tasks)
    completed_hours = sum(task["hours"] for task in all_tasks if task["completed"])
    if total_hours != EXPECTED_TOTAL_HOURS:
        raise ValueError(f"Total inesperado: {total_hours}h")
    if any(week["totalHours"] > DEFAULT_WEEKLY_HOURS for week in weeks):
        raise ValueError("Semana acima de 8h")
    meta = {
        "schemaVersion": 1, "title": "Plano de transição para Engenharia de IA",
        "referenceDate": REFERENCE_DATE, "defaultStartDate": DEFAULT_START_DATE,
        "defaultWeeklyHours": DEFAULT_WEEKLY_HOURS, "storageKey": STORAGE_KEY,
        "totalHours": total_hours, "completedHours": completed_hours,
        "remainingHours": total_hours - completed_hours, "totalWeeks": len(weeks),
        "pillarCount": len(PILLARS),
        "milestoneCount": sum(bool(p.get("milestone")) for p in PILLARS),
        "formationHours": sum(f["hours"] for f in formations),
        "formations": formations, "pillars": pillar_summaries,
        "projectThread": {
            "name": "decision-intelligence-ai",
            "url": "https://github.com/pedrogouveia001/decision-intelligence-ai",
            "dataPolicy": "Somente dados públicos ou sintéticos; nunca dados privados.",
        },
        "autonomyPolicy": AUTONOMY,
    }
    return weeks, meta


def main() -> None:
    weeks, meta = build()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "ai_weeks.json").write_text(
        json.dumps(weeks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (DATA_DIR / "plan_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Plano gerado: {meta['pillarCount']} pilares | {meta['totalWeeks']} semanas | "
        f"{meta['totalHours']}h ({meta['completedHours']}h concluídas, "
        f"{meta['remainingHours']}h restantes) | {meta['milestoneCount']} marcos"
    )


if __name__ == "__main__":
    main()
