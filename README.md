# NGO Proposal Builder Demo

A Streamlit web application for building NGO project proposals with a guided multi-step form.

## Features

✨ **5-Step Form Wizard**
- Step 1: Basic Information (NGO name, project title, type, location, duration)
- Step 2: Needs Assessment & Goals (beneficiaries, problem statement, goals, expected outcomes)
- Step 3: Activities & Budget (key activities, budget, resources needed, budget notes)
- Step 4: Risks & Additional Notes (challenges, risks, mitigation strategies, additional notes)
- Step 5: Review & Download (view all details and download as text file)

🎨 **Custom Styling**
- Professional blue and green color scheme
- Responsive two-column layouts
- Smooth form card design with shadows and borders
- Mobile-friendly interface

💾 **Data Management**
- Session state management to preserve form data
- Download proposals as text files
- Reset form functionality
- Progress indicator

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chazerich-prog/NGO-Proposal-builder-Demo.git
cd NGO-Proposal-builder-Demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## How to Use the App

1. **Fill out the form** step by step using the "Next" button
2. **Navigate back** if you need to edit previous sections
3. **Review your proposal** in Step 5
4. **Download your proposal** as a text file with all your information

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Python** - Programming language
- **Streamlit** - Web framework for data applications
- **HTML/CSS** - Custom styling

## Features Included

- ✅ Multi-step form navigation
- ✅ Session state management
- ✅ Custom CSS styling
- ✅ Form data persistence
- ✅ Download functionality
- ✅ Form reset option
- ✅ Progress indicator
- ✅ Sidebar navigation

## Notes

- All form data is stored in Streamlit's session state and persists during the session
- Downloaded files will be named based on your project title
- The app uses responsive columns that adapt to different screen sizes

## Author

Created by chazerich-prog

## License

This project is open source and available for use.
