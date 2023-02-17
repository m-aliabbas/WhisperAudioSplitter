def check_next_segments(query_word, segments):
    """Check for the next segments that contain the query word.

    Args:
        query_word (str): The query word to search for.
        segments (list): A list of segments to search through.

    Returns:
        The timestamp of the next segment containing the query word if found, otherwise None.
    """
    for segment in segments:
        for words in segment['whole_word_timestamps']:
            if query_word in words['word']:
                return words['timestamp'] + 0.3
    return None

def get_word_index(query_word, words, segments):
    """Get the timestamp of the word in the segment.

    Args:
        query_word (str): The query word to search for.
        words (list): A list of words to search through.
        segments (list): A list of segments to search through.

    Returns:
        The timestamp of the word in the segment if found, otherwise the timestamp of the next segment containing the word.
    """
    for word in words:
        if query_word in word['word']:
            return word['timestamp']
    return check_next_segments(query_word=query_word, segments=segments)

def search_for_words(segment, annotator_text, segments=''):
    """Search for the start and end times of a given text segment.

    Args:
        segment (dict): A dictionary containing the segment.
        annotator_text (str): The text to search for.
        segments (list): A list of segments to search through.

    Returns:
        A tuple containing the start and end times of the text segment.
    """
    annotator_text_words = annotator_text.split()
    word_segments = segment['whole_word_timestamps']
    start = get_word_index(annotator_text_words[0], word_segments, segments)
    end = get_word_index(annotator_text_words[-1], word_segments, segments)
    return start, end

