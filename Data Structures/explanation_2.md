# Problem 2: Finding Files

Iterating through the returned output of os.list_dir() is linear as we have to check if the item is a folder or a file.

I chose to recursively look for files and let the call stack handle recursive function calls. Therefore, space complexity is linear where n is the number of folder to look into.

So, time complexity is O(n) and space complexity is also O(n).
