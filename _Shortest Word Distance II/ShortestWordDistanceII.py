
class WordDistance(object):
	def __init__(self, words):
		# Interate over the wordList and mapping a word to all its locations in the array
		self.wordsDictionary = {}
		self.wordListLength = len(words)

		for idx, word in enumerate(words):
			self.wordsDictionary[word] = self.wordsDictionary.get(word, []) + [idx]
		

	def shortest_path(self, word1, word2):
		first_word = self.wordsDictionary[word1]
		second_word = self.wordsDictionary[word2]
		i = 0
		j = 0
		result = self.wordListLength

		while i < len(first_word) and j < len(second_word):
			result = min(result, abs(first_word[i] - second_word[j]))
			if first_word[i] < second_word[j]:
				i += 1
			else: 
				j += 1

			return result


wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(wordDistance.shortest_path("coding", "practice"))

# Algorithm

# In the constructor of the class, we simply iterate over the given list of words and prepare a dictionary, mapping a word to all it's locations in the array.
# Since we process all the words from left to right, we will get all the indices in a sorted order by default for all the words. So, we don't have to sort the indices ourselves.
# Let's call the dictionary that we build, locations.
# For a given pair of words, obtain the list of indices (appearances inside the original list/array of words). Let's call the two arrays loc1 and loc2.
# Initialize two pointer variables l1 = 0 and l2 = 0.
# For a given l1 and l2, we first update (if possible) the minimum difference (distance) till now i.e. dist = min(dist, abs(loc1[l1] - loc2[l2])). Then, we check if loc1[l1] < loc2[l2] and if this is the case, we move l1 one step forward i.e. l1 = l1 + 1. Otherwise, we move l2 one step forward i.e. l2 = l2 + 1.
# We keep doing this until all the elements in the smaller of the two location arrays are processed.
# Return the global minimum distance between the words.