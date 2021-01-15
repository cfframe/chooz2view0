from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_table import Table, Col, LinkCol
from flask_table.html import element
from random import randint

app = Flask(__name__)


class Film(object):
    def __init__(self, name, url, genres):
        self.name = name
        self.url = url
        self.genres = ', '.join(genres)


class ExternalURLCol(Col):
    def __init__(self, name, url_attr, **kwargs):
        self.url_attr = url_attr
        super(ExternalURLCol, self).__init__(name, **kwargs)

    def td_contents(self, item, attr_list):
        text = self.from_attr_list(item, attr_list)
        url = self.from_attr_list(item, [self.url_attr])
        return element('a', {'href': url}, content=text)


class FilmTable(Table):
    url = ExternalURLCol('URL', url_attr='url', attr='name')
    genres = Col('genres')


@app.route("/catalogue")
def catalogue():
    #video_path = "C:\\Users\\cffra\\OneDrive - University of Dundee\\" +\
    #             "Documents\\AC51041 DevOps and Microservices\\Assign - Microservices\\Films\\Films orig\\"
    video_path = "rtmp://35.195.155.247:1935/vod2/"
    films = [
        Film("Big Buck Bunny", video_path + "BigBuckBunny_512kb.mp4", ["comedy", "animation"], "BigBuckBunny-pic.png"),
        Film("Elephant Dreams", video_path + "ed_1024_512kb.mp4", ["fantasy"], "ElephantsDream-pic.png"),
        Film("Sintel", video_path + "sintel-2048-surround.mp4", ["fantasy", "adventure"], "Sintel-pic.png")
        ]

    film_list = FilmTable(films)

    # return render_template('test_template2.html', **locals())
    return render_template('catalogue.html', film_list=film_list)


@app.route("/")
def index():
    # film_url = "rtmp://35.189.221.9:1935/vod/" + "BigBuckBunny_512kb.mp4"
    film_url = "rtmp://35.195.155.247:1935/vod2/" + "bbb.mp4"
    poster = "static/posters/BigBuckBunny-pic.png"
    return render_template('video_player.html', film_url=film_url, poster=poster)


if __name__ == "__main__":
    app.run()
