import multiprocessing
import requests
import shutil
import os

def Downloader(URL, name):
    print(f"Started Downloading...file-{name}")
    response=requests.get(URL)
    os.makedirs("file",exist_ok=True)
    open(f"file/file-{name}.jpg", "wb").write(response.content)
    print(f"Completed Downloading...file-{name}")

url="https://learnandsupport.getolympus.com/sites/default/files/styles/rectangular_768px/public/2023-05/20230331-_3310122-edit-ftsmithphotos.jpg?itok=R16X_43U"
# Multiprocessing in Python
'''
1. Built-in module in Python
2. The multiprocessing module runs tasks in separate processes to achieve true parallelism, ideal for CPU-bound or heavy I/O operations on multi-core systems.
'''
import multiprocessing
import requests
import shutil
import os

# Just created a function that downloads the image from URL passed into it as an agrument
def Downloader(URL, name):
    print(f"Downloading file-{name}...")
    response = requests.get(URL)
    os.makedirs("file", exist_ok=True)
    with open(f"file/file-{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Downloaded file-{name}.")


url="https://learnandsupport.getolympus.com/sites/default/files/styles/rectangular_768px/public/2023-05/20230331-_3310122-edit-ftsmithphotos.jpg?itok=R16X_43U"

# Method 1:
'''It downloads the images one-by-one'''
# for i in range(5):
#     Downloader(url, i)

# Method 2:
'''Starts all Downloading together and completes it with the time it takes to complete.
This multiprocessing is used when you want to make your computer do heavy tasks using different processors of your computer parallely...It help doing multiple tasks parallely... decreases execution time of code.'''
''' NOTE: Enclosing it with if __name__=="__main__" is necessary for windows for code to work.'''


if __name__ == "__main__":
    url = "https://images.pexels.com/photos/3861959/pexels-photo-3861959.jpeg"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(target=Downloader, args=(url, i + 1))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

    try:
        comm = input("Do you want to delete the files created? [yes/no]: ").strip().lower()
        if comm == "yes":
            folder_path = "file"
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                print("Deleted folder.")
            else:
                print("Folder does not exist.")
    except Exception as e:
        print("Error:", e)