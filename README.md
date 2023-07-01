# Anime_Face_Generator_Practice
 this is my code when learning GAN hope this helpful to someone who learning btw i will use small dataset of anime face
 ""if i describe something wrong am so sorry for that""

## what is GAN?
generative adversarial networks(GAN) is a concept of discriminator(dis) and generator(gen) where a dis will tell is this fake or real and gen will try to generate image from random number(latent space) to create a fake image. the main point is gen will update it own weight through backpropage loss from dis
<img src="/image/gan.png" alt="Alt text" title="Optional title">

## DC-GAN 
this architecture dis will use convolution to capture information and gen will use tranpose convolution to generate image. you can see train process in this file(anime_generator.ipynb)
* generated image(256x256 size)
<img src="/image/Figure_1.png" alt="Alt text" title="Optional title">

* training metric
<img src="/image/first_plot%20loss.png" alt="Alt text" title="Optional title">

## W-GAN(upcoming)

## reference 
image gan from : https://developers.google.com/machine-learning/gan/gan_structure?hl=th
paper DCGAN source : https://arxiv.org/abs/1511.06434 
this data is a small pick from other dataset
you can get full dataset from here : https://www.kaggle.com/datasets/splcher/animefacedataset


