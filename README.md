---
language: 
  - en
tags:
- classifier
- multimodal
- olfaction-vision-language
- olfaction
- olfactory
- scentience
- neural-network
- graph-neural-network
- gnn
- vision-language
- vision
- language
- robotics
- multimodal
- smell
license: mit
datasets:
- kordelfrance/olfaction-vision-language-dataset
- detection-datasets/coco
- seyonec/goodscents_leffingwell
base_model: Scentience-OVL-Classifiers-Base
---

# Olfaction-Vision-Language Classifiers


[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Colab](https://img.shields.io/badge/Run%20in-Colab-yellow?logo=google-colab)](https://colab.research.google.com/drive/1x6CfAvUUlS1gabNJoHqEQU-HyAy6yHoE?usp=sharing)
[![Paper](https://img.shields.io/badge/Research-Paper-red)](https://arxiv.org/abs/2506.00398)
[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/kordelfrance/olfaction-vision-language-classifiers)

</div>

---

## Description

This repository is a foundational series of multimodal joint classifier models trained on olfaction, vision, and language data.
It is meant as a quick start on loading the olfaction-vision-language models and getting the probability/logits of the presence of observed chemical compounds in a visual scene given a set of aroma descriptors.
For example, given an input image and a set of observed aromas (fruity, musky, etc), these models can give the probability that acetone is present.

Based on the original series of [embeddings models here](https://huggingface.co/kordelfrance/Olfaction-Vision-Language-Embeddings), these models are built specifically for prototyping and exploratory tasks within AR/VR, robotics, and embodied artificial intelligence.
Analogous to how CLIP and SigLIP embeddings give vision-language relationships, our embeddings models here give olfaction-vision-language (OVL) relationships.

Whether these models are used for better vision-scent navigation with drones, triangulating the source of an odor in an image, extracting aromas from a scene, or augmenting a VR experience with scent, we hope their release will catalyze further research in olfaction, especially olfactory robotics.
We especially hope these models encourage the community to contribute to building standardized datasets and evaluation protocols for olfaction-vision-language learning.

## Models
We offer two olfaction-vision-language (OVL) classifier models with this repository:
 - (1) `ovlc-gat`: The OVL base model built around a graph-attention network. This model is optimal for online tasks where accuracy is paramount and inference time is not as critical.
 - (2) `ovlc-base`: The original OVL base model optimized for faster inference and edge-based robotics. This model is optimized for export to common frameworks that run on Android, iOS, Rust, and others.

## Training Data
A sample dataset is included, but the full datasets are linked in the `Datasets` pane of this repo.
Training code for replicating full construction of all models will be released soon.

Please refer to original series of [embeddings models here](https://huggingface.co/kordelfrance/Olfaction-Vision-Language-Embeddings) for more information.


## Directory Structure

```text
Olfaction-Vision-Language-Classifier-Models/
├── data/                     # Sample training dataset
├── requirements.txt          # Python dependencies
├── model/                    # Classifier models
├── model_cards/              # Specifications for each embedding model
├── notebooks/                # Notebooks for loading the models for inference
├── src/                      # Source code for inference, model loading, utils
└── README.md                 # Overview of repository contributions and usage
```

---

## Citation
If you use any of these models, please cite:
```
    @misc{france2025ovlclassifiers,
        title = {Scentience-OVLC-v1: Joint Olfaction-Vision-Language Classifiers},
        author = {Kordel Kade France},
        year = {2025},
        howpublished = {Hugging Face},
        url = {https://huggingface.co/kordelfrance/Olfaction-Vision-Language-Classifiers}
    }
```

```
    @misc{france2025olfactionstandards,
          title={Position: Olfaction Standardization is Essential for the Advancement of Embodied Artificial Intelligence}, 
          author={Kordel K. France and Rohith Peddi and Nik Dennler and Ovidiu Daescu},
          year={2025},
          eprint={2506.00398},
          archivePrefix={arXiv},
          primaryClass={cs.AI},
          url={https://arxiv.org/abs/2506.00398}, 
    }
```


If you leverage the CLIP or SigLIP models, please cite:
```
    @misc{radford2021clip,
        title        = {Learning Transferable Visual Models From Natural Language Supervision},
        author       = {Alec Radford and Jong Wook Kim and Chris Hallacy and Aditya Ramesh and Gabriel Goh and Sandhini Agarwal and Girish Sastry and Amanda Askell and Pamela Mishkin and Jack Clark and Gretchen Krueger and Ilya Sutskever},
        year         = 2021,
        url          = {https://arxiv.org/abs/2103.00020},
        eprint       = {2103.00020},
        archiveprefix = {arXiv},
        primaryclass = {cs.CV}
    }
```

```
    @misc{zhai2023siglip,
          title={Sigmoid Loss for Language Image Pre-Training}, 
          author={Xiaohua Zhai and Basil Mustafa and Alexander Kolesnikov and Lucas Beyer},
          year={2023},
          eprint={2303.15343},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2303.15343}, 
}
```