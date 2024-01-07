import os
import shutil
# Select the directory from which you want to choose the files, H was for mine  
src_dir = 'H:/Google chrome/'

# Define the destination directories
meme_folder = 'H:/Google chrome/meme/'
docs_folder = 'H:/Google chrome/documents/'
zip_folder = 'H:/Google chrome/zips/'

#  the file extensions that should be moved to the meme_folder
meme_extensions = ['.mp4', '.png', '.jpeg', '.jpg', '.gif', '.jiff', '.PNG', '.jfif']

#  the file extensions that should be moved to the docs_folder
docs_extensions = ['.pdf', '.docx']

#  the file extensions that should be moved to the zip_folder
zip_extensions = ['.zip', '.7z', '.exe', '.msi', '.jar']

for filename in os.listdir(src_dir):
    file_extension = os.path.splitext(filename)[1]

    if file_extension in meme_extensions:
        dest_folder = meme_folder
    elif file_extension in docs_extensions:
        dest_folder = docs_folder
    elif file_extension in zip_extensions:
        dest_folder = zip_folder
    else:
        continue

    # Construct full file paths
    src_file = os.path.join(src_dir, filename)
    dest_file = os.path.join(dest_folder, filename)

    # Moves the file to the destination folder
    shutil.move(src_file, dest_file)
