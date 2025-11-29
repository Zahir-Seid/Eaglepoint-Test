def smart_text_analyzer(text: str):
    # Convert all text to lowercase to make frequency counting case-insensitive
    text = text.lower()

    words = []  # This will hold all words found
    buffer = []  # Temporary buffer to build each word character by character

    # Step 1: Build words manually (O(n) complexity)
    # This avoids using split() which might fail on punctuation
    for ch in text:
        if ch.isalnum():  # Only consider letters and numbers as part of words
            buffer.append(ch)
        else:
            if buffer:
                # End of a word reached, join buffer into a string and add to words
                words.append("".join(buffer))
                buffer = []  # Reset buffer for the next word

    # If text ends with a word, add the last buffer
    if buffer:
        words.append("".join(buffer))

    # If no words found, return a default empty structure
    if not words:
        return {
            "word_count": 0,
            "average_word_length": 0.00,
            "longest_words": [],
            "word_frequency": {}
        }

    # Step 2: Analyze words
    freq = {}  # Dictionary to store word frequencies
    total_length = 0  # To calculate average word length
    max_len = 0  # Length of the longest word(s)
    longest_words = []  # List to store longest word(s)
    longest_set = set()  # Set for quick lookup to avoid duplicates

    for w in words:
        # Count frequency
        freq[w] = freq.get(w, 0) + 1

        # Count total length for average calculation
        l = len(w)
        total_length += l

        # Track the longest word(s)
        if l > max_len:
            max_len = l
            longest_words = [w]  # Start new list with the current word
            longest_set = {w}
        elif l == max_len and w not in longest_set:
            longest_words.append(w)
            longest_set.add(w)

    # Calculate word count and average word length
    word_count = len(words)
    avg_length = round(total_length / word_count, 2)

    return {
        "word_count": word_count,
        "average_word_length": avg_length,
        "longest_words": longest_words,
        "word_frequency": freq
    }

# Example using a poem

poem = """
No man is an island,

Entire of itself,

Every man is a piece of the continent,

A part of the main.

If a clod be washed away by the sea,

Europe is the less.

As well as if a promontory were.

As well as if a manor of thy friend’s

Or of thine own were:

Any man’s death diminishes me,

Because I am involved in mankind,

And therefore never send to know for whom the bell tolls;

It tolls for thee.
"""

# calling the function and Running it
result = smart_text_analyzer(poem)

print(result)

