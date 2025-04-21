class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


class Queue:  # Added Queue class for completeness
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


def main():
    data_structure = input("Pilih struktur data (queue/stack): ").lower()
    
    if data_structure == 'queue':
        queue = Queue()
    elif data_structure == 'stack':
        stack = Stack()
    else:
        print("Pilihan tidak valid")
        return
    
    while True:
        if data_structure == 'queue':
            print("|Menu Aplikasi Queue|")
            print("1. Enqueue Object")
            print("2. Dequeue Object")
            print("3. Cek Empty")
            print("4. Tampilkan Objek Terdepan")
            print("5. Panjang Dari Queue")
        else:
            print("|Menu Aplikasi Stack|")
            print("1. Push Object")
            print("2. Pop Object")
            print("3. Cek Empty")
            print("4. Tampil Objek Terakhir")
            print("5. Panjang Dari Stack")
        
        print("===========================")
        
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if data_structure == 'queue':
                if pilihan == 1:
                    obj = input("Objek yang ingin ditambahkan: ")
                    queue.enqueue(obj)
                    print(f'Objek "{obj}" berhasil ditambahkan.')
                elif pilihan == 2:
                    obj = queue.dequeue()
                    print(f'Objek "{obj}" berhasil dikeluarkan.')
                elif pilihan == 3:
                    print("Queue kosong." if queue.is_empty() else "Queue tidak kosong.")
                elif pilihan == 4:
                    obj = queue.peek()
                    print(f'Objek terdepan: "{obj}"')
                elif pilihan == 5:
                    print(f'Panjang Queue: {queue.size()}')
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            else:  # Jika 'stack'
                if pilihan == 1:
                    obj = input("Objek yang ingin ditambahkan: ")
                    stack.push(obj)
                    print(f'Objek "{obj}" berhasil ditambahkan.')
                elif pilihan == 2:
                    obj = stack.pop()
                    print(f'Objek "{obj}" berhasil dikeluarkan.')
                elif pilihan == 3:
                    print("Stack kosong." if stack.is_empty() else "Stack tidak kosong.")
                elif pilihan == 4:
                    obj = stack.peek()
                    print(f'Objek terakhir: "{obj}"')
                elif pilihan == 5:
                    print(f'Panjang Stack: {stack.size()}')
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
        except IndexError as e:
            print(e)

# Menjalankan program
if __name__ == "__main__":
    main()