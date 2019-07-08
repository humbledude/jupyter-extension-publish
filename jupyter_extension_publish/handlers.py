from notebook.base.handlers import IPythonHandler
import tornado
import json

class TestHandler(IPythonHandler):
    def get(self):
        self.write('hello')
        self.flush()

class PublishS3Handler(IPythonHandler):
    def initialize(self, nbapp, access_key, secret_key, endpoint_url):
        self.nbapp = nbapp
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint_url = endpoint_url

    def post(self):
        post_data = tornado.escape.json_decode(self.request.body)

        nb_path = post_data['nb_path']
        version = post_data['version']

        self.nbapp.log.info('nb_path: ' + nb_path + ' version: ' + version)
        new_filename = '/published/{}__{}.{}'.format(nb_path.split('.')[0], version, nb_path.split('.')[1])
        self.nbapp.log.info('new path :' + new_filename)

        # s3 put
        # save checkpoint, duplicate file to published folder, rename file, upload

        ret = {
                'new_filename' : new_filename
                
                }
        self.write(json.dumps(ret))
        self.flush()
        
