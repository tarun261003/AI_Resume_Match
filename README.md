# AI Resume Match Maker

## Video Demonstration
For a detailed walkthrough and demonstration of the AI Resume Match Maker, please refer to the video  




https://github.com/user-attachments/assets/6a07dc38-df50-49cd-8b56-6e10dd54ae0b



## Introduction
The AI Resume Match Maker is a Streamlit application designed to match resumes with job descriptions based on their content. Leveraging NLP models and AI services, it extracts and compares relevant details, providing a similarity score to streamline the hiring process.

## Project Scope
- Extraction of text from PDF, DOCX, and TXT resumes and job descriptions.
- Normalization and preprocessing of extracted text.
- Utilization of NLP models for information extraction and similarity computation.
- User interface development using Streamlit for interaction and visualization.

## Limitations and Constraints
- Focuses only on text-based resumes and job descriptions.
- The similarity score is based purely on textual content.
- Performance may vary based on the quality and format of the uploaded documents.

## Requirements

### Functional Requirements
- Ability to upload and parse job descriptions.
- Ability to upload and parse resumes.
- Matching algorithm to score and rank candidates based on job descriptions.
- User interface for displaying matching results to employers.

### Non-Functional Requirements
- The system should provide responses within a reasonable time frame.
- The user interface should be intuitive and easy to use.
- The system should handle various PDF formats and text extraction challenges.

## User Stories/Use Cases
- As a recruiter, I want to upload a resume and a job description to see how well they match.
- As a recruiter, I want to upload a resume and multiple job descriptions to find the best matches.
- As a user, I want to view the similarity score and detailed matching criteria.

## Technical Stack
- **Programming Languages:** Python
- **Frameworks/Libraries:** Streamlit, Scikit-learn, PyMuPDF, SentenceTransformer, Spacy, NLTK, OpenAI API, Qdrant
- **Databases:** Qdrant
- **Tools/Platforms:** Docker, Git, GitHub

## Architecture/Design
- **Frontend:** Developed using Streamlit for an interactive user interface.
- **Backend:** Flask application to handle requests and integrate with AI models.
- **Database:** Qdrant for vector storage.

## Development
- **Technologies and Frameworks:** Streamlit, PyMuPDF, SentenceTransformer, Spacy, NLTK, OpenAI
- **Coding Standards and Best Practices:** Followed PEP 8 guidelines, modular code structure, thorough commenting, and documentation.
- **Challenges:** Handling diverse PDF formats, optimizing similarity computation, integrating various NLP models.
- **Solutions:** Robust text extraction, efficient algorithms for text embedding, extensive testing for seamless integration.

## Testing
- **Testing Approach:** Unit tests for individual functions, system tests for overall functionality and performance.
- 
## User Guide
- **Using the Application:**
  1. Open your web browser and go to http://localhost:8501.
  2. Choose between "One Resume and One Job Description Matcher" or "One Resume and Multiple Job Descriptions Matcher".
  3. Upload the required PDF, DOCX, or TXT files.
  4. Click on "Check Match" to get the similarity score and insights.
- **Troubleshooting Tips:**
  - Ensure the uploaded files are in PDF, DOCX, or TXT format.
  - If the application is slow, try reloading the page or restarting the server.

## Conclusion
- **Project Outcomes and Achievements:**
  - Developed a functional Streamlit application that matches resumes with job descriptions.
  - Successfully integrated various NLP models.
  - Implemented robust document parsing and text extraction.
  - Optimized similarity computation for accurate and relevant matching results.
  - Provided an intuitive user interface for recruiters.

## Lessons Learned
- Importance of thorough testing and validation.
- Challenges with handling diverse document formats.
- Benefits of a modular code structure.
- Significance of choosing the right tools and frameworks.
- Value of continuous learning and adapting to new technologies.

## Areas for Improvement
- Expand to handle additional document formats.
- Incorporate additional factors like location and cultural fit.
- Enhance the user interface with more features.
- Implement advanced AI models for more accurate matching.
- Improve deployment process for cloud-based solutions.
