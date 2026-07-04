import subprocess
from pathlib import Path


def convert(input_file, output_file):
    """
    Convert an audio file using FFmpeg.
    Returns True on success, False on failure.
    """

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_file),
        str(output_file),
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    return result.returncode == 0
