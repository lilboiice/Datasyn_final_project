from pathlib import Path
import albumentations as A
import os

NUM_EPOCHS = 1
LEARNING_RATE = 0.02
BATCH_SIZE = 12
EARLY_STOP_TH = 3

VISUAL_DEBUG = True
LOAD = False
SAVE = False
TEST = False
TRAIN = False

BASE_PATH = Path("datasets")
MODEL_SAVE_DIR = Path("Saved_Models")
SAVE_DIR = os.path.join(os.getcwd(), 'Saved_Models/')

RESOLUTION = 384

PREPROCESS_RECIPE = ['gaussian',
                    #'bilateral'
                    #'rotate',
                    #'resize'
                    ]


PREPROCESS_PARAMS = {
    # for gaussian blur; 2 by default
    "radius": 2,
    "rotate": 90,
    "resize": (384, 384),
    
    # for bilateral smoothing
    "kernel_size": 15,
    "sig_color": 15,
    "sig_space": 15,
}

