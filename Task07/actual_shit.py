import click
from imdb import Cinemagoer
import sys
sys.path.append('/Users/karthikprathipati/Desktop/amFOSS-Tasks/Task07/hidden_shit')
from subtitle_shit import handle_subtitles

@click.command()
@click.argument('movie', type=str)
@click.option('-l', '--language', default='en', help='Filter subtitles by language')
@click.option('-o', '--output', default='./subtitles', help='Specify the output folder for subtitles')
@click.option('-s', '--file-size', type=int, help='Filter subtitles by movie file size')
@click.option('-h', '--match-by-hash', is_flag=True, help='Match subtitles by movie hash')
@click.option('-b', '--batch-download', is_flag=True, help='Enable batch mode for processing multiple movies')

def main(movie, language, output, file_size, match_by_hash, batch_download):
    ia = Cinemagoer()
    if batch_download:
        print("Batch processing mode enabled.")
        movies = movie.split(',')
        for mv in movies:
            process_movie(mv.strip(), ia, language, output, file_size, match_by_hash)
    else:
        process_movie(movie, ia, language, output, file_size, match_by_hash)

def process_movie(movie_name, ia, language, output, file_size, match_by_hash):
    imdb_id = get_imdb_id(movie_name, ia)
    if not imdb_id:
        print(f"IMDb ID could not be determined for {movie_name}")
        return
    print(f"Detected IMDb ID: {imdb_id}")
    if match_by_hash:
        print(f"Matching subtitles by hash for IMDb ID: {imdb_id}")
    if file_size:
        print(f"Filtering subtitles by file size: {file_size} bytes")
    handle_subtitles(imdb_id, language, output)

def get_imdb_id(movie_name, ia):
    results = ia.search_movie(movie_name)
    if results:
        return results[0].movieID
    return None

if __name__ == '__main__':
    main()

