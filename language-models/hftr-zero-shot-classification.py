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
                 "The latest token offering will be next month",
                 "The light roast had a floral smell and taste and was less bitter",
                 "She scored several goals in the second half"]
    # labels = ["cryptocurrency", "coffee", "soccer", "weather", "cooking"]
    labels = ["cryptocurrency", "coffee", "soccer", "weather"]

    # models - misc
    model_names = ["distilbert-base-uncased", "bert-base-uncased"]

    # models - fine tuned on nli task for zero shot cls
    # https://huggingface.co/models?pipeline_tag=zero-shot-classification&sort=downloads&search=nli
    model_names.append("valhalla/distilbart-mnli-12-3")
    model_names.append("valhalla/distilbart-mnli-12-9")
    model_names.append("facebook/bart-large-mnli")
    model_names.append("typeform/distilbert-base-uncased-mnli")
    model_names.append("joeddav/xlm-roberta-large-xnli")

    results = {}


    # zero shot pipeline (pipeline wraps  model, tokenizer, pre/post-processing)
    for model_name in model_names:
        pipe = pipeline("zero-shot-classification", model=model_name)
        res = pipe(sequences=sequences, candidate_labels=labels)
        results[model_name] = res

    # show
    for model, result in results.items():
        show_results(result, model)


