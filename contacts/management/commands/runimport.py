from django.core.management.base import BaseCommand
import urllib2
import StringIO
import pandas
from sqlalchemy import create_engine
from PIL import Image
import base64
import cStringIO


class Command(BaseCommand):
    help = 'Will import a csv file with contacts'

    def handle(self, *args, **options):
        url = "https://docs.google.com/spreadsheets/d/1HclH8WugumpyWvNHfE1zopZGeA38DdCdM3458VjBeNg/pub?gid=1832240029&single=true&output=csv"
        data = urllib2.urlopen(url)

        df = pandas.read_csv(StringIO.StringIO(data.read()))
        df = df.rename(columns={'zip': 'zipcode',
                                'image': 'image_url'})

        # dowload all Images, scale and save as bitestring
        df['thumbnail'] = None
        for i in df.index:
            try:
                imagedata = urllib2.urlopen(df['image_url'][i])
                im = Image.open(imagedata)
                size = 64, 64
                im.thumbnail(size, Image.ANTIALIAS)
                buffer = cStringIO.StringIO()
                im.save(buffer, format="PNG")
                df['thumbnail'][i] = base64.b64encode(buffer.getvalue())
            except:
                pass

        CON = create_engine('sqlite:///db.sqlite3', encoding='utf-8')

        df.to_sql(con=CON, name="contacts_contact",
                  if_exists='replace', index='id')
