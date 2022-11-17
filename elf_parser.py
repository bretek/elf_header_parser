MAX_LABEL_WIDTH = 33

# read header from file
with open('ls', 'rb') as file:
    elf_header = file.read(64)
    file.close()

# format values
outputs = []
print('ELF Header:')

# magic bytes
magic_output = ''
for index in range(0, 16):
    magic_output += str(hex(elf_header[index]))[-2:] + ' '
print(f"  Magic:   {magic_output.replace('x', '0')}")

# class
class_byte = elf_header[4]
if class_byte == 0:
    class_output = 'Invalid'
elif class_byte == 1:
    class_output = 'ELF32'
elif class_byte == 2:
    class_output = 'ELF64'
else:
    class_output = 'ERROR'
outputs.append(('Class', class_output))

# data format
data_byte = elf_header[5]
if data_byte == 0:
    data_output = 'Unknown data format'
elif data_byte == 1:
    data_output = "2's complement, little endian"
elif data_byte == 2:
    data_output = "2's complement, big endian"
else:
    data_output = 'ERROR'
outputs.append(('Data', data_output))

# elf header version
version_output = elf_header[6]
if version_output == 1:
    version_output = '1 (current)'
outputs.append(('Version', version_output))

# OS or ABI specific extensions
OS_byte = elf_header[7]
if OS_byte == 0:
    OS_output = 'UNIX - System V'
elif OS_byte == 1:
    OS_output = 'HP-UX'
elif OS_byte == 2:
    OS_output = 'NetBSD'
elif OS_byte == 3:
    OS_output = 'Linux'
elif OS_byte == 6:
    OS_output = 'Sun Solaris'
elif OS_byte == 7:
    OS_output = 'AIX'
elif OS_byte == 8:
    OS_output = 'IRIX'
elif OS_byte == 9:
    OS_output = 'FreeBSD'
elif OS_byte == 10:
    OS_output = 'Compaq TRU64 UNIX'
elif OS_byte == 11:
    OS_output = 'Novell Modesto'
elif OS_byte == 12:
    OS_output = 'Open BSD'
elif OS_byte == 13:
    OS_output = 'Open VMS'
elif OS_byte == 14:
    OS_output = 'HP Non-Stop Kernel'
else:
    OS_output = 'UNKNOWN'
outputs.append(('OS/ABI', OS_output))

# ABI version
ABI_version_byte = elf_header[8]
outputs.append(('ABI Version', ABI_version_byte))

# file type
type_bytes = int.from_bytes(elf_header[16:17], 'little')
if type_bytes == 0:
    type_output = 'No file type'
elif type_bytes == 1:
    type_output = 'REL (Relocatable file)'
elif type_bytes == 2:
    type_output = 'EXEC (Executable file)'
elif type_bytes == 3:
    type_output = 'DYN (Shared object file)'
elif type_bytes == 4:
    type_output = 'CORE (Core file)'
else:
    type_output = 'UNKNOWN'
outputs.append(('Type', type_output))

# machine
machine_bytes = int.from_bytes(elf_header[18:19], 'little')
if machine_bytes == 0:
    machine_output = 'No machine'
elif machine_bytes == 1:
    machine_output = 'AT&T WE 32100'
elif machine_bytes == 50:
    machine_output = 'Intel IA-64'
elif machine_bytes == 62:
    machine_output = 'AMD x86-64'
else:
    machine_output = 'UNKNOWN'
outputs.append(('Machine', machine_output))

# object file version
file_version_bytes = int.from_bytes(elf_header[20:23], 'little')
if file_version_bytes != 0 and file_version_bytes != 1:
    file_version_output = 'ERROR'
else:
    file_version_output = hex(file_version_bytes)
outputs.append(('Version', file_version_output))

# entry point address
bytes = elf_header[24:31]
output = hex(int.from_bytes(bytes, 'little'))
outputs.append(('Entry point address', output))

# start of program headers
bytes = elf_header[32:39]
output = int.from_bytes(bytes, 'little')
outputs.append(('Start of program headers', f"{output} (bytes into file)"))

# start of section headers
bytes = elf_header[40:47]
output = int.from_bytes(bytes, 'little')
outputs.append(('Start of section headers', f"{output} (bytes into file)"))

# flags
bytes = elf_header[48:51]
output = hex(int.from_bytes(bytes, 'little'))
outputs.append(('Flags', output))

# size of this header
bytes = elf_header[52:53]
output = int.from_bytes(bytes, 'little')
outputs.append(('Size of this header', f"{output} (bytes)"))

# size of program headers
bytes = elf_header[54:55]
output = int.from_bytes(bytes, 'little')
outputs.append(('Size of program headers', f"{output} (bytes)"))

# number of program headers
bytes = elf_header[56:57]
output = int.from_bytes(bytes, 'little')
outputs.append(('Number of program headers', output))

# size of section headers
bytes = elf_header[58:59]
output = int.from_bytes(bytes, 'little')
outputs.append(('Size of section headers', f"{output} (bytes)"))

# number of section headers
bytes = elf_header[60:61]
output = int.from_bytes(bytes, 'little')
outputs.append(('Number of section headers', output))

# section header string table index
bytes = elf_header[62:63]
output = int.from_bytes(bytes, 'little')
outputs.append(('Section header string table index', output))

# format and print table
for output in outputs:
    print(f"  {output[0]}:{' ' * (MAX_LABEL_WIDTH - len(output[0]))} {output[1]}")