# automation cleanup (archieving files that the file age is > 30 days)

import os
import shutil
import time

def cleanup_logs(log_dir, archive_dir, days=30):
    now = time.time()
    age_limit = now - (days * 86400) # if the file lifetime is less  that it it will be achieved and moved
    for file_name in os.listdir(log_dir):# to pass on all files in the log dir
            path = os.path.join(log_dir, file_name)
            
            
            if os.path.isfile(path):  # if it 's a file get the lifetime of it
                file_age = os.path.getmtime(path)
                
                if file_age < age_limit:
                    archive_path = os.path.join(archive_dir, file_name + ".bak")

                    shutil.move(path, archive_path) #move it to python-arch
                    print(f"the  {file_name} is move to {archive_path}")


cleanup_logs("/home/nour/pharmacyapp/frontend/EzDrugMachine", "/home/nour/python-arch", days=30)
