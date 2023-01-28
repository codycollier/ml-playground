#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


if __name__ == "__main__":

    # data
    sequences = ["The latest drop for the loot NFT will be Thursday",
                 "The latest token offering will be next month",
                 "The light roast had a floral smell and taste and was less bitter",
                 "She scored several goals in the second half",
                 "His first touch and shots were great but did not result in a score",
                 ]

    # model + pipeline
    model_name = "sentence-transformers/all-mpnet-base-v2"
    pipe = pipeline("feature-extraction", model=model_name)
    results = pipe(sequences)

    # mean pool the output to a single embedding
    pooled =  []
    for r in results:
        p = np.mean(r, axis=0)
        pooled.append(p)

    shape_out = np.shape(np.array(results))
    shape_pooled =  np.shape(np.array(pooled))
    print("")
    print(f"model: {model_name}  vecs: {shape_out}  pooled: {shape_pooled}")
    print("")

    # similarity comparisons
    scores = cosine_similarity(pooled, pooled)
    for i, s in enumerate(sequences):
        print(f"text: {s}")
        for j, s2 in enumerate(sequences):
            print(f"{scores[i][j]} :: {s2}")
        print("")

    print("")
    print("similarity matrix:")
    print(scores)
    print("")


