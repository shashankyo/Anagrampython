from difflib import SequenceMatcher
text1 = "My Name is Kharwal"
text2 = "Hi, My Name is Aman Kharwal"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")