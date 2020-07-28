# Object Detection Tutorial
Learning how to train and test a custom image detection model

## Data Preparation
Obtain a reasonable amount of images for each category
(either by taking pictures or searching and downloading)

Create a new file named images in the object_detection directory and move all images into there

Transform resolution of images using this [file](https://github.com/holyjen123/object_detection/blob/master/transform_image_resolution.py)
```bash
python transform_image_resolution.py -d ~/object_detection/images/ -s 800 600

cd ~/object_detection/images
mkdir train
mkdir test
```

Move ~80% of the images into the train directory and the rest into test directory

Label the objects in each image using LabelImg
```bash
cd ~/object_detection
conda install pyqt
git clone https://github.com/tzutalin/labelImg.git
cd labelImg
make qt5py3;./labelImg.py
```
Open up each train and test folders and use the "Create RectBox" button to label 
When saving images, they will appear as XML files

Create TFRecords using SCRIPT and SCRIPT
```bash
cd ~/object_detection/images
python xml_to_csv.py
cd ~/object_detection
```

In generate_tfrecords.py file, change row_label to your own category names

Then, run these two commands
```bash
python generate_tfrecord.py --csv_input=~/object_detection/images/train_labels.csv --image_dir=~/object_detection/images/images/train --output_path=train.record

python generate_tfrecord.py --csv_input=~/object_detection/images/test_labels.csv --image_dir=~/object_detection/images/images/test --output_path=test.record
```
