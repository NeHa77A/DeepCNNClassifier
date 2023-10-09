from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import Evaluation
from DeepClassifier import logger

STAGE_NAME = "Evaluation stage"

def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()

if __name__=='__main__':
    try:
        logger.info(f"\n...............Stage {STAGE_NAME} started ...................")
        main()
        logger.info(f"...............Stage {STAGE_NAME} Completed ...................\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e