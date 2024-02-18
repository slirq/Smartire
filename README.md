
# SmartTire: AI-Powered Tire Defect Detection System

## Introduction

SmartTire leverages artificial intelligence techniques to revolutionize tire defect detection in the automotive industry. Our goal is to develop a real-time AI system capable of analyzing unprocessed tire images accurately without specialized equipment, aiming to enhance safety, reduce inspection time and costs, and improve tire maintenance.

## Features

- **High Accuracy**: Utilizes ResNet50 model achieving high accuracy in defect detection.
- **Real-Time Analysis**: Capable of analyzing tire images in real-time without the need for specialist gear.
- **Cost and Time Efficient**: Significantly reduces inspection time and costs.
- **Enhanced Safety**: Aims to improve vehicle safety through better tire maintenance.

## Installation

```bash
git clone https://github.com/yourgithub/smarttire.git
cd smarttire
pip install tensorflow
open jupyter notebook and run notebooks
```

## Usage

```python
in the notebooks folder
run the train.ipynb file to train models on the tire defect dataset
run the sal_qual.ipynb file to check for saliency maps of models on the tire defect dataset
run the pre-procssing.ipynb to see image pre-processing attempts while experimenting  

In the script folder
run server.py to run server for android app Ai model deployment

the Tyre Defect Camera Detection.zip and Tyre Defect Analyser.zip are the gallery and live camera varients of the client side Android APP

```

## Contributing

Contributions to SmartTire are welcome. Please refer to the contributing guidelines before making a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Kaggle](https://www.kaggle.com/datasets/warcoder/tyre-quality-classification) for the dataset.
- NVIDIA T4 GPUs on Kaggle IDE for training.
