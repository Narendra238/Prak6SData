def enqueue(queue,MaxQueue,newData):
    for i in range(MaxQueue-1,-1,-1):
        if queue[0] is not None:
            print("Penuh Mas ...")
            break
        if queue[i] == None:
            queue[i] = newData
            return queue  
def dequeue(queue,MaxQueue):
    tempQueue = queue
    queue = [None] * MaxQueue
    
    for i in range(MaxQueue-2,-1,-1):
        if tempQueue[MaxQueue - 1] is None:
            print("Kosong Mas ...")
        queue[i+1] = tempQueue[i]
    return queue
def checkQueueValue(queue, maxQueue):
    counter = 0
    for i in range(0,maxQueue,1):
        if (queue[i] == None):
            counter = counter + 1
        else:
            return counter
    return counter

#Main function
maxQueue = 5
queue = [None] * maxQueue
pilihan = None
counter = 0
while True:
        print("========= Simulasi Queue =================")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Cetak")
        print("0. Keluar")
        pilihan = int(input("Masukkan Pilihan Menu:"))
        if(pilihan == 1 ):               
            max = int(input("Masukkan Batas Input Queue : "))
            if(max > maxQueue):
                print("Inputan melebihi batas!")
            elif checkQueueValue(queue,maxQueue)<max:
                print("Antrian penuh")
                continue
            else:
                for i in range(max):
                    newData = input(f"Masukkan Data-{counter+1} : ")
                    counter +=1
                    queue = enqueue(queue,maxQueue,newData)         
        if(pilihan == 2 ):
            queue = dequeue(queue,maxQueue)
            counter -= 1
            if queue[-1] is not None:
                print("Data berhasil dihapus")
            else:
                print("Sudah Kosong")   
        if(pilihan == 3):    
            print(queue)
        if(pilihan == 0):
            print("Program Selesai")
            break