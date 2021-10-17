#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

import numpy as np
from transformers import pipeline


if __name__ == "__main__":

    # data
    sequences = ["The latest drop for the loot NFT will be Thursday",
                 "The latest token offering will be next month",
                 "The light roast had a floral smell and taste and was less bitter",
                 "She scored several goals in the second half"]

    # models - misc
    model_names = ["distilbert-base-uncased", "bert-base-uncased"]

    # models - specialized for feature extraction, similarity, etc
    # https://huggingface.co/models?pipeline_tag=feature-extraction&sort=downloads 
    # https://huggingface.co/models?pipeline_tag=sentence-similarity&sort=downloads
    model_names.append("sentence-transformers/distilbert-base-nli-mean-tokens")
    model_names.append("julien-c/distilbert-feature-extraction")
    model_names.append("sentence-transformers/paraphrase-xlm-r-multilingual-v1")
    model_names.append("sentence-transformers/all-MiniLM-L6-v2")

    # zero shot pipeline (pipeline wraps  model, tokenizer, pre/post-processing)
    results = {}
    for model_name in model_names:
        pipe = pipeline("feature-extraction", model=model_name)
        res = pipe(sequences)
        results[model_name] = res

    # show
    print("")
    print("-" * 80)
    print(f"Results")
    print(f"seq count: {len(sequences)}")
    print("-" * 80)

    for model, result in results.items():
        res = results[model_name]
        vecs = np.shape(np.array(res))
        print(f"model: {model}  vecs: {vecs}")

    print("")
    print("")


