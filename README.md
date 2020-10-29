Project: A java programme that recognizes single animal name(English) and produces matching animal sound.

Aim of this programme is to build up a visible system that is able to recognize some English words, and produce sound which represents the recognized word. Further, the number of English words is limited to only 36 in order to increase accuracy.

Approach:
1. Launch the programme by pressing the “start” button on screen
2. After loading is completed, wait approximately 10 seconds to let the computer starts
microphone, then people can speak to the microphone
3. Sphinx4 detects and recognizes the words that people speak
4. Sphinx4 outputs the recognized words (on the console)
5. The words is compared to a list of animal names
6. If the word exists, it will play the sound of the animal
7. If the word is not exist, it will not play any sound
8. Wait for another word and repeat step 3

About models
The work of speech recognition in this programme is done with the help of
CMU Sphinx. sphinx-core.jar and sphinx4-data.jar files are downloaded from: https://oss.sonatype.org/#nexus-search
There are basically three models required for speech recognition in Sphinx4:
1. Acoustic model
2. Phonetic dictionary
3. Language model

The acoustic model in this programme comes from the sphinx4-data,jar. However, the programme uses particular phonetic dictionary and language model due to the limited words that are used. The specific phonetic dictionary(5206.dic) and language model(5206.lm) are made by Sphinx Online Base Generator(http://www.speech.cs.cmu.edu/tools/lmtool- new.html).
