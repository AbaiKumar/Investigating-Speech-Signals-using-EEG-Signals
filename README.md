
# Investigating Speech Signals Using BCI

## Abstract:

Brain-Computer Interfaces (BCIs) offer a promising avenue for direct communication by bridging the gap between the brain and external devices. This project investigates the role of the TP9 region in speech generation using Electroencephalography (EEG) signals. The TP9 region remains relatively unexplored in speech production, but we hypothesize it plays a crucial role. By utilizing EEG, a non-invasive neuroimaging technique, this study aims to pinpoint the TP9 region's contribution to speech signal generation. Participants engaged in speech imagination tasks while their neural activity was recorded. The data underwent rigorous analysis using signal processing algorithms and machine learning to isolate the neural signatures associated with the TP9 region during speech production. This research has potential implications for advancing our understanding of neuroscience, as well as for developing clinical applications and interventions for speech disorders.

## Proposed System:

Traditional communication methods rely on a complex interplay between the brain, nerves, and muscles. However, for individuals with severe neurological conditions like ALS or brainstem stroke, these pathways become disrupted, leaving them struggling to speak, write, or even gesture. Brain-Computer Interfaces (BCIs) offer a glimmer of hope in such situations. These innovative systems act as a bridge between the brain and external devices, establishing a direct communication channel.

This project delves into the potential of BCIs for speech generation, specifically focusing on the role of the TP9 region in the brain. While relatively unexplored in speech production, we hypothesize that TP9 plays a crucial part in this process. To investigate this, the study utilizes Electroencephalography (EEG), a non-invasive neuroimaging technique that measures electrical activity in the brain. Participants engaged in tasks where they imagined speaking specific words while their brain activity was recorded.
Following data collection, the research team employs a two-pronged approach: signal processing algorithms and machine learning. These techniques are used to sift through the complex brain activity data and isolate the specific neural signatures associated with the TP9 region during speech production. By successfully identifying these signatures, the research has the potential to significantly advance our understanding of how the brain generates speech. Furthermore, it could pave the way for the development of crucial clinical applications and interventions for individuals suffering from speech disorders.

## Data Collection Steps and Cleaning STeps:

The data collection phase begins with participant selection based on predefined criteria. Speech and imagined speech tasks are designed to prompt specific word responses. The Muse EEG device is set up to record neural activities, focusing on the TP9 region. During the tasks, EEG data is collected, capturing brain responses associated with the spoken and imagined words. In the subsequent data cleaning phase, eye blink artifacts are removed. Further cleaning involves addressing challenges such as repeated values, connection loss, and noisy segments. Techniques like outlier removal, missing data imputation, and specialized algorithms for eye blink removal are applied to ensure data quality. Once cleaned, frequency domain features are extracted from the EEG data, providing insights into the neural correlates of speech processing. This rigorous process ensures that the collected data is reliable and suitable for subsequent analysis.

## T Test:

A t-test is a statistical method employed to assess whether there is a significant difference between the means of two groups. It's particularly useful when comparing the means of two sets of data, such as brain activity patterns recorded during different conditions.

![TTest Output](Output/ttest.png)

## Model Selection

Used Pycaret python library to select the most suitable model for our EEG Datasets. Both Random Forest and Extra Tree Classifier were rigorously evaluated. Through their application, valuable insights into the neural mechanisms underlying speech production were gleaned. While both models were utilized without a notion of superiority, Random Forest and Extra Tree Classifier each offered unique perspectives on the data. Additionally, recommendations were made for refining the models and improving data collection practices to bolster future studies.

![Pycaret Output](Output/pycaret.png)

## Testing with Unseen Data
![Pycaret Output](Output/test_sample.png)

