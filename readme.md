# 🚀 What Can You Really Do With 5M$ in Space?
### A Bayesian Decision Model for CubeSat Mission Design

**Author:** BRAVO Diego
**Affiliation:** Lycée Saint-Guilhem / Hérault / FRANCE
**Context:** ESA–CNES Student Poster Challenge 2026  

---

## 🧭 1. Project Overview

CubeSat missions exhibit significant cost variability, ranging from less than 0.1M$ to over 100M$.  
In the context of New Space, designing missions under strict budget constraints has become a central challenge.

Traditional cost estimation methods are often inaccessible in early design phases, especially in academic or student-led projects.

👉 This project proposes a **data-driven and interpretable model** to:
- Estimate CubeSat mission cost
- Quantify uncertainty
- Support early-stage design decisions under budget constraints

---

## 🎯 2. Objective

The main objective is to answer a simple but practical question:

> **What kind of space mission can realistically be achieved with a fixed budget (e.g. 5M$)?**

To address this, a **Bayesian log-normal regression model** is developed and used as a **decision-support tool**.

---

## 🛰️ 3. Dataset Construction

A dataset of approximately **~100 CubeSat missions** was manually constructed using public sources.

### 📊 Features included ans used in the model:
- **Platform size** (1U to 16U)
- **Orbit type** (LEO, SSO, GEO, Deep Space)
- **Mission type**
- **Complexity score** *(constructed index)*
- **Total mission cost (USD)**

### 🧹 Data processing:
- Standardization of heterogeneous sources
- Currency normalization
- Handling missing values
- Manual curation of mission characteristics

### 📌 Notes:
- GEO and Deep Space missions were grouped due to limited data and similar cost structures
- A **complexity index** was defined to approximate technological difficulty:
  - Tech demo → ~1.2  
  - Earth observation → ~1.5  
  - Science → ~2.0–2.3  
  - Deep Space → >3  

---

## 📈 4. Exploratory Data Analysis

### 🔹Dsitribution of total Cost and Distribution of mission sizes
<p align='center'>
    <img src="./fig/cost_distribution_size_distribution.png" alt="Texte alternatif" width="300"/>
</p>

### 🔹 Cost vs Complexity across orbits
<p align='center'>
    <img src="./fig/evolution_of_cost_with_size.png" alt="Texte alternatif" width="300"/>
</p>

👉 Key observation:
- Mission cost increases **non-linearly** with complexity
- Higher orbits introduce **structural cost shifts**

---

## 🧠 5. Model Description

A **Bayesian log-normal regression model** is used to estimate mission cost.

### 🔹 Model formulation

\[
\ln(\text{Cost}) = \alpha_{\text{orbit}} + \beta_{\text{size}} \cdot \text{Size} + \beta_{\text{complexity}} \cdot \text{Complexity} + \beta_{\text{commercial}} \cdot \text{Commercial} + \beta_{\text{year}} \cdot \text{Year} + \epsilon
\]

### 🔹 Why this model?

- Captures **multiplicative cost effects**
- Reflects **exponential scaling** of mission budgets
- Ensures **strictly positive predictions**
- Provides **uncertainty estimates** via Bayesian inference

---

## ⚙️ 6. Model Inputs

- **Orbit** → environmental and operational constraints  
- **Size (U)** → platform scale  
- **Complexity** → technological difficulty  
- **Commercial status** → shared infrastructure effects  
- **Year** → temporal trend  

---

## 📊 7. Parameter Analysis

<p align='center'>
    <img src="./fig/impact_of_parameters_on_final_cost.png" alt="Texte alternatif" width="300"/>
</p>

### 🔹 Key findings:

- **Complexity** is the dominant driver of cost  
- **Size** has a moderate but consistent effect  
- **Commercial missions** tend to be slightly cheaper (shared infrastructure)  
- **Year effect** is weak / not significant  

👉 Example:

> +1 level of complexity → cost ×2.5 (on average)

---

## 🌍 8. Role of Orbit

Orbit introduces strong structural constraints:

- **LEO / SSO** → lower baseline cost  
- **GEO / Deep Space** → significantly higher cost  

👉 Reason:
- Increased communication requirements  
- Higher reliability constraints  
- Radiation protection  
- Longer mission duration  

---

## 📉 9. Predictive Behavior

<p align='center'>
    <img src="./fig/predictive_analysis_by_destination.png" alt="Texte alternatif" width="300"/>
</p>

### Observations:

- Cost increases with size, but moderately  
- Complexity drives **exponential growth**  
- Uncertainty increases for extreme missions (Deep Space, GEO)  

---

## 💰 10. Decision Scenario: 5M$ Budget

A practical case study was conducted using a fixed budget of **5M$**.

### Assumptions:
- Platform: 6U CubeSat  
- Commercial mission: Yes  
- Year: 2026  
- Orbit-specific complexity  

---

### 📊 Estimated costs (±1σ uncertainty ≈ 68%)

| Mission Type        | Orbit              | Estimated Cost (M$) | Feasible |
|--------------------|-------------------|---------------------|----------|
| Tech Demo (1.2)    | LEO               | 0.92 - 7.10           | ✅ Yes   |
| Earth Obs (1.5)    | SSO               | 1.10 - 8.50           | ⚠️ Limited |
| Science (2.2)      | GEO / Deep Space  | 1.47 - 11.37           | ❌ No    |
| Deep Space (3.2+)  | GEO / Deep Space  | 3.68 - 28.32           | ❌ No    |

👉 Interpretation:
- Low-complexity missions are feasible under tight budgets  
- High-complexity missions quickly exceed constraints  
- Orbit transition significantly increases cost pressure  

---
## 📏 11. Model Validation

### 🔹 Coverage of uncertainty intervals

To evaluate the reliability of the probabilistic predictions, we measure how many real observations fall within the model’s predicted uncertainty ranges.

Using a ±2σ interval (≈95% confidence for a log-normal distribution):

> **97.8% of observed mission costs fall within predicted bounds**

👉 Interpretation:
- The model provides **realistic uncertainty estimates**
- It captures the **high variability of space mission costs**

⚠️ However:  
This high coverage is partly explained by the **large dispersion of costs** in New Space missions, rather than purely high predictive precision.

---

### 🔹 Goodness of fit (R²)

A coefficient of determination (R²) was computed on log-transformed costs:

> **R² ≈ 0.33**

👉 Interpretation:
- A moderate R² reflects the **intrinsic variability** of space mission costs  
- Some cost drivers are not included in the model (e.g. payload, propulsion, reliability constraints)

⚠️ Important note:  
R² is not the most relevant metric for Bayesian log-normal models,  
as the objective is not only predictive accuracy but also **uncertainty quantification and interpretability**.

---

### 🔹 Key takeaway

The model should be interpreted as a:

> **Decision-support tool with calibrated uncertainty**,  
rather than a precise cost prediction system.


## 📌 12. Key Insights

- Mission cost scales **exponentially with complexity**  
- Orbit imposes **strong structural constraints**  
- Size plays a **secondary role**  
- Simple models can support **early-stage decision-making**

---

## ⚠️ 13. Limitations

- Limited dataset (~100 missions)  
- Few Deep Space observations  
- Complexity is a **constructed proxy**  
- Simplified model (no subsystem-level detail)  
- High cost dispersion inherent to space missions  

---

## 🚀 14. Perspectives

- Integrate **subsystem-level cost drivers** (payload, ADCS, power)  
- Expand dataset with **industrial data**  
- Develop a **design-to-cost decision framework**  
- Apply model to **CubeSat mission planning tools**  

---

## 🔗 15. Reproducibility

All data, code, and analysis are available in this repository.

👉 The model can be reused and extended for:
- Other budget scenarios
- Different mission profiles
- Educational or research purposes

---

## 📚 16. References (APA 7.0)

European Space Agency. (2023). *CubeSat missions and cost analysis*. ESA Publications.

Centre National d'Études Spatiales. (2022). *Nano-satellite mission reports*. CNES.

Swartwout, M. (2013). The first one hundred CubeSats: A statistical look. *Journal of Small Satellites*, 2(2), 213–233.

NASA. (2020). *Small spacecraft cost estimation handbook*. NASA Technical Reports.

Fortescue, P., Swinerd, G., & Stark, J. (2011). *Spacecraft systems engineering* (4th ed.). Wiley.

---

## 🧩 17. Additional Visualizations

| Visualization | Description |
|--------------|------------|
| <img src="./fig/evolution_of_cost_with_size.png" width="250"/> | **Cost vs Size (global)**<br>Shows the overall scaling of cost with platform size. |
| <img src="./fig/validation_r_squared.png.png" width="250"/> | **Prediction vs Actual (log-log)**<br>Evaluates how well the model reproduces real mission costs. |
| <img src="./fig/residual_analysis.png.png" width="250"/> | **Residual analysis (log space)**<br>Assesses model errors and potential biases. |


---

👉 These visualizations are not included in the poster for clarity,  
but provide deeper insight into model performance and limitations.

---

## 📬 Contact

[diego.bravo.contact@gmail.com](mailto:diego.bravo.contact@gmail.com)
