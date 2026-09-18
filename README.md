# GAOR: Adversarial ML Robustness Research

Research notebooks associated with:

Thompson, A., & Suomalainen, J. (2025). **GAOR: Genetic Algorithm-Based
Optimization for Machine Learning Robustness in Communication Networks.**
*Network*, 5(1), 6. https://doi.org/10.3390/network5010006

This work explores machine-learning intrusion detection, genetic-algorithm
feature selection, and model behaviour under adversarial perturbations.
The notebooks cover classification with Random Forest, XGBoost and neural
networks, feature analysis, and experiments using IBM's Adversarial Robustness
Toolbox (ART).

The publication describes the wider study and its reported findings. This
repository provides selected research notebooks and subsequent code revisions.

## Contents

| File | Focus |
| --- | --- |
| `GAOR_NIDS_Using_RF,_XG_and_ANN.ipynb` | Classification, GA feature selection, and ART ZOO evaluation of RF/XGBoost models using full and selected feature sets. |
| `Feature Sensitivity with Machine Learning.ipynb` | Separate NSL-KDD exploration using SHAP, LIME, permutation importance and partial dependence. |
| `MACAU.ipynb` | Exploratory uncertainty quantification using the external MACAU package and prepared data. |
| `MACAU with random dataset.ipynb` | MACAU exploration using synthetic data. |

The main notebook uses `GeneticSelectionCV` to select feature subsets according
to predictive performance. Its ART section compares model predictions before
and after an attack.

## Versions

Original notebooks and saved outputs are available at commit
`eec1f50cac9ab65562c70fe1bd1862e9c5b44493` in Git history.
The current main and feature-sensitivity notebooks contain subsequent
preprocessing and evaluation revisions, with outputs cleared for a fresh run.
These revisions have not been executed end to end; the current ART procedure
is a revised experiment, rather than the source of the paper's numerical results.
Implementation details are in [REVIEW_NOTES.md](REVIEW_NOTES.md).

## Run the main notebook

1. Create an isolated Python environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
   The dependency list is unpinned; record versions for your run.
3. Place the prepared CSV at `data/cicddos2019_dataset.csv`, or set
   `GAOR_DATA_PATH` to its location before launching Jupyter.
4. Start Jupyter with `python -m jupyterlab` and run the notebook in order.

The expected input has numeric feature columns and a `Class` column containing
`Benign` and `Attack` labels, case-insensitively. Optional `Label` and
`Unnamed: 0` columns are removed, as are rows with missing or nonfinite values.
Datasets are supplied separately. Record the dataset source, preparation and
sampling alongside each run; the configured filename is an input convention.

The ART section defaults to a five-sample smoke test. For quantitative
comparisons, choose an appropriate sample size and report the sampling method,
attack settings and repeated-run results. Its continuous feature-space
perturbations are bounded to [0, 1]; network-traffic validity constraints are
not enforced.

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
  doi={10.3390/network5010006}
}
```

## Acknowledgements

Research supported by AI-NET-ANTILLAS and ERCIM. MACAU is an external tool used
in the exploratory notebooks; its implementation is not included here.
