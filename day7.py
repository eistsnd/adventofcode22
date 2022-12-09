from file_system import FileSystem, Folder
from file_system_commands import create_command

if __name__ == '__main__':
    with open('day7_input.txt') as file:
        commands = [create_command(line.rstrip()) for line in file]

    file_system = FileSystem()

    for command in commands:
        command.execute(file_system)

    # part 1 1432936

    folders_within_limit = file_system.find_folders(lambda folder: folder.get_size() < 100000)

    print(sum([folder.get_size() for folder in folders_within_limit]))

    # part 2
    disk_size = 70000000
    required_free_space = 30000000

    current_free_space = disk_size - file_system.root.get_size()
    space_still_needed = required_free_space - current_free_space

    folders_that_can_free_enough_space = file_system.find_folders(
        lambda folder: space_still_needed <= folder.get_size()
    )

    folders_that_can_free_enough_space.sort(key=Folder.get_size)
    print(folders_that_can_free_enough_space[0].get_size())



