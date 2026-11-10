# Jira and Scrum Summary

**Project:** SCRUM / SCAD (Scrum, team-managed) | **Sprint length:** 1 week | **Team:** 1 BA (Dasari Pallavi)

## Epics

| Epic | Purpose | Status |
|---|---|---|
| Requirements and Documentation | BRD, stories, KPI definitions | Done |
| Data Preparation | Data dictionary, cleaning | Done |
| Analysis and KPIs | EDA, KPI calculation | Done |
| AI Models | RFM, clustering, forecast | Done |
| Dashboard | Power BI build | Done |
| UAT and Release | Testing, sign-off, README | Done |

## Sprints

| Sprint | Goal | Stories completed | Points done | Outcome |
|---|---|---|---|---|
| 1 | Requirements and data understanding | Setup & Docs | 8 | Completed on schedule |
| 2 | Analysis and AI models | US-02, US-03, US-04 | 16 | Completed; US-01 & US-05 moved to Sprint 3 |
| 3 | Dashboard, UAT and release | US-01, US-05 | 8 | Completed; all 17 UAT cases passed |

## Backlog Management
- Stories prioritised with MoSCoW (Must / Should / Could) in the BRD.
- Story points estimated: US-01 (5), US-02 (3), US-03 (8), US-04 (5), US-05 (3).
- Items that slipped: US-01 and US-05 moved from Sprint 2 to Sprint 3 so data models could be finalized before building Power BI visuals.

## Retrospective (Sprint 3)

| Went well | To improve | Action |
|---|---|---|
| Automated `uat_checks.py` caught data issues early | Power BI table naming caused initial DAX errors | Standardize CSV table names immediately after Power Query load |

## Screenshots
- `images/jira_backlog.png`
- `images/jira_board.png`
- `images/jira_sprint1_complete.png`
- `images/jira_board_sprint3_progress.png`
- `images/jira_sprint3_report.png`
