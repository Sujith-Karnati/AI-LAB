# import these modules
import nltk
nltk.download('wordnet') 
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora")) 
 
# a denotes adjective in "pos" 
print("better :", lemmatizer.lemmatize("better", pos ="a")) 