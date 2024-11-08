---
title: "Airfoil Design Parameterization and Optimization using Bézier Generative Adversarial Networks"
authors:
- Wei_Chen
- Kevin Chiu
- Mark Fuge
date: "2020-10-01"
doi: "10.2514/1.J059317"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-10-01"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*AIAA Journal, 58*(11)"
publication_short: ""

abstract: Global optimization of aerodynamic shapes usually requires a large number of expensive computational fluid dynamics simulations because of the high dimensionality of the design space. One approach to combat this problem is to reduce the design space dimension by obtaining a new representation. This requires a parametric function that compactly and sufficiently describes useful variation in shapes. We propose a deep generative model, Bézier-GAN, to parameterize aerodynamic designs by learning from shape variations in an existing database. The resulted new parameterization can accelerate design optimization convergence by improving the representation compactness while maintaining sufficient representation capacity. We use the airfoil design as an example to demonstrate the idea and analyze Bézier-GAN's representation capacity and compactness. Results show that Bézier-GAN both (1) learns smooth and realistic shape representations for a wide range of airfoils and (2) empirically accelerates optimization convergence by at least two times compared to state-of-the-art parameterization methods.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://arc.aiaa.org/doi/10.2514/1.J059317"
url_pdf: 'files/papers/1.j059317.pdf'
url_code: 'https://github.com/IDEALLab/bezier-gan'
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
