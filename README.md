# AI Topics Notes

> Study notes, slide decks, and working code on transformers, retrieval-augmented generation, and neural networks.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini_API-4285F4?logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-vector_store-FF6B6B)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Written notes and reference material produced while working through modern AI topics. Where
a topic has runnable code, the code sits alongside the notes rather than in a separate place.

This is a notes repository, not a library — the value is in the explanations and diagrams.

## Contents

### `transformers/`

Notes on the transformer architecture, prepared as both PDF and slides:

- **`Transformers.pdf`** — the consolidated write-up
- **`Transformers Draft 1/2.pdf`**, **`.pptx`** — earlier drafts and the presentation deck
- **`Diagrams_V2.pdf`** — diagram set
- **`diagrams/`** — architecture illustrations covering attention, embeddings, encoder and
  decoder blocks, and vector similarity in embedding space

Topics covered: self-attention and multi-head attention, positional encoding, the
encoder-decoder stack, embeddings, and how transformers displaced recurrent models for
sequence tasks.

The original paper, *Attention Is All You Need* (Vaswani et al., 2017), is not mirrored here
— read it at [arXiv:1706.03762](https://arxiv.org/abs/1706.03762).

### `rag-systems/`

Retrieval-Augmented Generation — grounding a language model's output in retrieved documents
instead of relying on parametric memory alone.

- **`rag-systems-presentation.pptx`** — slide deck on RAG fundamentals and advanced techniques
- **`code/app.py`** — a working RAG pipeline using the Google Gemini API and ChromaDB

The code demonstrates model discovery and selection against the Gemini API, retry handling
with backoff when a model is unavailable, and a persistent ChromaDB collection for document
storage and embedding-based retrieval.

### `neural-networks/`

Notes on neural network fundamentals: network structure, forward propagation, activation
functions, backpropagation, and gradient descent.

### `regression/`

Notes on linear and logistic regression — the cost functions, gradient descent derivation,
and the jump from continuous prediction to classification via the sigmoid.

## Running the RAG Code

```bash
git clone https://github.com/0bada11/ai-topics-notes.git
cd ai-topics-notes
pip install -r requirements.txt
```

The RAG example needs a Google Gemini API key. Copy the template and add your own key:

```bash
cd rag-systems/code
cp .env.example .env
```

Then edit `.env`:

```
GOOGLE_API_KEY=your_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey). The `.env` file is
gitignored and must never be committed.

Run it:

```bash
python app.py
```

## Project Structure

```
ai-topics-notes/
├── transformers/
│   ├── Transformers.pdf            # Main write-up
│   ├── Transformers Draft 1.pptx   # Presentation deck
│   └── diagrams/                   # Architecture illustrations
├── rag-systems/
│   ├── rag-systems-presentation.pptx
│   └── code/
│       ├── app.py                  # Gemini + ChromaDB RAG pipeline
│       └── .env.example            # Template — copy to .env
├── neural-networks/
├── regression/
├── requirements.txt
└── LICENSE
```

## Related Repositories

[Machine Learning Algorithms](https://github.com/0bada11/machine-learning-algorithms) —
implementations of the classical algorithms these notes build on

## A Note on Attribution

Some diagrams in `transformers/diagrams/` were collected from public articles and papers
while studying, and are included for reference within these personal notes. They remain the
property of their original authors. The written notes, slides, and code are my own.

## License

The [MIT License](LICENSE) covers the code and my own written material. Third-party diagrams
retain their original rights.
