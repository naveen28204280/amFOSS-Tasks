import requests

class OpenSubtitlesAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.opensubtitles.com/api/v1"

    def search_subtitles(self, imdb_id, language):
        headers = {"Api-Key": self.api_key}
        params = {"imdb_id": imdb_id.lstrip("tt"), "languages": language}
        response = requests.get(f"{self.base_url}/subtitles", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return None

    def download_subtitle(self, file_id, output_folder):
        headers = {"Api-Key": self.api_key}
        response = requests.get(f"{self.base_url}/download/{file_id}", headers=headers)
        if response.status_code == 200:
            with open(f"{output_folder}/{file_id}.srt", "wb") as f:
                f.write(response.content)
            return f"Subtitle downloaded to {output_folder}/{file_id}.srt"
        else:
            return "Failed to download subtitle"

def handle_subtitles(imdb_id, language, output_folder):
    api = OpenSubtitlesAPI(api_key="DRiAlvQk6VEadS9yGEnYMo9F6axTJvDx")
    subtitles = api.search_subtitles(imdb_id, language)
    if subtitles:
        for subtitle in subtitles:
            file_id = subtitle["id"]
            print(f"Downloading subtitle {file_id}...")
            result = api.download_subtitle(file_id, output_folder)
            print(result)
    else:
        print("No subtitles found.")
