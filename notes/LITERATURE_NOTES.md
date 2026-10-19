# Literature notes

These are my first notes based on the papers' abstracts and the material available online. I still need to read some of them in more detail once I decide on the topic.

## Network intrusion detection

### Khraisat et al. (2019) — `khraisat2019survey`
This paper explains different intrusion detection systems, mainly signature-based and anomaly-based detection. It also discusses common datasets and some of the challenges these systems face.

**How I could use it:** As background for explaining what intrusion detection is and why machine learning is used in this area. Since the paper is from 2019, I would also need more recent sources for specific models.

### Ring et al. (2019) — `ring2019survey`
The authors compare datasets used for network intrusion detection and describe properties that matter when choosing a dataset, such as the type of traffic and the way it was collected.

**How I could use it:** If I build and test an intrusion detection model, I need to explain why I selected a particular dataset. This paper could help with that part of the methodology.

### Sharafaldin et al. (2018) — `sharafaldin2018dataset`
This paper introduces the CICIDS2017 dataset, which includes normal network traffic and several types of attacks. It also describes the network setup and the features extracted from traffic.

**How I could use it:** CICIDS2017 could be the dataset for a practical experiment. I would use the paper when describing the data and the attack categories, and then check whether the dataset has any known limitations.

### Sommer and Paxson (2010) — `sommer2010outside`
This paper discusses why machine learning models that work well in research experiments might still be difficult to use in real networks. It points out problems such as false alarms and the differences between testing and real-world traffic.

**How I could use it:** For deciding how to evaluate a model. I should not only look at accuracy, but also false positives and how realistic the test is.

## Phishing detection

### Sahingoz et al. (2019) — `sahingoz2019phishing`
The paper uses information from URLs and different machine learning methods to distinguish phishing links from legitimate ones.

**How I could use it:** This could be a starting point if I choose to build a phishing URL detector. I could compare a few models and investigate which URL features are useful.

### Safi and Singh (2023) — `safi2023phishing`
This review compares different approaches to phishing website detection, including blacklists, visual similarities, machine learning and deep learning. It also looks at datasets used in previous work.

**How I could use it:** To understand which methods already exist and choose a manageable approach for a bachelor's thesis. It would also help me find more specific papers later.

## Ransomware detection

### Albshaier et al. (2024) — `albshaier2024ransomware`
This review covers ransomware detection methods, including detecting suspicious behavior before files are seriously affected.

**How I could use it:** To see whether I could make a small program that detects suspicious file or process behavior. I would first need to find a safe dataset or sample traces.

### Cen et al. (2024) — `cen2024ransomware`
This survey focuses on early ransomware detection and the difficulties in recognizing ransomware activity in time.

**How I could use it:** It could help me understand what signals are worth monitoring if I choose ransomware as the topic. Getting realistic data for this area may be more difficult.

## Current thoughts

Network intrusion detection seems the easiest to turn into a measurable practical project because there are public datasets and clear evaluation metrics. Phishing URL detection is also appealing because the input data is simpler. Ransomware detection sounds interesting, but I need to check the data and difficulty before choosing it.
