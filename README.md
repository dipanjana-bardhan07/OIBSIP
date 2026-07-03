

# Oasis Infobyte - Python Programming Tasks
Teeno internship tasks niche di gayi files mein available hain:
- Task 2 (BMI Calculator): bmi_calculator.py
- Task 3 (Password Generator): password_generator.py
- Task 6 (Weather App): weather_app.py

---
---

## 📊 Dataset Information

The system utilizes a generated dataset named `student_performance_dataset.csv` containing over **2,500 rows** of student profiles.

### Features Utilized
| Column Name | Data Type | Description / Range |
| :--- | :--- | :--- |
| **StudentID** | Categorical | Unique student identifier |
| **Age** | Numerical | Student age |
| **Gender** | Categorical | Male / Female |
| **AttendancePercentage**| Numerical | Percentage of classes attended (0 - 100) |
| **StudyHoursPerWeek** | Numerical | Average weekly hours spent studying |
| **AssignmentCompletionRate** | Numerical | Percentage of homework assignments completed (0 - 100) |
| **PreviousExamScore** | Numerical | Exam marks obtained in prior evaluations (0 - 100) |
| **ParticipationScore** | Numerical | Active classroom contribution scoring (0 - 100) |
| **ExtracurricularActivities**| Categorical | Engagement in school clubs/sports (Yes / No) |
| **InternetAccessAtHome**| Categorical | Connectivity availability (Yes / No) |
| **ParentEducationLevel**| Categorical | High School / Graduate / Postgraduate |
| **FinalExamScore** | Numerical | **Target Variable** (0 - 100%) |

### Dataset Generation Process
The dataset was engineered synthetically via Python's `NumPy` and `Pandas` packages. To maintain industrial validity, `FinalExamScore` was not built randomly; instead, it incorporates weighted dependencies representing human tendencies:
* Positive coefficients scaling directly with **Attendance**, **Study Hours**, and **Assignment Completion**.
* Structural anchoring based on **Previous Exam Performance**.
* Conditional baseline adjustments dictated by **Participation Levels** and **Parental Education**.
* Normal distribution noise insertion to simulate real-world variance.

---

## 🛠️ Technologies & Libraries Used
* **Core Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning Engines:** Scikit-learn (`LinearRegression`, `RandomForestRegressor`, `GradientBoostingRegressor`)
* **Statistical Visualizations:** Matplotlib, Seaborn

---

## 📈 EDA Insights & Core Findings
*(Update these with your specific observations once your analysis plots render)*

1. **Attendance vs Final Score:** A strong linear upward trend demonstrates that a threshold of $>85\%$ attendance significantly bounds the student's final score ceiling.
2. **Impact of Study Hours:** Average scores scale predictably with weekly study durations; diminishing marginal returns are noted past 25 hours.
3. **Assignment Completion:** High rates directly correspond with minimized risk of failing marks.
4. **Parental Influence:** Post-graduate backgrounds display a minor positive shift on baseline student preparation scores.

---

## 🚀 Model Performance Metrics

The predictive model was validated using an **80/20 train-test split**. Multiple algorithms were cross-compared to find the absolute lowest error margins:

| ML Model | MAE | MSE | RMSE | $R^2$ Score |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Regression** | [Insert] | [Insert] | [Insert] | [Insert]% |
| **Random Forest Regressor** | [Insert] | [Insert] | [Insert] | [Insert]% |
| **Gradient Boosting Regressor** | [Insert] | [Insert] | [Insert] | [Insert]% |

* **Final Selection:** `[Insert best model name]` was selected for production integration due to maximizing variance interpretation ($R^2$).

---

## 💻 Running the Project Locally

### 1. Installation Instructions
Ensure Python 3.8+ is installed. Clone the repository and install required project layers via terminal commands:

```bash
# Clone the repository
git clone [https://github.com/dipanjana-bardhan07/OIBSIP.git](https://github.com/dipanjana-bardhan07/OIBSIP.git)

# Move into the project directory
cd OIBSIP

# Install dependencies 
pip install -r requirements.txt
