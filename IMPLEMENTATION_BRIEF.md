# Implementação: Plano de transição para Engenharia de IA

Data de referência: 2026-09-03 (UTC-03).

## Entregável

Transforme este repositório ainda sem commits em um site estático funcional para GitHub Pages e num plano rastreável de transição de Backend/PO para Engenheiro de IA aplicado/ML Engineer. Não faça commit nem push.

Leia primeiro `evidence/PLANO_ANTERIOR.md` e os geradores existentes. Preserve a filosofia e as regras compatíveis; substitua apenas a regra antiga que proibia IA/LLM por ser incompatível com o novo objetivo explícito.

## Perfil e diagnóstico obrigatório

- Formação: Engenharia de Produção UFPE, técnico em Mecânica; créditos de mestrado em PO; CS50x e CS50P concluídos.
- Experiência/evidência forte: sistemas de apoio multicritério à decisão, Delphi/Object Pascal, SQL/MySQL, otimização, Monte Carlo, NSGA-II, software registrado no INPI, comunicação técnico-científica.
- Experiência declarada/visível: backend Python/FastAPI/Flask/PostgreSQL/Pytest, mas o usuário informou explicitamente que TODOS os projetos Python foram construídos com auxílio de IA. Portanto, código existente prova exposição e capacidade de entregar com IA, mas não prova fluência autônoma em Python. Não classifique Python como avançado sem uma prova fechada sem IA.
- GitHub a auditar: 36 repositórios próprios em `pedrogouveia001` (26 públicos, 10 privados) + 22 na org `sad-mcdm` = 58 projetos acessíveis do escopo; não contar `code50`/`me50`. Gere `evidence/project_inventory.json` usando `gh api`, contendo apenas metadados seguros (owner/name, visibilidade, linguagem, descrição, URL, tamanho, updated_at, archived, fork). Não copie segredos nem código privado.
- LinkedIn atual documentado em `G:/Meu Drive/Pedro - Projetos/2 Carreira e Curriculos/linkedin_text.txt` e currículo em `C:/Users/pedro/Downloads/curriculo_pedro_gouveia_atualizado.md`. Não exponha telefone/e-mail/CNPJ/cliente confidencial no site público.

## Regras herdadas e novas

1. Coursera é eixo certificável. Toda entrada Coursera deve ser uma Specialization ou Professional Certificate COMPLETO. Nunca recomendar curso Coursera avulso; nunca pular curso, avaliação ou capstone. A tarefa do tracker deve dizer explicitamente “formação integral” e número de cursos.
2. Cursos da Coursera escolhidos (integrais, páginas verificadas em 03/09/2026):
   - Python 3 Programming Specialization, University of Michigan, 5 cursos, 118h (manter estimativa herdada): https://www.coursera.org/specializations/python-3-programming
   - Mathematics for Machine Learning and Data Science, DeepLearning.AI, 3 cursos, 94h: https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science
   - Machine Learning Specialization, Stanford Online + DeepLearning.AI, 3 cursos, 95h: https://www.coursera.org/specializations/machine-learning-introduction
   - Deep Learning Specialization, DeepLearning.AI, 5 cursos, usar estimativa oficial de 120h (3 meses × 10h/sem): https://www.coursera.org/specializations/deep-learning
   - Generative AI Engineering with LLMs, IBM, 7 cursos, 60h (6+10+9+8+9+9+9): https://www.coursera.org/specializations/generative-ai-engineering-with-llms
   - MLOps | Machine Learning Operations, Duke, 4 cursos, 145h (43+45+31+26): https://www.coursera.org/specializations/mlops-machine-learning-duke
3. Prática apenas em plataformas/fontes reconhecidas: Kaggle, Hugging Face, PyTorch official tutorials, Full Stack Deep Learning, roadmap.sh, LeetCode/HackerRank, AWS Skill Builder, docs oficiais, projetos públicos próprios.
4. Livro é só complemento rotulado; não é eixo.
5. Python independente antes de aprofundar ML; backend mínimo de produção (Git, testes, API, Docker, CI/CD) vem cedo.
6. Frontend, inglês, posicionamento e projeto confidencial ficam fora do tracker.
7. Evitar duplicação de formações. Coursera sempre integral mesmo se houver conteúdo repetido; sobreposição deve ser explicitamente reconhecida e usada como revisão, não como desculpa para pular módulos.
8. Novo projeto-fio público: `decision-intelligence-ai` com dados públicos/sintéticos. Evolui de baseline tabular para API, RAG com citações, avaliação, MLOps e deploy. Nunca usar dados privados.
9. Ritmo padrão 8h/semana, configurável. Semanas de no máximo 8h. Datas recalculadas.
10. Política de IA para recuperar autonomia: para cada marco, exigir uma prova fechada “sem IA” (sem Copilot/chat/geração), primeira tentativa e depuração próprias, seguida de revisão com IA somente depois do commit. Incluir defesa oral de 20–30 minutos, reimplementação e diagnóstico. O uso normal de IA é permitido e deve ser documentado; o objetivo é separar produtividade assistida de competência independente.
11. Não atribua senioridade/cargo automaticamente ao concluir cursos. Marcos devem dizer “prova mínima para candidatar-se a...” e depender de artefatos, não só certificados.
12. Certificação cloud opcional somente após prática real: AWS Certified Machine Learning Engineer – Associate. A página oficial em 03/09/2026 informa transição MLA-C01→MLA-C02; não fixar versão antiga como destino. URL: https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/

## Escopo curricular mínimo

Organize em 11–13 pilares, básico→avançado, incluindo:
- base já concluída (CS50x 100h + CS50P 45h, pre-marcados);
- Python autônomo + testes/debugging/SQL/Git;
- Docker, CI/CD e API de inferência cedo;
- álgebra linear, cálculo, probabilidade, estatística e experimentação;
- ML clássico: preparação de dados, leakage, validação, features, métricas, tuning, interpretabilidade/fairness;
- deep learning com PyTorch/TensorFlow e implementação de backprop/training loop;
- NLP/transformers/Hugging Face/fine-tuning eficiente;
- LLM apps: APIs/SDKs, embeddings, busca híbrida, reranking, RAG, structured output, tool calling, agentes;
- evals determinísticas/model-based/humanas, observabilidade, segurança contra prompt injection, privacidade, custo/latência;
- data engineering e reprodutibilidade;
- MLOps: MLflow, versionamento de dados/modelos, serving, monitoramento/drift, CI/CD, rollback;
- cloud AWS e capstone em produção.

Pilares devem combinar formação integral + prática e possuir critérios de aceite mensuráveis. Total alvo: aproximadamente 1.300–1.600h incluindo 145h já concluídas. O plano deve ser duro o bastante para formar um excelente profissional, mas cortar a redundância extrema do plano backend de 2.527h.

## Site e arquivos

Crie/atualize:
- `src/build_plan.py` → gera `data/ai_weeks.json` e `data/plan_meta.json`.
- `src/build_html.py` → gera `index.html` autocontido (sem framework/build Node), responsivo e acessível.
- `tests/test_plan.py` com invariantes de horas, IDs, HTTPS, semanas <=8h, Coursera apenas formações completas, cursos/horas esperados e projeto-fio.
- `evidence/COMPETENCY_AUDIT.md`: análise honesta do currículo, LinkedIn e 58 projetos, com matriz forte/em desenvolvimento/não comprovada e impacto do uso de IA.
- `evidence/SOURCES.md`: fontes citadas e data de acesso. Inclua Google Professional ML Engineer, AWS MLA, roadmap.sh AI/ML, Full Stack Deep Learning e as vagas Titan AI/Unstructured, além das seis páginas Coursera.
- `evidence/PLAN_SPEC.md`: regras, mudanças versus plano anterior, totais e política de corte por formações inteiras.
- `README.md`: como gerar, testar e publicar.
- `.github/workflows/pages.yml` para build+test+deploy do site no GitHub Pages.
- `requirements-dev.txt` apenas se realmente necessário.

O site deve mostrar, antes do tracker: diagnóstico pessoal, diferença AI Engineer vs ML Engineer vs Research Engineer, rota recomendada (AI Engineer aplicado com base de ML/MLOps), competências atuais/lacunas, política de autonomia sem IA, formações Coursera integrais, fontes. Depois, tracker semanal com busca/filtros, progresso ponderado por horas, localStorage com nova chave, tema, import/export, configuração de data e horas, e marcos. Preserve compatibilidade de progresso apenas para CS50x/CS50P; não reuse IDs do plano antigo para evitar colisão.

Não exiba dados privados, links para repositórios privados nem detalhes do cliente sob NDA. No inventário público do site, agregue contagens; não liste projetos privados.

## Fontes de requisitos (verificadas)

- Google PMLE: construir, avaliar, colocar em produção e otimizar; dados complexos; código repetível; modelos fundacionais; responsible AI; pipelines; MLOps; métricas; monitoramento: https://cloud.google.com/learn/certification/machine-learning-engineer
- AWS MLA: ingestão/preparo, modelagem, deploy/orquestração, monitoramento/manutenção/segurança; software engineering, CI/CD, IaC: https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html
- roadmap.sh AI Engineer: LLMs, embeddings, vector DB, RAG, agentes, multimodal, safety, evals/observabilidade e context engineering: https://roadmap.sh/ai-engineer
- roadmap.sh ML: matemática, estatística, Python, dados, ML, avaliação, DL e NLP: https://roadmap.sh/machine-learning
- Vaga Titan Applied AI Engineer: Python async/APIs, RAG híbrido, agentes, evals, observabilidade, backend auditável: https://jobs.ashbyhq.com/titan-ai/297cf9a9-289d-4cd5-a4a1-1e051f6f5d64
- Vaga Unstructured AI Engineer: sistemas-first, dados não estruturados, RAG/agentes, AWS, custo/latência/precisão, Python/SQL: https://jobs.ashbyhq.com/unstructured/9df95483-7177-4f98-850e-4abbdf530434
- Full Stack Deep Learning: https://fullstackdeeplearning.com/course/

## Validação obrigatória

Execute os geradores, `python -m unittest discover -s tests -v`, compilação Python, validação JSON e um teste de navegador/headless se disponível. Corrija falhas. Entregue diff e saída real dos testes. Não faça commit/push.