User Digital Twin – Insider Threat Detection

Overview
This project builds a **User Digital Twin system** to detect insider threats by modeling user behavior from email communication data. It identifies suspicious activities using machine learning and provides explainable risk insights.

Objective
To detect anomalous user behavior such as:
- Unusual communication patterns
- High number of recipients
- Excessive attachments
- Large data transfers
- Use of BCC (hidden recipients)

Approach

 1. Data Processing
- Cleaned and structured email dataset
- Extracted behavioral features:
  - Hour of activity
  - Day of week
  - Number of recipients
  - Attachment count
  - Email size
  - Content length

2. Feature Engineering
Created meaningful features:
- `total_recipients`
- `content_length`
- `to_count`, `cc_count`, `bcc_count`

3. Machine Learning Model
- Used **Isolation Forest** for anomaly detection
- Unsupervised learning (no labeled data required)

4. Risk Scoring
- Converted anomaly scores into **risk score (0–100)**
- Higher score = more suspicious behavior

5. Explainability
Each anomaly is explained using:
- Unusual time
- Too many recipients
- Multiple attachments
- Large email size
- BCC usage

Deployment
- Built an interactive dashboard using Streamlit
- Displays:
  - Data preview
  - Suspicious activities
  - Top risky users

Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

Sample Output
- Detects anomalies in user behavior
- Assigns risk score
- Provides explanation for flagged activities

Key Features
- Behavioral modeling (Digital Twin concept)
- Unsupervised anomaly detection
- Risk scoring system
- Explainable AI (XAI)
- Web-based dashboard

Live Demo
https://user-digital-twin-jadervkr6ypysbpfjgtlyx.streamlit.app/

Project Structure:
├── app.py
├── processed_sample.csv
├── README.md

Future Improvements
- Add real-time data streaming
- Improve model with deep learning (Autoencoders)
- Add user-wise behavior tracking dashboard
- Integrate alert system

Author
Harshita M
