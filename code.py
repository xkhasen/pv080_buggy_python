import yaml
import subprocess
import hashlib
import subprocess
import flask


def transcode_file(filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)


def load_config(filename):
    # Load a configuration file into YAML
    stream = filename.open(filename, "w")
    yaml.load(stream)


def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    # Import the requested version of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL
    http = urllib_version.PoolManager()
    r = http.request('GET', url)
    return r.data


def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)
