# GAOR: Genetic Algorithm-Based Optimization for ML Robustness

Code accompanying our peer-reviewed paper:

> Thompson, A.; Suomalainen, J. **GAOR: Genetic Algorithm-Based Optimization for Machine
> Learning Robustness in Communication Networks.** *Network* 2025, 5, 6.
> https://doi.org/10.3390/network5010006 (open access, CC BY 4.0)

## What this studies

Tree-based ML models (Random Forest, XGBoost) are widely used for network intrusion
detection because they're accurate and relatively interpretable on tabular data. But
they're vulnerable to **evasion attacks** — small, crafted input perturbations that push
a malicious sample across the decision boundary without changing what a human would
recognize as the same traffic.

This work evaluates whether **genetic-algorithm-optimized adversarial training** can make
RF and XGBoost intrusion detectors more robust to evasion — and, critically, what that
robustness costs in detection accuracy.

## Approach

- Adversarial samples generated using the **A2PM** (Adaptive Perturbation Pattern Method)
  framework, with a genetic algorithm (`sklearn-genetic`'s `GeneticSelectionCV`) optimizing
  feature selection and hyperparameters across generations (selection, crossover, mutation).
- Evaluated on two network intrusion datasets: **CIC-IDS2019** and **5G-NIDD**.
- Models attacked using IBM's Adversarial Robustness Toolbox (ART) — specifically
  **ZooAttack** against XGBoost and LightGBM classifiers.
- Robustness measured as adversarial accuracy (correct predictions on adversarial samples
  ÷ total adversarial samples), alongside standard cross-validation accuracy and AUC.

## Key finding

**Robustness has a cost.** Base models (RF, XGBoost, ANN) achieved ~99.5–99.96% baseline
accuracy. After GA-based adversarial training (GAOR), baseline accuracy held steady
(99.3–99.95%) — but adversarial-attack accuracy told a different story:

| Attack | RF (base → GAOR) | XGBoost (base → GAOR) |
|---|---|---|
| ZooAttack + XGBoostClassifier | 100% → 60% | 100% → 40% |
| ZooAttack + LightGBMClassifier | 40% → 20% | 80% → **100%** |

RF's detection ability degraded under both attack types after GA modification. XGBoost
degraded against the simpler attack but *improved* against the more sophisticated one —
suggesting GA-based adversarial training doesn't uniformly help, and its value is
attack- and model-specific rather than a general-purpose fix. Full discussion in Section 4
of the paper.

## Notebooks

- **`GAOR_NIDS_Using_RF,_XG_and_ANN.ipynb`** — main experiment: GA-based adversarial
  training and evaluation across RF, XGBoost, and ANN (Table 3 / Figure 8 in the paper).
- **`Feature Sensitivity with Machine Learning.ipynb`** — model-agnostic feature analysis
  (SHAP, LIME, partial dependence, correlation matrix) identifying which features are most
  exploitable by perturbation (Section 4.3).
- **`MACAU.ipynb`**, **`MACAU with random dataset.ipynb`** — exploratory work with VTT's
  MACAU uncertainty-quantification tool for Random Forest models, related to but separate
  from the core GAOR experiments.

## Data

This repo does not include the raw datasets. They're publicly available from their
original sources:
- CIC-IDS2019: https://www.unb.ca/cic/datasets/ids-2017.html
- 5G-NIDD: https://5gtnf.fi/

## Citation

```bibtex
@article{thompson2025gaor,
  title={GAOR: Genetic Algorithm-Based Optimization for Machine Learning Robustness in Communication Networks},
  author={Thompson, Aderonke and Suomalainen, Jani},
  journal={Network},
  volume={5},
  number={1},
  pages={6},
  year={2025},
  publisher={MDPI},
  doi={10.3390/network5010006}
}
```

## Funding

Supported by the AI-NET-ANTILLAS project (partially funded by Business Finland) and ERCIM.
