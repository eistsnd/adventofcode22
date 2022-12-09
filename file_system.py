class FileSystem:
    def __init__(self):
        self.root = Folder('/')
        self.active_folder = self.root

    def add_file_to_active(self, file):
        self.active_folder.add_file(file)

    def add_folder_to_active(self, folder):
        self.active_folder.add_folder(folder)

    def step_out(self):
        self.active_folder = self.active_folder.parent

    def step_in(self, folder_name):
        self.active_folder = self.active_folder.find_folder(folder_name)

    def find_folders(self, predicate):
        found = []

        def add_folder_to_found(folder):
            if predicate(folder):
                found.append(folder)

        self.traverse_folders(self.root, add_folder_to_found)

        return found

    @classmethod
    def traverse_folders(cls, folder, cb):
        for sub_folder in folder.folders:
            cls.traverse_folders(sub_folder, cb)

        cb(folder)


class Folder:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.folders = []
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        folder.set_parent(self)
        self.folders.append(folder)

    def set_parent(self, parent):
        self.parent = parent

    def find_folder(self, folder_name):
        for folder in self.folders:
            if folder.name == folder_name:
                return folder

    # ??? should size be memoized at some point and force recalc in case new folder or file is added
    def get_size(self):
        return sum([file.get_size() for file in self.files]) + sum([folder.get_size() for folder in self.folders])


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


