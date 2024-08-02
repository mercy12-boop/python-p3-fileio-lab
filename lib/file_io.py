def write_file(file_name, file_content):
    # Ensure the file has a .txt extension
    file_name = f"{file_name}.txt"
    
    # Open the file for writing with utf-8 encoding
    with open(file_name, mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)

def append_file(file_name, file_content):

    file_name = f"{file_name}.txt"
    
    # Open the file for appending with utf-8 encoding
    with open(file_name, mode='a', encoding='utf-8') as text_file:
        text_file.write(file_content)

def read_file(file_name):

    file_name = f"{file_name}.txt"
    
    # Open the file for reading with utf-8 encoding
    with open(file_name, mode='r', encoding='utf-8') as text_file:
        return text_file.read()

