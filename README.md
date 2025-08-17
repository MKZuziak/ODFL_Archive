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
├── datasets/                    # Dataset blueprints and translation files (see below)
│   ├── <DATASET>/               # MNIST, FMNIST, CIFAR10, PATHMNIST, BLOODMNIST
│   │   └── <split>/<balance>/<clients>/
│   │       ├── <DATASET>_<clients>_dataset_blueprint.csv
│   │       └── <DATASET>_<clients>_dataset_blueprinttranslation.txt
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

## Datasets Description

The `datasets/` folder contains the blueprint files describing the client splits for each experiment scenario.  
- **Blueprint CSVs** (`<DATASET>_<clients>_dataset_blueprint.csv`):  
  Define the data allocation for each client under a given split type (nonoverlaping/overlaping) and balance (balanced/imbalanced).
- **Translation TXT files** (`<DATASET>_<clients>_dataset_blueprinttranslation.txt`):  
  Provide mapping or translation information for the blueprint, if applicable.

**Structure Example:**
```
datasets/
├── MNIST/
│   └── nonoverlaping/
│       └── balanced/
│           └── 15/
│               └── MNIST_15_dataset_blueprint.csv
│               └── MNIST_15_dataset_blueprinttranslation.txt
...
├── CIFAR10/
│   └── overlaping/
│       └── imbalanced/
│           └── 30/
│               └── CIFAR10_30_dataset_blueprint.csv
│               └── CIFAR10_30_dataset_blueprinttranslation.txt
...
```
Each dataset (MNIST, FMNIST, CIFAR10, PATHMNIST, BLOODMNIST) is available under all split/balance/client scenarios.  
Blueprint files are used to reproduce the exact client data splits for federated experiments.

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