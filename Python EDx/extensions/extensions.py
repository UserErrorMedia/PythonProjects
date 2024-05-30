#This code identifies the file type from a file name

# Prompt user for the name of a file
answer = input("What is the name of the file? ")
answer = str(answer.lower().strip())

if answer.endswith(".jpg") or answer.endswith(".jpeg"):
    print("image/jpeg")
elif answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")