import requests
from pathlib import Path

def download_to_local(url:str, out_path:Path, parent_mkdir:bool=True):
    """
    Downloads a file from a given url.

    :param url: url to download.
    :param out_path: local path to save the downloaded file.
    :param parent_mkdir: create parent directories if they don't exist.
    :return: True if download was successful, False otherwise.
    :raises requests.RequestException: if there was a problem with the request or the response.
    """
    
    if not isinstance(out_path, Path):
        raise ValueError("out_path must be a Path object")
    
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
        out_path.write_bytes(response.content)

        # with requests.get(url, stream=True, timeout=10) as response:
        #     response.raise_for_status()

        #     with out_path.open("wb") as f:
        #         for chunk in response.iter_content(chunk_size=10000)
        #             f.write(chunk)

        return True
    except requests.RequestException as e:
        print(f"Error downloading file from {url}: {e}")
        return False
