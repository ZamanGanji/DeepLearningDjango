import os
import pytest
import numpy as np
import cv2
from django.conf import settings
import pickle
from .machinelearning import pipeline_model

STATIC_DIR = settings.STATIC_DIR
MEDIA_ROOT = settings.MEDIA_ROOT

@pytest.fixture
def sample_image():
    return cv2.imread(os.path.join(STATIC_DIR, 'images/sample.jpg'))

def test_pipeline_model(sample_image):
    results = pipeline_model(os.path.join(STATIC_DIR, 'images/sample.jpg'))

    # Check if count is an integer
    assert all(isinstance(count, int) for count in results['count'])

    # Check if face_detect_score is a list of floats
    assert all(isinstance(score, float) for score in results['face_detect_score'])

    # Check if face_name is a list of strings
    assert all(isinstance(name, str) for name in results['face_name'])

    # Check if face_name_score is a list of floats
    assert all(isinstance(score, float) for score in results['face_name_score'])

    # Check if the number of detected faces matches the expected value
    assert len(results['count']) == 2

    # Check if the expected face name is detected
    assert results['face_name'][0] == 'person1'

    # Check if the face name score is within the expected range
    assert results['face_name_score'][0] >= 0.9

    # Check if the output images are saved in the correct location
    assert os.path.isfile(os.path.join(MEDIA_ROOT, 'ml_output/process.jpg'))
    assert os.path.isfile(os.path.join(MEDIA_ROOT, 'ml_output/roi_1.jpg'))
    assert os.path.isfile(os.path.join(MEDIA_ROOT, 'ml_output/roi_2.jpg'))

    # Clean up the output images after testing
    os.remove(os.path.join(MEDIA_ROOT, 'ml_output/process.jpg'))
    os.remove(os.path.join(MEDIA_ROOT, 'ml_output/roi_1.jpg'))
    os.remove(os.path.join(MEDIA_ROOT, 'ml_output/roi_2.jpg'))
