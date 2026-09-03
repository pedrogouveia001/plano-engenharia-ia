# -*- coding: utf-8 -*-
"""Invariantes do Plano de transição para Engenharia de IA."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS_PATH = ROOT / "data" / "ai_weeks.json"
META_PATH = ROOT / "data" / "plan_meta.json"

# Seis formações Coursera integrais esperadas (title -> (cursos, horas))
EXPECTED_FORMATIONS = {
    "Python 3 Programming Specialization": (5, 118),
    "Mathematics for Machine Learning and Data Science": (3, 94),
    "Machine Learning Specialization": (3, 95),
    "Deep Learning Specialization": (5, 120),
    "Generative AI Engineering with LLMs": (7, 60),
    "MLOps | Machine Learning Operations": (4, 145),
}

PROJECT_THREAD = "decision-intelligence-ai"
COMPLETED_FAMILIAR_HOURS = 145  # CS50x 100h + CS50P 45h


class TestPlan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.weeks = json.loads(WEEKS_PATH.read_text(encoding="utf-8"))
        cls.meta = json.loads(META_PATH.read_text(encoding="utf-8"))

    # ---- Estrutura básica ------------------------------------------------

    def test_plan_generated(self):
        self.assertGreater(len(self.weeks), 0)
        self.assertGreater(self.meta["totalHours"], 0)

    def test_totals_match(self):
        total = sum(t["hours"] for w in self.weeks for t in w["tasks"])
        done = sum(t["hours"] for w in self.weeks for t in w["tasks"] if t.get("completed"))
        self.assertEqual(total, self.meta["totalHours"])
        self.assertEqual(done, self.meta["completedHours"])

    def test_week_hours_cap(self):
        for w in self.weeks:
            self.assertLessEqual(w["totalHours"], 8, f"semana {w['id']} passa de 8h")
            self.assertEqual(sum(t["hours"] for t in w["tasks"]), w["totalHours"],
                             f"semana {w['id']}: totalHours diverge das tarefas")

    def test_unique_week_ids(self):
        ids = [w["id"] for w in self.weeks]
        self.assertEqual(len(ids), len(set(ids)))

    def test_ids_sequential(self):
        seqs = [w["sequence"] for w in self.weeks]
        self.assertEqual(seqs, list(range(1, len(seqs) + 1)))

    def test_https_links(self):
        for w in self.weeks:
            for t in w["tasks"]:
                if t.get("url"):
                    self.assertTrue(t["url"].startswith("https://"),
                                    f"link não-https na tarefa {t['id']}: {t['url']}")

    def test_tasks_have_provider(self):
        for w in self.weeks:
            for t in w["tasks"]:
                self.assertTrue(t.get("provider"), f"tarefa {t['id']} sem provider")

    def test_tasks_have_acceptance(self):
        for w in self.weeks:
            for t in w["tasks"]:
                self.assertTrue(t.get("acceptance"),
                                f"tarefa {t['id']} sem critério de aceite")

    # ---- Formações Coursera integrais ------------------------------------

    def test_six_coursera_formations(self):
        formations = {f["title"]: (f["courseCount"], f["hours"])
                      for f in self.meta["formations"]}
        for name, (courses, hours) in EXPECTED_FORMATIONS.items():
            self.assertIn(name, formations, f"formação ausente: {name}")
            self.assertEqual(formations[name][0], courses, name)
            self.assertEqual(formations[name][1], hours, name)
        self.assertEqual(len(formations), len(EXPECTED_FORMATIONS))

    def test_formations_complete_flag(self):
        for f in self.meta["formations"]:
            self.assertTrue(f["complete"], f"{f['title']} não é formação integral")

    def test_coursera_links(self):
        for f in self.meta["formations"]:
            self.assertTrue(f["url"].startswith("https://www.coursera.org/"), f["title"])

    def test_formations_referenced_in_tasks(self):
        formation_ids = {f["id"] for f in self.meta["formations"]}
        referenced = {t.get("formationId") for w in self.weeks for t in w["tasks"]
                      if t.get("formationId")}
        missing = formation_ids - referenced
        self.assertEqual(missing, set(), f"formações não referenciadas em semanas: {missing}")

    # ---- Pré-concluído ---------------------------------------------------

    def test_completed_hours(self):
        self.assertEqual(self.meta["completedHours"], COMPLETED_FAMILIAR_HOURS)

    def test_completed_tasks_marked(self):
        done = [t for w in self.weeks for t in w["tasks"] if t.get("completed")]
        self.assertGreater(len(done), 0)
        self.assertEqual(sum(t["hours"] for t in done), COMPLETED_FAMILIAR_HOURS)

    # ---- Projeto-fio ------------------------------------------------------

    def test_project_thread(self):
        pt = self.meta["projectThread"]
        self.assertEqual(pt["name"], PROJECT_THREAD)
        self.assertTrue(pt["url"].startswith("https://github.com/"))
        self.assertIn("públicos", pt["dataPolicy"].lower())

    def test_project_thread_in_tasks(self):
        texts = " ".join(t.get("text", "") for w in self.weeks for t in w["tasks"]).lower()
        self.assertIn(PROJECT_THREAD, texts)

    # ---- Marcos -----------------------------------------------------------

    def test_milestones_present(self):
        ms = [w for w in self.weeks if w.get("milestone")]
        self.assertEqual(len(ms), self.meta["milestoneCount"])
        self.assertGreater(len(ms), 0)

    def test_milestones_have_title_and_evidence(self):
        for w in self.weeks:
            m = w.get("milestone")
            if m:
                self.assertTrue(m.get("title"), f"marco sem título na semana {w['id']}")
                self.assertTrue(m.get("evidence"), f"marco sem evidência na semana {w['id']}")
                self.assertIn("sem ia", m.get("closedProof", "").lower(),
                              f"marco {w['id']} sem prova fechada sem IA")

    # ---- Pilares ----------------------------------------------------------

    def test_pillar_count(self):
        self.assertGreaterEqual(self.meta["pillarCount"], 11)
        self.assertLessEqual(self.meta["pillarCount"], 13)
        self.assertEqual(len(self.meta["pillars"]), self.meta["pillarCount"])

    def test_pillars_ordered(self):
        seen = []
        for w in self.weeks:
            if w["pillarId"] not in seen:
                seen.append(w["pillarId"])
        pillar_order = [p["id"] for p in self.meta["pillars"]]
        self.assertEqual(seen, pillar_order)

    # ---- Meta -------------------------------------------------------------

    def test_meta_fields(self):
        for key in ("schemaVersion", "title", "referenceDate", "defaultStartDate",
                    "defaultWeeklyHours", "storageKey", "totalHours", "completedHours",
                    "remainingHours", "totalWeeks", "pillarCount", "milestoneCount",
                    "formations", "projectThread", "autonomyPolicy"):
            self.assertIn(key, self.meta)

    def test_storage_key_not_old(self):
        self.assertNotEqual(self.meta["storageKey"], "sad_backend_v3_full_tracker_state")

    def test_remaining_hours(self):
        self.assertEqual(self.meta["remainingHours"],
                         self.meta["totalHours"] - self.meta["completedHours"])

    def test_target_hours_range(self):
        self.assertGreaterEqual(self.meta["totalHours"], 1300)
        self.assertLessEqual(self.meta["totalHours"], 1600)

    def test_autonomy_policy_exists(self):
        self.assertTrue(self.meta["autonomyPolicy"])

    def test_meta_totals_consistent(self):
        self.assertEqual(self.meta["totalWeeks"], len(self.weeks))
        self.assertEqual(self.meta["formationHours"],
                         sum(f["hours"] for f in self.meta["formations"]))

    # ---- Inventário -------------------------------------------------------

    def test_inventory_totals(self):
        inv = json.loads((ROOT / "evidence" / "project_inventory.json")
                         .read_text(encoding="utf-8"))
        self.assertEqual(inv["totals"]["all"], 58)
        self.assertEqual(inv["totals"]["public"], 48)
        self.assertEqual(inv["totals"]["private"], 10)
        self.assertEqual(inv["totals"]["personalOwned"], 36)
        self.assertEqual(inv["totals"]["orgSadMcdm"], 22)

    def test_inventory_no_private_names(self):
        inv = json.loads((ROOT / "evidence" / "project_inventory.json")
                         .read_text(encoding="utf-8"))
        pub = inv.get("publicRepos", [])
        for r in pub:
            self.assertFalse(r.get("private"), r["name"])
        self.assertEqual(inv.get("privateCount"),
                         inv["totals"]["all"] - len(pub))


if __name__ == "__main__":
    unittest.main()
