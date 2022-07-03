##  Overview

This project aims to extract useful features by using causal inferences and building the model to predict the diagnosis for breast cancer.
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:

    - “What will happen if I halve the price of my product?”
    - “Which clients will pay their debts only if I call them?
## Introduction

Breast-cancer Diagnostic being the second greates cause of death in cancer for women, it is considered most prevalent invasive cancer in females. Since 1989, significant progress has been made in the detection and treatment of breast cancer. More than 3.1 million Americans have survived breast cancer, according to the American Cancer Society (ACS). About 1 in 38 women will develop breast cancer in their lifetime (2.6 percent ). Early detection of the disease and precise diagnosis both increase the likelihood of long-term survival for a person with breast cancer.The prognosis, or anticipated long-term behavior of the disease, heavily influences the choice of appropriate therapy immediately following surgery.
The causal graph is a central object Judea Pearl framework but often unknown, subject to personal knowledge and bias, or loosely connected to the available data. In this project we will be highlighting the importance of the matter in a concrete way. we will be:
    1.  Perform a causal inference task using Pearl’s framework;
    2. Infer the causal graph from observational data and then validate the graph;
    3. Merge machine learning with causal inference;

## Causal Graphs

Modeling causality through graphs brings an appropriate language to describe the dynamics of causality. Whenever we think an event A is a cause of B we draw an arrow in that direction. Causal graphs are probabilistic graphical models used to encode assumptions about the data-generating process. It can be used for communication and for inference

## Data

Data was found from kagle [here](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?resource=download)
Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

## Installation

    git clone https://github.com/nardoshood/Causal-Inference
    cd Causal-Inference
    pip install -r requirements.txt

## Contributors 
 ![Contributor list](https://contrib.rocks/image?repo=nardoshood/Causal-Inference)


