
# Opening the txt file and reading its contents
txt_file=open("C:\\Users\\kenne\\OneDrive\\Desktop\\CS 162\\inputqueue.txt",'r')

# Creating a list from the txt file
queue_list=txt_file.readlines()

# Creating 3 different queues
p_queue = []
s_queue = []
e_queue = []

# Creating a for loop to sort the items into their appropriate queues
for packet_in in queue_list:
    pclass = packet_in[0]

    if pclass == "P":
        p_queue.append(packet_in)
    elif pclass == "S":
        s_queue.append(packet_in)
    elif pclass == "E":
        e_queue.append(packet_in)
    else:
        print("ERROR")

# Creating a function to queue based on weight of specific queue
def print_queue(Weight,Queue):
    for x in range(Weight):
        try:
            print(Queue[0])
            Queue.pop(0)
        except:
            break

# Calling my function "print_queue" and printing from queues until they are all empty
while p_queue or s_queue or e_queue:
    print_queue(3,p_queue)
    print_queue(2,s_queue)
    print_queue(1,e_queue)
