# Notebook version notes

## Original research files

Commit `eec1f50cac9ab65562c70fe1bd1862e9c5b44493` preserves the original
repository notebooks and their saved outputs. The publication is the reference
for the wider study and reported results.

Additional historical A2PM notebooks inspected separately contain interval and
combination patterns, a saved five-sample generation step, and Random Forest
prediction comparisons. They are separate from the current main notebook.

## Subsequent implementation changes

The current main and feature-sensitivity notebooks include:

- Configurable prepared-data loading and binary-label validation.
- Training-only preprocessing and a separate ANN validation partition.
- Probability scores for ROC and precision-recall curves.
- GA feature selection with internal training-data cross-validation.
- An ART comparison using the fitted RF/XGBoost models, with full and selected
  features, a shared sample subset, class-ID scoring and attack-success counts.
- NSL-KDD training-only encoding, held-out permutation importance and compatible
  SHAP output handling.

The revised ART comparison replaces standalone XGBoost/LightGBM attack snippets.
It is a subsequent experiment and does not reproduce the publication's attack
results. Saved outputs were cleared in the two revised notebooks. MACAU
notebooks retain their historical code and outputs.

## Execution and interpretation

Local regression checks cover notebook syntax, cleared outputs, label scoring,
input validation and data splitting. They do not execute the full experiments.
Run them with `python -m unittest discover -s tests -v`.

The revised notebooks have not been run end to end. Dependencies are unpinned;
a new run should record package versions, data provenance and experimental
settings. Main-notebook scaling clips held-out values to the training range.
The default ART run uses five samples with both classes represented, for a
smoke test. Quantitative robustness assessment requires suitable sampling and
attack constraints. Row-level splits should be assessed against the dataset's
flow, session and temporal structure.
