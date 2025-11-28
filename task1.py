import re 
from collections import Counter

def text_analyze(text):

    #Clean split text regex
    words = re.findall(r"[A-za-z]+(?:'[A-za-z]+)?", text.lower())


    #Handle Empty Cases
    if not words:
        return { "word_count":0, "average_word_length": 0.000}

    #Average word length(2 decimals)
    total_characterstics = sum(len(w) for w in words )
    average_word_length = total_characterstics / len(words)
    formatted_averager = float(f"{average_word_length:.2f}") #an algorithm to round it

    #longest word printer
    max_length = max(len(w) for w in words)
    longest_words = [w for w in words if len(w) == max_length]
   

#word Frequenxy counter
    word_frequency = Counter(words)
    return {
        "word_count": len(words),
        "average_word_length": formatted_averager,
        "longest_words": longest_words,
        "word_frequency": dict(word_frequency)

    }

#input
input_text = "The quick brown fox jumps over the lazy dog the fox"
input_text2 = "This is another test code to count"
print(text_analyze(input_text))
print(text_analyze(input_text2))