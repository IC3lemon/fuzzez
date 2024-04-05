import filecmp
import os

def compare_directories(dir1, dir2):
    # Walk through the directory trees and compare files
    for dirpath, dirnames, filenames in os.walk(dir1):
        for filename in filenames:
            file1 = os.path.join(dirpath, filename)
            file2 = os.path.join(dir2, os.path.relpath(file1, dir1))
            if not os.path.exists(file2):
                print(f"File {file2} does not exist in directory {dir2}")
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
    print(ver)
    os.chdir("/home/crabsnk/Desktop/linux")
    os.system("pwd")
    os.system('curl -O  mirrors.edge.kernel.org/pub/linux/kernel/{}/{}'.format(str('v'+ver[0]+'.x'),'linux-'+ver+'.tar.gz'))
    os.system("tar -xf {a}".format(a = 'linux-'+ver+'.tar.gz'))
    directory1 = "home/crabsnk/linux/{}".format('linux-'+ver+'.tar.gz')
    directory2 = "home/crabsnk/Desktop/linux/linux-6.8.3"

    compare_directories(directory1, directory2) 
