# from src.cnnClassifier import logger
from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import  DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"



try:
    logger.info(f">>-->>> stage {STAGE_NAME} started <---<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>--->>>> stage {STAGE_NAME} completed <<---<<")

except Exception as e:
    logger.exception(e)
    raise e
