# Conversation Summarization Model with Google Pegasus

<p align="center">
  <img src="https://github.com/123Satyajeet123/text-summarizer/assets/103361055/3c9e4b08-3079-4a67-8a5c-b3aecd0aa6b6" alt="model pipeline" height=300rem>
</p>

## Description

This Jupyter notebook showcases a Conversation Summarization Model using the Google Pegasus model from the Hugging Face Transformers library. The model is fine-tuned on the SAMSum dataset, which contains dialogues and their corresponding summaries. The goal of the model is to generate concise summaries of chat conversations.

## Requirements

To run this notebook, you need the following dependencies:

- Python 3.x
- Hugging Face Transformers
- Datasets library
- Matplotlib
- Pandas
- NLTK
- Tqdm

You can install the required packages using `pip`:

```bash
pip install transformers datasets matplotlib pandas nltk tqdm
```

# How to Use
1. Install the required dependencies as mentioned above.
2. Clone this repository to your local machine:
```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

3. Open the Jupyter notebook Conversation_Summarization_Model_Google_Pegasus.ipynb in your Jupyter environment.

4. Make sure you have access to a GPU if you want to leverage GPU acceleration during the model training and inference.

5. Run the notebook cells in sequential order. The notebook will guide you through the following steps:

5. Loading the SAMSum dataset.
  - Setting up the Google Pegasus model and tokenizer.
  - Preprocessing the data and converting it into appropriate input encodings.
  - Fine-tuning the model using the Trainer class from the Transformers library.
  - Evaluating the model on the validation dataset and tracking the training progress.
  - Generating summaries for sample dialogues and displaying the results.

# Dataset and Model

The SAMSum dataset contains chat conversations and their corresponding summaries, making it suitable for training a conversation summarization model. We used the Google Pegasus model, a state-of-the-art transformer-based model for sequence-to-sequence tasks, and fine-tuned it on the SAMSum dataset.

# Performance Metrics
During training, we used the evaluation strategy to compute validation loss. Additionally, we used the ROUGE metric to evaluate the generated summaries against the ground truth summaries for the test dataset.

# Results
After training, the model should be capable of generating informative and concise summaries for chat conversations. The notebook will demonstrate the model's performance on sample dialogues and their generated summaries.

# Acknowledgments
I would like to thank Hugging Face for providing the Transformers library, which made it easy to access and fine-tune state-of-the-art language models like Google Pegasus.





