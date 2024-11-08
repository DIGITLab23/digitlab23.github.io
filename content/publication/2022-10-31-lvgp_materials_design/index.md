---
title: "Uncertainty-Aware Mixed-Variable Machine Learning for Materials Design"
authors:
- Hengrui Zhang
- Wei_Chen
- Akshay Iyer
- Daniel W. Apley
- Wei Chen
date: "2022-10-31"
doi: "10.1038/s41598-022-23431-2"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-10-31"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Scientific Reports, 12*"
publication_short: ""

abstract: Data-driven design shows the promise of accelerating materials discovery but is challenging due to the prohibitive cost of searching the vast design space of chemistry, structure, and synthesis methods. Bayesian optimization (BO) employs uncertainty-aware machine learning models to select promising designs to evaluate, hence reducing the cost. However, BO with mixed numerical and categorical variables, which is of particular interest in materials design, has not been well studied. In this work, we survey frequentist and Bayesian approaches to uncertainty quantification of machine learning with mixed variables. We then conduct a systematic comparative study of their performances in BO using a popular representative model from each group, the random forest-based Lolo model (frequentist) and the latent variable Gaussian process model (Bayesian). We examine the efficacy of the two models in the optimization of mathematical functions, as well as properties of structural and functional materials, where we observe performance differences as related to problem dimensionality and complexity. By investigating the machine learning models’ predictive and uncertainty estimation capabilities, we provide interpretations of the observed performance differences. Our results provide practical guidance on choosing between frequentist and Bayesian uncertainty-aware machine learning models for mixed-variable BO in materials design.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://www.nature.com/articles/s41598-022-23431-2"
url_pdf: 'files/papers/2207.04994.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
