# ODFL_Archive

The following repository contains a complete archive of results - including those reported in the original paper titled One-Shot Clustering for Federated Learning Under Clustering-Agnostic Assumption.  
The results archived here include experiment outputs (metrics, clustering logs, explanation quality), figure-generation notebooks, and helper analysis code used for the final submission.

## Directory Structure

```
ODFL_JMLR_Archive/
├── experiments/                 # Raw + aggregated FL experiment outputs
│   ├── <DATASET>/               # MNIST, FMNIST, CIFAR10, PATHMNIST, BLOODMNIST
│   │   ├── centralised_test/    # Centralised baseline runs (metrics, losses, explanations)
│   │   └── <split>/<balance>/<clients>/
│   │       └── <algo>_<dataset>_<split>_<balance>_<clients>/
│   │           └── results/     # cluster_id_mapping.csv, metrics, generalizability
├── temperature_experiments/     # Temperature scheduling analysis inputs
├── explanations/                # XAI (INDE insertion/deletion) per experiment scenario
│   └── experiment1[A|B|C]/<DATASET>/ #[A] - InCluster, [B] - OutofCluster, [C] - Orchestrator Distribution
├── tables/                      # Generated LaTeX tables (clustering performance, last clustering round)
├── Notebok_I_centralised_performance.ipynb
├── Notebook_II_temperature_experiments_analysis.ipynb
├── Notebook_III_algorithms_evaluation.ipynb
├── Notebook_IV_xai.ipynb
├── Noteboox_V_xai_boxplots.ipynb
├── LICENSE
└── README.md
```

## Naming Conventions

Scenario directory components:  
<dataset>_<overlap>_<balance>_<clients>

Where:
- overlap: nonoverlaping | overlaping
- balance: balanced | imbalanced
- clients: 15 | 30

Algorithm run folder:  
<algo>_<dataset>_<overlap>_<balance>_<clients>

Algorithm codes:
- baseline → BNC
- sattler → SCL
- briggs → BCL
- kmeans → OCFL-KM
- affinity → OCFL-AFF
- meanshift → OCFL-MS
- HDBSCAN → OCFL-HDB / OCFL-HDBS (XAI plots)

Key result files (inside results/):
- cluster_id_mapping.csv         (per-round cluster assignments)
- after_update_metrics.csv       (personalisation metrics)
- after_update_generalizability.csv (generalisation metrics)
- clusters_temperature.csv       (temperature schedule)
- explanations/*.csv (centralised; INDE metrics)

Generated analysis outputs:
- tables/clustering_performance/*.tex
- tables/clustering_round/last_clustering_round.tex
- explanations/**/INDE_avg.csv
- XAI CD plots: Insertion_CD_plot.png, Deletion_CD_plot.png

## Notebooks

| Notebook | Purpose |
|----------|---------|
| Notebok_I_centralised_performance | Centralised baselines (metrics, losses, explanation quality) |
| Notebook_II_temperature_experiments_analysis | Temperature evolution + normalization and aggregation |
| Notebook_III_algorithms_evaluation | Clustering + federated personalization/generalization evaluation + last clustering detection |
| Notebook_IV_xai | Statistical XAI aggregation + critical difference diagrams |
| Noteboox_V_xai_boxplots | Cross-split insertion/deletion boxplots |

## Last Clustering Detection

Implemented in Notebook_III: compares final cluster state to earlier rows to infer final performed clustering round per (dataset, split, balance, clients, algo).

## Quick Start

1. Create environment with pandas, seaborn, matplotlib, altair, scikit-learn, scipy, networkx.
2. Place experiment outputs under experiments/ following structure above.
3. Run notebooks in numeric order to reproduce tables and figures.

## License

MIT License (see LICENSE).

## Citation

Please cite the associated submission if using these artefacts.
