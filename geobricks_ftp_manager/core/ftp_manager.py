import subprocess
from geobricks_ftp_manager.config.config import config
from geobricks_common.core.log import logger

log = logger(__file__)
config = config["settings"]


def publish_raster_to_ftp(folder_path, server):
    _publish_to_ftp(folder_path, server, "raster")


def publish_vector_to_ftp(folder_path, server):
    _publish_to_ftp(folder_path, server, "vector")


def _publish_to_ftp(input_path, server, layer_type):
    folder_ftp = config["folders"]["ftp"] + layer_type
    ftp = config["ftp"][server]

    subprocess.call(['ls', '-1'], shell=True)
    args = [
        'sshpass',
        '-p', ftp["password"],
        'rsync',
        '-azP',
        input_path,
        ftp["user"] + '@' + ftp["url"] + ":" + folder_ftp
    ]

    proc = subprocess.Popen(args,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    stdout_value, stderr_value = proc.communicate()
    log.info(repr(stdout_value))
    log.info(repr(stderr_value))


publish_raster_to_ftp("/home/vortex/Desktop/LAYERS/processing/test/", "fenix")