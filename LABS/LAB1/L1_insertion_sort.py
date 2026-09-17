import random

N = 10
arr = [0] * N

def insertion_sort(A, n):
	"""Sort a list or numpy array.

	Argument:
	A -- a list or numpy array
	n -- length of A
	"""
	# Traverse the list or array from index 1 to n-1.
	for i in range(1, n):
		key = A[i]

		# Insert A[i] into the sorted subarray a[0:i].
		# Compare stored key with the already sorted values to its left.
		# Move each item one position to the right until we find the
		# position for the key or fall off the left end of the list or array.
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1

		# Insert key at the correct position in the list or array.
		A[j + 1] = key


def main():
	for i in range(N):
		arr[i] = random.randint(0, 100 * N - 1)
	print_array(arr)


def print_array(A):
	print("Lab 1 - insertion sort")
	print(f'List before sorting: {A}')
	insertion_sort(A, N)
	print(f'List after sorting: {A}')


main()