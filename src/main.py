import train
import argparse


TRAININGDIR = "/home/deivit/Desktop/dades/Documents/david/upc/AIDL/projecte/unet/BrainTumourImages/Generated_50-50"
LOGDIR = '/tmp/aidl/current'
NUM_EPOCHS = 5 
BATCH_SIZE_TRAIN = 25
BATCH_SIZE_TEST = 25
BATCH_SIZE_VALID = 25
STEP_METRICS = 10
LEARNING_RATE = 1e-5
STEPS_SAVER = 100
MODEL_TO_USE = "unet_keras"
RESTORE_WEIGHTS=False
PERFORM_ONE_HOT=False
BINARIZE_LABELS=False


train.main(TRAININGDIR,MODEL_TO_USE,NUM_EPOCHS,BATCH_SIZE_TRAIN,BATCH_SIZE_TEST,BATCH_SIZE_VALID, STEP_METRICS,STEPS_SAVER,LEARNING_RATE, LOGDIR, RESTORE_WEIGHTS,PERFORM_ONE_HOT,BINARIZE_LABELS)