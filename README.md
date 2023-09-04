# Large Language Model from scratch

This project is the implementation from scratch of a LLM, using the GPT transformer model. It was implemented with Python and PyTorch.
The model was trained on the [OpenWebCorpus](https://skylion007.github.io/OpenWebTextCorpus/).
The original Transformer architecture is derived from the paper: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

I gained an understanding of the following material:
 - GPT Decoders
 - Masked multi-head attention
 - Scaled dot-product attention (query, key, values)
 - Calculation of attention scores
 -  Embeddings, positional embeddings
 - Weight initialization (e.g. Xavier init)
 - Optimization techniques (Adam with weight decay)
 - Data extraction from large .xz files

<img width="600" src="https://machinelearningmastery.com/wp-content/uploads/2021/08/attention_research_1.png">
