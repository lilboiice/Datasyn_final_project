from pathlib import Path
import albumentations as A
import os

NUM_EPOCHS = 10
LEARNING_RATE = 0.04
BATCH_SIZE = 12

VISUAL_DEBUG = True
LOAD = True
SAVE = True
BASE_PATH = Path("./datasets/CAMUS_resized")
SAVE_DIR = os.path.join(os.getcwd(), 'saved_models/')

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

