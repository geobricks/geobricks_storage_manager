import subprocess
from geobricks_common.core.log import logger

log = logger(__file__)


class StorageManager():

    def __init__(self, config):
        self.config = config["settings"]

    def publish_raster_to_ftp(self, folder_path):
        self._publish_to_ftp(folder_path, "raster")

    def publish_vector_to_ftp(self, folder_path):
        self._publish_to_ftp(folder_path, "vector")

    def _publish_to_ftp(self, input_path, layer_type):
        folder_server = self.config["folders"]["storage"] + layer_type
        server = self.config["server"]

        subprocess.call(['ls', '-1'], shell=True)
        args = [
            'sshpass',
            '-p', ftp["password"],
            'rsync',
            '-azP',
            input_path,
            server["user"] + '@' + server["url"] + ":" + folder_server
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
