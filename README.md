# GAOR related research notebooks

Research notebooks associated with:

Thompson, A. F., & Suomalainen, J. (2025). **GAOR: Genetic Algorithm-Based
Optimization for Machine Learning Robustness in Communication Networks.**
*Network*, 5(1), 6. https://doi.org/10.3390/network5010006

The research concerns machine-learning intrusion detection, feature selection
and adversarial robustness. This repository contains experimental code and
separate exploratory notebooks. It is not yet a complete, independently
validated reproduction package for the published paper.

## Current status

The main and feature-sensitivity notebooks have been revised to address
label scoring, preprocessing leakage and test-set use during early stopping.
Their saved outputs have been cleared. **The revised notebooks have not been
run end to end on the original data, and no corrected research results are
claimed here.** See [REVIEW_NOTES.md](REVIEW_NOTES.md).

Original notebooks remain available in Git history at commit
`eec1f50cac9ab65562c70fe1bd1862e9c5b44493`. Historical outputs should not be treated
as validated results from this revision.

## Contents and scope

| File | What it contains |
| --- | --- |
| `GAOR_NIDS_Using_RF,_XG_and_ANN.ipynb` | RF, XGBoost and ANN experiments; GA feature selection; an exploratory ART ZOO evaluation of fitted RF/XGBoost models with full and selected features. |
| `Feature Sensitivity with Machine Learning.ipynb` | A separate NSL-KDD interpretability demonstration using SHAP, LIME, permutation importance and partial dependence. It is not established as a reproduction of the paper's feature analysis. |
| `MACAU.ipynb` | Historical exploratory uncertainty-quantification notebook requiring an external MACAU package and prepared local data. Not revised or validated in this review. |
| `MACAU with random dataset.ipynb` | Historical MACAU exploration with synthetic data. Requires the external MACAU package; not revised or validated in this review. |

`GeneticSelectionCV` selects features using a model's predictive score. In the
uploaded implementation it does not generate adversarial samples or optimise
model hyperparameters. The revised main notebook does not implement A2PM,
adversarial retraining, or a 5G-NIDD experiment. Any claims about these parts of
the wider study must be supported by the paper and corresponding experiment
files, rather than inferred from this repository.

## Running the revised main notebook

1. Create an isolated Python environment.
2. Install the candidate dependencies: `python -m pip install -r requirements.txt`.
   Versions are not locked or validated as a complete environment yet.
3. Supply your prepared CSV at `data/cicddos2019_dataset.csv`, or set the
   `GAOR_DATA_PATH` environment variable to its location before launching Jupyter.
4. Open Jupyter with `python -m jupyterlab` and run the main notebook in order.
5. Save the package versions (`python -m pip freeze`), dataset provenance,
   preprocessing steps, file hash, sample counts and new results for that run.

Expected prepared CSV schema:

- `Class`: binary labels `Benign` and `Attack` (case-insensitive).
- Numeric feature columns. An optional `Label` and `Unnamed: 0` column are removed.
- Nonfinite values and rows with missing values are removed explicitly.
- Any label mapping, feature engineering, deduplication or sampling used to
  create this prepared CSV must be documented separately. The raw download is
  not guaranteed to have this schema.

The original filenames suggest CIC-DDoS2019. Its official dataset page is
https://www.unb.ca/cic/datasets/ddos-2019.html . Confirm the provenance of the
prepared CSV; a filename alone cannot establish the exact dataset or subset.
The previous README incorrectly linked to IDS2017. The NSL-KDD demonstration
loads a different dataset from the URL embedded in its notebook.

Raw datasets and the original preprocessing pipeline are not included.

## Evaluation and limitations

- Training, validation and test partitions are separate. Scalers and encoders
  are fitted only on training data. ANN early stopping uses validation data.
- Main-notebook min-max scaling explicitly clips held-out extremes to the
  training range. This preprocessing choice must accompany reported results.
- GA feature selection uses training data only. Post-selection cross-validation
  summaries have been removed because selection happened outside those folds;
  nested evaluation is needed before reporting such CV estimates.
- ROC and precision-recall plots use probability scores rather than hard labels.
- ART evaluation uses class IDs for reference labels and class probabilities for
  predictions. Attack success is also reported among initially correct samples.
- The default attack sample size is **five rows, for a smoke test only**. Both
  classes are represented; this forced representation is not a prevalence-weighted
  benchmark. Larger, justified samples and repeated seeds are needed for conclusions.
- The attack operates on continuous features with values bounded to [0, 1]. It
  does not enforce immutable fields, valid discrete values or traffic semantics.
  It therefore does not demonstrate physically feasible evasion on a network.
- The attack section is a revised experiment, not a reconstruction of the
  paper's numerical table. ZOO is one attack; its results do not establish
  general robustness. No numerical robustness claims are made in this README.
- Random row splits do not establish independence across duplicate flows,
  sessions, hosts or time periods. Check these before interpreting generalisation.
- Feature importance shows model associations, not proof of causal effects or
  exploitability. MACAU notebooks retain historical limitations.

## Research relevance

The notebooks illustrate ML experiment design, feature selection, interpretation
and adversarial evaluation in network intrusion detection. These methods are
relevant background for AI security research. This repository does not claim
experience evaluating frontier-model scheming or coding-agent control systems.

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
