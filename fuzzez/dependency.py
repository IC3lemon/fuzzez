import filecmp
import os
import shutil

def resolve(file_path, source_dir, destination_dir):
     
    # Copy the missing file from source to destination
    file_addr =  os.path.join(destination_dir, os.path.relpath(file_path, source_dir))
    print(f"resolved address: {file_addr}")
    shutil.copy(file_path,file_addr)

def compare_directories(dir1, dir2):
    # Walk through the directory trees and compare files
    print("comparing.....")
    for dirpath, dirnames, filenames in os.walk(dir1):
        for filename in filenames:
            file1 = os.path.join(dirpath, filename)
            file2 = os.path.join(dir2, os.path.relpath(file1, dir1))
            if not os.path.exists(file2):
                print(f"File {filename} does not exist in directory {dir2}")
                print(f"resolving...{filename} in {dir2}")
                print(file1)
                resolve(file1, dir1, dir2)
            elif not filecmp.cmp(file1, file2, shallow=False):
                print(f"Differences found in file: {file1}")
          
            
                
def ver(fp):
    version_lines = []
    with open(fp, 'r') as file:
        for i, line in enumerate(file, start=1):
            if 2 <= i <= 4:
                version_lines.append(line.strip())
            elif i > 4:
                break
    
    # Extract version numbers from version lines
    version_numbers = [line.split('=')[1].strip() for line in version_lines]

    # Concatenate version numbers to form the version string
    version = '.'.join(version_numbers)
    return version

if __name__ == "__main__":
    
    
    ver = ver("/home/crabsnk/Desktop/linux/Makefile")
    print("version is:",ver)
    os.chdir("/home/crabsnk/Desktop/linux")
    os.system("pwd")
    if not os.path.exists("/home/crabsnk/Desktop/linux/{}".format('linux-'+ver)):
    	os.system('curl -O  mirrors.edge.kernel.org/pub/linux/kernel/{}/{}'.format(str('v'+ver[0]+'.x'),'linux-'+ver+'.tar.gz'))
    	os.system("tar -xf {a}".format(a = 'linux-'+ver+'.tar.gz'))
    directory1 = "/home/crabsnk/Desktop/linux/{}".format('linux-'+ver)
    directory2 = "/home/crabsnk/Desktop/linux/testcase"

    compare_directories(directory1, directory2) 
