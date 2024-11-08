---
title: "Inverse Design of 2D Airfoils using Conditional Generative Models and Surrogate Log-Likelihoods"
authors:
- Qiuyi Chen
- Jun Wang
- Phillip Pope
- Wei_Chen
- Mark Fuge
date: "2021-10-29"
doi: "10.1115/1.4052846"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-10-29"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 144*(2)"
publication_short: ""

abstract: This paper shows how to use conditional generative models in two-dimensional (2D) airfoil optimization to probabilistically predict good initialization points within the vicinity of the optima given the input boundary conditions, thus warm starting and accelerating further optimization. We accommodate the possibility of multiple optimal designs corresponding to the same input boundary condition and take this inversion ambiguity into account when designing our prediction framework. To this end, we first employ the conditional formulation of our previous work BézierGAN–Conditional BézierGAN (CBGAN)—as a baseline, then introduce its sibling conditional entropic BézierGAN (CEBGAN), which is based on optimal transport regularized with entropy. Compared with CBGAN, CEBGAN overcomes mode collapse plaguing conventional GANs, improves the average lift-drag (Cl/Cd) efficiency of airfoil predictions from 80.8% of the optimal value to 95.8%, and meanwhile accelerates the training process by 30.7%. Furthermore, we investigate the unique ability of CEBGAN to produce a log-likelihood lower bound that may help select generated samples of higher performance (e.g., aerodynamic performance). In addition, we provide insights into the performance differences between these two models with low-dimensional toy problems and visualizations. These results and the probabilistic formulation of this inverse problem justify the extension of our GAN-based inverse design paradigm to other inverse design problems or broader inverse problems.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://asmedigitalcollection.asme.org/mechanicaldesign/article/144/2/021712/1122916/Inverse-Design-of-Two-Dimensional-Airfoils-Using"
url_pdf: 'files/papers/md_144_2_021712.pdf'
url_code: 'https://github.com/IDEALLab/CEBGAN_JMD_2021'
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
