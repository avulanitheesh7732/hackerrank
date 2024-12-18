def winner(andrea, maria, s):
    # Determine starting index based on the string s
    start_index = 0 if s == "Even" else 1
    
    # Initialize scores
    andrea_score = 0
    maria_score = 0
    
    # Iterate through the indices based on the start_index and step of 2
    for i in range(start_index, len(andrea), 2):
        andrea_score += andrea[i] - maria[i]
        maria_score += maria[i] - andrea[i]
    
    # Determine the result
    if andrea_score > maria_score:
        return "Andrea"
    elif maria_score > andrea_score:
        return "Maria"
    else:
        return "Tie"
