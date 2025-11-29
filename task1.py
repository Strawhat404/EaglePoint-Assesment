def analyze_text(input_string):

  # First i need to handle the case where the input is completely empty

  if not input_string:

    return {

      "word_count": 0,

      "average_word_length": 0.0,

      "longest_words": [],

      "word_frequency": {}

    }



  # Manual text cleaning 

  # avoiding regex here to make the logic clearer. 

  # only want to keep letters and spaces.

  allowed_chars = "abcdefghijklmnopqrstuvwxyz '"

  cleaned_string = ""

   

  # Process one character at a time

  for char in input_string.lower():

    if char in allowed_chars:

      cleaned_string += char

    else:

      # If it's punctuation turns it into a space so words don't stick together

      cleaned_string += " "

       

  # Create our list of words by splitting on whitespace
  raw_word_list = cleaned_string.split()

   

  #  Calculate statistics

  # We need to sum up all the lengths to get the average aight

  accumulated_length = 0

  for single_word in raw_word_list:

    accumulated_length += len(single_word)

     

  # Calculate the average being careful not to divide by zero

  if len(raw_word_list) > 0: 

    math_avg = accumulated_length / len(raw_word_list)

    # Format it strictly to 2 decimal places

    final_average = float(format(math_avg, ".2f"))

  else:

    final_average = 0.0



  # Step 3: Find the max length manually

  current_max_len = 0

  for item in raw_word_list:

    if len(item) > current_max_len:

      current_max_len = len(item)

       

  # Now that we know the max length  grab all words that match it

  # using a loop here instead of a list comprehension for readability

  longest_matches = []

  for item in raw_word_list:

    if len(item) == current_max_len:

      # Make sure we don't add the same word twice to this list

      if item not in longest_matches:

        longest_matches.append(item)



  #Build the frequency map

  frequency_tracker = {}

  for item in raw_word_list:

    if item in frequency_tracker:

      frequency_tracker[item] = frequency_tracker[item] + 1

    else:

      frequency_tracker[item] = 1



  # Return the final dictionary structure

  stats_result = {

    "word_count": len(raw_word_list),

    "average_word_length": final_average,

    "longest_words": longest_matches,

    "word_frequency": frequency_tracker

  }

   

  return stats_result



# Execution Check

if __name__ == "__main__":

  test_str = "The quick brown fox jumps over the lazy dog the fox"

  print(analyze_text(test_str))