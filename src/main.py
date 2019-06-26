import train
import argparse


TRAININGDIR = "/path_of_training_images"
LOGDIR = '/tmp'
NUM_EPOCHS = 2
BATCH_SIZE_TRAIN = 25
BATCH_SIZE_TEST = 25
BATCH_SIZE_VALID = 25
STEP_VALID = 50
STEP_METRICS = 50
LEARNING_RATE = 1e-4
STEPS_SAVER = 100
MODEL_TO_USE = "unet_keras"
RESTORE_WEIGHTS=False


train.main(TRAININGDIR,MODEL_TO_USE,NUM_EPOCHS,BATCH_SIZE_TRAIN,BATCH_SIZE_TEST,BATCH_SIZE_VALID,STEP_VALID, STEP_METRICS,STEPS_SAVER,LEARNING_RATE, LOGDIR, RESTORE_WEIGHTS)