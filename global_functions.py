import sys
import time

def update_progress(progress, total):
    sys.stdout.write('\r[{0}] {1}%'.format('#'*int((((progress+1) * 10)/total)), int(((progress+1) * 100)/total)))
    sys.stdout.flush()


