class Pagination:
    def __init__(self, items=None, pageSize=10):
        # Initialize with empty list if items is None
        self.items = items if items is not None else []
        # Convert pageSize to integer
        self.pageSize = int(pageSize)
        # Calculate total pages
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        # Set current page to 1 (first page)
        self.currentPage = 1

    def getVisibleItems(self):
        # Calculate start and end indices for current page
        start = (self.currentPage - 1) * self.pageSize
        end = min(start + self.pageSize, len(self.items))
        # Return items for current page
        return self.items[start:end]

    def prevPage(self):
        # Go to previous page if possible
        if self.currentPage > 1:
            self.currentPage -= 1
        return self  # Return self for method chaining

    def nextPage(self):
        # Go to next page if possible
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self  # Return self for method chaining

    def firstPage(self):
        # Go to first page
        self.currentPage = 1
        return self  # Return self for method chaining

    def lastPage(self):
        # Go to last page
        self.currentPage = self.totalPages
        return self  # Return self for method chaining

    def goToPage(self, pageNum):
        # Convert pageNum to integer
        pageNum = int(pageNum)

        # Handle edge cases
        if pageNum <= 0:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum

        return self  # Return self for method chaining


# Example usage
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")

    p = Pagination(alphabetList, 4)

    print(p.getVisibleItems())  # ["a", "b", "c", "d"]

    p.nextPage()
    print(p.getVisibleItems())  # ["e", "f", "g", "h"]

    p.lastPage()
    print(p.getVisibleItems())  # ["y", "z"]

    # Test chaining
    p.firstPage().nextPage().nextPage()
    print(p.getVisibleItems())  # ["i", "j", "k", "l"]

    # Test goToPage
    p.goToPage(10)  # Should go to last page (7)
    print(p.currentPage)  # 7
    print(p.getVisibleItems())  # ["y", "z"]

    p.goToPage(-5)  # Should go to first page
    print(p.currentPage)  # 1
    print(p.getVisibleItems())  # ["a", "b", "c", "d"]