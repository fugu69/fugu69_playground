def binary_search_iterative(data, item):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high)//2
        
        if item == data[mid]:
            return mid
        elif item > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return "Not found"

books = ["The Silent Patient", "Atomic Habits", "Sapiens", "The Psychology of Money", "Educated", "Dune"]

sorted_books = sorted(books)

print(binary_search_iterative(sorted_books, "Atomic Habits"))


