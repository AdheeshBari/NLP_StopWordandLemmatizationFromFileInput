# NLP_StopWordandLemmatizationFromFileInput
A file-based NLP script that reads text, removes stop words, and lemmatizes words to output a refined token list.

This script processes text from a specified file, performing tokenization, stop word removal, and lemmatization to produce a refined output of words in their base forms.
Steps:
1. Setup and Downloads: The script first checks for and downloads necessary NLTK data files.
2. File Input: Prompts the user to enter the file path of the text file to be processed.
3. File Reading: Opens and reads the content of the specified file.
4. Tokenization: Tokenizes the text into individual words.
5. Stop Word Removal: Filters out common English stop words to clean up the token list.
6. Lemmatization: Applies lemmatization to each remaining word to reduce it to its base or root form.
Output: Prints two lists—filtered words (without stop words) and lemmatized words (base forms of the filtered words).
