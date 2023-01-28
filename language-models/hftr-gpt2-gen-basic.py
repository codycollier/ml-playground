#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Tinkering with gpt2 text generation
#
#
# references
#   . https://huggingface.co/transformers/task_summary.html#causal-language-modeling
#
#
#

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline, top_k_top_p_filtering
import torch
from torch.nn import functional as F


if __name__ == "__main__":

    # Load from pre-trained model
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

    # input, tokenize, encode
    sequence = f"The rain in spain stays mainly in the plain,"
    sequence = f"The general population of the island has been found"
    input_ids = tokenizer.encode(sequence, return_tensors="pt")

    # forward pass through the model
    next_token_logits = model(input_ids).logits[:, -1, :]

    # process output, select most probably next word
    filtered_next_token_logits = top_k_top_p_filtering(next_token_logits, top_k=30, top_p=1.0)
    probs = F.softmax(filtered_next_token_logits, dim=-1)
    next_token = torch.multinomial(probs, num_samples=1)

    # concatenate the original sequence and next token
    generated = torch.cat([input_ids, next_token], dim=-1)

    # decode the tokens
    result_string = tokenizer.decode(generated.tolist()[0])
    print("")
    print(" input: %s" % sequence)
    print("output: %s" % result_string)
    print("")

    # iterative generation for longer output
    text_generator = pipeline("text-generation")
    seqout = text_generator(sequence, max_length=50, do_sample=False)
    print("")
    print("seqout:\n%s" % seqout[0]["generated_text"])
    print("")



