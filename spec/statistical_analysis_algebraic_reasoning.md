# Statistical Analysis & Algebraic Reasoning — Course Map

> **STATUS: CONFIRMED 2026-08-05 — course map approved by the user; scaffolded the same day.**

## Course philosophy

A statistics-first course for students who have completed Algebra 1. It blends the
data-analysis and function strands of AFDA with the Probability & Statistics SOLs,
leaning heavier on statistics than algebra and carrying no trigonometry. Every lesson
starts from a real-world context, computes, then **interprets and justifies**. The
data cycle (formulate → collect → represent → analyze/communicate) recurs in every
unit, and each semester ends in inference-ready territory: semester 1 is *data and
chance* (Units 1–4), semester 2 is *models and decisions* (Units 5–8). Projects with
real data anchor Units 1, 5, 6, and 8.

Source standards (all in `spec/`):

- **PS.\*** — 2023 Probability & Statistics SOL (primary stats strand)
- **AFDA.\*** — 2023 Algebra, Functions & Data Analysis SOL (function families, data
  cycle, probability, normal distribution)
- **A2.\*** — 2023 Algebra 2 SOL (cited only where the course description exceeds
  AFDA: polynomial characteristics, logarithmic functions, curve of best fit)

Scope notes: read the matching "Understanding the Standards" pages before authoring
any lesson. AFDA.AF.3 (linear programming) is **excluded** — it is outside the
course description. No trig. Counting (permutations/combinations) is included via
AFDA.DA.3g–i / A2.ST.3, with a second lesson applying counting to probability
(licensed by AFDA.DA.3a's theoretical-probability formula).

**Lesson 0 convention:** every unit carries an introductory **Lesson 0**
(`lesson00/`) — a unit-launch lesson (hook context, vocabulary preview,
prerequisite review) that sits *outside* the 8-content-lesson cap. The numbered
lessons below are content lessons only.

## Unit map

### Unit 1 — Asking Questions with Data: Study Design (8 lessons)
Standards: PS.DC.1, PS.DC.2, PS.DC.3, AFDA.DA.2

1. The statistical cycle; formulating questions; types of data (PS.DC.1a–c; AFDA.DA.2a)
2. Population vs. sample; parameter vs. statistic; constraints (PS.DC.1d–e)
3. Sampling techniques: SRS, stratified, systematic, cluster (PS.DC.2a–b; AFDA.DA.2b)
4. Bias in samples and surveys (PS.DC.2c; AFDA.DA.2e–g)
5. Observational studies (PS.DC.2d)
6. Principles of experimental design (PS.DC.3a–b; AFDA.DA.2c)
7. Experiments vs. observational studies; choosing a collection method (PS.DC.3c–e)
8. Project: design and conduct a class survey (AFDA.DA.2d, h–j; PS.DC.2d)

### Unit 2 — Describing One Variable (7 lessons)
Standards: PS.DS.1, PS.DS.2, PS.DS.3

1. Dot plots, stemplots, histograms (PS.DS.1a)
2. Boxplots and cumulative frequency graphs (PS.DS.1a)
3. Shape, center, spread, and unusual features from graphs (PS.DS.1b)
4. Measures of center: mean, median, mode (PS.DS.2a)
5. Measures of spread: range, IQR, variance, standard deviation (PS.DS.2b, e)
6. Outliers and their influence (PS.DS.2c–d)
7. Comparing distributions (PS.DS.3a–b)

### Unit 3 — Categorical Data & Probability (8 lessons)
Standards: PS.DS.4, PS.P.1, AFDA.DA.3

1. Displaying categorical data: bar graphs & two-way tables (PS.DS.4a–d)
2. Probability basics: theoretical probability, complements (PS.P.1a; AFDA.DA.3a, e)
3. Venn diagrams, tree diagrams, two-way-table probabilities (PS.P.1b; AFDA.DA.3c)
4. Addition & multiplication rules; mutually exclusive vs. independent (PS.P.1a, c; AFDA.DA.3f)
5. Conditional probability and independence (PS.P.1d; AFDA.DA.3b)
6. Simulations and probability-based decisions (AFDA.DA.3d)
7. Counting techniques: Fundamental Counting Principle, permutations, combinations (AFDA.DA.3g–i; A2.ST.3a–c, e)
8. Probability with counting: applications (AFDA.DA.3a, g–i; A2.ST.3d)

### Unit 4 — Random Variables & the Normal Distribution (7 lessons)
Standards: PS.P.2, PS.P.3, AFDA.DA.4

1. Discrete random variables and probability distributions (PS.P.2a, g)
2. Expected value and standard deviation of a discrete RV (PS.P.2b)
3. Binomial distributions (PS.P.2c–f)
4. Continuous distributions; properties of the normal curve (PS.P.3a; AFDA.DA.4a–c)
5. The Empirical Rule (PS.P.3b; AFDA.DA.4b)
6. z-scores; comparing values across distributions (PS.P.3d–e; AFDA.DA.4d–e)
7. Normal probabilities with technology (PS.P.3c, f; AFDA.DA.4f–h)

### Unit 5 — Linear Functions & Linear Models (7 lessons)
Standards: AFDA.AF.1 (linear), AFDA.AF.2, PS.DS.5, PS.DS.6, AFDA.DA.1

1. Function families and transformations: the linear parent (AFDA.AF.1a–b, d, f)
2. Characteristics of graphs: domain/range, intercepts, behavior, incl. piecewise (AFDA.AF.2a–e, h)
3. Scatterplots: form, direction, strength, unusual features (PS.DS.5a–b; AFDA.DA.1a–c)
4. Least-squares regression: slope and intercept in context (PS.DS.6a)
5. Correlation r and coefficient of determination r² (PS.DS.6b–c)
6. Predictions, extrapolation, residuals (PS.DS.6d–f; AFDA.DA.1d)
7. Project: the data cycle with bivariate data (AFDA.DA.1a–d; A2.ST.2a–c)

### Unit 6 — Nonlinear Models: Polynomial, Exponential & Logarithmic (8 lessons)
Standards: AFDA.AF.1, AFDA.AF.2, AFDA.DA.1, A2.F.1, A2.F.2, A2.ST.2

1. Quadratic functions and transformations (AFDA.AF.1a–b, d, f)
2. Characteristics of quadratics: vertex, zeros, max/min (AFDA.AF.2c–d, h)
3. Polynomial functions: graphs and end behavior (A2.F.2b, g; AFDA.AF.2f)
4. Exponential functions: growth and decay (AFDA.AF.1a–b; A2.F.1a–c; AFDA.AF.2g)
5. Logarithmic functions (A2.F.1a–c, e; A2.F.2h)
6. Which model fits? Comparing function families (AFDA.AF.1c, g; A2.ST.2d)
7. Curve of best fit with technology (AFDA.DA.1c–d; A2.ST.2e–f)
8. Project: model a real dataset and justify the choice (AFDA.DA.1a–d; A2.ST.2g–h)

### Unit 7 — Sampling Distributions & Inference for Proportions (7 lessons)
Standards: PS.IS.1

1. Sampling variability; the sampling distribution of p̂ (PS.IS.1a)
2. Point estimates and margin of error (PS.IS.1d)
3. Confidence intervals for a proportion (PS.IS.1b)
4. Confidence level, sample size, and interval width (PS.IS.1c)
5. The logic of hypothesis testing (PS.IS.1e)
6. One-sample z test for a proportion (PS.IS.1f)
7. Project: a statistical study about a proportion (PS.IS.1g)

### Unit 8 — Inference for Means & Course Capstone (6 lessons)
Standards: PS.IS.2

1. The sampling distribution of the mean; Central Limit Theorem (PS.IS.2a, c)
2. The t distribution (PS.IS.2d)
3. Confidence intervals for a mean (PS.IS.2b, e)
4. One-sample t test: hypotheses, conditions, p-value (PS.IS.2f.i–iii)
5. One-sample t test: decisions and interpretation (PS.IS.2f.iv–v)
6. Capstone: the full data cycle with inference

## Coverage audit

- Every PS standard is covered: DC.1–3 (U1), DS.1–3 (U2), DS.4 (U3), DS.5–6 (U5),
  P.1 (U3), P.2–3 (U4), IS.1 (U7), IS.2 (U8).
- Every AFDA standard is covered except **AFDA.AF.3** (linear programming — excluded
  by design): AF.1–2 (U5–6), DA.1 (U5–6), DA.2 (U1), DA.3 (U3), DA.4 (U4).
- A2 codes are cited only for polynomial/logarithmic reach-ins (A2.F.1, A2.F.2,
  A2.ST.2, A2.ST.3) — never as standalone lesson drivers.
- Total: 58 content lessons across 8 units (≤ 8 content lessons per unit), plus one
  Lesson 0 unit launch per unit (66 lesson directories in all).
