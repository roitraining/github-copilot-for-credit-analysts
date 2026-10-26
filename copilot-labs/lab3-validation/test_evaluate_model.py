import numpy as np
import pytest

from evaluate_model import build_decile_table, compute_ks


def test_compute_ks_perfect_separation_is_one() -> None:
    y_true = np.array([1] * 20 + [0] * 20)
    y_prob = np.array([0.95] * 20 + [0.05] * 20)

    ks = compute_ks(y_true, y_prob)

    assert ks == pytest.approx(1.0)


def test_build_decile_table_shape_order_and_count() -> None:
    y_true = np.array(([1, 0, 0, 0, 1] * 20), dtype=int)
    y_prob = np.linspace(1.0, 0.01, num=y_true.shape[0])

    decile_df = build_decile_table(y_true, y_prob)

    assert len(decile_df) == 10
    assert decile_df.loc[decile_df["decile"] == 1, "mean_predicted_prob"].iloc[0] == pytest.approx(
        decile_df["mean_predicted_prob"].max()
    )
    assert int(decile_df["account_count"].sum()) == len(y_true)


@pytest.mark.parametrize(
    "y_true,y_prob",
    [
        (np.array([]), np.array([])),
        (np.array([0, 1, 0]), np.array([0.1, np.nan, 0.2])),
        (np.array([0, 0, 0]), np.array([0.1, 0.2, 0.3])),
    ],
)
def test_compute_ks_invalid_inputs_raise_value_error(
    y_true: np.ndarray, y_prob: np.ndarray
) -> None:
    with pytest.raises(ValueError):
        compute_ks(y_true, y_prob)
