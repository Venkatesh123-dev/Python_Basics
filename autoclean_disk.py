#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:30:36 2020

@author: venky
"""

import  os
import  shutil

# Specify the file suffix to be deleted
del_extension_file  = [ '.tmp' , '._mp' , '.log' , '.gid' , 'to the .chk' , '.old' , '.xlk' , '.bak' ]
# Specify the name of the directory to be deleted
del_temp_dir  = [ 'cookies' , 'recent' , 'Temporary Internet Files' , 'Temp' , 'prefetch' , 'temp' ]

# Get system disk path
root_sys_drive  =  os . environ [ 'systemdrive' ] +  ' //'
# print(root_sys_drive)

def  delete_file_or_dir ( path ):
    try :
        if  os . path . isfile ( path ):
            # Delete Files
            # os.remove(path)
            print ( 'file: '  +  path  +  ' removed' )
        elif  os . path . isdir ( path ):
            # Delete folder
            # shutil.rmtree(path)
            print ( 'directory: '  +  path  +  ' removed' )
    except  WindowsError :
        print ( 'failure: '  +  path  +  "can't remove" )


def  main ():
    # Traverse all files and directories under the specified directory
    for  roots , dirs , files  in  os . walk ( root_sys_drive ):
        # Traverse all files
        for  find_file  in  files :
            # Get file extension
            file_extension  =  os . path . splitext ( find_file )[ 1 ]
            # Check whether the file suffix matches the specified
            if  file_extension  in  del_extension_file :
                # Combined file full path
                complete_path  =  os . path . join ( roots , find_file )
                # Delete Files
                delete_file_or_dir ( complete_path )
        # Traverse all directories
        for  find_dir  in  dirs :
            if  find_dir  in  del_temp_dir :
                # Combined directory name
                complete_path  =  os . path . join ( roots , find_dir )
                # Delete Files
                delete_file_or_dir ( complete_path )


if  __name__  ==  ' __main__ ' :
    main ()