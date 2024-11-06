import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sort_numbers():
    numbers = entry_numbers.get().split(',')
    arr = [int(num) for num in numbers]
    
    bubble_sort(arr)
    
    sorted_numbers.set(", ".join(map(str, arr)))

def search_number():
    # Get user input
    numbers = entry_numbers.get().split(',')
    target = int(entry_target.get())
    
    arr = sorted([int(num) for num in numbers])
    
    result = binary_search(arr, target)
    
    if result != -1:
        messagebox.showinfo("Result", f"Number found at index: {result}")
    else:
        messagebox.showinfo("Result", "Number not found")
root = tk.Tk()
root.title("Sort & Search: A GUI Solution")

# Create input feild
tk.Label(root, text="Enter numbers (comma-separated):",font=("Arial", 12,"bold"), fg="black").grid(row=0, column=0)
entry_numbers = tk.Entry(root,width=40)
entry_numbers.grid(row=1, column=0)

tk.Label(root, text="Enter number to search:",font=("Arial", 12,"bold"), fg="black").grid(row=0, column=6)
entry_target = tk.Entry(root,width=20)
entry_target.grid(row=1, column=6)

# Create button to sort numbers
sort_button = tk.Button(root,width=12,height=3,text="Sort Numbers", command=sort_numbers,font=("times new roman",10,"bold"),bg="yellow")
sort_button.grid(row=4, column=0)
# create button to search numbers
search_button = tk.Button(root, text="Search",width=12,height=3, command=search_number,font=("times new roman",10,"bold"),bg="lightblue")
search_button.grid(row=4, column=6)
sorted_numbers = tk.StringVar() 
tk.Label(root, text="Sorted Numbers are :",font=("Arial", 12,"bold"), fg="black", padx=20, pady=20).grid(row=6, column=0, columnspan=3)
tk.Label(root, textvariable=sorted_numbers,font=("Arial", 12,"bold"), fg="black", padx=20, pady=20).grid(row=6, column=1, columnspan=3)

root.mainloop()