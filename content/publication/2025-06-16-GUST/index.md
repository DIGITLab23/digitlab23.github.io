---
title: "GUST: Quantifying Free-Form Geometric Uncertainty of Metamaterials Using Small Data"
authors:
- Cal_Zheng
- Cole_Jahnke
- Wei_Chen
date: "2025-06-16"
doi: "10.48550/arXiv.2506.12051"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-06-16"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "arXiv preprint arXiv:2506.12051"
publication_short: ""

abstract: This paper introduces GUST (Generative Uncertainty learning via Self-supervised pretraining and Transfer learning), a framework for quantifying free-form geometric uncertainties inherent in the manufacturing of metamaterials. GUST leverages the representational power of deep generative models to learn a high-dimensional conditional distribution of as-fabricated unit cell geometries given nominal designs, thereby enabling uncertainty quantification. To address the scarcity of real-world manufacturing data, GUST employs a two-stage learning process. First, it leverages self-supervised pretraining on a large-scale synthetic dataset to capture the structure variability inherent in metamaterial geometries and an approximated distribution of as-fabricated geometries given nominal designs. Subsequently, GUST employs transfer learning by fine-tuning the pretrained model on limited real-world manufacturing data, allowing it to adapt to specific manufacturing processes and nominal designs. With only 960 unit cells additively manufactured in only two passes, GUST can capture the variability in geometry and effective material properties. In contrast, directly training a generative model on the same amount of real-world data proves insufficient, as demonstrated through both qualitative and quantitative comparisons. This scalable and cost-effective approach significantly reduces data requirements while maintaining the effectiveness in learning complex, real-world geometric uncertainties, offering an affordable method for free-form geometric uncertainty quantification in the manufacturing of metamaterials. The capabilities of GUST hold significant promise for high-precision industries such as aerospace and biomedical engineering, where understanding and mitigating manufacturing uncertainties are critical.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# tags:
# - Source Themes
featured: false

links:
- name: Link
  url: https://arxiv.org/abs/2506.12051
url_pdf: 'https://arxiv.org/pdf/2506.12051'
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

