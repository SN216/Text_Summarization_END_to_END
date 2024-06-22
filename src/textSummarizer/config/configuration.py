from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    #class having two instance attributes. one is 'config' and other is 'params'
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        #config and params value read from 'CONFIG_FILE_PATH' and 'PARAMS_FILE_PATH'
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        #create directories with artifacts_root as artifacts as mentioned in config>config.yaml
        create_directories([self.config.artifacts_root])

    
    #method with return type DataIngestionConfig defined above in the code
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        #config = config>config.yaml-->data_ingestion
        config = self.config.data_ingestion

        #create directories as root_dir in config>config.yaml
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config