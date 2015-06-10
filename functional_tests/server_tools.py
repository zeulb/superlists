from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
	return subprocess.check_output(
		[
			'fab',
			'create_session_on_server:email={}'.format(email),
			'-i', '~/Dropbox/key-torrify.pem',
			'--host={}'.format(host),
			'--hide=everything,status'
		],
		cwd=THIS_FOLDER
	).decode().strip()

def reset_database(host):
	subprocess.check_call(
		['fab', 'reset_database', '-i', '~/Dropbox/key-torrify.pem', '--host={}'.format(host)],
		cwd=THIS_FOLDER
	)