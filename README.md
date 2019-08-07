Checksum Generator Readme
======

Special Instructions
------
Please be aware that this program *ONLY* takes in and generates __csv files__. If another file type is needed, the program will need to be modified to do so.

This program is also written in Python3. In Mac, this may need to be specified when calling the program from the command line, because at this time Python2 comes automatically installed on Mac. If program is not run in Python3, TKinter will not run properly.

__When using Mac:__

This program also will __not__ show text correctly in MacOS: Mojave in Dark Mode. This is a problem with Dark Mode and TKinter that has not yet been resolved by Apple. *Please switch to light mode if you are unable to view text or buttons.*


Input/Output Specifics:
------
**This section will help to instruct on the input and output specifics for the checksum 
generator program.**

__Input Path Instructions:__

When creating the input path, please be sure to use the entire path, including the file name and extension. Please be aware that if the file is currently open, the program will not have permission to access the file and will encounter a critical error.

__Output Path Instructions:__

When creating the output path, you will want to be sure to add your chosen file name and extension at the end of the path. Please be sure to choose a file name that does not already exist in the given directory, or this file may be overwritten or changed.


CSV Layout Information:
------
**This section will help to explain the layout necessary for the csv to be processed by the checksum generator program.**

__Headers:__

The program will take in the first row of the csv file as headers for the output csv. It cannot distinguish between a header and the first row of input, so please be sure to input headers into your csv before processing the file.


__Column/Field Specifics:__

The program is designed to take in a csv file with any amount of fields (columns), as long as a file number is present in the first column and the path variable field is in the second column. If the path variable is not in the second column, the program will encounter a critical error when generating checksums, display an error message and close.

__Log Path Instructions:__

When creating a log path, please be aware that logs are outputted at .txt files in the given directory. You will need to provide a name for this file and the .txt extension at the end of the path. File numbers and any minor errors will be outputted here, however critical errors will interrupt program function.

__How Data is Input/Output:__

With each file, the checksum will be created and appended to the end of the row, then printed into a new csv. Each row will contain any previous information in the file with this checksum added as a new field.
