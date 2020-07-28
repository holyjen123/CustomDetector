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

Create TFRecords using [xml_to_csv.py](https://github.com/holyjen123/object_detection/blob/master/xml_to_csv.py) and [generate_tfrecord.py](https://github.com/holyjen123/object_detection/blob/master/generate_tfrecord.py)
```bash
cd ~/object_detection/images
python ~/object_detection/xml_to_csv.py
cd ~/object_detection
```
This creates two files: test_labels and train_labels

In generate_tfrecords.py file, change row_label to your own category names

Then, run these two commands
```bash
python generate_tfrecord.py --csv_input=~/object_detection/images/train_labels.csv --image_dir=~/object_detection/images/images/train --output_path=train.record

python generate_tfrecord.py --csv_input=~/object_detection/images/test_labels.csv --image_dir=~/object_detection/images/images/test --output_path=test.record
```
This generates train.record and test.record

## Training and Testing Model
Use [labelmap.json](https://github.com/holyjen123/object_detection/blob/master/labelmap.json) and change items to category names

```bash
cd ~/object_detection
mkir label
mv ~/Downloads/labelmap.json ./label
```

Use this [file](https://github.com/holyjen123/object_detection/blob/master/faster_rcnn_inception_v2_pets.config)

Change /Users/hollyjen123/object_detection/ to your own directory and make necessary changes accordingly
```bash
cd ~/object_detection
mv ~/Downloads/
mkdir train_model

python models/research/object_detection/model_main.py --logtostderr --model_dir=train_model/ --pipeline_config_path=faster_rcnn_inception_v2_pets.config
```

After training, create model

Note to change XXXX to your highest file

```bash
python models/research/object_detection/export_inference_graph.py \
--input_type image_tensor \
--pipeline_config_path faster_rcnn_inception_v2_pets.config \
--trained_checkpoint_prefix train_model/model.ckpt-XXXX \
--output_directory inference_graph
```

Use testing [code](https://github.com/holyjen123/object_detection/blob/master/detectionTester.py) to check quality of your model

Make sure to change necessary parts in the code
