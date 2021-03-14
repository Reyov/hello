import os

for root, dirs, files in os.walk('c:\Temp'):
        for file in files:
            if file.endswith('.xlsm'):
                print(os.path.join(root, file))


                #this is a comment for a pull request test
                #comment no 2
            