---
title: "28강_Anti-Anti-Forensic_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\28강_Anti-Anti-Forensic_v.1.2.pdf"
source_size_bytes: 614999
source_modified: 2025-10-18T20:15:05
imported_at: 2026-06-14T14:25:18
tags:
  - acs
  - acs-advanced
  - imported
---

# 28강_Anti-Anti-Forensic_v.1.2

- Source: [28강_Anti-Anti-Forensic_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/28%EA%B0%95_Anti-Anti-Forensic_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Anti-Anti-Forensic
• New-Anti Forensic
• Anti-Anti Forensic
28
1

## Page 2

2
01. current page topic
New-Anti Forensic01
While the term "Minimizing the Footprint" is used in many fields,
computer security and digital forensics, it's a particularly important concept to understand.
In this context, "footprint" refers to the amount of trace or data you leave behind on a system or
network, and "minimizing the footprint" refers to the process of minimizing that trace.
Minimizing the Footprint in Digital Security
A hacker's perspective: Hackers attempt to leave as few traces as possible while carrying out an attack.
This is to prevent the attack from being detected or traced back to them. Attackers can minimize their
traces by manipulating log files or deleting data.
A security professional's perspective: Security professionals monitor and manage systems or networks,
looking for signs of security threats. They need to conduct their investigations with as little impact on
the system as possible, so they use methods to minimize their "footprint.
Minimizing the Footprint in Digital Forensics
Forensic investigation: Digital forensic experts strive to have as little impact on the original data as
possible during the evidence collection process. This is to protect the integrity of the evidence and
prevent further data corruption or alteration during the investigation.
Minimizing the Footprint in Data Centers and Cloud Computing
Resource optimization: In a data center or cloud environment, use strategies to minimize your
"footprint" to optimize storage space, processing power, energy usage, etc.
Strategies for Minimizing the Footprint
Data encryption and anonymization, access control and permission management, log management
and monitoring

## Page 3

3
01. current page topic
New-Anti Forensic01
Data self-destruction
A technique that automatically deletes or transforms
data when certain conditions are met, which can be
triggered by a physical trigger or software command.
This code, On the first execution, the script simulates an
action that could be considered deleting program data,
and then deletes itself.
When a second execution is attempted, the script prints
a message that it has already self-destructed and
performs no further actions.
New-Anti Forensic

## Page 4

4
01. current page topic
New-Anti Forensic01
Declared a global variable called self_destructed and initialized it to False.
Tracks whether the script has already been executed and self-destructed
Define the main function and use the global keyword to make the
self_destructed variable available as a global variable within the function
Check for self-destruct condition If self_destructed is False,
 i.e. the script hasn't self-destructed yet,
 print a self-destruct message to the user and wait 5 seconds
New-Anti Forensic

## Page 5

5
01. current page topic
01
Read the self-correcting script file and changed the
line self_destructed = False to self_destructed =
True. Makes sure that the script does not meet the
self-destruct condition on the next run.
Deleting a file The script deletes itself using the
os.remove function.  The __file__ variable represents
the path to the currently running script file.
What to do if it has already self-destructed.
If self_destructed is True, i.e. the script has already
been executed and self-destructed, print a message
to notify the user.
Calls the main function when the script is run
directly. Standard Python code that is not executed
when the script is imported as a module.
New-Anti Forensic

## Page 6

6
01. current page topic
New-Anti Forensic01
Paper summaries
New-Anti Forensic

## Page 7

7
01. current page topic
New-Anti Forensic01
Weak anti-forensic techniques for media forgery detection
 Image Sharpening Detection
1
2
Unsharp Masking (USM) is a popular technique in image processing, designed to
improve the sharpness of images.
Despite the name "Unsharp", the technique is used to make images sharper.
USM increases the contrast of an image, making details stand out more.
3
WHAT IS
USM
HOW IT
WORKSFEATURES
Generate a low-bandwidth image from the original image: First, soften the original
image to create a low-bandwidth version (blurred image).
This process usually uses a Gaussian blur filter.
Calculate the difference between the blurred image and the original image: by
subtracting the blurred image from the original image,
Create a "mask" that corresponds to the details and edges of the image.
Highlight mask and add to original image: Highlight (increase contrast) the generated
mask and add it back to the original image.
This increases the sharpness of the image, making details and edges stand out more.
Emphasize details: By emphasizing details and textures in the image,
improving overall sharpness
Variable adjustability: USM can be adjusted by adjusting parameters such as "Amount"
(intensity), "Radius" (blur range), "Threshold" (application threshold), etc,
Granular control over how much sharpness is increased
Wide range of applications: Used in digital photo editing, print media preparation,
online content creation, etc.
New-Anti Forensic

## Page 8

8
01. current page topic
New-Anti Forensic01
Weak anti-forensic techniques for media forgery detection
 Using Unsharp Masking to Detect Image Sharpening
1
2
Frequency analysis of images:
USM processed images can show changes in certain frequency bands.
These changes can be analyzed to determine if the image has been USM processed.
3
ANALYZE
THE
FREQUENC
Y OF AN
IMAGE
DETECT
EDGE AND
DETAIL
CHANGES
STATISTICAL
METHODS
Detect edge and detail changes:
USM emphasizes the edges and details of an image.
USM processing can be detected by analyzing the changed edge intensity and contrast of details.
Statistical methods:
You can analyze statistical properties of an image to find features of USM processing.
For example, you can statistically analyze the histogram or contrast variation of an image.
New-Anti Forensic

## Page 9

9
01. current page topic
New-Anti Forensic01
Weak anti-forensic techniques for media forgery detection
GAN Based Techniques
Application and ethical considerations
While they can be used for legitimate purposes, such as art, entertainment, and data
augmentation, they also have the potential to be abused for negative purposes, such as
copyright violations, privacy violations, and the creation of fake news. Therefore, ethical
consideration of the purpose and application of these technologies is critical when
developing and using them.
Advances in image forensics are constantly evolving to respond to new technologies, such
as image generation using GANs. Efforts to verify the provenance of images and identify
manipulated content will need to continue alongside technological advances.
01 Basic GAN structure: A GAN is composed of two neural networks: a Generator and a Discriminator
02
Learning and inserting camera model traces:
Camera model traces are subtle patterns or noise that originate from a camera's sensor, lens, image processing algorithms, etc.
03
Forensic detector deception:
Fake images with traces of the camera model can look more similar to images taken with a real camera than images generated with a typical GAN
Can be used to disguise the origin of an image or manipulate its
authenticity. In particular, it can be used to make an image appear to have
been taken with a real camera, or to trick a GAN image detector into
mistaking a fake image for a real one.
Generative Adversarial Networks (GANs)
to insert traces of the camera model into the generated image.
New-Anti Forensic

## Page 10

10
01. current page topic
New-Anti Forensic01
In-paper detection methods
M e d i a n  f i l t e r
A technique often used to remove noise in
image processing. For a given pixel's value, it
calculates the median value of neighboring
pixel values and replaces that pixel's value with
the median value. This process can effectively
blur features used for source identification,
such as noise from the camera sensor or
specific patterns.
G e n e r a t i v e  n e t w o r k s
Generating new images using algorithms such as
Generative Adversarial Networks (GANs). The
generated images can mimic the features of a
specific camera sensor or create images with
entirely new features. This technique can be used
to completely hide or tamper with existing camera
traces to thwart forensic analysis.
New-Anti Forensic

## Page 11

11
New-Anti Forensic01
In-paper detection methods
C o m p r e s s i o n  B a s e d  T e c h n i q u e s
This involves changing the primary statistics of an image so that it appears to have undergone a single compression cycle, even if
the image has been compressed multiple times. This can be achieved through a variety of methods, including the use of
optimization algorithms designed to remove signs of JPEG compression.
Optimization algorithms can modify certain characteristics of the image data (such as the quantization table and DCT coefficients)
in a way that masks typical patterns left behind by JPEG compression. This helps preserve the visual quality of the image andmakes
it more difficult for forensic analysts to use compression artifacts as a way to prove that the image has been manipulated. This is an
advanced technique that requires a deep understanding of video compression algorithms and forensic detection methods.
By applying these techniques, manipulated images can be delivered as if they were compressed only once to avoid arousing
suspicion in forensic analysis. However, it is important to note that while these techniques can be used for legitimate purposes,
such as protecting the privacy of individuals or intellectual property, they can also be useful for deceptive behavior, such as creating
convincing forgeries or hiding evidence of image manipulation.
New-Anti Forensic

## Page 12

12
01. current page topic
New-Anti Forensic01
In-paper detection methods
STATISTICAL BASED TECHNIQUES
03
STEP
 as one of the anti-forensic methods to disrupt the detection
of contrast enhancement in images,
Techniques to transform the
 first order statistics of image histograms
One method suggested by statistical-based techniques.
Helps to hide artifacts from contrast enhancement
without degrading the quality of the image.
One of the most common methods used to
improve the sharpness of an image.
Adjusting the brightness contrast of an image to
make details stand out more
ENHANCE
CONTRAST
LOCAL
RANDOM
DITHERING
New-Anti Forensic

## Page 13

13
01. current page topic
New-Anti Forensic01
In-paper detection methods
H i s t o g r a m  m a n i p u l a t i o n
The histogram of an image shows the brightness
distribution of the pixels.
By manipulating the histogram, you can hide
traces of manipulation, such as certain statistical
patterns left by brightness adjustments or
sharpening.
U s i n g  W G A N- GP
WGAN-GP is a type of GAN known for its stable
training and high-quality image generation.
Compared to regular GANs, WGAN-GP uses the
Wasserstein distance to measure the difference
between the generated image and the real
image, and introduces a gradient penalty for
more stable training.
New-Anti Forensic

## Page 14

14
01. current page topic
Anti-Anti Forensic02
Anti-Anti Forensic
 Technologies and methodologies developed to combat anti-forensic techniques

## Page 15

15
01. current page topic
Anti-Anti Forensic02
Counter anti-forensic techniques in your paper
Sensor Based Techniques
Used to detect methods for planting sensor
fingerprints in manipulated images. When
noise patterns that mimic the noise patterns of
a real camera sensor are added to a
manipulated image, the manipulated image
will show sensor fingerprints similar to the real
image. This method uses sensor noise analysis
to find traces of these fake sensor fingerprints,
which can be used to determine whether an
image has been manipulated.
Statistical Based Counter Techniques
Statistical counterparts to Contrast Enhancement
(CE) detection Algorithms analyze the statistical
properties of an image, using techniques that
exploit features of images that have used CE to
make CE detection more difficult. For example, a
Spatial Co-occurrence Matrix can be used to
determine whether CE has been used in an
image. These methods are effective in detecting
the use of anti-forensic techniques to hide traces
of CE.
Anti-Anti Forensic

## Page 16

16
01. current page topic
Anti-Anti Forensic02
Monitor log files for hiding or tampering
01
STEP
Generate and store an
initial hash value
Anti-Anti Forensic
“““Create hash value for a file”””
“““Save the hash value file”””

## Page 17

17
01. current page topic
Anti-Anti Forensic02
Monitor log files for hiding or tampering
Validating hash values
02
STEP
Anti-Anti Forensic
“““Create current file hash value, compare to stored hash value”””
