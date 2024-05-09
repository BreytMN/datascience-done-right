from typing import Hashable, Optional, Sequence

import pandas as pd
from sklearn.datasets import make_blobs


def make_classification_df(
    n_samples: Sequence[int],
    features: list[str],
    centers: Sequence[Sequence[int]],
    cluster_std: Sequence[float],
    target: str = "y",
    custom_targets: Optional[Sequence[Hashable]] = None,
    random_state: int = 0,
) -> pd.DataFrame:
    """Make simple classification dataframe for testing purposes

    Args:
        n_samples (Sequence[int]): A Sequence containing the number of points
        to be generated for each target.

        features (list[str]): List of names to be used as features. The lenght
        of this list will determinate the number of features to be generated.

        centers (Sequence[Sequence[int]]): Sequences containing the centers of
        each cluster. The lenght of the centers Sequence must match the lenght
        of n_samples while the lenght of its Sequences must match the lenght of
        `features`

        cluster_std (Sequence[float]): Standard deviation for cluster generation.
        The lenght must match the lenght of `n_samples`.

        target (str, optional): Name of the target column. Defaults to "y".

        custom_targets (Sequence[Hashable], optional): List of custom labels.
        Defaults to None.

        random_state (int, optional): Integer to be used in the generator for
        reproducible experiments. Defaults to 0.

    Returns:
        pd.DataFrame: The generated dataframe
    """

    if len(n_samples) != len(centers) or len(n_samples) != len(cluster_std):
        condition1 = "Length of features must match length of centers"
        condition2 = "Lenght of n_samples must match lenght of cluster_std"
        msg = f"{condition1}. {condition2}."
        raise ValueError(msg)

    X_, y_ = make_blobs(
        n_samples=n_samples,
        n_features=len(features),
        centers=centers,
        cluster_std=cluster_std,
        random_state=random_state,
    )

    df = pd.concat(
        (
            pd.DataFrame(X_, columns=features),
            pd.Series(y_, name=target),
        ),
        axis=1,
    )

    if custom_targets is not None:
        df = df.assign(
            **{target: df[target].replace(range(len(custom_targets)), custom_targets)}
        )

    return df
