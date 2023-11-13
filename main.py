from lyricsgenius import genius
from quart import Quart , jsonify , request
import syncedlyrics


app = Quart(__name__)

async def get_lyrics(query:str)->None:
    token = "8dBj0DYppiqQjhyNMZa_2q535hyCG7ZqXCEPAfpKpboHWjzrvedhaW3ffXyHheg-"
    api = genius.Genius(token,verbose=False)
    genius.skip_non_songs = True
    genius.excluded_terms = ['(Live)', '(Remix)', 'Remix', '(Show)', '(Music awards)', '(Victoire de la musique)', '(Accapella)']
    lyric = api.search_song(query)
    if lyric is not None:
        lyrics_text = lyric.lyrics
        lyrics_lines = lyrics_text.split('\n')
        if len(lyrics_lines) > 1:
          lyrics_lines = lyrics_lines[1:]
        lyrics_text = '\n'.join(lyrics_lines)
        lyricsentries = lyrics_text.split('\n')
        return lyricsentries
    
async def fallback(query:str)->None:
    lyrics  = syncedlyrics.search(search_term=query,providers=['Musixmatch'])
    if lyrics:
        return lyrics
    
@app.route('/')
async def home():
    return f"""
<html>
<h1 style="text-align: center;">Ayush is Gay</h1>
</html>
"""        
    
@app.route('/lyrics/')
async def lyrics():
    query = request.args.get('query')
    lyrics = await get_lyrics(query)
    if lyrics:
        return jsonify(lyrics)
    else:
        lrc = await fallback(query)
        if lrc:
            return jsonify(lrc)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)    


