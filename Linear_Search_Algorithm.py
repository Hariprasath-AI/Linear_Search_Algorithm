# Linear Search Algorithm
def Linear_Search(arr, key):

    # 'for' loop used to check element one by one
    for i in range(len(arr)):

        # If element in 'arr' is matched with the key, prints position of element
        # To avoid 'Data type mismatch' error, all element in 'arr' and data in 'key' is converted into string  
        if str(arr[i]) == str(key):
            print("Search element found at position", i + 1)
            break

    # If 'for' loop returns nothing i.e., 'if' condition inside the for loop doesn't satisfies the condition throughout the loop
    # Then, else part will be executed 
    else:
        print("Search element not found")

if __name__ == "__main__":
    # In the first line of input, A list of input typed in a single line separated with spaces and these inputs were stored in variable 'arr'
    arr = list(map(int, input().split()))

    # In the next line, Search element is typed and it will be stored in variable 'key' 
    key = input()

    # That's all, calling the function 'Linear_Search' and passing the argument 
    Linear_Search(arr, key)