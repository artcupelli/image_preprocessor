import base64


class Image:
    """
    A class to represent a single image.
    """

    def __init__(self, path: str = "", base64: str = "", bytes: bytes = []) -> None:
        self.__check_inital_params(path, base64, bytes)

        self.path = path
        self.base64 = base64
        self.bytes = bytes

    def __check_inital_params(
        self, path: str = "", base64: str = "", bytes: bytes = []
    ) -> bool:
        """Checks if at least one of the arguments was provided for the constructor."""
        if not len(path) and not len(base64) and not len(bytes):
            raise ValueError(
                "Image instance needs one of the arguments: path, base64 or bytes"
            )

    def __open_img_from_path(self) -> bytes:
        """Tries to get the image bytes from a path."""

        img_path = self.path

        if not len(img_path):
            raise ValueError("Image has no path.")

        try:
            img_bytes = open(img_path, "rb").read()
            self.bytes = img_bytes
            return self.bytes

        except Exception as e:
            raise e

    def __convert_base64_to_bytes(self):
        """Tries to get the image bytes from a base64 string."""

        img_base64 = self.base64

        if not len(img_base64):
            raise ValueError("Image has no base64.")

        try:
            img_bytes = base64.b64decode(img_base64.encode())
            self.bytes = img_bytes
            return self.bytes

        except Exception as e:
            raise e

    def get_bytes(self) -> bytes:
        """Return the bytes of the image. If doesn't exist, try to convert."""

        if len(self.bytes):
            return self.bytes

        if len(self.path):
            return self.__open_img_from_path()

        return self.__convert_base64_to_bytes()
