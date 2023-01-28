#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import sys

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")


if __name__ == "__main__":

    input_seq = "A step by step recipe for a smoothie:"
    input_seq = "Q: Can Geoffrey Hinton have a conversation with George Washington? Give the rationale before answering."
    try:
        input_seq = sys.argv[1]
    except IndexError:
        pass

    # Optionally leverage gpu
    device = "cpu"
    if torch.cuda.is_available():
        device = "cuda:0"

    # Tokenize
    inputs = tokenizer(input_seq, return_tensors="pt").to(device)
    print()
    print(f">> {input_seq}")
    # print(f">> {inputs}")

    # Generate
    model = model.to(device)
    outputs = model.generate(**inputs,
                             max_new_tokens=300,
                             num_beams=1,
                             # do_sample=True, num_return_sequences=3,
                             do_sample=False, num_return_sequences=1,
                             )
    output_seqs = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    print()
    for i,seq in enumerate(output_seqs):
        print(f">> {i}) {seq}")
    print()


