import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tslearn.shapelets import LearningShapelets
from .TimeModel import TimeModel

class LS(TimeModel):
    def __init__(self, shapelet_length=0.3, total_lengths=3, max_iter=12000, optimizer='adam', batch_size=128, weight_regularizer=0.1):
        self.model = LearningShapelets(
            verbose=0, 
            scale=False, 
            shapelet_length=shapelet_length, 
            total_lengths=total_lengths, 
            max_iter=max_iter,
            optimizer=optimizer,
            batch_size=batch_size,
            weight_regularizer=weight_regularizer
        )
