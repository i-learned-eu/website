from staticjinja import Site
from jinja2 import Environment, FileSystemLoader
from distutils.dir_util import copy_tree
import yaml
import sass
import os
import shutil
from babel.support import Translations


if os.path.exists("output") and os.path.isdir("output"):
    shutil.rmtree("output")
with open("./data.yml", 'r') as data:
    try:
        parsedData = yaml.safe_load(data)
        locale_dir = "translations"
        msgdomain = "html"
        list_of_desired_locales = ["en"]
        loader = FileSystemLoader("templates")
        extensions = ['jinja2.ext.i18n']

        translations = Translations.load(locale_dir, list_of_desired_locales)
        env = Environment(extensions=extensions, loader=loader)
        env.make_globals(parsedData)
        env.install_gettext_translations(translations)

        template = env.get_template("index.html")
        rendered_template = template.render()
        os.mkdir("output")
        indexFile = open("output/index.html", "a")
        indexFile.write(rendered_template)
        os.mkdir("output/static")
        copy_tree("static", "output/static")
        sass.compile(dirname=('output/static/sass',
                     'output/static/css'), output_style='compressed')
        shutil.rmtree("output/static/sass")

        print("🤩 Rendered site")
    except yaml.YAMLError as exc:
        print("😢 Unable to load data file", exc)
