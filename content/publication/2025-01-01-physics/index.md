---
title: "Physics-Informed Geometric Operators to Support Surrogate, Dimension Reduction and Generative Models for Engineering Design"
authors:
- Shahroz Khan
- Zahid Masood
- Muhammad Usama
- Konstantinos Kostas
- Panagiotis Kaklis
- Wei_Chen
date: "2024-11-05"
doi: "10.1016/j.aei.2024.102937"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-11-05"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Advanced Engineering Informatics, 63*"
publication_short: ""

abstract: In this work, we propose a set of physics-informed geometric operators (GOs) to enrich the geometric data provided for training surrogate/discriminative models, dimension reduction, and generative models, typically employed for performance prediction, dimension reduction, and creating data-driven parameterisations, respectively. However, as both the input and output streams of these models consist of low-level shape representations, they often fail to capture shape characteristics essential for performance analyses. Therefore, the proposed GOs exploit the differential and integral properties of shapes--accessed through Fourier descriptors, curvature integrals, geometric moments, and their invariants--to infuse high-level intrinsic geometric information and physics into the feature vector used for training, even when employing simple model architectures or low-level parametric descriptions. We showed that for surrogate modelling, along with the inclusion of the notion of physics, GOs enact regularisation to reduce over-fitting and enhance generalisation to new, unseen designs. Furthermore, through extensive experimentation, we demonstrate that for dimension reduction and generative models, incorporating the proposed GOs enriches the training data with compact global and local geometric features. This significantly enhances the quality of the resulting latent space, thereby facilitating the generation of valid and diverse designs. Lastly, we also show that GOs can enable learning parametric sensitivities to a great extent. Consequently, these enhancements accelerate the convergence rate of shape optimisers towards optimal solutions.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# tags:
# - Source Themes
featured: false

links:
- name: Link
  url: https://www.sciencedirect.com/science/article/pii/S1474034624005883
url_pdf: 'https://arxiv.org/pdf/2407.07611'
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
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

