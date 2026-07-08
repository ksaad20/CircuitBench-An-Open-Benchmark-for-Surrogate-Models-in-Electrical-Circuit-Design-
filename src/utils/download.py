"""
Dataset download utilities.
"""

import requests
from pathlib import Path
from tqdm import tqdm


def download_file(url,
                  output_path):

    response = requests.get(url, stream=True)

    response.raise_for_status()

    total = int(response.headers.get("content-length", 0))

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "wb") as f:

        with tqdm(
            total=total,
            unit="B",
            unit_scale=True
        ) as bar:

            for chunk in response.iter_content(1024):

                f.write(chunk)

                bar.update(len(chunk))


def download_dataset(name,
                     url,
                     dataset_dir="datasets"):

    output = Path(dataset_dir) / name

    download_file(url, output)

    return output


def file_exists(path):

    return Path(path).exists()
