import subprocess
args = [
    'python',
    '-m',
    'http.server',
    '8080'
]
subprocess.run(args, shell=True)