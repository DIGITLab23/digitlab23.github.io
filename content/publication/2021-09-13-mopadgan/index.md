---
title: "MO-PaDGAN: Reparameterizing Engineering Designs for Augmented Multi-objective Optimization"
authors:
- Wei_Chen
- Faez Ahmed
date: "2021-09-13"
doi: "10.1016/j.asoc.2021.107909"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-09-13"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Applied Soft Computing, 113*(A)"
publication_short: ""

abstract: Multi-objective optimization is key to solving many Engineering Design problems, where design parameters are optimized for several performance indicators. However, optimization results are highly dependent on how the designs are parameterized. Researchers have shown that deep generative models can learn compact design representations, providing a new way of parameterizing designs to achieve faster convergence and improved optimization performance. Despite their success in capturing complex distributions, existing generative models face three challenges when used for design problems&#58; (1) generated designs have limited design space coverage, (2) the generator ignores design performance, and 3) the new parameterization is unable to represent designs beyond training data. To address these challenges, we propose MO-PaDGAN, which adds a Determinantal Point Processes based loss function to the generative adversarial network to simultaneously model diversity and (multi-variate) performance. MO-PaDGAN can thus improve the performances and coverage of generated designs, and even generate designs with performances exceeding those from training data. When using MO-PaDGAN as a new parameterization in multi-objective optimization, we can discover much better Pareto fronts even though the training data do not cover those Pareto fronts. In a real-world multi-objective airfoil design example, we demonstrate that MO-PaDGAN achieves, on average, an over 180% improvement in the hypervolume indicator when compared to the vanilla GAN or other state-of-the-art parameterization methods.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://www.sciencedirect.com/science/article/pii/S1568494621008310?via%3Dihub"
url_pdf: 'files/papers/MOPadGAN_ASC__ArXiv_.pdf'
url_code: 'https://github.com/wchen459/MO-PaDGAN-Optimization'
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
