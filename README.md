This repository contains codes for my pet project titled “Atom-based vector magnetometer self-calibrated via Deep Learning,” which was started after I finished my Ph.D. and while I was waiting for a visa to start my postdoctoral position at UCLA.  

Here I am numerically investigating if applying deep learning to a microwave-optical double-resonance signal in rubidium vapor can be used for measuring the magnitude and orientation of an external magnetic field.

Deconstruction of the title:

- “vector magnetometer” - a device that measures the magnitude and orientation of a magnetic field vector.
- “self-calibrated” -  it does not need any other magnetic-field device for calibration.
- “atom-based” - it relies on quantum effects in atomic rubidium vapor.
- “…via deep learning” - the magnetic field parameters are extracted from the optical signal by an artificial neural network.

## Set up

This project is based on the experimental setup used in my Ph.D. work at the University of Alberta. For detailed information, please see my [PhD thesis](https://era.library.ualberta.ca/items/b0cd4cfb-e3bd-46ac-a270-8950baea0d94) or our [paper](https://arxiv.org/pdf/2110.10673.pdf). Below I present a brief description.

The magnetometer is based on room-temperature rubidium vapor inside a microwave cavity. Depending on the frequency, applying a microwave magnetic field can affect the absorption of a laser light going through the vapor. A linear sweep of the microwave frequency results in an optical absorption pattern consisting of several peaks. The distance between the peaks depends on the magnitude of an external DC magnetic field, while their relative heights depend on the orientation of the DC field and the cavity axis. There is no analytical expression to relate the DC field angle and the relative peak heights, so I proposed to use Deep Learning to tackle this problem.

![Untitled](<img width="226" alt="image" src="https://user-images.githubusercontent.com/62848703/193723285-b91e5e57-c90c-4707-a02b-4ca8136c0c11.png">)

## Main idea

In particular, I was interested in investigating if a neural network trained on a synthetic, i.e., numerically simulated, data set can in principle be applied to real signals via transfer learning on a relatively small experimental data set.

## File Description

I experimented a lot with different network architectures, hyper-parameters, and approaches. I only include the most notable results.

Generate data.py - numerical simulation of the double-resonance signal. I use it to generate a synthetic data set to train and test neural networks.

pretrained_CNN  - I train a convolutional neural network on a “vanilla” data set, i.e., the signal is unaffected by the cavity linewidth and has no noise.

CNN fine-tune

Denoiser - autoencoder-based network for reducing noise in the signal. I suspect “denoiser” is not a real word, but it sounds cool, so I use it.

Classifier

## Future steps

- Investigate why there is no improvement in fine-tuning on the noisy data set when applying the denoiser, even though that is what someone would expect.
- I tried real transfer learning by adding new layers and freezing some of the old ones, but it did not seem to perform better than fine-tuning. Maybe needs more investigation.
- My classifier accuracy is 50% for 4 classes, which is better than randomly choosing one of them (25%) but still a very poor performance. In addition to tweaking the hyper-parameters, I assume that using a dataset with fully separated peaks might show a better performance.
