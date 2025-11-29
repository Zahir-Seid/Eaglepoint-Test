# Smart Text Analyzer

This Python function analyzes a block of text and provides key insights about its content.

## Features

- **Total word count** – Counts the total number of words in the text.  
- **Average word length** – Calculates the mean word length, rounded to 2 decimal places.  
- **Longest word(s)** – Identifies all words with the maximum length.  
- **Word frequency** – Counts how many times each word appears (case-insensitive).  

## How It Works

- The function **parses text manually**, character by character, without using any external libraries.  
- Punctuation is ignored, and only alphanumeric characters are considered part of words.  
- Case-insensitive counting ensures `The` and `the` are treated as the same word.  
- The longest words are tracked efficiently using a set to avoid duplicates.  
