# one.py
def myhello():
    print('myhello() in one.py')

print('TOP LEVEL IN ONE.PY')

# build in variable __name__
if __name__ == "__main__":
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
