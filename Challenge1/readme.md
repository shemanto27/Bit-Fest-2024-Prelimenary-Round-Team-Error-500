# Bengali Transliteration Project

## Project Overview

This project aims to develop a model for transliterating text from Romanized Bengali (rm) to Bengali script (bn). Transliteration is the process of converting text from one script to another, and in this case, we are focusing on converting Bengali words written in Roman letters to their native Bengali script.

## Dataset

The project uses the 'bengali-transliteration-data' dataset from Hugging Face Datasets (`SKNahin/bengali-transliteration-data`). This dataset provides a collection of parallel sentences in Romanized Bengali and Bengali script, which is used to train and evaluate the transliteration model.

## Model Selection

**Model:** We have selected the **T5 (Text-To-Text Transfer Transformer)** model for this project.

**Justification:**

* **Suitability for Low-Resource Languages:** T5 is a powerful multilingual model pre-trained on a massive dataset, making it suitable for low-resource languages like Bengali, where labeled data might be limited. Its pre-training allows it to leverage knowledge from other languages, potentially improving its performance on Bengali transliteration.
* **Text-to-Text Framework:** T5 is designed as a text-to-text model, which naturally fits the task of transliteration, where the input is Romanized text and the output is Bengali script. This framework simplifies the training process and avoids the need for complex input-output representations.
* **Performance:** T5 has demonstrated strong performance across various NLP tasks, including machine translation, summarization, and question answering. Its architecture and pre-training make it a strong candidate for achieving high accuracy in Bengali transliteration.
* **Efficiency:** While T5 can be computationally demanding, we have chosen the 't5-small' variant for this project, which offers a good balance between performance and efficiency. This variant is more resource-friendly and can be trained and deployed with relatively lower computational resources.

## Hyperparameters

The following hyperparameters were used for training the model:

| Hyperparameter | Value | Justification |
|---|---|---|
| Learning Rate | 2e-5 | This learning rate is a common starting point for fine-tuning pre-trained transformer models. It allows for gradual and stable learning, preventing large updates that could lead to instability. |
| Batch Size | 8 | A batch size of 8 was chosen to balance computational efficiency with effective training. Larger batch sizes can accelerate training, but they might require more memory and could lead to overfitting. |
| Number of Epochs | 3 | We trained the model for 3 epochs to ensure sufficient learning without overfitting. The number of epochs was chosen based on the model's performance on the validation set, where we observed that further training did not lead to significant improvements. |
| Weight Decay | 0.01 | Weight decay is a regularization technique used to prevent overfitting. This value was chosen based on common practices in fine-tuning transformer models. |


## Data Split

We used an 80/20 train/test split for this project.

**Justification:**

* **Sufficient Training Data:** The 80/20 split provides a large enough training set to allow the model to learn effectively from the data.
* **Reliable Evaluation:** The 20% test set is held out for evaluating the model's performance on unseen data, giving us a reliable estimate of its generalization ability.
* **Common Practice:** The 80/20 split is a widely used standard in machine learning for dividing datasets into training and testing sets.

## Evaluation

The model's performance is evaluated using the **Accuracy** metric. Accuracy measures the percentage of correctly transliterated words. It provides a straightforward and interpretable measure of the model's ability to perform the task.

## Code Structure

* `train.py`: This script handles the model training and evaluation.
* `transliterate.py`: This script contains the `transliterate` function, which takes an input text and returns the transliterated output.
* `README.md`: This file provides documentation for the project.

## Future Work

* Experiment with other transliteration models, such as IndicBERT or XLM-RoBERTa.
* Fine-tune the model further using a larger dataset or different hyperparameters to improve its performance.
* Explore techniques for handling out-of-vocabulary words and rare characters.
* Develop a user interface to make the transliteration model more accessible.

## Acknowledgments

* The creators of the 'bengali-transliteration-data' dataset.
* The Hugging Face team for their Transformers library and Datasets hub.