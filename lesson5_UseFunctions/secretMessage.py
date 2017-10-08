import os
def rename_files():
    #get file names from a folder
    file_list = os.listdir(r"C:\Users\ThunderBear\Documents\Udacity\full_stack_web\lesson5_UseFunctions\prank")
    #for each file, rename filename
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\ThunderBear\Documents\Udacity\full_stack_web\lesson5_UseFunctions\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
