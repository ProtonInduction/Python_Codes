
class Count_Word_Multiples:
    def count_word_multiples(file_path):
        word_counts = {}
        
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        
        multiples = {word: count for word, count in word_counts.items() if count > 1}
        
        return multiples
    
    file_path = 'file.txt'
    multiples = count_word_multiples(file_path)
    
    for word, count in multiples.items():
        print(f"The word '{word}' appears {count} times.")
