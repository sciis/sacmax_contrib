#config: utf-8
#.confファイル(一部除く)のread処理

import json
from collections import OrderedDict

class ReadConf:

    def __init__(self):
        self.conf_list = []

    def config_read(self, target_file_path):
        try:            
            f= open(target_file_path, 'r')
            json_data = json.load(f, object_pairs_hook=OrderedDict)
            del json_data["INFO_COMMENT"]
            f.close()
            
            self.conf_list = json_data

            return True

        except Exception as e:
            print(e)
            return False

