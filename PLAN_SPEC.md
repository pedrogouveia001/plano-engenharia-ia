# Especificação do plano — v1 (03/09/2026)

Substitui o plano Backend/Fullstack v3 Full (18 pilares, 324 semanas, 2.527h) como itinerário único de transição para **Engenharia de IA aplicada**.

## Totais

| Métrica | Valor |
|---|---|
| Pilares | 12 |
| Semanas | 183 (8h/semana padrão) |
| Horas totais | 1.451h |
| Já concluídas (CS50x 100h + CS50P 45h) | 145h |
| Restantes | 1.306h |
| Marcos de empregabilidade | 6 |
| Formações Coursera integrais | 6 (632h) |

## Mudanças vs plano anterior

| Antes (v3 Full) | Agora (v1 IA) | Por quê |
|---|---|---|
| Backend fullstack como alvo | **Engenharia de IA aplicada** | Objetivo explícito do usuário |
| Zero IA/LLM (regra "CESAR overlap") | **IA é o núcleo do plano** | A regra antiga era incompatível com o objetivo novo; CESAR School é para engenharia de software com IA, não impede formação autônoma em IA |
| Coursera avulso permitido em algumas trilhas | **Somente formações completas** (Specialization / Professional Certificate) | Regra do usuário: certificado final obrigatório |
| FIAP, CS50, Coursera mistos sem hierarquia | **FIAP Nano Courses (gratuitos) → CS50 → Coursera** como ordem prática de prioridade | Preferência do usuário |
| Projeto-fio E-Commerce API | **decision-intelligence-ai** (dados públicos/sintéticos) | Conecta a base MCDM existente com IA; nunca dados privados |
| Docker/CI adiantados mas IA longe | **Docker/CI/API de inferência cedo** (Pilar 3) | Prática de produção cedo; requisito universal em vagas de IA |
| 2.527h em 18 pilares (redundância extrema) | 1.451h em 12 pilares | Corte de redundância mantendo profundidade de elite |
| Autonomia não explicitada | **Política de prova fechada sem IA** por marco | Transparência: separa produtividade assistida de competência independente |

## Regras vigentes

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

1. **Nunca cortar:** Pilar 2 (Python autônomo), Pilar 4 (Matemática), Pilar 10 (MLOps), Pilar 11 (LLM/RAG).
2. Encurtar Pilar 12 (Cloud/AWS) para núcleo sem certificação.
3. Adiar Pilar 5 (Deep Learning avançado) para depois de conseguir primeiro emprego em IA.
4. Último recurso: mover Pilar 9 (MLOps) para trilha pós-contratação, mas isso quebra o requisito "MLOps" das vagas — exige reabrir esta especificação antes de fazer.

## Estrutura de 12 pilares

| # | Pilar | Foco | Horas (aprox.) |
|---|---|---|---|
| 1 | Base de computação já concluída | CS50x + CS50P | 145 (pré-marcadas) |
| 2 | Python autônomo + ferramentas | Python 3 Programming + prática sem IA + Git/SQL/testes | ~160 |
| 3 | Containers, CI/CD e API de inferência | Docker, Actions, FastAPI serving | ~60 |
| 4 | Matemática para ML | Mathematics for ML (álgebra, cálculo, prob/estatística) | 94 |
| 5 | ML clássico | Machine Learning Specialization + prática Kaggle | ~150 |
| 6 | Deep Learning | Deep Learning Specialization + PyTorch tutorial + backprop manual | ~170 |
| 7 | NLP e Transformers | Hugging Face, fine-tuning, tokenização | ~80 |
| 8 | LLM Apps | Generative AI Engineering with LLMs + RAG/agentes/evals | ~150 |
| 9 | Data engineering e reprodutibilidade | versionamento de dados, pipelines, qualidade | ~60 |
| 10 | MLOps | MLOps Duke + MLflow + serving + monitoramento | ~180 |
| 11 | Capstone em produção | decision-intelligence-ai completo (RAG + evals + deploy) | ~150 |
| 12 | Cloud AWS (opcional certificação MLA) | AWS Skill Builder + prática | ~100 |

Verificação: a soma exata está em `data/plan_meta.json` (`formationHours`, `totalHours`).
