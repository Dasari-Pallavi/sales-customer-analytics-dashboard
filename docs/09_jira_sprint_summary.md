# Jira & Scrum Agile Delivery Summary

**Project Key:** `SCAD` (Sales & Customer Analytics Dashboard)  
**Methodology:** Scrum (3 Sprints × 1 Week each)  
**Role:** Business Analyst / Product Owner Proxy  

---

## 1. Epic Breakdown

| Epic ID | Epic Name | Description | Target Sprint |
| :--- | :--- | :--- | :--- |
| **SCAD-E1** | Requirements & Process Mapping | Elicit stakeholder needs, map As-Is/To-Be flows, and finalize BRD & KPI definitions. | Sprint 1 |
| **SCAD-E2** | Data Governance & Cleaning | Profile Online Retail II data (~1.06M rows), handle missing Customer IDs, and isolate returns. | Sprint 1–2 |
| **SCAD-E3** | Exploratory Analysis & AI Models | Build SQL/Python KPI queries, RFM + K-Means segmentation, and 6-month revenue forecast. | Sprint 2 |
| **SCAD-E4** | BI Dashboarding & UAT Sign-Off | Build 4-page Power BI dashboard, execute UAT test cases, and publish executive insights. | Sprint 3 |

---

## 2. Sprint Plan & Backlog Allocation

### Sprint 1: Discovery, Requirements & Data Profiling (13 Story Points)
* **Goal:** Lock down scope, document functional/non-functional requirements, and establish data cleaning rules.
* **Work Items:**
  * `SCAD-1`: Conduct stakeholder interviews and draft Problem Statement & RACI Matrix (2 pts) — **Done**
  * `SCAD-2`: Map As-Is manual Excel workflow vs. To-Be automated pipeline in draw.io (3 pts) — **Done**
  * `SCAD-3`: Author Business Requirements Document (BRD) including COGS/profit scope constraint (5 pts) — **Done**
  * `SCAD-4`: Define Data Dictionary and profile 243K missing Customer IDs & `"C"` cancellation invoices (3 pts) — **Done**

### Sprint 2: Data Engineering, KPIs & AI Modeling (16 Story Points)
* **Goal:** Produce clean analytical datasets, validate revenue KPIs, and train customer segmentation & forecasting models.
* **Work Items:**
  * `SCAD-5` (`US-01`): Build Python ETL pipeline to clean raw transactions and isolate return rates (5 pts) — **Done**
  * `SCAD-6` (`US-02`): Write SQL queries to validate Total Revenue, AOV, MoM growth, and top countries (3 pts) — **Done**
  * `SCAD-7` (`US-03`): Develop RFM scoring and K-Means clustering model to classify 4 customer segments (5 pts) — **Done**
  * `SCAD-8` (`US-04`): Train Holt-Winters time-series model to generate 6-month sales forecast (3 pts) — **Done**

### Sprint 3: Dashboard Visualization, UAT & Release (13 Story Points)
* **Goal:** Deliver interactive Power BI dashboard, complete User Acceptance Testing, and hand over decision-support insights.
* **Work Items:**
  * `SCAD-9` (`US-05`): Build 4-page Power BI dashboard with interactive slicers and AI Smart Narratives (5 pts) — **Done**
  * `SCAD-10`: Map Requirements Traceability Matrix (RTM) linking FRs to dashboard visuals (2 pts) — **Done**
  * `SCAD-11`: Execute 10 User Acceptance Testing (UAT) test cases and log stakeholder sign-off (3 pts) — **Done**
  * `SCAD-12`: Compile final Executive Insights Report and publish project documentation on GitHub (3 pts) — **Done**

---

## 3. Scrum Ceremonies Executed
* **Sprint Planning:** Prioritized backlog items with stakeholders using MoSCoW (Must-Have, Should-Have) and estimated effort using Fibonacci story points.
* **Daily Stand-Ups:** Tracked progress across `To Do`, `In Progress`, `In Review/UAT`, and `Done` columns, resolving data-quality blockers (such as handling negative quantities on cancelled invoices).
* **Sprint Review & Demo:** Demonstrated cleaned KPIs, RFM segments, and interactive Power BI views to Commercial and Marketing leads.
* **Sprint Retrospective:** Documented lessons learned, notably establishing early data constraints (absence of COGS data) in the BRD to prevent mid-sprint scope creep.

---

## 4. Visual Artifacts (Jira Proof)
* **Jira Backlog & Epics:** `../images/jira_backlog.png`
* **Active Scrum Board:** `../images/jira_board.png`
