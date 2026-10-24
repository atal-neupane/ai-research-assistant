# AI Research Assistant: Project Spec (Draft v0.1)
## Problem
Researchers in fast-moving subfields spend hours reading papers to answer simple questions and hand-building tables that compare reported results. General-purpose tools give fluent answers but rarely show how reliable those answers are.
## Goal
An open-source RAG assistant for one subfield (3D Gaussian Splatting compression) that answers questions with passage-level citations, extracts structured results (datasets, metrics, numbers) across papers, and ships with a published evaluation harness that measures how well it works.
## Users
* **Primary:** me, for baseline comparisons in my thesis.
* **Secondary:** peers and labs doing literature reviews who want to point it at their own paper collection.
## Scope (v1)
**In:** 40-60 research papers; cited Q&A with abstention; results-table extraction and cross-paper comparison tables; evaluation harness with CI regression checks; FastAPI service, Docker, simple UI.
**Out:** claim verification, citation graphs, model fine-tuning, user accounts, paywalled papers.
