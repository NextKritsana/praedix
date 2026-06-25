---
title: "23강_Audio,Subtitle_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\23강_Audio,Subtitle_v1.2.pdf"
source_size_bytes: 800604
source_modified: 2025-10-18T20:01:18
imported_at: 2026-06-14T14:25:14
tags:
  - acs
  - acs-advanced
  - imported
---

# 23강_Audio,Subtitle_v1.2

- Source: [23강_Audio,Subtitle_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/23%EA%B0%95_Audio%2CSubtitle_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Audio, Subtitle, Multi Medio
• What is Audio
• Basic Concepts of Audio Data
• Extracting Information from Audio Data
• Subtitle is
• Basic Concepts of Subtitle Data
• Extracting Information in Subtitle Data
• Categorizing and synchronizing multimedia files
23
1

## Page 2

2
01. current page topic
What is Audio01
Audio
A signal of sound, especially vibrations transmitted within the range of sound that humans can hear.
Can exist in many forms, including music, speech, and environmental sounds, and can be recorded
and played back in two forms: analog and digital.
*Analog signal
A continuous signal, representing a physical quantity that changes over time (e.g., sound, light intensity,
voltage) as a continuous value.
*Digital signal
Represent information as discrete values.
Analog and digital signals have their own unique characteristics and uses.
Analog signals are best suited for direct representation of natural phenomena, while digital signals favor
accurate storage, processing, and transmission of data. Modern technology converts between these two
types of signals, taking advantage of the best of both worlds.

## Page 3

3
01. current page topic
What is Audio01
21st Century - Streaming Services and High-Resolution Audio
Streaming services have been around since the 2000s
High-resolution audio formats and services enter the consumer marketplace
19th Century - The Beginnings of Sound Recording
1877: Thomas Edison invents the phonograph,
 realizing the first technology to record and play back sound.
1887: Emile Berliner invents the gramophone and introduces the disk form of record.
Early 20th Century - Introduction of biographical recording
Circa 1925: Electrical recording was introduced, greatly improving the quality of audio.
The 1930s: Advances in magnetic tape technology
1930s: Magnetic tape technology is developed, making it much easier to record and edit audio
1960s: The rise of stereo sound Stereo recording is introduced commercially
The 1980s: Digital audio and CDs emerge
1982: Philips and Sony jointly introduce the compact disc (CD) to the market
1990s: MP3 and digital audio file formats emerge
1991: The MP3 (ISO/MPEG Audio Layer III) format is developed

## Page 4

4
01. current page topic
What is Audio01
Lossless formatting
WAV
Waveform Audio File Format
A standard audio file format developed
by Microsoft and IBM.
It is primarily used for storing lossless
quality audio and is highly compatible.
Widely used for professional audio
editing and recording, and as a system
sound file.
FLAC
Free Lossless Audio Codec
Open source format that provides lossless
compression.
Preserves full original audio quality while
providing a significantly lower file size
compared to WAV.
Ideal for storing and sharing high-quality
music files and archiving digital audio.
ALAC
Apple Lossless Audio Codec
A lossless audio codec developed by
Apple.
Compresses audio data similarly to FLAC,
but focuses on compatibility with Apple
devices and software.
Ideal for users who want to enjoy high-
quality audio on iTunes and Apple Music.
How to compress audio data while preserving it exactly the same as the original

## Page 5

5
01. current page topic
What is Audio01
Lossy compression formats
MP3
MPEG Audio Layer III
Most popular lossy audio compression
formats.
Compress audio at different bitrates to
 for flexible file size and quality
adjustments.
Digital music playback, over the Internet
Great for sharing and streaming audio
files.
AAC
Advanced Audio Coding
Formats that offer better
audio compression than MP3.
Maintain high audio quality at smaller file
sizes.
Widely used for music playback on
mobile devices, digital broadcasting, and
streaming services
OGG Vorbis
Open source lossy audio codec, free to
use without patent restrictions

Provides efficient compression and high
audio quality.
Ideal for storing background music and
sound effects from video games, internet
streaming services.
Removed some of the audio data to reduce file size

## Page 6

6
01. current page topic
Basic Concepts of Audio Data02
Sampling rate Bitrate
Sampling rate is the number of times a sample is taken (measured) per unit
of time. It is an important factor in determining the resolution of digital audio,
usually expressed in kilohertz (kHz) per second.
The sampling rate directly affects the quality of the audio signal.
Higher sampling rates allow for a more precise digital representation of the original
analog signal, resulting in higher sound quality.
Determines the bandwidth of an audio file.
According to the Nyquist theorem, frequencies up to half of the maximum
sampling rate can be accurately reproduced.
44.1 kHz: Used for CD-quality audio and covers the frequency range that humans
can hear (approximately 20 Hz to 20 kHz).
48 kHz, 96 kHz, 192 kHz: Used for professional audio work and high-resolution
audio.
You should choose the appropriate sampling rate based on your intended use.
For example, if you're producing CD-quality music, 44.1 kHz might be appropriate,
while you might consider a higher sampling rate for professional audio work.
Higher sampling rates mean larger file sizes and longer processing times.
The number of bits transmitted per second in an audio stream. It refers to the data
rate or encoding rate of an audio file, usually expressed in kbps (kilobits per second).
Bitrate directly affects the quality and size of an audio file.
Higher bitrates typically mean better audio quality, but also larger file sizes.
Conversely, lower bitrates can reduce file size, but at the expense of audio quality.
Bitrate is especially important in lossy compression audio formats (e.g. MP3, AAC).
These formats reduce file size by removing some information from the original
audio, and the bitrate setting determines how much of this information is removed.
At higher bitrates, lossy compression is less noticeable, improving audio quality.
Lossless compression vs. bitrate Lossless compression formats (e.g., FLAC, ALAC)
reduce file size while preserving exactly the original data. Bitrate still affects quality
and file size, but not as much as lossy compression formats.
In lossless compression, bitrate is primarily affected by compression efficiency.

## Page 7

7
01. current page topic
Basic Concepts of Audio Data02
Bit depth or sample depth
Bit depth refers to the number of bits used to represent one digital audio sample. Each
sample represents the amplitude (height) of a sound, and bit depth determines how finely this
amplitude value can be represented.
The higher the bit depth (i.e., the more bits are used to represent a sample), the more accurately
the subtle changes in the audio signal can be reproduced. This results in a wider dynamic range
in the audio file, better contrast of the signal against background noise, and better overall audio
quality.
16-bit: Most commonly used in CD-quality audio. Provides about 96 dB of dynamic range.
24-bit: Widely used in professional studio recordings, with a dynamic range of 144 dB, allowing
for more detailed audio recording and editing.
Dynamic range
The difference between the minimum audible noise level and the maximum undistorted signal
level. The higher the bit depth, the wider the possible dynamic range, allowing you to precisely
capture larger changes in sound.
Higher bit depth means better quality, but also larger file sizes. You should choose the
appropriate bit depth based on the quality needs of your project and the limitations of your
storage space.

## Page 8

8
01. current page topic
Basic Concepts of Audio Data02
Reverb
A mix of multiple echoes produced by sound
repeatedly bouncing off multiple surfaces,
Adds depth and space to your sound
Channels
Independent streams of audio signals. Each channel
contains different audio information, creating a spatial
dimension of sound when played together.
Phases
Dynamic scope
The difference between the minimum possible level
in an audio signal (typically the noise level) and the
maximum level (where distortion begins).
Echo
The phenomenon where the original audio signal is
reflected and heard after a certain time delay, which
depends on the size and shape of the room.
Describes how the waveform of an audio
signal varies along a time axis, expressing
how well two or more audio signals are
matched (synchronized).
Basic Concepts of Audio Data

## Page 9

9
01. current page topic
Basic Concepts of Audio Data02
FFT
Fast Fourier Transform
MFCC
Mel-Frequency Cepstral Coefficients
A "fast Fourier transform," an algorithm that converts a signal in the time
domain to the frequency domain. The transformation allows you to analyze
the different frequency components within a signal.
It is used to determine the presence or absence of certain frequency ranges
in an audio signal, or to analyze the spectrum of a signal.
For example, it can be used to isolate the sound of a particular instrument
in music, or to remove noise.
A technique for extracting features from audio signals that mimics the
way the human ear perceives them.
It is commonly used for speech recognition, music information retrieval,
sentiment analysis, and more.
The audio signal is divided into short frames, and an FFT is applied to
each frame to obtain a frequency spectrum. Then, a mel-scale filterbank
is applied to calculate the energy of the frequency bands that reflect
human hearing characteristics, which is then converted to a logarithmic
scale and cosine transformed to obtain the MFCC.
It effectively summarizes the characteristics of the speech signal and is
widely used as input to speech recognition and audio classification
algorithms.
Audio signal processing

## Page 10

10
01. current page topic
Basic Concepts of Audio Data02
STFT
Short-Time Fourier Transform
Wavelet Transform
LPC
Linear Predictive Coding
ZCR
Zero Crossing Rate
Energy and Entropy
How to analyze a signal by
breaking it down into
 short bursts at different
frequencies.
Audio signal processing
Along the time axis
Measure how often it passes
through zero
Used to analyze the frequency
component of a time-varying
 signal.
The spectrum of the speech signal
is represented by the
Technologies used to model
The energy of a signal is the
strength of the signal, Entropy
describes the disorder or
complexity of a signal.

## Page 11

11
01. current page topic
Extracting Information from Audio Data03
S p e e c h  r e c o g n i t i o n
The process of converting words that make
sense from audio data into text.
This technique is widely used in virtual
assistants, voice command systems, automatic
subtitle generation, and more.
The key is to accurately identify linguistic
features in the audio signal and map them to
text.
S e n t i m e n t  a n a l y s i s
The process of identifying the emotional state
of a speaker.
This is done by analyzing the tone, pitch, and
intensity of the voice to infer emotions such as
happiness, sadness, anger, etc.
Sentiment analysis can be used in customer
service, AI systems that require emotional
interaction, mental health monitoring, and
more.
Extracting Information from Audio Data

## Page 12

12
01. current page topic
Extracting Information from
Audio Data03
Adobe Audition
Software that provides advanced editing features
for professional audio work.
Features include noise reduction, audio restoration, multitrack editing,
and mastering to create high-quality audio productions. Helps you
extract information from audio data with advanced features like
speech analytics and automatic transcript alignment.
Audacity
Open source audio editing software that provides basic audio
processing functions such as recording, editing, and converting
audio files.
Users can use Audacity to remove noise from audio clips, adjust
volume, add effects, and more. Analysis tools allow users to visually
view the waveform and spectrum of an audio signal.
Extracting Information from Audio Data

## Page 13

13
01. current page topic
What is Subtitle04
Subtitle
Text that accompanies a multimedia file (movie, TV show, video, etc.) to allow viewers to
see the audio content in text form.
Translate and deliver audio content in other
languages into your audience's native
language.
Similar to closed captioning for the hard of
hearing, but often including more detailed
information, designed to help people with
hearing loss understand the subtleties of an
audio track.
Provide not only dialog, but also
background sounds, music, and
important nonverbal sound information
(such as "(the sound of a door closing)")
in text to help viewers with hearing
impairments understand audio content.
Used to provide essential information in a
particular scene or conversation.
Representative subtitle file formats:
SubRip Text (SRT), Advanced SubStation Alpha (ASS), Web Video Text Tracks (VTT), Web Video Text Tracks (VTT)

## Page 14

14
01. current page topic
What is Subtitle04
Subtitle
The latest advances in captioning technology
Automatic captioning: Advances in speech recognition technology have led to the development of
automatic captioning in real-time.
Increased multimedia accessibility: Closed captioning is not just for people with hearing impairments,
access to multimedia content, not only for people with hearing impairments, but also for people in
different languages.
Evolution of subtitle file formats
Analog subtitling era: In the early days, subtitles were printed directly on film or shown via separate
filmstrips
The rise of digital subtitling: The advent of digital video formats and DVDs revolutionized subtitle
production
Use of initial subtitles
In the dawn of the movie industry: Early movies were silent, so to convey dialog or descriptions
text cards on the screen to convey dialog or description.
The transition from silent to talkies: the rise of talkies in the late 1920s.
                                             Increased need for subtitles for multilingual audiences.
History of Subtitle

## Page 15

15
01. current page topic
Basic Concepts of Subtitle Data05
Understanding the Subtitle data format
One of the most widely used subtitle formats, simple
and highly compatible.
It consists of timecode and subtitle text, and does not
support complex styling options.
SRT (SubRip Text)
A modern subtitle format designed for use with
HTML5 video tags.
Similar to SRT, but supports styling, positioning, and
more metadata.
Web Video Text Tracks (WebVTT)

## Page 16

16
01. current page topic
Basic Concepts of Subtitle Data02
The process of separating text into tokens,
the smallest meaningful units, which can
often be words, phrases, or sentences.
Tokenization
The process of breaking down words into smaller
semantic units, morphemes, and analyzing their
structure. Morphemes are the smallest units of a
word's meaning, and depending on the
language, they may be suffixes, prefixes, roots,
etc.
Morphological analysis
The process of assigning a part of speech
(noun, verb, adjective, etc.) to each token
in a text.
Part of speech tagging
Natural language processing
05

## Page 17

17
01. current page topic
Basic Concepts of Subtitle Data02
Natural language processing
The process of identifying and
categorizing specific information in text,
such as people, places, institutions, etc.
Extracting noun phrases
The process of analyzing dependencies
between words in a sentence.
Dependency analysis
The process of analyzing the meaning
of text so that it can be understood by a
computer.
Semantic analysis
05

## Page 18

18
01. current page topic
Extracting information within Subtitle Data06
Tools for natural language processing
One of Python's oldest and most
widely used natural language
processing libraries. It is widely used
for educational and research
purposes, and supports basic NLP
tasks such as tokenization,
morphological analysis, part-of-
speech tagging, and parsing.
Modern NLP libraries
aimed at industrial
applications, with a focus
on speed and accuracy,
and strong support for a
wide range of languages.
Python library focused on topic
modeling and document similarity
analysis. Designed for processing
large text corpora.
A library that makes it easy to use
modern deep learning models
(BERT, GPT, etc.) for modern
natural language processing tasks.
Developed by Hugging Face.

## Page 19

19
01. current page topic
Extracting Information in
Subtitle Data03
How to Analyze Content with Subtitle Data
Extract keywords
Identifying important words or
phrases in your text data.
TF-IDF (Term Frequency-Inverse Document Frequency)
This method calculates importance based on how
often a word appears within a document and how
rare it is in the document set as a whole.
Text Rank
Graphs the relationships between words
in a document, then applies the PageRank
algorithm to extract important words.
Sentiment analysis
The process of identifying sentiment states such as
positive, negative, and neutral from text data.
06 Extracting information within Subtitle Data

## Page 20

20
01. current page topic
Extracting Information in
Subtitle Data03
How to Analyze Content with Subtitle Data
Machine learning methods
Train a classification model based on a
pre-tagged sentiment dataset. The model
classifies each sentence or line of subtitles
into a sentiment category, such as
positive, negative, etc.
Lexicon-based approaches
Dictionaries such as AFINN and
VADER assign a positive or
negative weight to each word.
The weights of the words in a
subtitle can be aggregated to
calculate a sentiment score for
the entire text.
06 Extracting information within Subtitle Data

## Page 21

21
01. current page topic
Multimedia file classification07
One of the most powerful and widely used command-line-based tools that can be used to rip video, audio, and subtitle tracks.
Supports almost all video and audio formats, and can perform a variety of conversion and processing tasks.
Multi-media extraction
where -i input.mp4 specifies the input file, -vn means to ignore the video track, -acodec copy means to copy the audio
codec without converting it, and output.aac is the name of the output audio file.
-an means to ignore the audio track, -vcodec copy means to copy the video codec without converting it
map 0:s:0 is an option to select the first subtitle stream
- Audio extraction example
- Video extraction example
- Example subtitle extraction

## Page 22

22
01. current page topic
Multimedia file classification01
Multi-media Compositing
-i video.mp4 and -i audio.mp3 represent the input files, -c:v copy means no video codec conversion,
 -c:a aac means use AAC as the audio codec output.mp4 is the filename to be generated
Combining the video file video.mp4 and the subtitle file subtitle.srt to create output.mp4.
where -c:s mov_text is the codec option for the subtitle stream.
One of the most powerful and widely used command-line-based tools that can be used to rip video, audio, and subtitle tracks.
Supports almost all video and audio formats, and can perform a variety of conversion and processing tasks.
07
