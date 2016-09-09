### publish new version of this library to PyPI
### Read more about publishing here: http://peterdowns.com/posts/first-time-with-pypi.html

import git 
from shutil import copyfile
import fileinput
import sys
import os

yesOrNo = input('Have you commited all changes? Yes (Y) or no (n)?')

if "Y" == yesOrNo:  
    copyfile("./setup.py.default", "./setup.py")

    repo    = git.Repo(".")
    nexttag = "0." + str(int(str(repo.tags[-1]).replace("0.", "")) + 1)

    for line in fileinput.input("./setup.py", inplace=True):
        line = line.replace("$VERSION", str(nexttag))
        sys.stdout.write(line),

    os.system("git add -A && git commit")

    new_tag = repo.create_tag(str(nexttag), message='Automatic deployment of new version "{0}"'.format(nexttag)) 
    repo.remotes.origin.push(new_tag)

    os.system("/usr/local/bin/python3.5 setup.py register -r pypitest")
    os.system("/usr/local/bin/python3.5 setup.py sdist upload -r pypitest")
    os.system("/usr/local/bin/python3.5 setup.py register -r pypi")
    os.system("/usr/local/bin/python3.5 setup.py sdist upload -r pypi")