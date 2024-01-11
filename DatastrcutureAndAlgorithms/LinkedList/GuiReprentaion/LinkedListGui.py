import tkinter as tk
from tkinter import messagebox, simpledialog


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_is_empty(self):
        return not self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.list_is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_ending(self, data):
        new_node = Node(data)
        if self.list_is_empty():
            self.head = new_node
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = new_node

    def get_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if self.list_is_empty():
            self.head = new_node
        elif index <= 0:
            new_node.next = self.head
            self.head = new_node
        elif index >= self.get_length():
            self.insert_at_ending(data)
        else:
            itr = self.head
            for _ in range(index - 1):
                itr = itr.next
            new_node.next = itr.next
            itr.next = new_node

    def delete_at_beginning(self):
        if not self.list_is_empty():
            temp = self.head
            self.head = temp.next
            del temp

    def delete_at_ending(self):
        if not self.list_is_empty():
            temp = self.head
            if temp.next is None:
                self.head = None
                del temp
            else:
                while temp.next.next is not None:
                    temp = temp.next
                del temp.next
                temp.next = None

    def display(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result


class LinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Linked List GUI")

        self.linked_list = LinkedList()

        self.head_label = tk.Label(master, text="Head Pointer: None")
        self.head_label.pack()

        self.label = tk.Label(master, text="Linked List:")
        self.label.pack()

        self.display_text = tk.StringVar()
        self.display_label = tk.Label(master, textvariable=self.display_text)
        self.display_label.pack()

        self.data_entry = tk.Entry(master, width=10)
        self.data_entry.pack()

        self.insert_beginning_button = tk.Button(master, text="Insert at Beginning", command=self.insert_at_beginning)
        self.insert_beginning_button.pack()

        self.insert_ending_button = tk.Button(master, text="Insert at Ending", command=self.insert_at_ending)
        self.insert_ending_button.pack()

        self.insert_index_button = tk.Button(master, text="Insert at Index", command=self.insert_at_index)
        self.insert_index_button.pack()

        self.delete_beginning_button = tk.Button(master, text="Delete at Beginning", command=self.delete_at_beginning)
        self.delete_beginning_button.pack()

        self.delete_ending_button = tk.Button(master, text="Delete at Ending", command=self.delete_at_ending)
        self.delete_ending_button.pack()

        self.display_button = tk.Button(master, text="Display Linked List", command=self.display_linked_list)
        self.display_button.pack()

    def insert_at_beginning(self):
        data = self.data_entry.get()
        if data.isdigit():
            self.linked_list.insert_at_beginning(int(data))
            self.update_head_label()
            self.display_linked_list()
        else:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def insert_at_ending(self):
        data = self.data_entry.get()
        if data.isdigit():
            self.linked_list.insert_at_ending(int(data))
            self.update_head_label()
            self.display_linked_list()
        else:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def insert_at_index(self):
        data = self.data_entry.get()
        index = simpledialog.askinteger("Input", "Enter index:")
        if data.isdigit() and index is not None:
            self.linked_list.insert_at_index(index, int(data))
            self.update_head_label()
            self.display_linked_list()
        else:
            messagebox.showerror("Error", "Please enter a valid integer and index.")

    def delete_at_beginning(self):
        self.linked_list.delete_at_beginning()
        self.update_head_label()
        self.display_linked_list()

    def delete_at_ending(self):
        self.linked_list.delete_at_ending()
        self.update_head_label()
        self.display_linked_list()

    def update_head_label(self):
        head_value = "None" if self.linked_list.list_is_empty() else str(self.linked_list.head.data)
        self.head_label.config(text=f"Head Pointer: {head_value}")

    def display_linked_list(self):
        result = self.linked_list.display()
        self.display_text.set(result)


def main():
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
