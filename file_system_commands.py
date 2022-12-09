from file_system import File, Folder


class AddFile:
    def __init__(self, file):
        self.file = file

    def execute(self, file_system):
        file_system.add_file_to_active(self.file)


class AddFolder:
    def __init__(self, folder):
        self.folder = folder

    def execute(self, file_system):
        file_system.add_folder_to_active(self.folder)


class StepOut:
    @classmethod
    def execute(cls, file_system):
        file_system.step_out()


class StepIn:
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def execute(self, file_system):
        file_system.step_in(self.folder_name)


class DoJackShit:
    @classmethod
    def execute(cls, file_system):
        pass


def create_command(text):
    command = None
    if text == '$ ls':
        command = DoJackShit()
    if text.startswith('$ cd '):
        next_folder = text.removeprefix('$ cd ')

        if next_folder == '/':
            command = DoJackShit()
        elif next_folder == '..':
            command = StepOut()
        else:
            command = StepIn(next_folder)
    if text.startswith('dir'):
        command = AddFolder(Folder(text.removeprefix('dir ')))

    if text.split(' ')[0].isnumeric():
        name, size = reversed(text.split(' '))
        command = AddFile(File(name, int(size)))
    return command
