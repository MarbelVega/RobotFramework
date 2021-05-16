from pathlib import Path

# gives full path
cwd = Path.cwd()

# is that file or dir
print("Current Working Dir " + str(cwd) + '\n' + str(cwd.is_file()))

new_file = Path.joinpath(cwd, 'demo.txt')    # don't worry abt / or \
print('Does that file exist -' + str(new_file.exists()))
print(" EXTN - " + new_file.suffix  + " SIZE - " + str(new_file.stat().st_size))

# print only dirs in current
for child in cwd.iterdir():
    if child.is_dir():
        print(child)

stream = open('./demo.txt')
print("\n First char - " + stream.read(1))
print("\n First line - " + stream.readline())          # it resumes so first char is not printed
print("\n Everything - " + str(stream.readlines()))

w_stream = open('./demo.txt','wt')   # open for writing
print("Can I write ", str(w_stream.writable()))
w_stream.writelines(['ello', ' World!'])
#move to start of file stream
w_stream.seek(0)
w_stream.write('H')
# saves file stream to file
w_stream.close()