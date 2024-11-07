import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

if __name__ == "__main__":
    # Prompt the user to enter the file path
    file_path = input("Enter the path to the file: ")
    
    # Read the content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Tokenize words from the file content
    word_tokens = word_tokenize(file_content)
    
    # Define stop words in English
    stop_words = set(stopwords.words('english'))
    
    # Remove stop words
    filtered_words = [word for word in word_tokens if word.lower() not in stop_words]
    
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Apply lemmatization to the filtered words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    
    # Output the results
    print("Filtered Words (without stop words):\n", filtered_words)
    print("Lemmatized Words:\n", lemmatized_words)

# OUTPUT
# Enter the path to the file: Textfile.txt
# Filtered Words (without stop words):
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'centuries', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum', '.']
# Lemmatized Words:
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'century', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheet', 'containing', 'Lorem', 'Ipsum', 'passage', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'version', 'Lorem', 'Ipsum', '.']