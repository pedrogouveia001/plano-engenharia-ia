"""Gera index.html autocontido a partir dos JSONs do plano."""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\/")


def formation_cards(meta: dict) -> str:
    return "\n".join(
        f"""<article class="formation-card">
          <p class="eyebrow">{item['courseCount']} cursos · {item['hours']}h</p>
          <h3>{html.escape(item['title'])}</h3>
          <p>{html.escape(item['provider'])}</p>
          <a href="{html.escape(item['url'])}" rel="noopener noreferrer">Formação integral ↗</a>
        </article>"""
        for item in meta["formations"]
    )


def pillar_rows(meta: dict) -> str:
    return "\n".join(
        f"""<tr><td>{item['id'].replace('ai-p', 'P')}</td>
          <td><strong>{html.escape(item['title'])}</strong><br><span class="muted">{html.escape(item['goal'])}</span></td>
          <td>{item['hours']}h</td><td>{item['weeks']}</td></tr>"""
        for item in meta["pillars"]
    )


def inventory_summary() -> dict:
    path = ROOT / "evidence" / "project_inventory.json"
    if not path.exists():
        return {
            "total": 58, "public": 48, "private": 10, "owners": 2,
            "status": "escopo informado; inventário local ainda indisponível",
            "languages": [],
        }
    repos = load_json(path)
    public_repos = repos.get("publicRepos", [])
    totals = repos.get("totals", {})
    languages = Counter(r["language"] for r in public_repos if r.get("language"))
    return {
        "total": totals.get("all", 0),
        "public": totals.get("public", 0),
        "private": totals.get("private", 0),
        "owners": len({r["owner"] for r in public_repos}),
        "status": "metadados auditados via GitHub API",
        "languages": languages.most_common(5),
    }


TEMPLATE = r"""<!doctype html>
<html lang="pt-BR" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Plano rastreável de transição para AI Engineer aplicado e ML Engineer.">
  <title>Plano de transição · Engenharia de IA</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #0b1220; --surface: #111c30; --surface-2: #172641;
      --text: #edf3ff; --muted: #a9b8d1; --border: #2a3d5f;
      --accent: #5eead4; --accent-2: #60a5fa; --warn: #fbbf24;
      --ok: #34d399; --danger: #fb7185; --shadow: 0 16px 48px #02061766;
    }
    [data-theme="light"] {
      color-scheme: light;
      --bg: #f4f7fb; --surface: #ffffff; --surface-2: #eaf0f8;
      --text: #14213a; --muted: #52637d; --border: #cad6e6;
      --accent: #087f72; --accent-2: #1769aa; --warn: #9a5c00;
      --ok: #087f5b; --danger: #be123c; --shadow: 0 16px 40px #1e293b18;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
      line-height: 1.6; color: var(--text); background:
      radial-gradient(circle at 10% 0, #2563eb24, transparent 30rem),
      radial-gradient(circle at 100% 20%, #0d948824, transparent 32rem), var(--bg);
    }
    a { color: var(--accent); }
    a:hover { text-decoration-thickness: .16em; }
    :focus-visible { outline: 3px solid var(--warn); outline-offset: 3px; }
    .skip { position: absolute; left: -9999px; top: 1rem; z-index: 20; }
    .skip:focus { left: 1rem; background: var(--surface); padding: .75rem; border-radius: .5rem; }
    .wrap { width: min(1120px, calc(100% - 2rem)); margin-inline: auto; }
    .hero { padding: 5rem 0 3rem; }
    .hero-grid { display: grid; grid-template-columns: 1.5fr .8fr; gap: 2rem; align-items: end; }
    .eyebrow { margin: 0 0 .5rem; color: var(--accent); font-weight: 800; letter-spacing: .09em; text-transform: uppercase; font-size: .76rem; }
    h1, h2, h3 { line-height: 1.15; text-wrap: balance; }
    h1 { max-width: 16ch; margin: 0; font-size: clamp(2.55rem, 7vw, 5.5rem); letter-spacing: -.055em; }
    h2 { margin: 0 0 1rem; font-size: clamp(1.7rem, 4vw, 2.7rem); letter-spacing: -.035em; }
    h3 { margin: 0 0 .55rem; }
    .lead { max-width: 65ch; font-size: 1.12rem; color: var(--muted); }
    .hero-panel, .card, .formation-card, .stat, .week {
      background: color-mix(in srgb, var(--surface) 92%, transparent);
      border: 1px solid var(--border); border-radius: 1rem; box-shadow: var(--shadow);
    }
    .hero-panel, .card { padding: 1.35rem; }
    .hero-panel strong { display: block; font-size: 2rem; color: var(--accent); }
    nav { position: sticky; top: 0; z-index: 10; backdrop-filter: blur(14px); background: color-mix(in srgb, var(--bg) 82%, transparent); border-block: 1px solid var(--border); }
    nav .wrap { display: flex; gap: .4rem; align-items: center; overflow-x: auto; padding-block: .65rem; }
    nav a { color: var(--text); text-decoration: none; white-space: nowrap; padding: .45rem .7rem; border-radius: .55rem; }
    nav a:hover { background: var(--surface-2); }
    .theme-button { margin-left: auto; }
    main section { padding-block: 3.5rem; scroll-margin-top: 4rem; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    .grid.two { grid-template-columns: repeat(2, 1fr); }
    .card p:last-child, .formation-card p:last-child { margin-bottom: 0; }
    .route { border-left: .3rem solid var(--accent); }
    .muted { color: var(--muted); }
    .callout { padding: 1.2rem; background: color-mix(in srgb, var(--warn) 9%, var(--surface)); border: 1px solid color-mix(in srgb, var(--warn) 55%, var(--border)); border-radius: .85rem; }
    .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: .8rem; margin: 1.2rem 0; }
    .stat { padding: 1rem; box-shadow: none; }
    .stat strong { display: block; font-size: 1.7rem; }
    .table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: .9rem; }
    table { width: 100%; border-collapse: collapse; min-width: 680px; }
    th, td { padding: .85rem; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
    th { background: var(--surface-2); }
    tr:last-child td { border-bottom: 0; }
    .formation-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .8rem; }
    .formation-card { padding: 1rem; box-shadow: none; }
    .formation-card p { color: var(--muted); }
    .source-list { columns: 2; padding-left: 1.2rem; }
    .source-list li { break-inside: avoid; margin-bottom: .5rem; }
    .tracker-head { display: flex; justify-content: space-between; gap: 1rem; align-items: end; flex-wrap: wrap; }
    .progress-shell { height: .8rem; background: var(--surface-2); border: 1px solid var(--border); border-radius: 999px; overflow: hidden; }
    .progress-fill { height: 100%; width: 0; background: linear-gradient(90deg, var(--accent-2), var(--accent)); transition: width .2s; }
    .controls { display: grid; grid-template-columns: 1.35fr repeat(4, 1fr); gap: .7rem; padding: 1rem; margin: 1rem 0; background: var(--surface); border: 1px solid var(--border); border-radius: 1rem; }
    label { font-size: .83rem; font-weight: 700; }
    input, select, button, .button {
      width: 100%; margin-top: .3rem; min-height: 2.65rem; padding: .55rem .7rem;
      border: 1px solid var(--border); border-radius: .6rem; color: var(--text);
      background: var(--surface-2); font: inherit;
    }
    button, .button { cursor: pointer; font-weight: 750; text-align: center; text-decoration: none; }
    button:hover, .button:hover { border-color: var(--accent); }
    .actions { display: flex; flex-wrap: wrap; gap: .55rem; margin-bottom: 1rem; }
    .actions > * { width: auto; margin: 0; }
    .button input { position: absolute; opacity: 0; pointer-events: none; }
    .weeks { display: grid; gap: .75rem; }
    .week { overflow: clip; box-shadow: none; }
    .week[open] { border-color: var(--accent-2); }
    summary { display: grid; grid-template-columns: 1fr auto; gap: 1rem; align-items: center; cursor: pointer; padding: 1rem; }
    summary::marker { color: var(--accent); }
    .week-title { font-weight: 800; }
    .week-meta { color: var(--muted); font-size: .84rem; }
    .week-body { padding: 0 1rem 1rem; border-top: 1px solid var(--border); }
    .task { display: grid; grid-template-columns: auto 1fr auto; gap: .8rem; padding: 1rem 0; border-bottom: 1px solid var(--border); }
    .task:last-child { border-bottom: 0; }
    .task input { width: 1.2rem; min-height: 1.2rem; margin-top: .25rem; accent-color: var(--accent); }
    .task.done .task-name { text-decoration: line-through; color: var(--muted); }
    .task-name { font-weight: 750; }
    .task p { margin: .25rem 0; }
    .task-hours { white-space: nowrap; color: var(--accent); font-weight: 800; }
    .badge { display: inline-block; margin-right: .35rem; padding: .12rem .45rem; border-radius: 999px; background: var(--surface-2); color: var(--muted); font-size: .72rem; }
    .milestone { margin-top: 1rem; padding: 1rem; border: 1px solid var(--warn); border-radius: .7rem; background: color-mix(in srgb, var(--warn) 8%, transparent); }
    .empty { text-align: center; padding: 2rem; color: var(--muted); }
    footer { padding: 2rem 0 4rem; color: var(--muted); border-top: 1px solid var(--border); }
    @media (max-width: 850px) {
      .hero-grid, .grid, .grid.two, .formation-grid { grid-template-columns: 1fr; }
      .stats { grid-template-columns: repeat(2, 1fr); }
      .controls { grid-template-columns: repeat(2, 1fr); }
      .controls .search { grid-column: 1 / -1; }
      .source-list { columns: 1; }
    }
    @media (max-width: 520px) {
      .hero { padding-top: 3rem; }
      .stats, .controls { grid-template-columns: 1fr; }
      summary, .task { grid-template-columns: auto 1fr; }
      .task-hours { grid-column: 2; }
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { scroll-behavior: auto !important; transition: none !important; }
    }
  </style>
</head>
<body>
  <a class="skip" href="#conteudo">Pular para o conteúdo</a>
  <header class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Plano rastreável · referência 03/09/2026</p>
        <h1>Engenharia de IA aplicada.</h1>
        <p class="lead">Uma rota de Backend/PO para construir, avaliar e operar sistemas de ML e LLMs. Cursos contam como base; candidatura depende de artefatos, operação e prova independente.</p>
      </div>
      <aside class="hero-panel" aria-label="Rota recomendada">
        <span class="eyebrow">Rota recomendada</span>
        <strong>AI Engineer aplicado</strong>
        <span>com base de ML Engineering e MLOps</span>
      </aside>
    </div>
  </header>
  <nav aria-label="Navegação principal">
    <div class="wrap">
      <a href="#diagnostico">Diagnóstico</a><a href="#papeis">Papéis</a>
      <a href="#rota">Rota</a><a href="#formacoes">Formações</a>
      <a href="#plano">Plano</a><a href="#tracker">Tracker</a>
      <button class="theme-button" id="theme-toggle" type="button" aria-label="Alternar tema">Tema</button>
    </div>
  </nav>
  <main id="conteudo">
    <section id="diagnostico">
      <div class="wrap">
        <p class="eyebrow">Diagnóstico pessoal</p><h2>Boa base de decisão; autonomia em Python ainda precisa de prova.</h2>
        <div class="grid">
          <article class="card"><h3>Forte</h3><p>Engenharia de Produção, técnico em Mecânica, créditos de mestrado em PO, decisão multicritério, otimização, Monte Carlo, NSGA-II, Delphi/Object Pascal e SQL/MySQL.</p></article>
          <article class="card"><h3>Em desenvolvimento</h3><p>Python, FastAPI/Flask, PostgreSQL e Pytest têm entregas visíveis. Como todos os projetos Python tiveram auxílio de IA, eles provam exposição e capacidade assistida, não fluência autônoma avançada.</p></article>
          <article class="card"><h3>Não comprovado</h3><p>Treino e avaliação de modelos, transformers, RAG medido, segurança de LLM, pipelines MLOps, drift, serving e operação cloud. O plano exige artefatos públicos para fechar essas lacunas.</p></article>
        </div>
        <div class="stats" aria-label="Inventário de projetos">
          <div class="stat"><span>Projetos acessíveis</span><strong>__INV_TOTAL__</strong><small>__INV_STATUS__</small></div>
          <div class="stat"><span>Públicos</span><strong>__INV_PUBLIC__</strong><small>agregados no site</small></div>
          <div class="stat"><span>Privados</span><strong>__INV_PRIVATE__</strong><small>sem links ou detalhes</small></div>
          <div class="stat"><span>Escopos</span><strong>__INV_OWNERS__</strong><small>perfil + organização</small></div>
        </div>
        <p class="muted">A auditoria usa somente metadados seguros. Telefone, e-mail, CNPJ, cliente sob NDA, código e links privados não são publicados.</p>
      </div>
    </section>
    <section id="papeis">
      <div class="wrap">
        <p class="eyebrow">Escolha de papel</p><h2>Três trabalhos próximos, com evidências diferentes.</h2>
        <div class="grid">
          <article class="card"><h3>AI Engineer</h3><p>Integra modelos fundacionais em produtos: RAG, ferramentas, agentes, evals, segurança, observabilidade, custo e latência. É a entrada mais aderente ao backend e aos sistemas de decisão.</p></article>
          <article class="card"><h3>ML Engineer</h3><p>Constrói dados, features, treino, serving, versionamento, monitoramento e rollback. Exige matemática aplicada, ML clássico e MLOps além de API.</p></article>
          <article class="card"><h3>Research Engineer</h3><p>Transforma pesquisa em experimentos e implementações eficientes. Pede profundidade matemática, leitura de papers e sistemas de treino ainda não comprovados no inventário atual.</p></article>
        </div>
      </div>
    </section>
    <section id="rota">
      <div class="wrap">
        <p class="eyebrow">Decisão</p><h2>Produto primeiro, profundidade operacional crescente.</h2>
        <div class="card route">
          <h3>AI Engineer aplicado com base de ML/MLOps</h3>
          <p>Python independente vem primeiro. API, Docker e CI/CD entram cedo. Depois: matemática e ML clássico, deep learning, transformers, aplicações LLM, evals/segurança, dados, MLOps e AWS.</p>
          <p>O projeto-fio <a href="https://github.com/pedrogouveia001/decision-intelligence-ai">decision-intelligence-ai</a> evolui de baseline tabular para API, NLP, RAG com citações, avaliação, MLOps e deploy. Usa somente dados públicos ou sintéticos.</p>
        </div>
        <div class="callout">
          <strong>Política de autonomia.</strong> Em cada marco: primeira tentativa e depuração sem IA; commit; revisão com IA registrada; defesa oral de 20–30 minutos; reimplementação de um núcleo; diagnóstico de falha inédita. Uso normal de IA é permitido e documentado fora da prova.
        </div>
      </div>
    </section>
    <section id="competencias">
      <div class="wrap">
        <p class="eyebrow">Matriz de competências</p><h2>O que já sustenta entrevista e o que ainda exige evidência.</h2>
        <div class="table-wrap"><table>
          <thead><tr><th>Estado</th><th>Competências</th><th>Evidência / lacuna</th></tr></thead>
          <tbody>
            <tr><td><strong>Forte</strong></td><td>PO, MCDM, otimização, Monte Carlo, NSGA-II, SQL/MySQL, Delphi</td><td>Software registrado no INPI, sistemas reais e comunicação técnico-científica.</td></tr>
            <tr><td><strong>Em desenvolvimento</strong></td><td>Python, FastAPI, Flask, PostgreSQL, Pytest, Git, Docker</td><td>Projetos mostram entrega assistida por IA; falta prova fechada de implementação e depuração.</td></tr>
            <tr><td><strong>Não comprovada</strong></td><td>ML/DL, transformers, RAG, evals, MLOps, drift, AWS para ML</td><td>Será comprovada por métricas, artefatos, deploy, operação e defesa independente.</td></tr>
          </tbody>
        </table></div>
      </div>
    </section>
    <section id="formacoes">
      <div class="wrap">
        <p class="eyebrow">Coursera certificável</p><h2>Seis formações integrais, sem módulos pulados.</h2>
        <p class="lead">Sobreposição é revisão deliberada. Se o prazo cair, adia-se uma formação inteira; nunca se declara certificado parcial.</p>
        <div class="formation-grid">__FORMATION_CARDS__</div>
      </div>
    </section>
    <section id="fontes">
      <div class="wrap">
        <p class="eyebrow">Fontes</p><h2>Requisitos de mercado e currículos usados.</h2>
        <ul class="source-list">
          <li><a href="https://cloud.google.com/learn/certification/machine-learning-engineer">Google Professional ML Engineer</a></li>
          <li><a href="https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html">AWS ML Engineer Associate</a></li>
          <li><a href="https://roadmap.sh/ai-engineer">roadmap.sh AI Engineer</a> e <a href="https://roadmap.sh/machine-learning">Machine Learning</a></li>
          <li><a href="https://fullstackdeeplearning.com/course/">Full Stack Deep Learning</a></li>
          <li><a href="https://jobs.ashbyhq.com/titan-ai/297cf9a9-289d-4cd5-a4a1-1e051f6f5d64">Titan · Applied AI Engineer</a></li>
          <li><a href="https://jobs.ashbyhq.com/unstructured/9df95483-7177-4f98-850e-4abbdf530434">Unstructured · AI Engineer</a></li>
        </ul>
        <p><a href="evidence/SOURCES.md">Registro completo das fontes e datas de acesso</a></p>
      </div>
    </section>
    <section id="plano">
      <div class="wrap">
        <p class="eyebrow">12 pilares</p><h2>Do fundamento à operação em produção.</h2>
        <div class="stats">
          <div class="stat"><span>Total</span><strong>__TOTAL_HOURS__h</strong><small>alvo 1.300–1.600h</small></div>
          <div class="stat"><span>Concluído</span><strong>__DONE_HOURS__h</strong><small>CS50x + CS50P</small></div>
          <div class="stat"><span>Restante</span><strong>__REMAINING_HOURS__h</strong><small>a executar</small></div>
          <div class="stat"><span>Formações</span><strong>__FORMATION_HOURS__h</strong><small>Coursera integral</small></div>
        </div>
        <div class="table-wrap"><table>
          <thead><tr><th>#</th><th>Pilar e objetivo</th><th>Horas</th><th>Semanas</th></tr></thead>
          <tbody>__PILLAR_ROWS__</tbody>
        </table></div>
      </div>
    </section>
    <section id="tracker">
      <div class="wrap">
        <div class="tracker-head">
          <div><p class="eyebrow">Tracker semanal</p><h2>Execução e evidência.</h2></div>
          <p id="progress-text" aria-live="polite"></p>
        </div>
        <div class="progress-shell" role="progressbar" aria-label="Progresso ponderado por horas" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="progress-fill" id="progress-fill"></div></div>
        <div class="controls">
          <label class="search">Buscar<input id="search" type="search" placeholder="Tarefa, plataforma, critério…"></label>
          <label>Pilar<select id="pillar-filter"><option value="all">Todos</option></select></label>
          <label>Status<select id="status-filter"><option value="all">Todos</option><option value="open">Pendentes</option><option value="done">Concluídos</option></select></label>
          <label>Data inicial<input id="start-date" type="date"></label>
          <label>Horas/semana<input id="weekly-hours" type="number" min="1" max="40" step="1"></label>
        </div>
        <div class="actions">
          <button id="export" type="button">Exportar progresso</button>
          <label class="button" for="import-file">Importar progresso<input id="import-file" type="file" accept="application/json"></label>
          <button id="reset" type="button">Restaurar padrão</button>
        </div>
        <div class="weeks" id="weeks" aria-live="polite"></div>
      </div>
    </section>
  </main>
  <footer><div class="wrap">Plano gerado por Python, sem framework ou build Node. Dados públicos/sintéticos no projeto-fio.</div></footer>
  <script>
    "use strict";
    const WEEKS = __WEEKS_JSON__;
    const META = __META_JSON__;
    const LEGACY_KEY = "sad_backend_v3_full_tracker_state";
    const taskIndex = new Map(WEEKS.flatMap(w => w.tasks.map(t => [t.id, t])));
    const defaults = Object.fromEntries([...taskIndex].map(([id, task]) => [id, Boolean(task.completed)]));
    const defaultState = () => ({
      version: 1, startDate: META.defaultStartDate, weeklyHours: META.defaultWeeklyHours,
      theme: matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark",
      completed: {...defaults}
    });
    function loadState() {
      const base = defaultState();
      try {
        const raw = localStorage.getItem(META.storageKey);
        if (raw) {
          const value = JSON.parse(raw);
          if (value && value.version === 1) {
            base.startDate = /^\d{4}-\d{2}-\d{2}$/.test(value.startDate || "") ? value.startDate : base.startDate;
            base.weeklyHours = Math.min(40, Math.max(1, Number(value.weeklyHours) || 8));
            base.theme = value.theme === "light" ? "light" : "dark";
            for (const id of taskIndex.keys()) {
              if (typeof value.completed?.[id] === "boolean") base.completed[id] = value.completed[id];
            }
          }
        } else if (localStorage.getItem(LEGACY_KEY)) {
          // Compatibilidade intencional limitada: CS50x/CS50P já entram concluídos.
          // Nenhum ID antigo nem progresso de outro item é reaproveitado.
          base.migratedLegacyCs50 = true;
        }
      } catch (error) { console.warn("Estado local inválido ignorado.", error); }
      return base;
    }
    let state = loadState();
    const el = id => document.getElementById(id);
    const escapeHtml = value => String(value).replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
    const formatDate = date => new Intl.DateTimeFormat("pt-BR", {day:"2-digit", month:"short", year:"numeric"}).format(date);
    function save() { localStorage.setItem(META.storageKey, JSON.stringify(state)); }
    function setTheme(theme) {
      state.theme = theme; document.documentElement.dataset.theme = theme;
      el("theme-toggle").textContent = theme === "dark" ? "Tema claro" : "Tema escuro"; save();
    }
    function weekDates(index) {
      const start = new Date(state.startDate + "T12:00:00");
      const before = WEEKS.slice(0, index).reduce((sum, week) => sum + week.totalHours, 0);
      const from = new Date(start); from.setDate(from.getDate() + Math.floor(before / state.weeklyHours) * 7);
      const to = new Date(start); to.setDate(to.getDate() + Math.max(0, Math.ceil((before + WEEKS[index].totalHours) / state.weeklyHours) * 7 - 1));
      return formatDate(from) + " – " + formatDate(to);
    }
    function progress() {
      const done = [...taskIndex].reduce((sum, [id, task]) => sum + (state.completed[id] ? task.hours : 0), 0);
      const percent = Math.round(done / META.totalHours * 1000) / 10;
      el("progress-text").textContent = done + "h de " + META.totalHours + "h · " + percent.toLocaleString("pt-BR") + "%";
      el("progress-fill").style.width = percent + "%";
      el("progress-fill").parentElement.setAttribute("aria-valuenow", String(percent));
    }
    function matches(week) {
      const pillar = el("pillar-filter").value;
      const status = el("status-filter").value;
      const query = el("search").value.trim().toLocaleLowerCase("pt-BR");
      if (pillar !== "all" && week.pillarId !== pillar) return false;
      const done = week.tasks.every(task => state.completed[task.id]);
      if (status === "done" && !done) return false;
      if (status === "open" && done) return false;
      if (!query) return true;
      return [week.pillarTitle, week.title, ...week.tasks.flatMap(t => [t.text, t.provider, t.description, t.acceptance])]
        .join(" ").toLocaleLowerCase("pt-BR").includes(query);
    }
    function taskHtml(task) {
      const checked = state.completed[task.id] ? " checked" : "";
      const done = checked ? " done" : "";
      return '<div class="task' + done + '"><input type="checkbox" id="' + escapeHtml(task.id) + '" data-task="' + escapeHtml(task.id) + '"' + checked + '>' +
        '<div><label class="task-name" for="' + escapeHtml(task.id) + '">' + escapeHtml(task.text) + '</label>' +
        '<p><span class="badge">' + escapeHtml(task.kind) + '</span><a href="' + escapeHtml(task.url) + '" rel="noopener noreferrer">' + escapeHtml(task.provider) + '</a></p>' +
        '<p class="muted">' + escapeHtml(task.description) + '</p><p><strong>Aceite:</strong> ' + escapeHtml(task.acceptance) + '</p></div>' +
        '<span class="task-hours">' + task.hours + 'h</span></div>';
    }
    function render() {
      const visible = WEEKS.filter(matches);
      el("weeks").innerHTML = visible.length ? visible.map(week => {
        const index = WEEKS.indexOf(week);
        const done = week.tasks.filter(task => state.completed[task.id]).reduce((sum, task) => sum + task.hours, 0);
        const milestone = week.milestone ? '<aside class="milestone"><strong>' + escapeHtml(week.milestone.title) + '</strong><p>' + escapeHtml(week.milestone.evidence) + '</p><p>' + escapeHtml(week.milestone.closedProof) + '</p></aside>' : "";
        return '<details class="week"><summary><span><span class="week-title">Semana ' + String(week.sequence).padStart(3, "0") + ' · ' + escapeHtml(week.title) + '</span><br><span class="week-meta">' + escapeHtml(week.pillarTitle) + ' · ' + weekDates(index) + '</span></span><strong>' + done + '/' + week.totalHours + 'h</strong></summary><div class="week-body">' + week.tasks.map(taskHtml).join("") + milestone + '</div></details>';
      }).join("") : '<p class="empty">Nenhuma semana corresponde aos filtros.</p>';
      document.querySelectorAll("[data-task]").forEach(input => input.addEventListener("change", event => {
        state.completed[event.target.dataset.task] = event.target.checked; save(); render(); progress();
      }));
      progress();
    }
    function populatePillars() {
      for (const pillar of META.pillars) {
        const option = document.createElement("option"); option.value = pillar.id;
        option.textContent = pillar.id.replace("ai-p", "P") + " · " + pillar.title;
        el("pillar-filter").append(option);
      }
    }
    function exportState() {
      const blob = new Blob([JSON.stringify({...state, exportedAt: new Date().toISOString()}, null, 2)], {type:"application/json"});
      const link = document.createElement("a"); link.href = URL.createObjectURL(blob);
      link.download = "progresso-engenharia-ia.json"; link.click(); URL.revokeObjectURL(link.href);
    }
    async function importState(file) {
      try {
        const value = JSON.parse(await file.text());
        if (!value || value.version !== 1 || typeof value.completed !== "object") throw new Error("formato incompatível");
        for (const id of taskIndex.keys()) if (typeof value.completed[id] === "boolean") state.completed[id] = value.completed[id];
        if (/^\d{4}-\d{2}-\d{2}$/.test(value.startDate || "")) state.startDate = value.startDate;
        state.weeklyHours = Math.min(40, Math.max(1, Number(value.weeklyHours) || state.weeklyHours));
        save(); syncControls(); render();
      } catch (error) { alert("Não foi possível importar: " + error.message); }
    }
    function syncControls() {
      el("start-date").value = state.startDate; el("weekly-hours").value = state.weeklyHours; setTheme(state.theme);
    }
    populatePillars(); syncControls(); render();
    ["search", "pillar-filter", "status-filter"].forEach(id => el(id).addEventListener("input", render));
    el("start-date").addEventListener("change", event => { if (event.target.value) { state.startDate = event.target.value; save(); render(); } });
    el("weekly-hours").addEventListener("change", event => { state.weeklyHours = Math.min(40, Math.max(1, Number(event.target.value) || 8)); event.target.value = state.weeklyHours; save(); render(); });
    el("theme-toggle").addEventListener("click", () => setTheme(state.theme === "dark" ? "light" : "dark"));
    el("export").addEventListener("click", exportState);
    el("import-file").addEventListener("change", event => { if (event.target.files[0]) importState(event.target.files[0]); event.target.value = ""; });
    el("reset").addEventListener("click", () => { if (confirm("Restaurar o padrão e apagar o progresso deste plano?")) { state = defaultState(); save(); syncControls(); render(); } });
  </script>
</body>
</html>
"""


def main() -> None:
    weeks = load_json(DATA_DIR / "ai_weeks.json")
    meta = load_json(DATA_DIR / "plan_meta.json")
    inventory = inventory_summary()
    output = (
        TEMPLATE
        .replace("__WEEKS_JSON__", safe_json(weeks))
        .replace("__META_JSON__", safe_json(meta))
        .replace("__FORMATION_CARDS__", formation_cards(meta))
        .replace("__PILLAR_ROWS__", pillar_rows(meta))
        .replace("__TOTAL_HOURS__", str(meta["totalHours"]))
        .replace("__DONE_HOURS__", str(meta["completedHours"]))
        .replace("__REMAINING_HOURS__", str(meta["remainingHours"]))
        .replace("__FORMATION_HOURS__", str(meta["formationHours"]))
        .replace("__INV_TOTAL__", str(inventory["total"]))
        .replace("__INV_PUBLIC__", str(inventory["public"]))
        .replace("__INV_PRIVATE__", str(inventory["private"]))
        .replace("__INV_OWNERS__", str(inventory["owners"]))
        .replace("__INV_STATUS__", html.escape(inventory["status"]))
    )
    (ROOT / "index.html").write_text(output, encoding="utf-8")
    print(f"Site gerado: index.html ({len(weeks)} semanas, {meta['totalHours']}h)")


if __name__ == "__main__":
    main()
