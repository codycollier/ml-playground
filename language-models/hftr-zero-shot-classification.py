#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

import numpy as np
from transformers import pipeline


def show_results(results, model_name):
    """Print results from prediction"""

    print("")
    print("-" * 80)
    print(f"Results  (model_name: {model_name})")
    print("-" * 80)

    for res in results:

        text = res['sequence']
        scores = res['scores']
        labels = res['labels']

        idx = np.argmax(scores)
        cls = labels[idx]
        score = scores[idx]

        print(f"prediction: {score} :: {cls} :: {text}")

    print("")
    print("")

    


if __name__ == "__main__":


    # data
    sequences = ["The latest drop for the loot NFT will be Thursday",
                 "The light roast had a floral smell and taste",
                 "She scored several goals in the second half"]
    labels = ["cryptocurrency", "coffee", "soccer", "weather", "cooking"]

    model_names = ["distilbert-base-uncased", "bert-base-uncased"]
    results = {}


    # zero shot pipeline (pipeline wraps  model, tokenizer, pre/post-processing)
    for model_name in model_names:
        pipe = pipeline("zero-shot-classification", model=model_name)
        res = pipe(sequences=sequences, candidate_labels=labels)
        results[model_name] = res

    # show
    for model, result in results.items():
        show_results(result, model)


