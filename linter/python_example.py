"""
This module checks if all characters in a string are unique.
"""

def is_unique(
			s
			):
	"""
	Determines if a string has all unique characters.

	:param s: The input string to check.
	:return: 1 if all characters are unique, otherwise 0.
	"""
	s = list(s
				)
	s.sort()


	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			return 0

	return 1


if __name__ == "__main__":
	print(
		is_unique(input())
		)
