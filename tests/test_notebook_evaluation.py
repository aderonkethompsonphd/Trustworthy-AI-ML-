"""Small regression checks; does not claim to reproduce research experiments."""
import ast
import json
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / 'GAOR_NIDS_Using_RF,_XG_and_ANN.ipynb'

def sources(path):
    return [''.join(c['source']) for c in json.loads(path.read_text())['cells']
            if c['cell_type'] == 'code']

class EvaluationTests(unittest.TestCase):
    def test_revised_code_compiles_and_outputs_are_cleared(self):
        for path in [MAIN, ROOT / 'Feature Sensitivity with Machine Learning.ipynb']:
            for index, cell in enumerate(json.loads(path.read_text())['cells']):
                if cell['cell_type'] == 'code':
                    ast.parse(''.join(cell['source']), filename=f'{path.name}:{index}')
                    self.assertEqual(cell['outputs'], [])
                    self.assertIsNone(cell['execution_count'])

    def metric(self):
        source = next(s for s in sources(MAIN) if s.startswith('def evaluate_predictions'))
        function = ast.parse(source).body[0]
        ns = {'np': np, 'accuracy_score': accuracy_score}
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<metric>', 'exec'), ns)
        return ns['evaluate_predictions']

    def test_column_labels_are_not_collapsed_to_zero(self):
        metric = self.metric()
        scores = np.array([[.9, .1], [.2, .8], [.4, .6]])
        expected = 2 / 3
        for labels in [np.array([0, 1, 0]), np.array([[0], [1], [0]])]:
            accuracy, predicted = metric(scores, labels)
            self.assertAlmostEqual(accuracy, expected)
            np.testing.assert_array_equal(predicted, [0, 1, 1])

    def test_invalid_reference_and_probability_shapes_fail(self):
        metric = self.metric()
        with self.assertRaises(ValueError):
            metric(np.eye(2), np.eye(2))
        with self.assertRaises(ValueError):
            metric(np.array([.2, .8]), np.array([0, 1]))
        with self.assertRaises(ValueError):
            metric(np.array([[np.nan, .8]]), np.array([1]))

    def test_scaler_is_fitted_on_training_partition(self):
        from sklearn.model_selection import train_test_split
        X = pd.DataFrame({'a': np.arange(200, dtype=float), 'b': np.arange(200, dtype=float) ** 2})
        y = pd.Series(np.tile([0, 1], 100))
        ns = {'X': X, 'y': y, 'pd': pd, 'train_test_split': train_test_split}
        source = next(s for s in sources(MAIN) if '# Reserve test data first' in s)
        exec(source, ns)
        self.assertFalse(set(ns['X_train'].index) & set(ns['X_test'].index))
        self.assertFalse(set(ns['X_train'].index) & set(ns['X_val'].index))
        self.assertFalse(set(ns['X_val'].index) & set(ns['X_test'].index))
        np.testing.assert_allclose(ns['scaler'].data_max_, ns['X_train_raw'].max())
        original = ns['scaler'].data_max_.copy()
        ns['scaler'].transform(pd.DataFrame({'a': [1e9], 'b': [1e9]}))
        np.testing.assert_array_equal(original, ns['scaler'].data_max_)

if __name__ == '__main__':
    unittest.main()
