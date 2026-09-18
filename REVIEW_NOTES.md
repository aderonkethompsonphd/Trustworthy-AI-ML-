# Research notebook review

## Scope

Review of the publicly available notebooks at original commit
`eec1f50cac9ab65562c70fe1bd1862e9c5b44493`.
The review did not establish which exact code or data produced the published
paper's results. It does not amend the publication or certify reproduction.

## Changes

- README now describes the code actually present: GA feature selection,
  classification experiments and exploratory ZOO evaluation. Unsupported
  A2PM, hyperparameter-optimisation and adversarial-training implementation
  claims were removed. Historical percentages were removed pending validation.
- NSL-KDD feature sensitivity is explicitly a separate demonstration.
- Main notebook loads a configurable prepared CSV and validates binary labels.
- Training-only scaling, separate ANN validation data, and score-based ROC/PR
  curves replace the previous evaluation choices.
- Post-selection CV estimates were removed. Feature selection retains its
  internal training-only CV; a future CV performance estimate requires nesting.
- The former standalone attack snippets were replaced by a unified comparison
  using the actual fitted RF/XGBoost models and selected feature dimensions.
  This deliberately changes the attack experiment; LightGBM results are not
  reproduced. Reference class IDs are no longer reduced with argmax.
- Default five-sample attacks are labelled smoke tests. The evaluation records
  sample counts and attack success among initially correct predictions.
- Main and feature-sensitivity outputs were cleared to prevent stale numerical
  claims. Original versions remain available in Git history.
- NSL-KDD encoders are trained on the training partition; difficulty metadata
  is removed; permutation importance uses held-out data. SHAP output handling
  accommodates the list and class-axis array representations.
- MACAU notebooks remain historical exploratory work and were not modified.

## Verification performed

Four local regression tests pass: revised code-cell syntax and cleared outputs;
correct scoring for flat and column-shaped labels; rejection of malformed
label/probability arrays; separate data partitions and training-only scaler fit.
Run with `python -m unittest discover -s tests -v`.

This does not execute model fitting, genetic selection, TensorFlow, SHAP, LIME
or ART ZOO. The prepared dataset is unavailable here, and a complete compatible
dependency environment has not been established. requirements.txt is a candidate
package list, not a tested lockfile. Full notebook execution remains required.

## Before making numerical claims

1. Confirm the dataset's actual source, version, prepared CSV schema and hash.
2. Supply the preprocessing and sampling history, including duplicate/session
   checks and an appropriate independent evaluation split.
3. Run each revised notebook from a clean kernel. Resolve dependency issues,
   record exact versions, and retain outputs with experiment settings.
4. Increase attack sample size, justify sampling, repeat seeds, and report
   denominators and uncertainty. Five observations are not a robust benchmark.
5. Specify threat-model constraints and validate whether perturbations correspond
   to feasible network traffic. Current continuous attacks do not do this.
6. Treat any new results as revised experiments. Reconcile differences with the
   paper separately; do not silently replace published numbers.

## Sources checked

- CIC-DDoS2019 official dataset page:
  https://www.unb.ca/cic/datasets/ddos-2019.html
- ART classifier API and BlackBoxClassifier:
  https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/estimators/classification.html
