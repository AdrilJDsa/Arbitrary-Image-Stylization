# Arbitrary-Image-Stylization
Arbitrary Image Stylization aloows the combination of any content image with any style image. The model we use here is from Tensorflow Hub, arbitrary-image-stylization-v1-256/2, is based on a Feed-Forward Convolutinal Neural Network(CNN) that can perform stylization in real-time.

## Key Components of Neural Style Transfer
**1. Content Image:** This is the image whose structure or whose content is preserve in the stylized output.<br/>
**2.Style Image:** TThis is the image that defined the artistic styles(colors, texture) that are to be applied to the content image.<br/>
**3.Output Image(Stylized Image):** This is the result of blending the content image with the style of the second image.<br/>

## Architecture Behind Neural Style Transfer
The architecture used in the model is based on the following principles:

**1. Feature Extraction Using a Pre-trained CNN (VGG-based Network)**
The model leverages pre-trained CNNs (like VGG-19 or similar) to extract content and style features from the input images. These networks are trained on large datasets (like ImageNet) and are known to capture hierarchical features (edges, textures, patterns) from images.

Content Features: These are derived from deeper layers of the CNN where the network encodes the semantic structure of the image (such as objects and shapes).
Style Features: Style features are extracted from earlier layers of the CNN. These layers capture lower-level textures, patterns, and colors present in the style image.<br/>
**2. Gram Matrix for Style Representation**
To represent the style of an image, the model calculates a Gram matrix from the feature maps extracted by the CNN:<br/>

The Gram matrix computes the correlations between different feature maps of the style image, capturing the textures and patterns present.
This matrix essentially captures the relationships between different channels of the feature maps, representing the style without relying on the spatial arrangement of pixels.<br/>
**3. Transformation Network (Feed-forward Network)**
The core of the model is a feed-forward network that takes the content and style features as inputs and outputs a stylized image. This network is typically composed of convolutional layers that apply non-linear transformations to the content image based on the style image features.<br/>

Key components of the transformation network:

- Convolutional Layers: These are used to extract features from the content and style images.
- Instance Normalization Layers: Normalization is applied to improve the consistency of the output, which helps the network produce visually pleasing results.
- Non-linear Activation Functions (ReLU): These introduce non-linearity into the network, allowing it to capture complex patterns in the style image.
- The transformation network directly generates the stylized image in a single forward pass, making the model extremely efficient for real-time applications.<br/>

**4. Loss Functions**
The model optimizes several loss functions to achieve neural style transfer:

Content Loss:
This loss ensures that the output image retains the structure and details of the content image. It is typically calculated as the mean squared error between the feature maps of the content image and the stylized image, using deeper layers of the CNN.
Style Loss:
This loss ensures that the output image mimics the style of the style image. It is computed as the mean squared error between the Gram matrices of the style image and the stylized image.
Total Variation Loss (Optional):
This regularization term smooths the output by reducing noise and artifacts, promoting spatial coherence in the stylized image.
The overall loss function is a weighted sum of these components, where different weights are assigned to the content and style losses to control the trade-off between preserving the content and applying the style.

Training Process
The model is trained using pairs of content and style images, and it learns to combine the style of the style image with the content of the content image. The weights of the transformation network are updated using gradient-based optimization techniques (like Adam or SGD) to minimize the total loss function.

Once trained, the model can generalize to arbitrary content and style images, meaning it can be applied to any new pair of images for real-time style transfer.

## Arbitrary Style Transfer Architecture
Unlike earlier methods that required re-training for each style image, the model you are using achieves arbitrary style transfer. This is done by decoupling the content and style representations and allowing the model to transfer any style to any content image without needing re-training for new styles.
