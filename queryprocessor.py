def get_name_color(user_query):
    import nltk
    
    # Download necessary resources from NLTK (one-time download)
    nltk.download('punkt')
    nltk.download('wordnet')
    
    def preprocess_text(text):
      """
      This function takes a text string and performs tokenization, lowercase conversion,
      and lemmatization.
    
      Args:
          text: The text string to preprocess.
    
      Returns:
          A list of lemmatized tokens.
      """
      # Tokenize the text
      tokens = nltk.word_tokenize(text)
    
      # Convert tokens to lowercase
      lowercase_tokens = [token.lower() for token in tokens]
    
      # Lemmatize the lowercase tokens (using WordNet lemmatizer)
      lemmatizer = nltk.WordNetLemmatizer()
      lemmatized_tokens = [lemmatizer.lemmatize(token) for token in lowercase_tokens]
    
      return lemmatized_tokens
    
    # Get user input
    text = user_query
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Print the lemmatized tokens
    #print("Lemmatized tokens:", processed_text)
    
    color_names = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white", "gray","brown","gold","silver","biege"]
    colors=[]
    
    for elem in processed_text:
      if elem in color_names:
        colors.append(elem)
        processed_text.remove(elem)
    
    return processed_text,colors


def itself(user_query):
    colors=None
    return [user_query],colors
    