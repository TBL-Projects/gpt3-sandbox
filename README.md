# GPT-3 Word Generator

Humans' thinking is limited to their vocabulary.
When we encounter ideas that we can't exactly put into words, we try to find the best existing word to describe/fit what we're thinking.
The author believes that when humans expand their vocabulary, humans can expand their thinking.
This belief is the stem of this project which propses an alternative way of dealing with 'ideas we cant put into words' by creating contextually sensitive words. 

Fortunately, most NLP models don't have this limitation of trying to fit ideas into existing words. 
With NLP models, words are encoded into embeddings (a number array). 
These embeddings are mathematically similar to how words have synonymous meanings with other words.
If there is a new abstract idea that don't have words, NLP models can compute the idea's embedding and translate that into a word.

This project aims to use those newly computed embeddings to create new words for the English language.

# Starting
## Requirements

Coding-wise, you only need Python. But for the app to run, you will need:

* API key from the OpenAI API beta invite
* Python 3
* `yarn`

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r api/requirements.txt`
4. To add your secret key: create a file anywhere on your computer called `openai.cfg` with the contents `OPENAI_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (including quotes). If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.
5. Set your environment variable to read the secret key: run `export OPENAI_CONFIG=/path/to/config/openai.cfg` (for MacOS, Unix, or Linux users) or `set OPENAI_CONFIG=/path/to/config/openai.cfg` (for Windows users)
6. Run `yarn install` in the root directory
Initial release date: 29 July 2021
Author: Tomas Lastrilla
Project forked from: https://github.com/shreyashankar/gpt3-sandbox

## Authors

Sandbox:
The following authors have committed 20 lines or more (ordered according to the Github contributors page):

* Shreya Shankar
* Bora Uyumazturk
* Devin Stein
* Gulan
* Michael Lavelle

Word Generator:

* Tomas Lastrilla


