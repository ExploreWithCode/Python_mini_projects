print("Here are the contents of the file:")
pending_file = open("pending.txt", "r")
for client in pending_file.readlines():
    print(client, end="")
pending_file.close()
accepted_replies = ["yes", "y", "YES", "Y", "Yes"]
if_add = input("\nDo you want to add something to the document?\n")
if if_add in accepted_replies:
    pending_file = open("pending.txt", "a")
    print("Add to the document: ")
    inp = pending_file.write(f"\n{input()}")
    pending_file.close()
pending_file = open("pending.txt", "r")
for client in pending_file.readlines():
    print(client, end="")
pending_file.close()
