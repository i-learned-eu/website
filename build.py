from staticjinja import Site
from distutils.dir_util import copy_tree
import yaml
import sass
import os

with open("./data.yml", 'r') as data:
    try:
        parsedData = yaml.safe_load(data)
        site = Site.make_site(
            env_globals=parsedData,
            outpath="output",
            )
        site.render()
        os.mkdir("output/static")
        copy_tree("static", "output/static")
        sass.compile(dirname=('output/static/sass',
                     'output/static/css'), output_style='compressed')
        print("🤩 Rendered site")
    except yaml.YAMLError as exc:
        print("😢 Unable to load data file", exc)
