#This script converts text to emojis

# Define a function named "convert"
def convert(input_str):
# Convert emoticons to emojis
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

# Define the main function
def main():
    message = input("Tell me something ")
    result = convert(message)
    print(result)

if __name__ == "__main__":
    main()