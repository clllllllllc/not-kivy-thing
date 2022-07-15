import csv
import xml.sax

# Function: linear search - search for an element linearly
# Input: arr - an array, n - the element u are searching for
# Output: the position of the element in that array - int
def linear_search(arr: list, n: any) -> int:
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


# Function: linear search - search for an element binary
# Input: arr - an array, n - the element u are searching for, low: the lower bound, high: the upper bound
# Output: the position of the element in that array - int
def binary_search(arr: list, low: int, high: int, x: any) -> int:
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Function: Sorts the array
# Input: arr - an array
# Output: sorted array
def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Function: qucikly sort an array
# Input: l- the lower bound, r - the upper bound, nums - the array
# Output: sorted array
def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi - 1, nums)
        quicksort(pi + 1, r, nums)
    return nums


# Function: qucikly sort an array
# Input: l- the lower bound, r - the upper bound, nums - the array
# Output: the position of ptr
def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


# Function: read csv
# Input: file_url - string containg the url of the csv
# Output: csv_content - the content of th csv
def csv_reader(file_url):
    with open("file_url.csv", newline="") as csvfile:
        csv_content = csv.reader(csvfile, delimiter=" ", quotechar="|")
        return csv_content


# Function: parse xml
# Input: file_url - string containg the url of the csv
# Output: csv_content - the content of th csv
class ParseXML(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print("Book")
            book_id = attributes["id"]
            print(f"Id: {book_id}")

    def endElement(self, tag):
        print(f"{self.CurrentData}: {self.content}")

    def characters(self, content):
        self.content = content

def encryption():
    # Check the c++ file
    pass
