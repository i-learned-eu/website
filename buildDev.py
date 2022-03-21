from staticjinja import Site
from distutils.dir_util import copy_tree
import yaml

with open("./data.yml", 'r') as data:
    try:
        parsedData = yaml.safe_load(data)
        site = Site.make_site(
            env_globals=parsedData,
            outpath="output",
            )
        site.render(use_reloader=True)
        copy_tree("static/", "output/")
        print("🤩 Rendered site")
    except yaml.YAMLError as exc:
        print("😢 Unable to load data file", exc)
