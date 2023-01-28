#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# References:
# . https://huggingface.co/docs/transformers/model_doc/flan-t5
# . 
# . https://huggingface.co/docs/transformers/training
#
#
#

from pprint import pprint
import sys

import numpy as np
import evaluate
import torch
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import TrainingArguments, Trainer


global model, tokenizer



if __name__ == "__main__":

    # Optionally leverage gpu
    device = "cpu"
    if torch.cuda.is_available():
        device = "cuda:0"

    # initialize
    modname = "bert-base-cased"
    modname = "bert-base-uncased"
    modname = "distilbert-base-uncased"
    global model, tokenizer
    model = AutoModelForSequenceClassification.from_pretrained(modname, num_labels=5)
    model = model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(modname)


    # dataset
    dataset = load_dataset("yelp_review_full")

    def tokenize_func(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_func, batched=True)
    small_train_dataset = tokenized_datasets["train"].shuffle(seed=8888).select(range(64))
    small_eval_dataset = tokenized_datasets["test"].shuffle(seed=8888).select(range(64))

    # eval
    metric = evaluate.load("accuracy")

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

    # trainer
    training_args = TrainingArguments(output_dir="test_trainer", evaluation_strategy="epoch")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=small_train_dataset,
        eval_dataset=small_eval_dataset,
        compute_metrics=compute_metrics,
    )
    
    trainer.train()



