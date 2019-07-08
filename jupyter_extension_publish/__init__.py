def _jupyter_server_extension_paths():
    return [{
        "module": "jupyter_extension_publish"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src="static",
        # directory in the `nbextension/` namespace
        dest="jupyter_extension_publish",
        # _also_ in the `nbextension/` namespace
        require="jupyter_extension_publish/index")]

def load_jupyter_server_extension(nbapp):
    from notebook.utils import url_path_join
    from .handlers import TestHandler

    url = nbapp.web_app.settings['base_url']
    nbapp.web_app.add_handlers(
        r'.*',  # match any host
        [
            (url_path_join(url, '/hello'), TestHandler),
        ]
    )
    nbapp.log.info("jupyter_extention_publish enabled!")
