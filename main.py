# from src.cnnClassifier import logger
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>-->>> stage {STAGE_NAME} started <---<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>--->>>> stage {STAGE_NAME} completed <<---<< \n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f"************")
    logger.info(f">>>>>> stage{STAGE_NAME} started <<---<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<--<<\n\n x=====x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainning"

try:
    logger.info(f"*****************")
    logger.info(f">> Stage {STAGE_NAME} started <<--<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<< \n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"******************")
    logger.info(f">>> stage {STAGE_NAME} started <<--<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<--<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


