import math
import os
import sys

import numpy as np
from PIL import Image
from tqdm import tqdm

import cv2
import glob
import numpy as np



def images_square_grid(images, mode):
    """
    Save images as a square grid
    :param images: Images to be used for the grid
    :param mode: The mode to use for images
    :return: Image of images in a square grid
    """
    # Get maximum size for square grid of images
    save_size = math.floor(np.sqrt(images.shape[0]))

    # Scale to 0-255
    images = (((images - images.min()) * 255) / (images.max() - images.min())).astype(np.uint8)

    # Put images in a square arrangement
    images_in_square = np.reshape(
            images[:save_size*save_size],
            (save_size, save_size, images.shape[1], images.shape[2], images.shape[3]))

    if mode == 'L':
        images_in_square = np.squeeze(images_in_square, 4)

    # Combine images to grid image
    new_im = Image.new(mode, (images.shape[1] * save_size, images.shape[2] * save_size))
    for col_i, col_images in enumerate(images_in_square):
        for image_i, image in enumerate(col_images):
            im = Image.fromarray(image, mode)
            new_im.paste(im, (col_i * images.shape[1], image_i * images.shape[2]))

    return new_im


def get_image(image_path, width, height, mode):
    """
    Read image from image_path
    :param image_path: Path of image
    :param width: Width of image
    :param height: Height of image
    :param mode: Mode of image
    :return: Image data
    """
    image = Image.open(image_path)

    if image.size != (width, height):  # HACK - Check if image is from the CELEBA dataset
        # Remove most pixels that aren't part of a face
        face_width = face_height = 108
        j = (image.size[0] - face_width) // 2
        i = (image.size[1] - face_height) // 2
        image = image.crop([j, i, j + face_width, i + face_height])
        image = image.resize([width, height], Image.BILINEAR)

    return np.array(image.convert(mode))


def get_batch(image_files, width, height, mode):
    data_batch = np.array(
        [get_image(sample_file, width, height, mode) for sample_file in image_files]).astype(np.float32)

    # Make sure the images are in 4 dimensions
    if len(data_batch.shape) < 4:
        data_batch = data_batch.reshape(data_batch.shape + (1,))

    return data_batch



class Dataset(object):
    """
    Dataset
    """
    def __init__(self, dataset_name, data_files):
        """
        Initalize the class
        :param dataset_name: Database name
        :param data_files: List of files in the database
        """
        DATASET_CATS_NAME = 'cats'
        DATASET_CELEBA_NAME = 'celeba'
        DATASET_MNIST_NAME = 'mnist'
        IMAGE_WIDTH = 28
        IMAGE_HEIGHT = 28

        if dataset_name == DATASET_CELEBA_NAME:
            self.image_mode = 'RGB'
            image_channels = 3

        elif dataset_name == DATASET_CATS_NAME:
            self.image_mode = 'RGB'
            image_channels = 3

        elif dataset_name == DATASET_MNIST_NAME:
            self.image_mode = 'L'
            image_channels = 1

        self.data_files = data_files
        self.shape = len(data_files), IMAGE_WIDTH, IMAGE_HEIGHT, image_channels

    def get_batches(self, batch_size):
        """
        Generate batches
        :param batch_size: Batch Size
        :return: Batches of data
        """
        IMAGE_MAX_VALUE = 255

        current_index = 0
        while current_index + batch_size <= self.shape[0]:
            data_batch = get_batch(
                self.data_files[current_index:current_index + batch_size],
                *self.shape[1:3],
                self.image_mode)

            current_index += batch_size

            yield data_batch / IMAGE_MAX_VALUE - 0.5



# Functions below are related to deal with the Cats Dataset
def rotate_coords(coords, center, angle_radians):
	# Positive y is down so reverse the angle, too.
	angle_radians = - angle_radians
	xs, ys = coords[::2], coords[1::2]
	new_coords = []
	n = min(len(xs), len(ys))
	i = 0
	centerX = center[0]
	centerY = center[1]
	cos_angle = math.cos(angle_radians)
	sin_angle = math.sin(angle_radians)
	while i < n:
		x_offset = xs[i] - center_X
		y_offset = ys[i] - center_Y
		new_X = x_offset * cos_angle - y_offset * sin_angle + center_X
		new_Y = x_offset * sin_angle + y_offset * cos_angle + center_Y
		new_coords += [new_X, new_Y]
		i += 1
	return new_coords


def preprocess_cat_face(coords, image):
	left_eye_X, left_eye_Y = coords[0], coords[1]
	right_eye_X, right_eye_Y = coords[2], coords[3]
	mouth_X = coords[4]

	if left_eye_X > right_eye_X and left_eye_Y < right_eye_Y and mouthX > rightEyeX:
		# The "right eye" is in the second quadrant of the face,
		# while the "left eye" is in the fourth quadrant (from the
        # viewer's perspective.) Swap the eyes' labels in order to
        # simplify the rotation logic.
		left_eye_X, right_eye_X = right_eye_X, left_eye_X
		left_eye_Y, right_eye_Y = right_eye_Y, left_eye_Y

	eyes_center = (0.5 * (left_eye_X + right_eye_X),
				   0.5 * (left_eye_Y + right_eye_Y))

	eyes_delta_X = right_eye_X - left_eye_X
	eyes_delta_Y = right_eye_Y - left_eye_Y
	eyes_angle_radians = math.atan2(eyes_delta_Y, eyes_delta_X)
	eyes_angle_degrees = eyes_angle_radians * 180.0 / math.pi

	# Straighten the image and fill in gray for blank borders.
	rotation = cv2.getRotationMatrix2D(eyes_center, eyes_angle_degrees, 1.0)
	image_size = image.shape[1::-1]
	straight = cv2.warpAffine(image, rotation, image_size, border_value=(128, 128, 128))

	# Straighten the coordinates of the features.
	new_coords = rotate_coords(coords, eyes_center, eyes_angle_radians)

	# Make the face as wide as the space between the ear bases.
	w = abs(new_coords[16] - new_coords[6])
	# Make the face square.
	h = w
	# Put the center point between the eyes at (0.5, 0.4) in proportion to the entire face.
	min_X = eyes_center[0] - w/2
	if minX < 0:
		w += min_X
		min_X = 0
	min_Y = eyes_center[1] - h*2/5
	if min_Y < 0:
		h += min_Y
		min_Y = 0

	# Crop the face and return
	crop = straight[int(min_Y):int(min_Y+h), int(min_X):int(min_X+w)]
	return crop


def describe_positive():
	output = open('log.txt', 'w')
	for img_path in glob.glob('cat_dataset/*.jpg'):
		# Open the '.cat' annotation file associated with this image.
		input = open('%s.cat' % img_path, 'r')
		# Read the coordinates of the cat features from the
		# file. Discard the first number, which is the number
		# of features.
		coords = [int(i) for i in input.readline().split()[1:]]
		# Read the image.
		image = cv2.imread(img_path)
		# Straighten and crop the cat face.
		crop = preprocess_cat_face(coords, image)
		if crop is None:
			print('Failed to preprocess image at {imagePath}.', file=sys.stderr)
			continue
		# Save the crop to folders based on size
		h, w, colors = crop.shape
		if min(h,w) >= 64:
			Path1 = img_path.replace("cat_dataset", "cats_64x64")
			cv2.imwrite(Path1, crop)
		# if min(h,w) >= 128:
		# 	Path2 = img_path.replace("cat_dataset", "cats_128x128")
		# 	cv2.imwrite(Path2, crop)

		# Append the cropped face and its bounds to the positive description.
		# h, w = crop.shape[:2]
		# print (cropPath, 1, 0, 0, w, h, file=output)


def main():
	describe_positive()

if __name__ == '__main__':
	main()
