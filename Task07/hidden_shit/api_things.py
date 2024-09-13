import requests

class OpenSubtitlesAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.opensubtitles.com/api/v1"

    def search_subtitles(self, imdb_id, language=None):
        headers = {"Api-Key": self.api_key}
        params = {"imdb_id": imdb_id}
        
        if language:
            params["languages"] = language
        
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
api_key= "DRiAlvQk6VEadS9yGEnYMo9F6axTJvDx"
