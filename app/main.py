import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
    raise Exception("Invalid command. Usage: cp source_file destination_file")
else:
    _, source_file, destination_file = parts
    # Now you have the source_file and destination_file variables
    print("Source File:", source_file)
    print("Destination File:", destination_file)

    if source_file == destination_file:
        print("Source and destination files "
              "have the same name. Doing nothing.")
        return

    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    with open(source_file, "rb") as file_in, (
        open(destination_file, "wb") as file_out):
    file_out.write(file_in.read())


    print(f"File {source_file}' copied to "
          f"'{destination_file}' successfully.")
