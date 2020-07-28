# Setting Up Environment
## Tutorial

install anaconda using this LINK
```bash
cd ~/
mkdir object_detection
cd object_detection

export PATH="$PATH:~?opt/anaconda3/bin"
```

Define the dependencies pacakages in the YAML file
```bash
conda env create -f object_detection.yaml
conda activate object_detection
conda search pycocotools
```

Download MODELS
```bash
mv ~/Downloads/models-master ./models

echo $PYTHONPATH 
cd ~/object_detection/models/research/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim 

cd ~/object_detection/models/research/object_detection/packages/tf1
python setup.py build
python setup.py install

cd ~/objection_detection/models/research
protoc object_detection/protos/*.proto --python_out=.

cd ~/object_detection
```
