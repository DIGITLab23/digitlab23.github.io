---
title: "GAN-DUF: Hierarchical Deep Generative Models for Design Under Free-Form Geometric Uncertainty"
authors:
- Wei_Chen
- Doksoo Lee
- Oluwaseyi Balogun
- Wei Chen
date: "2022-09-25"
doi: "10.1115/1.4055898"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-09-25"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 145*(1)"
publication_short: ""

abstract: Deep generative models have demonstrated effectiveness in learning compact and expressive design representations that significantly improve geometric design optimization. However, these models do not consider the uncertainty introduced by manufacturing or fabrication. The past work that quantifies such uncertainty often makes simplifying assumptions on geometric variations, while the “real-world,” “free-form” uncertainty and its impact on design performance are difficult to quantify due to the high dimensionality. To address this issue, we propose a generative adversarial network-based design under uncertainty framework (GAN-DUF), which contains a deep generative model that simultaneously learns a compact representation of nominal (ideal) designs and the conditional distribution of fabricated designs given any nominal design. This opens up new possibilities of (1) building a universal uncertainty quantification model compatible with both shape and topological designs, (2) modeling free-form geometric uncertainties without the need to make any assumptions on the distribution of geometric variability, and (3) allowing fast prediction of uncertainties for new nominal designs. We can combine the proposed deep generative model with robust design optimization or reliability-based design optimization for design under uncertainty. We demonstrated the framework on two real-world engineering design examples and showed its capability of finding the solution that possesses better performance after fabrication.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://asmedigitalcollection.asme.org/mechanicaldesign/article/145/1/011703/1147303/GAN-DUF-Hierarchical-Deep-Generative-Models-for"
url_pdf: 'https://arxiv.org/pdf/2202.10558'
url_code: 'https://github.com/wchen459/GAN-DUF'
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
