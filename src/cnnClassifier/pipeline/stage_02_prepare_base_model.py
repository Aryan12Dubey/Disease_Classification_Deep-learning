from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f"*******************0")
        config = ConfigurationManager()
        logger.info(f"*******************1")
        prepare_base_model_config = config.get_prepare_base_model_config()
        logger.info(f"*******************2")
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        logger.info(f"*******************3")
        prepare_base_model.get_base_model()
        logger.info(f"*******************4")
        prepare_base_model.update_base_model()
        logger.info(f"*******************5")


    
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e