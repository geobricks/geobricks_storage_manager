import subprocess
from geobricks_common.core.log import logger

log = logger(__file__)


class FTPManager():

    def __init__(self, config):
        self.config = config["settings"]

    def publish_raster_to_ftp(self, folder_path):
        self._publish_to_ftp(folder_path, "raster")

    def publish_vector_to_ftp(self, folder_path):
        self._publish_to_ftp(folder_path, "vector")

    def _publish_to_ftp(self, input_path, layer_type):
        folder_ftp = self.config["folders"]["ftp"] + layer_type
        ftp = self.config["ftp"]

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

ftp_manager = FTPManager()
ftp_manager.publish_raster_to_ftp("/home/vortex/Desktop/LAYERS/processing/test/", "fenix")