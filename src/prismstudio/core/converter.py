from pathlib import Path

from .ffmpeg import convert


class Converter:

    def convert_file(
        self,
        input_path,
        output_folder,
        extension,
    ):

        input_path = Path(input_path)

        output_folder = Path(output_folder)

        output_file = (
            output_folder /
            f"{input_path.stem}.{extension}"
        )

        return convert(
            input_path,
            output_file,
        )
