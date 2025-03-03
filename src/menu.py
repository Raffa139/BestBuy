class Menu:
    def __init__(self, title):
        self.title = title
        self.commands = []

    def print_title(self):
        print(f"********** {self.title} **********")

    def print_menu(self):
        print("\n   Menu")
        print("   ----")

        for i, command in enumerate(self.commands):
            print(f"{i + 1}. {command['title']}")

    def add_command(self, title, action):
        self.commands.append({
            "title": title,
            "action": action
        })

    def get_command(self):
        max_command_index = len(self.commands) - 1

        while True:
            self.print_menu()

            command = input(f"\nEnter choice (1-{max_command_index + 1}): ").strip()

            try:
                command_index = int(command) - 1

                if command_index < 0 or command_index > max_command_index:
                    raise ValueError()

                return command_index
            except ValueError:
                print(f"Invalid choice '{command}'")

    def run_command(self, command_index):
        print()
        self.commands[command_index]["action"]()
        input("\nPress enter to continue ")

    def run(self):
        self.print_title()

        while True:
            command = self.get_command()
            self.run_command(command)
