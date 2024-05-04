class TextEditor:
    def __init__(self):
        self.file = None
        self.commands = {
            'open': self.open_file,
            'write': self.write_to_file,
            'edit': self.edit_file,  # Add 'edit' command
            'quit': self.exit
        }

    def run(self):
        while True:
            command = input('Enter a command (open, write, edit, quit): ')  # Add 'edit' in the input prompt
            action = self.commands.get(command)

            if action:
                action()
            else:
                print("Invalid command")

    def open_file(self):
        filename = input('Enter the file name to open: ')
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")

    def write_to_file(self):
        filename = input('Enter the file name to write: ')
        try:
            with open(filename, 'w') as f:
                text = input('Enter the text to write: ')
                f.write(text)
        except Exception as e:
            print("Error occurred while writing", str(e))

    def edit_file(self):  # New method to edit files
        filename = input('Enter the file name to edit: ')
        try:
            with open(filename, 'r') as f:
                print("Current content of the file:")
                print(f.read())
            with open(filename, 'a') as f:
                text = input('Enter the text to append: ')
                f.write(text)
        except FileNotFoundError:
            print("File not found")

    def exit(self):
        quit()

if __name__ == "__main__":
    TextEditor().run()