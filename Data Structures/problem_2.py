import os


def find_files(suffix, path):
    files_found = []

    def search_path(file_suffix, filepath):
        if not isinstance(file_suffix, str) or not os.path.isdir(filepath):
            return

        folders, file_with_suffix = [], []

        for item in os.listdir(filepath):
            pathname = os.path.join(filepath, item)

            if os.path.isdir(pathname):
                folders.append(pathname)

            if os.path.isfile(pathname) and pathname.endswith(file_suffix):
                file_with_suffix.append(pathname)

        # explore folders first before adding suffix items
        for folder_path in folders:
            search_path(file_suffix, folder_path)

        for item in file_with_suffix:
            files_found.append(item)
                
    search_path(suffix, path)
    return files_found

def os_walk(file_suffix, root_folder):
    try:
        files_found = []
        for root, dirs, files in os.walk(root_folder, topdown=False):
            for name in files:
                if name.endswith(file_suffix):
                    files_found.append(os.path.join(root, name))
        
        return files_found

    except:
        return files_found

def testcase(suffix, path):
    files_found = find_files(suffix, path)
    if files_found == os_walk(suffix, path):
        print("Test passed")
    else:
        print(f"Test failed")

    return files_found


testcase1 = testcase(".c", ".")
# expected output: ['.\\testdir\\subdir1\\a.c', '.\\testdir\\subdir3\\subsubdir1\\b.c', '.\\testdir\\subdir5\\a.c', '.\\testdir\\t1.c']

testcase2 = testcase(" ", ".")
# expected output: []

testcase3 = testcase(None, "")
# expected output: []

testcase4 = testcase(1, "")
# expected output: []

testcase5 = testcase(".c", "./testdir/subdir1")
# expected output: ['./testdir/subdir1\\a.c']